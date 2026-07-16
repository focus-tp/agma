import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Favicon
html = re.sub(
    r'<link rel="icon" type="image/svg\+xml" href="/vite.svg" />',
    '<link rel="icon" type="image/jpeg" href="/logo.jpg" />',
    html
)

# 2. Header logo
html = html.replace(
    '<img src="/logo.jpg" alt="Beauty Sekta" class="header-logo" />',
    '<div class="logo logo-difference">Beauty Sekta</div>'
)

# 3. Add Marquee to manifesto section
marquee_html = """
        <div class="marquee-bg">
          <div class="marquee-content">
            <span>ТВОЯ КРАСОТА • ТВОЯ СЕКТА • </span>
            <span>ТВОЯ КРАСОТА • ТВОЯ СЕКТА • </span>
            <span>ТВОЯ КРАСОТА • ТВОЯ СЕКТА • </span>
            <span>ТВОЯ КРАСОТА • ТВОЯ СЕКТА • </span>
          </div>
        </div>
"""
html = html.replace('<section class="manifesto section-dark" id="manifesto">', '<section class="manifesto section-dark" id="manifesto">\n' + marquee_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML Updated.")
