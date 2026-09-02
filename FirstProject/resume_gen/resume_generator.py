"""
resume_generator.py

Create an editable .DOCX resume from:
    1) input.txt  -> changing resume/content data
    2) RajanGauchanResume.docx -> formatting/template

The template controls the visual format. The text file controls the content.

Requirements:
    pip install python-docx

Usage:
    python resume_generator.py input.txt RajanGauchanResume.docx output.docx

LibreOffice Writer and Microsoft Word can edit the generated DOCX.
"""

import copy
import re
import sys
from pathlib import Path

from docx import Document
from docx.text.paragraph import Paragraph


# ---------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------

# The first three paragraphs of the supplied template are the header.
# They are intentionally preserved exactly unless you later decide to
# make the header configurable.
KEEP_TEMPLATE_HEADER_PARAGRAPHS = 3

# The source has both "CORE ATS SKILLS & KEYWORDS" and "TECHNICAL SKILLS".
# The supplied sample template has one "Tech Stack & Skills" section.
# Therefore both source skill sections are merged into that one section.
SKILL_SECTION_NAMES = {
    "CORE ATS SKILLS & KEYWORDS",
    "TECHNICAL SKILLS",
}

SECTION_NAME_MAP = {
    "CORE ATS SKILLS & KEYWORDS": "Tech Stack & Skills",
    "PROFESSIONAL EXPERIENCE": "Professional Experiences",
    "SECURITY PROJECTS": "Projects",
    "TECHNICAL SKILLS": "Tech Stack & Skills",
}

# Template paragraph numbers used only as FORMAT PROTOTYPES.
# These numbers refer to the supplied RajanGauchanResume.docx.
PROTO = {
    "section": 3,       # section heading
    "skill": 9,         # skill row with bold label
    "job_title": 21,    # job/project title + date
    "company": 22,      # company/location
    "bullet": 23,       # normal bullet
    "project_title": 49,
    "education": 56,
    "education_head": 53,
    "volunteer_title": 65,
    "volunteer_company": 66,
}


# ---------------------------------------------------------------------
# TEXT PARSING
# ---------------------------------------------------------------------

def clean_markdown(text: str) -> str:
    """Remove markdown emphasis markers while preserving the words."""
    return re.sub(r"(\*\*|__)", "", text).strip()


def parse_source(text: str):
    """
    Parse the input.txt format:

        # MAIN SECTION
        paragraph

        ## SUBSECTION
        **date**
        * bullet

    Returns a list of logical blocks.
    """
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")

    blocks = []
    current_section = None
    current_subsection = None
    paragraph_buffer = []

    def flush_paragraph():
        nonlocal paragraph_buffer
        if paragraph_buffer:
            value = " ".join(x.strip() for x in paragraph_buffer).strip()
            if value:
                blocks.append({
                    "type": "paragraph",
                    "section": current_section,
                    "subsection": current_subsection,
                    "text": value,
                })
            paragraph_buffer = []

    for raw in lines:
        line = raw.strip()

        if not line:
            flush_paragraph()
            continue

        # Markdown H1
        if line.startswith("# "):
            flush_paragraph()
            current_section = clean_markdown(line[2:])
            current_subsection = None
            blocks.append({
                "type": "section",
                "name": current_section,
            })
            continue

        # Markdown H2
        if line.startswith("## "):
            flush_paragraph()
            current_subsection = clean_markdown(line[3:])
            blocks.append({
                "type": "subsection",
                "section": current_section,
                "name": current_subsection,
            })
            continue

        # Bullet
        if line.startswith("* "):
            flush_paragraph()
            blocks.append({
                "type": "bullet",
                "section": current_section,
                "subsection": current_subsection,
                "text": clean_markdown(line[2:]),
            })
            continue

        # Markdown bold-only date line, e.g. **June 2021 – August 2025**
        if re.fullmatch(r"\*\*.+\*\*", line):
            flush_paragraph()
            blocks.append({
                "type": "date",
                "section": current_section,
                "subsection": current_subsection,
                "text": clean_markdown(line),
            })
            continue

        paragraph_buffer.append(clean_markdown(line))

    flush_paragraph()
    return blocks


# ---------------------------------------------------------------------
# DOCX HELPERS
# ---------------------------------------------------------------------

def clone_paragraph(document, prototype: Paragraph) -> Paragraph:
    """
    Clone a template paragraph, including its formatting, numbering,
    tabs, indentation, spacing, and run properties.
    """
    new_p = copy.deepcopy(prototype._p)

    # Insert immediately before sectPr because Word requires sectPr
    # to remain the final element in the document body.
    body = document._body._body
    sect_pr = body.sectPr
    if sect_pr is not None:
        body.insert(body.index(sect_pr), new_p)
    else:
        body.append(new_p)

    return Paragraph(new_p, document)


