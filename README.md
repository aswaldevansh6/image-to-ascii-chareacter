# 🖼️ Smart ASCII Studio

**Transform ordinary images into creative ASCII art using Python and image processing.**

Smart ASCII Studio is a Python-based image processing application that converts digital images into ASCII art using pixel intensity mapping. It provides multiple character styles, image enhancement, color ASCII rendering, and downloadable outputs through an interactive Streamlit interface.

## 📌 Problem Statement

Digital images contain visual information represented by pixels. This project explores how pixel brightness and image processing techniques can be used to represent images using text characters.

The goal is to develop an interactive application that converts images into readable and creative ASCII artwork.

## ✨ Features

- Upload JPG and PNG images.
- Capture images directly using the camera.
- Convert images into grayscale.
- Resize images and adjust ASCII output width.
- Map pixel brightness to ASCII characters.
- Multiple ASCII character styles.
- Invert image brightness.
- Adaptive contrast enhancement.
- Edge-aware image enhancement.
- Compare normal and enhanced ASCII output.
- Generate color ASCII art.
- Download ASCII output as TXT.
- Download ASCII artwork as PNG.
- Download color ASCII artwork as PNG.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| Pillow (PIL) | Image loading and processing |
| NumPy | Pixel manipulation and array operations |
| Matplotlib | Image visualization and PNG generation |

## ⚙️ How It Works

1. The user uploads an image or captures a photo.
2. The image is loaded and converted into RGB format.
3. The image is converted into grayscale.
4. Image enhancement techniques can be applied.
5. Pixel brightness values are mapped to ASCII characters.
6. The characters are arranged into rows to generate ASCII art.
7. The result can be previewed and downloaded in different formats.

## 📂 Project Structure

```text
Smart-ASCII-Studio/
│
├── app.py
├── ascii_converter.py
├── visualization.py
├── requirements.txt
├── README.md
│
└── output/
    └── ascii_output.txt
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/deva965/Smart-ASCII-Studio.git
```

### 2. Open the project folder

```bash
cd Smart-ASCII-Studio
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

### 5. Open in browser

```text
http://localhost:8501
```

## 📸 Application Screenshots

### 1. Main Interface
![Main Interface](screenshots/main-interface.png)

### 2. ASCII Conversion Output
![ASCII Output](screenshots/ascii-output.png)

### 3. Color ASCII Output
![Color ASCII Output](screenshots/color-output.png)

## 🔮 Future Enhancements

- Real-time video-to-ASCII conversion.
- More advanced character mapping algorithms.
- Additional image enhancement techniques.
- Custom ASCII character sets.
- More export and customization options.

## 🎯 Applications

- Digital art and creative typography.
- Learning image processing concepts.
- Text-based image representation.
- Educational demonstrations of pixel manipulation.

## 👨‍💻 Developed With

**Python | Streamlit | Pillow | NumPy | Matplotlib**

**Project:** Smart ASCII Studio
