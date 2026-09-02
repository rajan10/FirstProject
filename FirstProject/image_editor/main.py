# Professional Image Ad Editor

# Resize + Brightness + Vibrance + Contrast + Sharpness + Text + Center Price

from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import os

# ============================================================

# SETTINGS — CUSTOMIZE THESE

# ============================================================

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"

# Fixed output size

OUTPUT_WIDTH = 1200
OUTPUT_HEIGHT = 1200

# Image adjustments

BRIGHTNESS = 1.15      # 1.0 = original, >1 = brighter
CONTRAST = 1.10        # 1.0 = original
COLOR = 1.25           # 1.0 = original, >1 = more colourful
SHARPNESS = 1.15       # 1.0 = original

# Optional text

ADD_TEXT = True

HEADLINE = "GTA MOVERS"
SUBTITLE = "MOVERS + TRUCK"

# Enter the price you want displayed in the centre of the image.

# Examples: "$40/HR", "$99", "FROM $40/HR", or "CALL FOR PRICE"

PRICE = "$40/HR"

PHONE = "437-438-7160"

# Text positions

HEADLINE_Y = 50
SUBTITLE_Y = 105
PHONE_Y = 1080

# Price position and appearance

PRICE_CENTER_X = OUTPUT_WIDTH // 2
PRICE_CENTER_Y = OUTPUT_HEIGHT // 2

PRICE_FONT_SIZE = 110
PRICE_TEXT_COLOR = "white"
PRICE_SHADOW_COLOR = "black"

# Optional semi-transparent background behind the centre price

ADD_PRICE_BACKGROUND = True
PRICE_BACKGROUND_COLOR = (0, 0, 0, 150)
PRICE_BACKGROUND_PADDING_X = 45
PRICE_BACKGROUND_PADDING_Y = 25

# ============================================================

# CREATE OUTPUT FOLDER

# ============================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ============================================================

# LOAD FONT

# ============================================================

def get_font(size):
    """
    Try to load a professional bold font.
    Falls back to the PIL default font if unavailable.
    """
    font_paths = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "C:/Windows/Fonts/segoeuib.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf"
    ]

    for path in font_paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)

    return ImageFont.load_default()

# ============================================================

# CROP IMAGE TO FIXED SIZE

# ============================================================

def crop_to_size(image, target_width, target_height):
    target_ratio = target_width / target_height
    image_ratio = image.width / image.height

    if image_ratio > target_ratio:
        # Image is too wide
        new_height = image.height
        new_width = int(new_height * target_ratio)

        left = (image.width - new_width) // 2
        top = 0

    else:
        # Image is too tall
        new_width = image.width
        new_height = int(new_width / target_ratio)

        left = 0
        top = (image.height - new_height) // 2

    image = image.crop(
        (
            left,
            top,
            left + new_width,
            top + new_height
        )
    )

    return image.resize(
        (target_width, target_height),
        Image.Resampling.LANCZOS
    )

# ============================================================

# ADD TEXT WITH SHADOW

# ============================================================

def draw_text_with_shadow(
    draw,
    position,
    text,
    font,
    fill="white",
    shadow="black",
    shadow_offset=4
):
    x, y = position

    draw.text(
        (x + shadow_offset, y + shadow_offset),
        text,
        font=font,
        fill=shadow
    )

    draw.text(
        (x, y),
        text,
        font=font,
        fill=fill
    )

# ============================================================

# DRAW CENTRED TEXT

# ============================================================

def center_text(draw, text, font, y, fill="white", shadow="black"):
    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]

    x = (OUTPUT_WIDTH - text_width) // 2

    draw_text_with_shadow(
        draw,
        (x, y),
        text,
        font,
        fill=fill,
        shadow=shadow
    )

# ============================================================

# DRAW PRICE IN THE CENTRE

# ============================================================

