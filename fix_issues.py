import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Cursor: remove custom cursor html
html = re.sub(r'<div class="custom-cursor".*?</div>', '', html, flags=re.DOTALL)

# 2. Large text dots: remove dot from hero title
html = html.replace('Твоя красота.<br>Твоя секта.', 'Твоя красота<br>Твоя секта')

# And remove dots from marquee just in case
html = html.replace('ТВОЯ КРАСОТА • ТВОЯ СЕКТА •', 'ТВОЯ КРАСОТА ТВОЯ СЕКТА')

# 3. Hero subtitle: new line before 'Закрытое'
html = html.replace(
    'Премиальный салон красоты в Екатеринбурге. Закрытое комьюнити',
    'Премиальный салон красоты в Екатеринбурге.<br>Закрытое комьюнити'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Now fix CSS to remove cursor: none
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('cursor: none;', '')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed issues.")