def clear_paragraph(paragraph: Paragraph):
    """Remove all runs/content while retaining paragraph formatting."""
    p = paragraph._p
    for child in list(p):
        if child.tag.endswith("}pPr"):
            continue
        p.remove(child)


def set_plain_text(paragraph: Paragraph, text: str):
    clear_paragraph(paragraph)
    run = paragraph.add_run(text)

    # Use the first run of the prototype paragraph for its font settings.
    # The paragraph's copied formatting remains intact.
    return run


def add_bold_markdown_runs(paragraph: Paragraph, text: str):
    """
    Add text with **bold** portions while preserving the formatting
    characteristics of the template's normal body run.
    """
    clear_paragraph(paragraph)

    parts = re.split(r"(\*\*.*?\*\*)", text)

    for part in parts:
        if not part:
            continue

        bold = part.startswith("**") and part.endswith("**")
        value = part[2:-2] if bold else part

        run = paragraph.add_run(value)
        run.bold = bold

    return paragraph


def add_skill_row(document, prototype: Paragraph, text: str):
    """
    Convert:
        **Cybersecurity / Security Operations:** A • B • C

    into the template's two-part skill row:
        Cybersecurity / Security Operations:    A • B • C
    """
    p = clone_paragraph(document, prototype)

    match = re.match(r"\*\*(.+?)\*\*\s*:?\s*(.*)", text)
    if match:
        label = match.group(1).strip()
        values = match.group(2).strip()

        clear_paragraph(p)

        r1 = p.add_run(label + ":")
        r1.bold = True
        r1.font.size = prototype.runs[0].font.size

        p.add_run("\t\t")

        r2 = p.add_run(values)
        if prototype.runs:
            r2.font.size = prototype.runs[-1].font.size
    else:
        set_plain_text(p, clean_markdown(text))

    return p


def split_job_title_and_date(title: str, date: str | None):
    """
    Source:
        ## IT Security Engineer / Developer (Contract) | Takeo, Toronto, ON
        **June 2021 – August 2025**

    Target:
        IT Security Engineer / Developer (Contract)       June 2021 – August 2025
        Takeo | Toronto, ON

    Returns role, company/location.
    """
    parts = [x.strip() for x in title.split("|")]

    role = parts[0]
    company_location = " | ".join(parts[1:]) if len(parts) > 1 else ""

    # Convert "Company, Toronto, ON" to the target style
    # "Company | Toronto, ON" when possible.
    if company_location and " | " not in company_location:
        pieces = [x.strip() for x in company_location.split(",")]
        if len(pieces) >= 3:
            company_location = pieces[0] + " | " + ", ".join(pieces[1:])
        elif len(pieces) == 2:
            company_location = pieces[0] + " | " + pieces[1]

    return role, company_location, date or ""


# ---------------------------------------------------------------------
# DOCUMENT BUILDING
# ---------------------------------------------------------------------

def remove_body_after_header(document):
    """
    Keep the sample resume header and remove all template body content.
    """
    body = document._body._body
    children = list(body)

    # Keep paragraphs, sectPr, etc. before the content cutoff.
    paragraph_indexes = [
        i for i, child in enumerate(children)
        if child.tag.endswith("}p")
    ]

    if len(paragraph_indexes) < KEEP_TEMPLATE_HEADER_PARAGRAPHS:
        raise RuntimeError("Template does not contain the expected header.")

    cutoff_child = paragraph_indexes[KEEP_TEMPLATE_HEADER_PARAGRAPHS - 1]

    for child in list(children):
        if children.index(child) > cutoff_child:
            if not child.tag.endswith("}sectPr"):
                body.remove(child)


