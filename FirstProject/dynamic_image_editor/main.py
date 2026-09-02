# ============================================================
#
#              BARBIE / DOLL IMAGE PRICE FINDER
#
# ============================================================
#
# COMPLETE PROGRAM
#
# NO OPENAI API
#
# This program:
#
# 1. Reads Barbie / doll images from input_images
# 2. Uses the IMAGE FILENAME as the product search name
# 3. Searches Google using SerpAPI
# 4. Finds prices for the product
# 5. Calculates a reasonable market price
# 6. Enhances the image
#       - fixed size
#       - brighter
#       - more colourful
#       - better contrast
#       - sharper
# 7. Places the estimated price in the CENTER
# 8. Places the product name near the bottom
# 9. Saves the finished image in output_images
#
# ============================================================


# ============================================================
#                         IMPORTS
# ============================================================

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont

import os
import requests
import re
import statistics

from streamlit import text


# ============================================================
#                         API KEY
# ============================================================
#
# IMPORTANT:
#
# OpenAI has been completely removed.
#
# Only SerpAPI is used.
#
# Get your SerpAPI key from:
#
# https://serpapi.com/
#
# Then put your key between the quotation marks below.
#
# Example:
#
# SERPAPI_KEY = "your_real_serpapi_key"
#
# ============================================================

SERPAPI_KEY = "c3323cee8636d758b58dcdac30eaac830faa7037d0ce6d2f871313e059015b6f"


# ============================================================
#                      FOLDER SETTINGS
# ============================================================

# Find the folder where this main.py is located.

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# Folder containing original images.

INPUT_FOLDER = os.path.join(
    BASE_DIR,
    "input_images"
)


# Folder containing finished images.

OUTPUT_FOLDER = os.path.join(
    BASE_DIR,
    "output_images"
)


# Automatically create output folder.

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)


# ============================================================
#                       IMAGE SETTINGS
# ============================================================

# Final image width.

OUTPUT_WIDTH = 1200


# Final image height.

OUTPUT_HEIGHT = 1200


# ============================================================
#                  IMAGE ENHANCEMENT SETTINGS
# ============================================================

# Brightness:
#
# 1.00 = original
# 1.10 = slightly brighter
# 1.20 = bright
# 1.30 = very bright

BRIGHTNESS = 1.15


# Contrast:
#
# 1.00 = original
# 1.10 = slightly stronger
# 1.20 = stronger

CONTRAST = 1.10


# Colour:
#
# 1.00 = original
# 1.20 = colourful
# 1.30 = vibrant
# 1.40 = very vibrant

COLOR = 1.25


# Sharpness:
#
# 1.00 = original
# 1.15 = sharper
# 1.30 = very sharp

SHARPNESS = 1.15


# ============================================================
#                    PRICE SEARCH SETTINGS
# ============================================================

# Minimum acceptable price.

MIN_PRICE = 5


# Maximum acceptable price.
#
# This helps prevent accidentally picking up:
#
# $1,999
# $5,000
# etc.

MAX_PRICE = 500


# Number of Google results to request.

GOOGLE_RESULTS = 10


# ============================================================
#                      FALLBACK PRICE
# ============================================================

# If no reliable price is found.

FALLBACK_PRICE = "PRICE N/A"


# ============================================================
#                   PRODUCT TEXT SETTINGS
# ============================================================

# Show product name on image.

SHOW_PRODUCT_NAME = True


# Maximum product-name length.

MAX_PRODUCT_NAME_LENGTH = 55


# ============================================================
#                         PRICE TEXT
# ============================================================

PRICE_FONT_SIZE = 110

PRODUCT_FONT_SIZE = 40


# ============================================================
#                       TEXT POSITIONS
# ============================================================

PRICE_CENTER_X = OUTPUT_WIDTH // 2

PRICE_CENTER_Y = OUTPUT_HEIGHT // 2

PRODUCT_NAME_Y = 1060


# ============================================================
#                     PRICE BOX SETTINGS
# ============================================================

# Display a dark transparent box behind price.

ADD_PRICE_BACKGROUND = True


# RGBA:
#
# R = 0
# G = 0
# B = 0
# A = 170 transparency

PRICE_BACKGROUND_COLOR = (
    0,
    0,
    0,
    170
)


PRICE_BACKGROUND_PADDING_X = 45

