import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add data-image to all price rows if they don't have it
html = re.sub(r'<div class="price-row">(.*?)</div>', r'<div class="price-row" data-image="/master_clean1.jpg">\1</div>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added hover images to all prices.")
