import tkinter as tk
from PIL import Image, ImageTk

# Initialize Tkinter
root = tk.Tk()
root.geometry("480x320")  # Set this based on your Waveshare display resolution (480x320)
# Set the window to fullscreen
root.attributes("-fullscreen", True)

# Allow exiting fullscreen with the "Escape" key
def exit_fullscreen(event):
    root.attributes("-fullscreen", False)
# Load the image using Pillow
image_path = "test.png"  # Replace with the path to your image
image = Image.open(image_path)

# Resize the image to fit the screen if needed (optional)
image = image.resize((480, 320))

# Convert the image to a Tkinter-compatible format
tk_image = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=tk_image)
label.pack()

# Start the Tkinter event loop
root.mainloop()