PRICE_BACKGROUND_PADDING_Y = 25


# ============================================================
#                    SUPPORTED FILES
# ============================================================

SUPPORTED_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".bmp"
)


# ============================================================
#                       FONT LOADER
# ============================================================

def get_font(size):
    """
    Find a suitable bold font on Windows/Linux/Mac.
    """

    font_paths = [

        # Windows Arial Bold
        "C:/Windows/Fonts/arialbd.ttf",

        # Windows Calibri Bold
        "C:/Windows/Fonts/calibrib.ttf",

        # Windows Segoe UI Bold
        "C:/Windows/Fonts/segoeuib.ttf",

        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",

        # Mac
        "/Library/Fonts/Arial Bold.ttf"
    ]


    for path in font_paths:

        if os.path.exists(path):

            return ImageFont.truetype(
                path,
                size
            )


    return ImageFont.load_default()


# ============================================================
#                  CREATE PRODUCT NAME
# ============================================================

def get_product_name_from_filename(filename):
    """
    Convert the image filename into a clean product name.

    Example:

        Barbie_Dreamhouse.jpg

    becomes:

        Barbie Dreamhouse
    """

    # Remove extension.

    name = os.path.splitext(
        filename
    )[0]


    # Replace underscores.

    name = name.replace(
        "_",
        " "
    )


    # Replace hyphens.

    name = name.replace(
        "-",
        " "
    )


    # Remove words that are usually added to filenames.

    name = re.sub(
        r"\b(original|photo|image|img|pic|picture)\b",
        "",
        name,
        flags=re.IGNORECASE
    )


    # Remove extra spaces.

    name = re.sub(
        r"\s+",
        " ",
        name
    ).strip()


    # If filename is empty.

    if not name:

        name = "Barbie Doll"


    return name


# ============================================================
#                    CROP TO FIXED SIZE
# ============================================================

def crop_to_size(
    image,
    target_width,
    target_height
):
    """
    Crop the image to the correct aspect ratio,
    then resize to requested dimensions.

    This prevents the doll from looking stretched.
    """

    target_ratio = (
        target_width /
        target_height
    )


    image_ratio = (
        image.width /
        image.height
    )


    # --------------------------------------------------------
    # Image is wider than target.
    # --------------------------------------------------------

    if image_ratio > target_ratio:

        new_height = image.height

        new_width = int(
            new_height *
            target_ratio
        )


        left = (
            image.width -
            new_width
        ) // 2


        top = 0


    # --------------------------------------------------------
    # Image is taller than target.
    # --------------------------------------------------------

    else:

        new_width = image.width

        new_height = int(
            new_width /
            target_ratio
        )


        left = 0


        top = (
            image.height -
            new_height
        ) // 2


    # --------------------------------------------------------
    # Crop.
    # --------------------------------------------------------

    image = image.crop(
        (
            left,
            top,
            left + new_width,
            top + new_height
        )
    )


    # --------------------------------------------------------
    # Resize.
    # --------------------------------------------------------

    image = image.resize(
        (
            target_width,
            target_height
        ),
        Image.Resampling.LANCZOS
    )


    return image


# ============================================================
#                       ENHANCE IMAGE
# ============================================================

def enhance_image(image):
    """
    Make the photograph:

    - brighter
    - more colourful
    - stronger contrast
    - sharper
    """

    # --------------------------------------------------------
    # Brightness
    # --------------------------------------------------------

    image = ImageEnhance.Brightness(
        image
    ).enhance(
        BRIGHTNESS
    )


    # --------------------------------------------------------
    # Contrast
    # --------------------------------------------------------

    image = ImageEnhance.Contrast(
        image
    ).enhance(
        CONTRAST
    )


    # --------------------------------------------------------
    # Colour
    # --------------------------------------------------------

    image = ImageEnhance.Color(
        image
    ).enhance(
        COLOR
    )


    # --------------------------------------------------------
    # Sharpness
    # --------------------------------------------------------

    image = ImageEnhance.Sharpness(
        image
    ).enhance(
        SHARPNESS
    )


    return image


# ============================================================
#                    EXTRACT PRICES
# ============================================================



