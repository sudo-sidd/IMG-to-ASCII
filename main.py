import argparse
import numpy as np
from PIL import Image
import sys

# Character sets
DEFAULT_CHARS = "@%#*+=-:. "

def get_args():
    parser = argparse.ArgumentParser(description="Convert images to colored ASCII art.")
    parser.add_argument("image", help="Input image file path")
    parser.add_argument("--width", type=int, default=100, help="Output ASCII art width")
    parser.add_argument("--height", type=int, default=None, help="Output ASCII art height (auto if not set)")
    parser.add_argument("--charset", type=str, default=DEFAULT_CHARS, help="Characters to use for ASCII art")
    parser.add_argument("--colormode", choices=["grayscale", "ansi", "rgb"], default="ansi", help="Color mode")
    parser.add_argument("--html", type=str, help="Export as HTML file")
    parser.add_argument("--keep-size", action="store_true", help="Use original image pixel dimensions (no resizing, 1 char per pixel)")
    return parser.parse_args()

def resize_image(img, width, height, keep_size=False):
    if keep_size:
        return img  # preserve original dimensions
    w, h = img.size
    aspect_ratio = h / w
    if height is None:
        height = int(width * aspect_ratio * 0.55)  # font aspect ratio compensation
    return img.resize((width, height))

def map_pixels_to_chars(img, charset):
    # Convert to grayscale for brightness mapping
    gray = np.array(img.convert("L"))
    norm = (gray - gray.min()) / (np.ptp(gray) + 1e-6)
    idx = (norm * (len(charset) - 1)).astype(int)
    return np.array([charset[i] for i in idx.flatten()]).reshape(gray.shape)

def rgb_to_ansi(r, g, b):
    # Convert RGB to nearest ANSI 256 color
    def rgb_to_ansi_code(r, g, b):
        if r == g == b:
            if r < 8: return 16
            if r > 248: return 231
            return int(round(((r - 8) / 247) * 24)) + 232
        return 16 + (36 * int(r / 51)) + (6 * int(g / 51)) + int(b / 51)
    return rgb_to_ansi_code(r, g, b)

def get_color_code(r, g, b, mode):
    if mode == "grayscale":
        return ""
    elif mode == "ansi":
        code = rgb_to_ansi(r, g, b)
        return f"\033[38;5;{code}m"
    elif mode == "rgb":
        return f"\033[38;2;{r};{g};{b}m"
    return ""

def ascii_art(img, charset, colormode):
    img = img.convert("RGB")
    arr = np.array(img)
    chars = map_pixels_to_chars(img, charset)
    lines = []
    for y in range(arr.shape[0]):
        line = ""
        for x in range(arr.shape[1]):
            r, g, b = arr[y, x]
            color = get_color_code(r, g, b, colormode)
            line += f"{color}{chars[y, x]}\033[0m"
        lines.append(line)
    return "\n".join(lines)

def ascii_art_html(img, charset, colormode):
    img = img.convert("RGB")
    arr = np.array(img)
    chars = map_pixels_to_chars(img, charset)
    html_lines = []
    for y in range(arr.shape[0]):
        line = ""
        for x in range(arr.shape[1]):
            r, g, b = arr[y, x]
            char = chars[y, x]
            if colormode == "grayscale":
                style = f"color: rgb({r},{g},{b});"
            elif colormode == "ansi" or colormode == "rgb":
                style = f"color: rgb({r},{g},{b});"
            line += f"<span style='{style}'>{char}</span>"
        html_lines.append(line)
    html = "<pre style='font: 10px/5px monospace; background: #000;'>" + "\n".join(html_lines) + "</pre>"
    return html

def main():
    args = get_args()
    img = Image.open(args.image)
    img = resize_image(img, args.width, args.height, getattr(args, "keep_size", False))
    if args.html:
        html = ascii_art_html(img, args.charset, args.colormode)
        with open(args.html, "w") as f:
            f.write(html)
        print(f"HTML ASCII art saved to {args.html}")
    else:
        art = ascii_art(img, args.charset, args.colormode)
        print(art)

if __name__ == "__main__":
    main()