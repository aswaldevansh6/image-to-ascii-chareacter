from PIL import Image, ImageOps, ImageFilter
import numpy as np

# Different ASCII character styles
ASCII_STYLES = {
    "Standard": "@%#*+=-:. ",
    "Detailed": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "Simple": "#*:. ",
    "Blocks": "█▓▒░ "
}

def load_image(image):
    image = ImageOps.exif_transpose(image)
    return image.convert("RGB")


def preprocess_image(
    image,
    width=100,
    auto_contrast=True,
    edge_enhance=False
):
    gray = image.convert("L")

    if auto_contrast:
        gray = ImageOps.autocontrast(gray)

    if edge_enhance:
        edges = gray.filter(ImageFilter.FIND_EDGES)
        edges = ImageOps.autocontrast(edges)
        edges = ImageOps.invert(edges)
        gray = Image.blend(gray, edges, 0.25)

    aspect_ratio = gray.height / gray.width
    height = max(1, int(width * aspect_ratio * 0.5))

    return gray.resize(
        (width, height),
        Image.Resampling.LANCZOS
    )


def convert_to_ascii(
    image,
    width=100,
    invert=False,
    auto_contrast=True,
    edge_enhance=False,
    style="Standard"
):
    processed_image = preprocess_image(
        image,
        width,
        auto_contrast,
        edge_enhance
    )

    pixels = np.asarray(processed_image, dtype=np.uint8)

    if invert:
        pixels = 255 - pixels

    # Select character pattern
    ascii_chars = ASCII_STYLES.get(
        style, ASCII_STYLES["Standard"]
    )

    char_array = np.array(list(ascii_chars))

    indices = (
        pixels.astype(np.float32)
        * (len(char_array) - 1)
        / 255
    ).astype(np.int32)

    ascii_array = char_array[indices]

    ascii_text = "\n".join(
        "".join(row) for row in ascii_array
    )

    return ascii_text, processed_image
