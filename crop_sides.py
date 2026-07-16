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
            # Crop top 12% and bottom 15% (same as before)
            top = int(height * 0.12)
            bottom = int(height * 0.85)
            
            # Crop left 8% and right 8% to remove carousel arrows
            left = int(width * 0.08)
            right = int(width * 0.92)
            
            cropped = img.crop((left, top, right, bottom))
            
            if cropped.mode in ("RGBA", "P"):
                cropped = cropped.convert("RGB")
                
            cropped.save(dest, 'JPEG', quality=95)
            print(f"Cropped {src} -> {dest} (L:{left}, T:{top}, R:{right}, B:{bottom})")
