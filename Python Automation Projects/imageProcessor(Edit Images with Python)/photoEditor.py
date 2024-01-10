# python3 -m pip install --upgrade Pillow
from PIL import Image, ImageEnhance, ImageFilter
import os

# Get the relative path to the 'images' folder
path = os.path.join(os.path.dirname(__file__), 'images')

#  Get the relative path to the 'editedImages' folder
path_out = os.path.join(os.path.dirname(__file__), 'editedImages')

# Create the output directory if it doesn't exist
os.makedirs(path_out, exist_ok=True)

# Filter out non-image files
image_files = [filename for filename in os.listdir(path) if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]


for filename in image_files:
    img = Image.open(os.path.join(path, filename))

#   Sharpen image, turn it into greyscale, and rotate the image
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

#   Increasing contrast
    enhancer = ImageEnhance.Contrast(edit)
    factor = 2.0  # You can adjust this factor to control the contrast
    edit = enhancer.enhance(factor)

    cleaned_name = os.path.splitext(filename)[0]  # Use os.path.splitext to get the filename without extension

#     Save the edited image in the 'editedImages' folder
    edit.save(os.path.join(path_out, f"{cleaned_name}_edited.jpg"))
