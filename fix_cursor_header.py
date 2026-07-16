import re

# 1. Restore Custom Cursor in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cursor_html = """
    <!-- Custom Cursor -->
    <div class="custom-cursor" id="custom-cursor">
      <div class="cursor-text">Смотреть</div>
    </div>
"""
if '<div class="custom-cursor"' not in html:
    html = html.replace('<body>', '<body>\n' + cursor_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Fix CSS: restore cursor: none and update header background
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove my previous override that made header fully transparent
css = re.sub(
    r'\.header \{\n\s*background: transparent !important;\n\s*backdrop-filter: none !important;\n\s*border-bottom: none !important;\n\}',
    '''
.header.scrolled {
  background: rgba(14, 14, 14, 0.8) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
}
''',
    css
)

# Add cursor:none back to the top of the file
if 'cursor: none;' not in css:
    css = '''* {
  cursor: none !important;
}
''' + css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Cursor and Header fixed.")
