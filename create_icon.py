"""
Convert PNG to ICO for Windows executable icon
"""
from PIL import Image
import sys
from pathlib import Path

def create_icon():
    # Path to logo
    logo_path = Path(__file__).parent / "CLogo.png"
    icon_path = Path(__file__).parent / "CLogo.ico"

    if not logo_path.exists():
        print(f"Error: {logo_path} not found")
        sys.exit(1)

    try:
        # Open the PNG image
        img = Image.open(logo_path)

        # Create multiple sizes for the ICO file
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img_sizes = []

        for size in sizes:
            # Resize image maintaining aspect ratio
            resized = img.copy()
            resized.thumbnail(size, Image.Resampling.LANCZOS)
            img_sizes.append(resized)

        # Save as ICO
        img_sizes[0].save(
            icon_path,
            format='ICO',
            sizes=[(img.width, img.height) for img in img_sizes]
        )

        print(f"[OK] Icon created: {icon_path}")
        return icon_path

    except Exception as e:
        print(f"Error creating icon: {e}")
        sys.exit(1)

if __name__ == "__main__":
    create_icon()
