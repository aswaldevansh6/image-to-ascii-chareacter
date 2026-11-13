
import matplotlib.pyplot as plt


def display_images(original, grayscale):

    # Create two side-by-side plots
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Original image
    axes[0].imshow(original)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    # Grayscale image
    axes[1].imshow(grayscale, cmap="gray")
    axes[1].set_title("Grayscale Image")
    axes[1].axis("off")

    plt.tight_layout()

    return fig
