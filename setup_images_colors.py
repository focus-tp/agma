import re
import glob
import shutil
import os

# 1. Copy images
source_dir = "/Users/tanya/.gemini/antigravity-ide/brain/937f7bd0-3170-4bcd-8dd0-daf73ae69110/"
dest_dir = "public/"

images = glob.glob(source_dir + "category_*.png")
img_map = {}

for img_path in images:
    filename = os.path.basename(img_path)
    # Extract the base category name, e.g., category_hair
    match = re.match(r'(category_[a-z]+)_.*\.png', filename)
    if match:
        base_name = match.group(1)
        new_name = base_name + ".png"
        shutil.copy(img_path, os.path.join(dest_dir, new_name))
        img_map[base_name] = "/" + new_name

print("Images copied:", img_map)

# 2. Update CSS: Change accent color to Rose Gold and resize hover image
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change accent color
css = re.sub(r'--color-accent:\s*#[a-fA-F0-9]+;', '--color-accent: #E3C2B0;', css)

# Change hover image size
css = re.sub(
    r'width: 250px; height: 350px;',
    'width: 160px; height: 220px;',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update HTML: Map categories to specific images
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to map specific accordion contents to specific images.
# This requires parsing the HTML and replacing the data-image attribute inside each accordion.
# Let's define the mapping from Accordion Header text to image
category_mapping = {
    'Брови': '/category_brows.png',
    'Перманентный макияж': '/category_pm.png',
    'Волосы': '/category_hair.png',
    'Ногти': '/category_nails.png',
    'Ресницы': '/category_lashes.png',
    'Макияж': '/category_makeup.png',
    'Лицо': '/category_face.png',
    'Обучение': '/category_education.png'
}

# The easiest way is to split by accordion item
items = re.split(r'(<div class="accordion-item">)', html)
new_html = ""
current_category = "/master_clean1.jpg" # fallback

for block in items:
    # Check if this block contains an accordion header
    header_match = re.search(r'<button class="accordion-header">\s*<h3>(.*?)</h3>', block)
    if header_match:
        cat_name = header_match.group(1).strip()
        if cat_name in category_mapping:
            current_category = category_mapping[cat_name]
    
    # Replace any data-image inside this block with current_category
    block = re.sub(r'data-image="[^"]+"', f'data-image="{current_category}"', block)
    new_html += block

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML and CSS updated.")
