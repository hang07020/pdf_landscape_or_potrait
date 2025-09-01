# PDF Rotation Tool (GUI)

A simple Python GUI tool to rotate PDF pages by **+90° (clockwise)** or **-90° (counter-clockwise)**.  
The tool automatically renames the output file by appending `_plus90` or `_minus90` to the input filename.

---

## Features
- **GUI-based** (Tkinter) for ease of use  
- Rotate all PDF pages by:
  - +90° (clockwise) → saved as `<filename>_plus90.pdf`  
  - -90° (counter-clockwise) → saved as `<filename>_minus90.pdf`  
- Automatic output file naming, no need to type filenames  
- Uses the actively maintained [pypdf](https://pypi.org/project/pypdf/) library  

---

## Requirements
- Python 3.x  
- Install dependency:
```bash
pip install pypdf
```

---

## Usage
Run the GUI:
```bash
python pdf_rotate_gui.py
```

Steps:
1. Click **Browse** to select your input PDF  
2. Choose rotation: **+90°** or **-90°**  
3. Click **Start**  
4. The rotated file is saved automatically in the same folder as the input file  

---

## Example
Input file:  
```
sample.pdf
```

If rotated **+90°**, the output will be:  
```
sample_plus90.pdf
```

If rotated **-90°**, the output will be:  
```
sample_minus90.pdf
```

---

## Project Structure
```
pdf-rotation-tool/
├── pdf_rotate_gui.py      # Main GUI script
├── samples/
│   └── sample.pdf         # Example input
│   └── sample_plus90.pdf  # Example output(+90°)
│   └── sample_minus90.pdf # Example output(-90°)
```