def extract_prices(text):
    """
    Extract Canadian-style prices from text.

    Examples:
        $29.99
        $49
        CAD $39.99
        C$59.99
        CA$79.99
    """

    prices = []

    patterns = [
        r'CAD\s*\$?\s*(\d+(?:\.\d{1,2})?)',
        r'C\$\s*(\d+(?:\.\d{1,2})?)',
        r'CA\$\s*(\d+(?:\.\d{1,2})?)',
        r'\$\s*(\d+(?:\.\d{1,2})?)'
    ]

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text,
            re.IGNORECASE
        )

        for match in matches:

            try:

                price = float(match)

                if MIN_PRICE <= price <= MAX_PRICE:

                    prices.append(price)

            except ValueError:

                pass

    return prices

# ============================================================
#                  REMOVE OBVIOUS BAD PRICES
# ============================================================

def clean_prices(prices):
    """
    Remove obvious duplicate and unreasonable values.
    """

    if not prices:

        return []


    cleaned = []


    for price in prices:

        if (
            MIN_PRICE <=
            price <=
            MAX_PRICE
        ):

            cleaned.append(price)


    return sorted(
        list(
            set(cleaned)
        )
    )


# ============================================================
#                   SEARCH PRODUCT PRICES
# ============================================================

def search_product_prices(
    product_name
):
    """
    Search Google through SerpAPI for the product.

    The product name comes from the image filename.
    """

    print()
    print("=" * 65)
    print("SEARCHING INTERNET FOR PRODUCT PRICE")
    print("=" * 65)


    # ========================================================
    # CHECK SERPAPI KEY
    # ========================================================

    if (
        not SERPAPI_KEY
        or
        SERPAPI_KEY ==
        "YOUR_SERPAPI_API_KEY"
    ):

        print()
        print(
            "ERROR: SerpAPI key is not configured."
        )

        return FALLBACK_PRICE


    # ========================================================
    # CREATE SEARCH QUERY
    # ========================================================

    search_query = (
        f"{product_name} "
        "Barbie doll "
        "Canada "
        "CAD "
        "price"
    )


    print()
    print("SEARCH QUERY:")

    print(
        search_query
    )


    # ========================================================
    # SERPAPI URL
    # ========================================================

    url = (
        "https://serpapi.com/search.json"
    )


    # ========================================================
    # REQUEST PARAMETERS
    # ========================================================

    params = {

        "engine": "google",

        "q": search_query,

        "location":
            "Toronto, Ontario, Canada",

        "hl": "en",

        "gl": "ca",

        "num":
            GOOGLE_RESULTS,

        "api_key":
            SERPAPI_KEY
    }


    # ========================================================
    # REQUEST
    # ========================================================

    try:

        response = requests.get(
            url,
            params=params,
            timeout=30
        )


        response.raise_for_status()


        data = response.json()


    except Exception as error:

        print()
        print(
            "ERROR searching Google:"
        )

        print(error)

        return FALLBACK_PRICE


    # ========================================================
    # CHECK SERPAPI ERROR
    # ========================================================

    if "error" in data:

        print()
        print(
            "SERPAPI ERROR:"
        )

        print(
            data["error"]
        )

        return FALLBACK_PRICE


    # ========================================================
    # GET RESULTS
    # ========================================================

    results = data.get(
        "organic_results",
        []
    )


    print()
    print(
        f"Google results found: "
        f"{len(results)}"
    )


    # ========================================================
    # COLLECT PRICES
    # ========================================================

    all_prices = []


    # ========================================================
    # PROCESS RESULTS
    # ========================================================

    for index, result in enumerate(
        results,
        start=1
    ):

        title = result.get(
            "title",
            ""
        )


        snippet = result.get(
            "snippet",
            ""
        )


        link = result.get(
            "link",
            ""
        )


        # ----------------------------------------------------
        # Combine information.
        # ----------------------------------------------------

        text = (
            title +
            " " +
            snippet
        )
        print("SEARCH TEXT:")
        print(text)


        # ----------------------------------------------------
        # Extract prices.
        # ----------------------------------------------------

        prices = extract_prices(
            text
        )


        # ----------------------------------------------------
        # Display result.
        # ----------------------------------------------------

        print()
        print("-" * 65)

        print(
            f"RESULT {index}"
        )

        print(
            "TITLE:",
            title
        )

        print(
            "PRICE(S):",
            prices
        )

        print(
            "WEBSITE:",
            link
        )


        # ----------------------------------------------------
        # Add prices.
        # ----------------------------------------------------

        all_prices.extend(
            prices
        )


    # ========================================================
    # CLEAN PRICES
    # ========================================================

    all_prices = clean_prices(
        all_prices
    )


    # ========================================================
    # DISPLAY PRICES
    # ========================================================

    print()
    print("=" * 65)

    print(
        "PRICES FOUND:"
    )

    print(
        all_prices
    )


    # ========================================================
    # NO PRICES
    # ========================================================

    if not all_prices:

        print()
        print(
            "No reliable prices found."
        )

        print(
            f"Using: {FALLBACK_PRICE}"
        )

        return FALLBACK_PRICE


    # ========================================================
    # CALCULATE MEDIAN
    # ========================================================

    median_price = statistics.median(
        all_prices
    )


    # ========================================================
    # CALCULATE LOW / HIGH
    # ========================================================

    minimum_price = min(
        all_prices
    )


    maximum_price = max(
        all_prices
    )


    # ========================================================
    # DISPLAY MARKET INFORMATION
    # ========================================================

    print()

    print(
        f"Lowest price: "
        f"${minimum_price:.2f} CAD"
    )

    print(
        f"Highest price: "
        f"${maximum_price:.2f} CAD"
    )

    print(
        f"Median price: "
        f"${median_price:.2f} CAD"
    )


    # ========================================================
    # FINAL PRICE
    # ========================================================

    final_price = (
        f"${median_price:.2f} CAD"
    )


    print()

    print(
        f"FINAL ESTIMATED PRICE: "
        f"{final_price}"
    )

    print(
        "=" * 65
    )


    return final_price