def draw_center_price(image, price):
    if not price.strip():
        return

    # Use RGBA overlay so the price background can be transparent
    overlay = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(overlay)

    price_font = get_font(PRICE_FONT_SIZE)

    bbox = draw.textbbox(
        (0, 0),
        price,
        font=price_font
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = PRICE_CENTER_X - (text_width // 2)
    text_y = PRICE_CENTER_Y - (text_height // 2) - bbox[1]

    if ADD_PRICE_BACKGROUND:

        background_left = (
            text_x - PRICE_BACKGROUND_PADDING_X
        )

        background_top = (
            text_y - PRICE_BACKGROUND_PADDING_Y
        )

        background_right = (
            text_x + text_width + PRICE_BACKGROUND_PADDING_X
        )

        background_bottom = (
            text_y + text_height + PRICE_BACKGROUND_PADDING_Y
        )

        draw.rounded_rectangle(
            (
                background_left,
                background_top,
                background_right,
                background_bottom
            ),
            radius=25,
            fill=PRICE_BACKGROUND_COLOR
        )

    # Price shadow
    draw.text(
        (
            text_x + 5,
            text_y + 5
        ),
        price,
        font=price_font,
        fill=PRICE_SHADOW_COLOR
    )

    # Main price
    draw.text(
        (
            text_x,
            text_y
        ),
        price,
        font=price_font,
        fill=PRICE_TEXT_COLOR
    )

    return Image.alpha_composite(
        image.convert("RGBA"),
        overlay
    ).convert("RGB")


# ============================================================
# PROCESS ONE IMAGE
# ============================================================

def process_image(input_path, output_path):
    print(f"Processing: {input_path}")

    image = Image.open(input_path).convert("RGB")

    # --------------------------------------------------------
    # Resize and crop
    # --------------------------------------------------------

    image = crop_to_size(
        image,
        OUTPUT_WIDTH,
        OUTPUT_HEIGHT
    )

    # --------------------------------------------------------
    # Brightness
    # --------------------------------------------------------

    image = ImageEnhance.Brightness(image).enhance(
        BRIGHTNESS
    )

    # --------------------------------------------------------
    # Contrast
    # --------------------------------------------------------

    image = ImageEnhance.Contrast(image).enhance(
        CONTRAST
    )

    # --------------------------------------------------------
    # Colour / Vibrance
    # --------------------------------------------------------

    image = ImageEnhance.Color(image).enhance(
        COLOR
    )

    # --------------------------------------------------------
    # Sharpness
    # --------------------------------------------------------

    image = ImageEnhance.Sharpness(image).enhance(
        SHARPNESS
    )

    # --------------------------------------------------------
    # Add text
    # --------------------------------------------------------

    if ADD_TEXT:

        draw = ImageDraw.Draw(image)

        headline_font = get_font(70)
        subtitle_font = get_font(45)
        phone_font = get_font(55)

        center_text(
            draw,
            HEADLINE,
            headline_font,
            HEADLINE_Y
        )

        center_text(
            draw,
            SUBTITLE,
            subtitle_font,
            SUBTITLE_Y
        )

        # Draw the editable price in the centre of the image
        image = draw_center_price(
            image,
            PRICE
        )

        draw = ImageDraw.Draw(image)

        center_text(
            draw,
            PHONE,
            phone_font,
            PHONE_Y
        )

    # --------------------------------------------------------
    # Save high-quality JPG
    # --------------------------------------------------------

    image.save(
        output_path,
        "JPEG",
        quality=95,
        optimize=True
    )

    print(f"Saved: {output_path}")

# ============================================================

# PROCESS ALL IMAGES

# ============================================================

supported_formats = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
)

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(supported_formats):

        input_path = os.path.join(
            INPUT_FOLDER,
            filename
        )

        name = os.path.splitext(filename)[0]

        output_path = os.path.join(
            OUTPUT_FOLDER,
            name + "_AD.jpg"
        )

        process_image(
            input_path,
            output_path
        )

print("\n===================================")
print("ALL IMAGES PROCESSED SUCCESSFULLY!")
print("===================================")
print(f"Output folder: {OUTPUT_FOLDER}")
