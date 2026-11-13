
import streamlit as st
from PIL import Image
from io import BytesIO
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def create_color_ascii_image(image, ascii_text):
    pixels = np.asarray(image.convert("RGB"))

    lines = ascii_text.splitlines()
    height = len(lines)
    width = len(lines[0])

    resized = image.resize((width, height))

    colors = np.asarray(resized.convert("RGB"))

    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    ax.set_xlim(0, width)
    ax.set_ylim(height, 0)
    ax.axis("off")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            color = colors[y, x] / 255.0

            ax.text(
                x, y, char,
                color=color,
                fontfamily="monospace",
                fontsize=8
            )

    plt.subplots_adjust(0, 0, 1, 1)
    return fig

from ascii_converter import (
    load_image,
    convert_to_ascii,
    ASCII_STYLES
)
from visualization import display_images

st.set_page_config(
    page_title="Smart ASCII Studio",
    page_icon="🖼️",
    layout="wide"
)

st.markdown("""
<style>
/* Dark upload section */
[data-testid="stFileUploader"] section {
    background: #1e293b !important;
    border: 1px dashed #8b5cf6 !important;
    border-radius: 12px !important;
}

[data-testid="stFileUploader"] section > div {
    background: transparent !important;
}

/* Upload text */
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span {
    color: #e2e8f0 !important;
}

/* Upload button */
[data-testid="stFileUploader"] button {
    background: #312e81 !important;
    color: white !important;
    border: 1px solid #8b5cf6 !important;
}

/* Empty-state information message */
[data-testid="stAlert"] {
    background: #1e293b !important;
    color: #e2e8f0 !important;
    border: 1px solid #37345c !important;
    border-radius: 12px !important;
}

/* Alert text and icons */
[data-testid="stAlert"] p,
[data-testid="stAlert"] svg {
    color: #cbd5e1 !important;
    fill: #cbd5e1 !important;
}

/* Fix top Streamlit toolbar */
[data-testid="stHeader"] {
    background: #0b1020 !important;
}

/* Toolbar icons and buttons */
[data-testid="stToolbar"] {
    background: transparent !important;
}

/* Deploy menu text */
[data-testid="stAppDeployButton"] {
    color: #e9d5ff !important;
}

/* Header action buttons */
[data-testid="stHeader"] button {
    color: #e9d5ff !important;
}

/* Keep the top-right menu area dark */
[data-testid="stDecoration"] {
    background: transparent !important;
}

/* Main background */
.stApp {
    background: linear-gradient(
        135deg,
        #0b1020 0%,
        #111827 50%,
        #17132e 100%
    );
    color: #f1f5f9;
}

/* Main content */
.block-container {
    padding-top: 2rem;
    max-width: 1400px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #101426;
    border-right: 1px solid #292d48;
}

/* Headings */
h1, h2, h3 {
    color: #e9d5ff !important;
}

/* Paragraphs */
p, label, .stMarkdown {
    color: #cbd5e1;
}

/* Cards and containers */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(30, 41, 70, 0.55);
    border: 1px solid #34345c;
    border-radius: 16px;
    padding: 12px;
}

/* Buttons */
.stDownloadButton button {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    padding: 10px 20px;
}

.stDownloadButton button:hover {
    background: linear-gradient(90deg, #6d28d9, #1d4ed8);
    color: white;
    border: none;
}

/* Upload area */
[data-testid="stFileUploader"] {
    background: rgba(30, 41, 70, 0.5);
    border: 1px dashed #8b5cf6;
    border-radius: 14px;
    padding: 15px;
}

/* Input widgets */
.stSelectbox, .stSlider, .stCheckbox {
    color: white;
}

/* Code output */
.stCodeBlock {
    border: 1px solid #37345c;
    border-radius: 12px;
}

/* Dividers */
hr {
    border-color: #34345c;
}
</style>
""", unsafe_allow_html=True)

st.title("🖼️ Smart ASCII Studio")
st.write(
    "Transform images into ASCII art using "
    "adaptive image processing."
)

st.divider()

# Sidebar settings
st.sidebar.header("Conversion Settings")

width = st.sidebar.slider(
    "ASCII Output Width",
    min_value=40,
    max_value=200,
    value=100,
    step=10
)