# ============================================================
#                     DRAW CENTRE PRICE
# ============================================================

def draw_center_price(
    image,
    price
):
    """
    Put the price in the center of the image.
    """

    # --------------------------------------------------------
    # Create transparent overlay.
    # --------------------------------------------------------

    overlay = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0)
    )


    draw = ImageDraw.Draw(
        overlay
    )


    # --------------------------------------------------------
    # Price font.
    # --------------------------------------------------------

    price_font = get_font(
        PRICE_FONT_SIZE
    )


    # --------------------------------------------------------
    # Find dimensions.
    # --------------------------------------------------------

    bbox = draw.textbbox(
        (0, 0),
        price,
        font=price_font
    )


    text_width = (
        bbox[2] -
        bbox[0]
    )


    text_height = (
        bbox[3] -
        bbox[1]
    )


    # --------------------------------------------------------
    # Calculate centre.
    # --------------------------------------------------------

    text_x = (
        PRICE_CENTER_X -
        text_width // 2
    )


    text_y = (
        PRICE_CENTER_Y -
        text_height // 2 -
        bbox[1]
    )


    # ========================================================
    # PRICE BACKGROUND
    # ========================================================

    if ADD_PRICE_BACKGROUND:

        left = (
            text_x -
            PRICE_BACKGROUND_PADDING_X
        )


        top = (
            text_y -
            PRICE_BACKGROUND_PADDING_Y
        )


        right = (
            text_x +
            text_width +
            PRICE_BACKGROUND_PADDING_X
        )


        bottom = (
            text_y +
            text_height +
            PRICE_BACKGROUND_PADDING_Y
        )


        draw.rounded_rectangle(
            (
                left,
                top,
                right,
                bottom
            ),
            radius=25,
            fill=PRICE_BACKGROUND_COLOR
        )


    # ========================================================
    # PRICE SHADOW
    # ========================================================

    draw.text(
        (
            text_x + 5,
            text_y + 5
        ),
        price,
        font=price_font,
        fill="black"
    )


    # ========================================================
    # PRICE
    # ========================================================

    draw.text(
        (
            text_x,
            text_y
        ),
        price,
        font=price_font,
        fill="white"
    )


    # ========================================================
    # COMBINE
    # ========================================================

    image = Image.alpha_composite(
        image.convert("RGBA"),
        overlay
    )


    return image.convert(
        "RGB"
    )


# ============================================================
#                    DRAW PRODUCT NAME
# ============================================================

