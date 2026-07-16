with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove inline styles
html = html.replace('style="display: grid; grid-template-columns: 1fr 1.5fr; gap: 40px; align-items: start;"', '')
html = html.replace('style="position: sticky; top: 100px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);"', 'class="services-image-sticky"')
html = html.replace('style="width: 100%; height: auto; display: block;"', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed inline styles.")
