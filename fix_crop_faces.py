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
            # The text starts around the middle of the image.
            # Instagram top UI is about 8-10%.
            # Let's crop from 10% to 50% to get just the head and shoulders, no text.
            top = int(height * 0.09)
            bottom = int(height * 0.50)
            
            cropped = img.crop((0, top, width, bottom))
            
            if cropped.mode in ("RGBA", "P"):
                cropped = cropped.convert("RGB")
                
            cropped.save(dest, 'JPEG', quality=95)
            print(f"Cropped {src} -> {dest} (top: {top}, bottom: {bottom})")
    else:
        print(f"Not found: {src}")
