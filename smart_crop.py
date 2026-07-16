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
            
            # 1. Crop Instagram UI (top 12%, bottom 15%)
            top = int(height * 0.12)
            bottom = int(height * 0.85)
            cropped = img.crop((0, top, width, bottom))
            
            # 2. "Clone stamp" the arrows on the left and right edges.
            # The cropped image has its own width and height.
            cw, ch = cropped.size
            
            # The arrows are usually perfectly centered vertically in the original image.
            # The original center was height / 2.
            # In the cropped image, that center is at (height / 2) - top.
            arrow_center_y = int((height * 0.5) - top)
            
            # Arrow height is roughly 100 pixels. We'll cover 160 pixels to be safe.
            arrow_h = 160
            # Arrow width is roughly 60 pixels.
            arrow_w = 60
            
            y1 = arrow_center_y - (arrow_h // 2)
            y2 = y1 + arrow_h
            
            # If the arrow is near text, wait, text is lower down. The arrow is at the exact vertical center.
            # We will grab a patch from just ABOVE the arrow (y1 - arrow_h to y1)
            # Left patch
            try:
                left_patch = cropped.crop((0, y1 - arrow_h, arrow_w, y1))
                cropped.paste(left_patch, (0, y1))
            except Exception as e:
                pass
                
            # Right patch
            try:
                right_patch = cropped.crop((cw - arrow_w, y1 - arrow_h, cw, y1))
                cropped.paste(right_patch, (cw - arrow_w, y1))
            except Exception as e:
                pass

            if cropped.mode in ("RGBA", "P"):
                cropped = cropped.convert("RGB")
                
            cropped.save(dest, 'JPEG', quality=95)
            print(f"Processed {src} -> {dest}")
