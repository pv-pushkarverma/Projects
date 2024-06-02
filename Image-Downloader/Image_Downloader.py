import tkinter as tk
from tkinter import filedialog, messagebox
import requests
from PIL import Image
from io import BytesIO

def download_image():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to download image: {e}")
        return

    # Ask user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPEG files", "*.jpg"),
                                                        ("All files", "*.*")])
    if not file_path:
        return  # User cancelled the save dialog

    try:
        image = Image.open(BytesIO(response.content))
        image.save(file_path)
        messagebox.showinfo("Success", f"Image successfully saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {e}")

# Set up the main window
root = tk.Tk()
root.title("Image Downloader")

# URL input field
tk.Label(root, text="Image URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Download button
download_button = tk.Button(root, text="Download Image", command=download_image)
download_button.grid(row=1, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()