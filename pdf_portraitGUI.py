import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def rotate_pdf(input_path, rotation):
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page in reader.pages:
            if rotation == "+90":
                rotated_page = page.rotate(90)  # clockwise
            elif rotation == "-90":
                rotated_page = page.rotate(-90)  # counter-clockwise
            else:
                rotated_page = page
            writer.add_page(rotated_page)

        # Auto-generate output filename
        input_file = Path(input_path)
        suffix = "_plus90" if rotation == "+90" else "_minus90"
        output_file = input_file.with_stem(input_file.stem + suffix)

        with open(output_file, "wb") as f:
            writer.write(f)

        messagebox.showinfo("Success", f"PDF saved as:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def select_input():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if file_path:
        input_var.set(file_path)


def start_rotation():
    input_path = input_var.get()
    rotation = rotation_var.get()

    if not input_path:
        messagebox.showwarning("Warning", "Please select an input file.")
        return

    rotate_pdf(input_path, rotation)


# --- GUI setup ---
root = tk.Tk()
root.title("PDF Rotation Tool")
root.geometry("400x200")

input_var = tk.StringVar()
rotation_var = tk.StringVar(value="+90")

tk.Label(root, text="Input PDF:").pack(pady=5)
tk.Entry(root, textvariable=input_var, width=50).pack()
tk.Button(root, text="Browse", command=select_input).pack(pady=5)

tk.Label(root, text="Rotation:").pack(pady=5)
tk.Radiobutton(root, text="Rotate +90° (clockwise)", variable=rotation_var, value="+90").pack()
tk.Radiobutton(root, text="Rotate -90° (counter-clockwise)", variable=rotation_var, value="-90").pack()

tk.Button(root, text="Start", command=start_rotation).pack(pady=15)

root.mainloop()
