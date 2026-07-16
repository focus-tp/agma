import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Clear data-image from all price-rows
html = re.sub(r'<div class="price-row" data-image="[^"]+">', '<div class="price-row">', html)

# Add data-image to accordion headers
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

def replace_header(match):
    full_match = match.group(0)
    title = match.group(1).strip()
    if title in category_mapping:
        img_src = category_mapping[title]
        # Replace the opening button tag to include data-image
        return full_match.replace('<button class="accordion-header">', f'<button class="accordion-header" data-image="{img_src}">')
    return full_match

html = re.sub(r'<button class="accordion-header">\s*<h3>(.*?)</h3>', replace_header, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update main.js
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the previous hover image logic
old_logic = """    const priceRows = document.querySelectorAll('.price-row[data-image]');"""
new_logic = """    const priceRows = document.querySelectorAll('.accordion-header[data-image]');"""
js = js.replace(old_logic, new_logic)

# Replace the mouseenter logic
old_mouseenter = """        const imageUrl = row.getAttribute('data-image');
        hoverImageEl.style.backgroundImage = `url(${imageUrl})`;
        hoverImageEl.classList.add('active');
        hoverImageEl.style.left = (e.clientX + 50) + 'px';
        hoverImageEl.style.top = (e.clientY) + 'px';"""

new_mouseenter = """        if (!row.parentElement.classList.contains('active')) {
          const imageUrl = row.getAttribute('data-image');
          hoverImageEl.style.backgroundImage = `url(${imageUrl})`;
          hoverImageEl.classList.add('active');
          hoverImageEl.style.left = (e.clientX + 50) + 'px';
          hoverImageEl.style.top = (e.clientY) + 'px';
        }"""
js = js.replace(old_mouseenter, new_mouseenter)

# Add click logic to hide image when opened
if "row.addEventListener('click'" not in js:
    hide_on_click = """      row.addEventListener('click', () => {
        hoverImageEl.classList.remove('active');
      });
"""
    # Insert before mouseleave
    js = js.replace("      row.addEventListener('mouseleave', () => {", hide_on_click + "      row.addEventListener('mouseleave', () => {")

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated hover logic.")