invert = st.sidebar.checkbox(
    "Invert Brightness",
    value=False
)

auto_contrast = st.sidebar.checkbox(
    "Adaptive Contrast",
    value=True
)

edge_enhance = st.sidebar.checkbox(
    "Edge-Aware Enhancement",
    value=False
)

style = st.sidebar.selectbox(
    "Choose ASCII Style",
    options=list(ASCII_STYLES.keys())
)

compare_mode = st.sidebar.checkbox(
    "Enable Comparison Mode",
    value=False
)

# Upload image
input_method = st.radio(
    "Choose Image Source",
    ["Upload Image", "Take Photo"],
    horizontal=True
)

if input_method == "Upload Image":
    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )
else:
    uploaded_file = st.camera_input("Take a picture")

if uploaded_file is not None:
    try:
        image_bytes = uploaded_file.getvalue()

        original_image = Image.open(
            BytesIO(image_bytes)
        )

        original_image = load_image(original_image)

        # Generate selected ASCII output
        ascii_output, grayscale_image = convert_to_ascii(
            original_image,
            width,
            invert,
            auto_contrast,
            edge_enhance,
            style
        )

        st.success("Image processed successfully!")

        st.subheader("Image Processing Results")

        fig = display_images(
            original_image,
            grayscale_image
        )

        st.pyplot(fig)
        plt.close(fig)

        st.divider()

        # Comparison mode
        if compare_mode:
            normal_output, _ = convert_to_ascii(
                original_image,
                width,
                invert,
                False,
                False,
                style
            )

            st.subheader("ASCII Output Comparison")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Normal ASCII Output**")
                st.code(normal_output, language="text")

            with col2:
                st.markdown("**Enhanced ASCII Output**")
                st.code(ascii_output, language="text")

        else:
            st.subheader("ASCII Art Output")
            st.code(ascii_output, language="text")

        # Save output
        output_folder = Path("output")
        output_folder.mkdir(exist_ok=True)

        output_path = output_folder / "ascii_output.txt"
        output_path.write_text(
            ascii_output,
            encoding="utf-8"
        )

        st.download_button(
            label="⬇️ Download ASCII Text",
            data=ascii_output,
            file_name="ascii_output.txt",
            mime="text/plain"
        )
        # Convert ASCII text into PNG image
        png_buffer = BytesIO()

        fig, ax = plt.subplots(figsize=(12, 8))
        fig.patch.set_facecolor("black")
        ax.set_facecolor("black")

        ax.text(
            0.02,
            0.98,
            ascii_output,
            fontfamily="monospace",
            fontsize=6,
            color="white",
            verticalalignment="top"
        )

        ax.axis("off")
        plt.savefig(
            png_buffer,
            format="png",
            facecolor="black",
            bbox_inches="tight",
            dpi=200
        )
        plt.close(fig)

        st.download_button(
            label="⬇️ Download ASCII Art as PNG",
            data=png_buffer.getvalue(),
            file_name="ascii_art.png",
            mime="image/png"
        )
        st.divider()
        st.subheader("Color ASCII Art")

        color_fig = create_color_ascii_image(
            original_image,
            ascii_output
        )

        st.pyplot(color_fig)

        color_buffer = BytesIO()

        color_fig.savefig(
            color_buffer,
            format="png",
            facecolor="black",
            bbox_inches="tight",
            dpi=200
        )

        plt.close(color_fig)

        st.download_button(
            label="Download Color ASCII Art",
            data=color_buffer.getvalue(),
            file_name="color_ascii_art.png",
            mime="image/png"
        )
        lines = ascii_output.splitlines()

        st.info(
            f"Output dimensions: {len(lines[0])} columns × "
            f"{len(lines)} rows | Style: {style}"
        )

    except Exception as error:
        st.error(f"Unable to process image: {error}")

else:
    st.info("Please upload a JPG or PNG image to get started.")

    st.subheader("Features")
    st.markdown("""
    - Adaptive Contrast
    - Edge-Aware Enhancement
    - Multiple ASCII Styles
    - Normal vs Enhanced Comparison
    - Downloadable ASCII Output
    """)
