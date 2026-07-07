"""
Convert PNG to ICO for Windows executable icon
Improved version for better quality icons
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
        img = Image.open(logo_path).convert("RGBA")

        # Create a square image (crop to center if needed)
        width, height = img.size
        min_dim = min(width, height)

        # Center crop to make it square
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        right = left + min_dim
        bottom = top + min_dim
        img = img.crop((left, top, right, bottom))

        # Create multiple sizes for the ICO file
        # These are the standard Windows icon sizes
        sizes = [16, 32, 48, 64, 128, 256]
        img_sizes = []

        for size in sizes:
            # Resize using high-quality resampling
            resized = img.resize((size, size), Image.Resampling.LANCZOS)
            img_sizes.append(resized)

        # Save as ICO with all sizes
        img_sizes[0].save(
            icon_path,
            format='ICO',
            sizes=[(size, size) for size in sizes]
        )

        print(f"[OK] Icon created: {icon_path}")
        print(f"Sizes: {sizes}")
        return icon_path

    except Exception as e:
        print(f"Error creating icon: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    create_icon()
