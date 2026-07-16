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
            # Remove only Instagram UI: top 12% and bottom 15%
            top = int(height * 0.12)
            bottom = int(height * 0.85)
            
            cropped = img.crop((0, top, width, bottom))
            
            if cropped.mode in ("RGBA", "P"):
                cropped = cropped.convert("RGB")
                
            cropped.save(dest, 'JPEG', quality=95)
            print(f"Cropped {src} -> {dest} (top: {top}, bottom: {bottom})")
