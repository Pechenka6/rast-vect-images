import os
from tkinter import Tk, Label, Button, Entry, filedialog, Frame, Scrollbar, Listbox
from PIL import Image

def get_image_info(directory):
    image_info_list = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.gif', '.tif', '.bmp', '.png', '.pcx')):
            try:
                img = Image.open(os.path.join(directory, filename))
                info = {
                    'filename': filename,
                    'size': f"{img.size[0]} x {img.size[1]}",
                    'dpi': img.info.get('dpi', 'N/A'),
                    'color_depth': img.mode,
                    'compression': img.info.get('compression', 'N/A')
                }
                image_info_list.append(info)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    return image_info_list

def load_directory():
    directory = filedialog.askdirectory()
    if directory:
        image_info = get_image_info(directory)
        display_info(image_info)

def display_info(image_info):
    listbox.delete(0, 'end')
    for info in image_info:
        listbox.insert('end', f"{info['filename']}: {info['size']}, DPI: {info['dpi']}, Color Depth: {info['color_depth']}, Compression: {info['compression']}")


root = Tk()
root.title("Image Info Reader")

frame = Frame(root)
frame.pack(pady=10)
entry = Entry(frame, width=50)
entry.pack(side='left')
button_browse = Button(frame, text="Browse", command=load_directory)
button_browse.pack(side='left')

listbox = Listbox(root, width=80, height=20)
listbox.pack(pady=10)

scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()
