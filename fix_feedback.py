import re

# 1. Restore Color in style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('--color-accent: #7a1a26;', '--color-accent: #d4af37;')

# Remove Noise Overlay CSS
css = re.sub(r'/\* 1\. Film Grain Overlay \*/[\s\S]*?/\* 2\. Text Reveal Animation \*/', '/* 2. Text Reveal Animation */', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Remove Noise Overlay HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<div id="noise-overlay"></div>', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed flickering and color.")
