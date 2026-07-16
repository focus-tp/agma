from PIL import Image
import os

images = {
    'public/Alexandra.png': 'public/master1.jpg',
    'public/Nataly.png': 'public/master2.jpg',
    'public/Anastasiya.png': 'public/master3.jpg',
    'public/Ekaterina.png': 'public/master4.jpg'
}

for src, dest in images.items():
    if os.path.exists(src):
        with Image.open(src) as img:
            width, height = img.size
            # Crop top 75% of the image to remove instagram text/dots at bottom
            # Actually, usually text is in the lower half. 
            # Let's crop from top=0 to bottom = height * 0.70
            new_height = int(height * 0.70)
            cropped = img.crop((0, 0, width, new_height))
            # Convert to RGB to save as jpg
            if cropped.mode in ("RGBA", "P"):
                cropped = cropped.convert("RGB")
            cropped.save(dest, 'JPEG', quality=95)
            print(f"Cropped {src} -> {dest}")