def draw_product_name(
    image,
    product_name
):
    """
    Put a short product name near the bottom.
    """

    if not SHOW_PRODUCT_NAME:

        return image


    if not product_name:

        return image


    # --------------------------------------------------------
    # Shorten product name.
    # --------------------------------------------------------

    product_name = product_name.strip()


    if len(product_name) > MAX_PRODUCT_NAME_LENGTH:

        product_name = (
            product_name[
                :MAX_PRODUCT_NAME_LENGTH - 3
            ] +
            "..."
        )


    # --------------------------------------------------------
    # Drawing object.
    # --------------------------------------------------------

    draw = ImageDraw.Draw(
        image
    )


    font = get_font(
        PRODUCT_FONT_SIZE
    )


    # --------------------------------------------------------
    # Get dimensions.
    # --------------------------------------------------------

    bbox = draw.textbbox(
        (0, 0),
        product_name,
        font=font
    )


    text_width = (
        bbox[2] -
        bbox[0]
    )


    text_height = (
        bbox[3] -
        bbox[1]
    )


    # --------------------------------------------------------
    # Centre text.
    # --------------------------------------------------------

    x = (
        OUTPUT_WIDTH -
        text_width
    ) // 2


    # --------------------------------------------------------
    # Background box.
    # --------------------------------------------------------

    padding_x = 25

    padding_y = 12


    left = (
        x -
        padding_x
    )


    top = (
        PRODUCT_NAME_Y -
        padding_y
    )


    right = (
        x +
        text_width +
        padding_x
    )


    bottom = (
        PRODUCT_NAME_Y +
        text_height +
        padding_y
    )


    draw.rounded_rectangle(
        (
            left,
            top,
            right,
            bottom
        ),
        radius=15,
        fill=(0, 0, 0, 170)
    )


    # --------------------------------------------------------
    # Text shadow.
    # --------------------------------------------------------

    draw.text(
        (
            x + 3,
            PRODUCT_NAME_Y + 3
        ),
        product_name,
        font=font,
        fill="black"
    )


    # --------------------------------------------------------
    # Product name.
    # --------------------------------------------------------

    draw.text(
        (
            x,
            PRODUCT_NAME_Y
        ),
        product_name,
        font=font,
        fill="white"
    )


    return image


# ============================================================
#                     PROCESS ONE IMAGE
# ============================================================

def process_image(
    input_path,
    output_path
):
    """
    Process one Barbie/doll photograph.
    """

    print()
    print()
    print("#" * 65)

    print(
        "PROCESSING:"
    )

    print(
        os.path.basename(
            input_path
        )
    )

    print(
        "#" * 65
    )


    # ========================================================
    # GET PRODUCT NAME FROM FILENAME
    # ========================================================

    filename = os.path.basename(
        input_path
    )


    product_name = get_product_name_from_filename(
        filename
    )


    print()

    print(
        "PRODUCT NAME FROM FILE:"
    )

    print(
        product_name
    )


    # ========================================================
    # OPEN IMAGE
    # ========================================================

    try:

        image = Image.open(
            input_path
        ).convert(
            "RGB"
        )


    except Exception as error:

        print()

        print(
            "ERROR opening image:"
        )

        print(error)

        return False


    # ========================================================
    # SEARCH PRICE
    # ========================================================

    price = search_product_prices(
        product_name
    )


    # ========================================================
    # RESIZE / CROP
    # ========================================================

    image = crop_to_size(
        image,
        OUTPUT_WIDTH,
        OUTPUT_HEIGHT
    )


    # ========================================================
    # ENHANCE IMAGE
    # ========================================================

    image = enhance_image(
        image
    )


    # ========================================================
    # ADD PRICE
    # ========================================================

    image = draw_center_price(
        image,
        price
    )


    # ========================================================
    # ADD PRODUCT NAME
    # ========================================================

    image = draw_product_name(
        image,
        product_name
    )


    # ========================================================
    # SAVE
    # ========================================================

    try:

        image.save(
            output_path,
            "JPEG",
            quality=95,
            optimize=True
        )


    except Exception as error:

        print()

        print(
            "ERROR saving image:"
        )

        print(error)

        return False


    # ========================================================
    # SUCCESS
    # ========================================================

    print()

    print("=" * 65)

    print(
        "IMAGE COMPLETE"
    )

    print(
        f"Product: {product_name}"
    )

    print(
        f"Price: {price}"
    )

    print(
        "Saved:"
    )

    print(
        output_path
    )

    print(
        "=" * 65
    )


    return True


