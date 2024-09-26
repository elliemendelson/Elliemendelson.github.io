import os
from PIL import Image

# Set the directory containing your images and the directory for thumbnails
image_dir = 'art-microcopy'
thumbnail_dir = "art-microcopy\_thumbs"

# Make the thumbnails directory if it doesn't exist
if not os.path.exists(thumbnail_dir):
    os.makedirs(thumbnail_dir)

# Set the size for the thumbnails
thumbnail_size = (400, 400)

# Iterate through the image directory
for filename in os.listdir(image_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(image_dir, filename)
        img = Image.open(img_path)
        img.thumbnail(thumbnail_size)
        base_name, ext = os.path.splitext(filename)
        filename = base_name + 'thumb' + ext
        # Save the thumbnail to the thumbnails directory
        thumb_path = os.path.join(thumbnail_dir, filename)
        img.save(thumb_path,"JPEG")
        print(f"Thumbnail for {filename} created.")