def build_document(input_file, template_file, output_file):
    source = Path(input_file).read_text(encoding="utf-8")
    blocks = parse_source(source)

    template = Document(template_file)

    # Capture prototype paragraphs before deleting the template body.
    prototypes = {
        name: copy.deepcopy(template.paragraphs[index])
        for name, index in PROTO.items()
    }

    # Keep the exact sample header.
    remove_body_after_header(template)

    current_section = None
    pending_subsection = None
    pending_date = None

    # Keep track of whether we have already created the merged skill heading.
    skill_heading_created = False

    for block in blocks:
        btype = block["type"]

        if btype == "section":
            raw_name = block["name"]
            normalized = raw_name.upper()

            if normalized in SKILL_SECTION_NAMES:
                if not skill_heading_created:
                    p = clone_paragraph(template, prototypes["section"])
                    set_plain_text(p, SECTION_NAME_MAP["CORE ATS SKILLS & KEYWORDS"])
                    skill_heading_created = True
                current_section = "MERGED_SKILLS"
                pending_subsection = None
                continue

            current_section = normalized
            pending_subsection = None

            display_name = SECTION_NAME_MAP.get(
                normalized,
                block["name"].title()
            )

            p = clone_paragraph(template, prototypes["section"])
            set_plain_text(p, display_name)
            continue

        if btype == "subsection":
            pending_subsection = block["name"]

            if current_section == "MERGED_SKILLS":
                add_skill_row(template, prototypes["skill"], pending_subsection)
                continue

            if current_section in {
                "PROFESSIONAL EXPERIENCE",
                "SECURITY PROJECTS",
                "VOLUNTEER EXPERIENCE",
            }:
                pending_date = None
                continue

            continue

        if btype == "date":
            pending_date = block["text"]
            continue

        if btype == "paragraph":
            # Professional Summary paragraphs become template bullets.
            if current_section == "PROFESSIONAL SUMMARY":
                p = clone_paragraph(template, prototypes["bullet"])
                add_bold_markdown_runs(p, block["text"])

            # A normal paragraph under a skills section is treated as a skill row.
            elif current_section == "MERGED_SKILLS":
                add_skill_row(template, prototypes["skill"], block["text"])

            else:
                p = clone_paragraph(template, prototypes["bullet"])
                add_bold_markdown_runs(p, block["text"])

            continue

        if btype == "bullet":
            if current_section == "MERGED_SKILLS":
                add_skill_row(template, prototypes["skill"], block["text"])
                continue

            # A subsection inside Professional Experience is a job.
            if current_section == "PROFESSIONAL EXPERIENCE":
                # If this is the first bullet after a new job, create the job
                # header now. This keeps all source bullet counts dynamic.
                if pending_subsection:
                    role, company, date = split_job_title_and_date(
                        pending_subsection, pending_date
                    )

                    title_p = clone_paragraph(
                        template, prototypes["job_title"]
                    )
                    clear_paragraph(title_p)

                    r1 = title_p.add_run(role)
                    r1.bold = True
                    r1.font.size = prototypes["job_title"].runs[0].font.size

                    title_p.add_run("\t\t\t\t\t\t\t")

                    r2 = title_p.add_run(date)
                    r2.font.size = prototypes["job_title"].runs[-1].font.size

                    company_p = clone_paragraph(
                        template, prototypes["company"]
                    )
                    set_plain_text(company_p, company)

                    pending_subsection = None
                    pending_date = None

                p = clone_paragraph(template, prototypes["bullet"])
                add_bold_markdown_runs(p, block["text"])
                continue

            # Security Projects
            if current_section == "SECURITY PROJECTS":
                if pending_subsection:
                    role, company, date = split_job_title_and_date(
                        pending_subsection, pending_date
                    )

                    p = clone_paragraph(
                        template, prototypes["project_title"]
                    )
                    clear_paragraph(p)

                    r1 = p.add_run(role)
                    r1.bold = True

                    p.add_run("\t\t\t\t\t\t\t")
                    p.add_run(date)

                    pending_subsection = None
                    pending_date = None

                p = clone_paragraph(template, prototypes["bullet"])
                add_bold_markdown_runs(p, block["text"])
                continue

            # Education / Certifications
            if current_section == "EDUCATION & CERTIFICATIONS":
                p = clone_paragraph(template, prototypes["education"])
                add_bold_markdown_runs(p, block["text"])
                continue

            # Volunteer Experience
            if current_section == "VOLUNTEER EXPERIENCE":
                if pending_subsection:
                    role, company, date = split_job_title_and_date(
                        pending_subsection, pending_date
                    )

                    p = clone_paragraph(
                        template, prototypes["volunteer_title"]
                    )
                    clear_paragraph(p)

                    r1 = p.add_run(role)
                    r1.bold = True
                    r1.font.size = prototypes["volunteer_title"].runs[0].font.size

                    p.add_run("\t\t\t\t\t\t")
                    r2 = p.add_run(date)
                    r2.font.size = prototypes["volunteer_title"].runs[-1].font.size

                    cp = clone_paragraph(
                        template, prototypes["volunteer_company"]
                    )
                    set_plain_text(cp, company)

                    pending_subsection = None
                    pending_date = None

                p = clone_paragraph(template, prototypes["bullet"])
                add_bold_markdown_runs(p, block["text"])
                continue

            # Generic section fallback
            p = clone_paragraph(template, prototypes["bullet"])
            add_bold_markdown_runs(p, block["text"])

    # Save editable DOCX.
    template.save(output_file)


def main():
    if len(sys.argv) != 4:
        print(
            "Usage:\n"
            "  python resume_generator.py active_job_search "
            "RajanGauchanResume.docx output.docx"
        )
        sys.exit(1)

    input_file, template_file, output_file = sys.argv[1:]

    for path in (input_file, template_file):
        if not Path(path).exists():
            print(f"ERROR: File not found: {path}")
            sys.exit(1)

    build_document(input_file, template_file, output_file)
    print(f"Created editable Word document: {output_file}")


if __name__ == "__main__":
    main()