# ============================================================
#                      MAIN PROGRAM
# ============================================================

def main():
    """
    Main program.
    """

    # ========================================================
    # HEADER
    # ========================================================

    print()
    print()

    print("=" * 65)

    print(
        "              BARBIE / DOLL PRICE FINDER"
    )

    print(
        "          GOOGLE PRICE + IMAGE ENHANCER"
    )

    print(
        "                 NO OPENAI API"
    )

    print("=" * 65)


    # ========================================================
    # DISPLAY FOLDERS
    # ========================================================

    print()

    print(
        "Input folder:"
    )

    print(
        INPUT_FOLDER
    )


    print()

    print(
        "Output folder:"
    )

    print(
        OUTPUT_FOLDER
    )


    # ========================================================
    # CHECK INPUT FOLDER
    # ========================================================

    if not os.path.exists(
        INPUT_FOLDER
    ):

        print()

        print(
            "ERROR:"
        )

        print(
            "The input_images folder does not exist."
        )

        print()

        print(
            "Create this folder:"
        )

        print(
            INPUT_FOLDER
        )

        return


    # ========================================================
    # CHECK SERPAPI KEY
    # ========================================================
    if not SERPAPI_KEY:
        print()
        print("WARNING:")
        print("SerpAPI key has not been configured.")
        print()
        print("Open main.py and add your SerpAPI key.")
        return
  


    # ========================================================
    # FIND IMAGES
    # ========================================================

    files = os.listdir(
        INPUT_FOLDER
    )


    image_files = [

        filename

        for filename in files

        if filename.lower().endswith(
            SUPPORTED_EXTENSIONS
        )
    ]


    # ========================================================
    # NO IMAGES
    # ========================================================

    if not image_files:

        print()

        print(
            "=" * 65
        )

        print(
            "NO IMAGES FOUND"
        )

        print(
            "=" * 65
        )

        print()

        print(
            "Put your Barbie/doll images inside:"
        )

        print(
            INPUT_FOLDER
        )

        print()

        print(
            "Supported formats:"
        )

        print(
            "JPG, JPEG, PNG, WEBP, BMP"
        )

        return


    # ========================================================
    # DISPLAY COUNT
    # ========================================================

    print()

    print(
        "=" * 65
    )

    print(
        f"FOUND {len(image_files)} IMAGE(S)"
    )

    print(
        "=" * 65
    )


    # ========================================================
    # COUNTERS
    # ========================================================

    successful = 0

    failed = 0


    # ========================================================
    # PROCESS EACH IMAGE
    # ========================================================

    for filename in image_files:

        # ----------------------------------------------------
        # Input path.
        # ----------------------------------------------------

        input_path = os.path.join(
            INPUT_FOLDER,
            filename
        )


        # ----------------------------------------------------
        # Remove extension.
        # ----------------------------------------------------

        name = os.path.splitext(
            filename
        )[0]


        # ----------------------------------------------------
        # Output filename.
        # ----------------------------------------------------

        output_filename = (
            name +
            "_priced.jpg"
        )


        # ----------------------------------------------------
        # Output path.
        # ----------------------------------------------------

        output_path = os.path.join(
            OUTPUT_FOLDER,
            output_filename
        )


        # ----------------------------------------------------
        # Process.
        # ----------------------------------------------------

        result = process_image(
            input_path,
            output_path
        )


        # ----------------------------------------------------
        # Count.
        # ----------------------------------------------------

        if result:

            successful += 1

        else:

            failed += 1


    # ========================================================
    # FINAL REPORT
    # ========================================================

    print()
    print()

    print("=" * 65)

    print(
        "                    FINISHED"
    )

    print("=" * 65)

    print()

    print(
        f"Images found: "
        f"{len(image_files)}"
    )

    print(
        f"Successfully processed: "
        f"{successful}"
    )

    print(
        f"Failed: "
        f"{failed}"
    )

    print()

    print(
        "Output folder:"
    )

    print(
        OUTPUT_FOLDER
    )

    print()

    print(
        "Finished Barbie/doll advertisements "
        "are ready!"
    )

    print()

    print(
        "=" * 65
    )


# ============================================================
#                       RUN PROGRAM
# ============================================================

if __name__ == "__main__":

    main()