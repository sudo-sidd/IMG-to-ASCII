# IMG-to-ASCII

Convert images to colored ASCII art in your terminal or export as HTML.

## Features

- Adjustable output resolution (`--width`, `--height`)
- Character set selection (`--charset`)
- Color modes: Grayscale, ANSI 256-color, TrueColor RGB
- Export to HTML with preserved color and spacing

## Requirements

- Python 3.8+
- [Pillow](https://pypi.org/project/Pillow/)
- [numpy](https://pypi.org/project/numpy/)

Install dependencies:

```fish
pip install pillow numpy
```

## Usage

### Terminal Output (ANSI 256-color)

```fish
python main.py image.png --width 100 --colormode ansi
```

### Terminal Output (TrueColor RGB)

```fish
python main.py image.png --width 100 --colormode rgb
```

### Grayscale Output

```fish
python main.py image.png --width 100 --colormode grayscale
```

### Custom Character Set

```fish
python main.py image.png --width 100 --charset " .:-=+*#%@"
```

### Export as HTML

```fish
python main.py image.png --width 100 --colormode rgb --html output.html
```

## Notes

- The image file must exist in the current directory or provide the correct path.
- For best color, use `--colormode rgb`.
- Adjust `--width` and `--height` for desired output size.

## Example

![Example](siddharth.png)

---

Created by sudo-sidd
