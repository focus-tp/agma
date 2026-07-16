import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the old line
old_line = '<div class="price-row"><span class="price-name">Бесплатная Консультация</span><span class="price-dots"></span><span class="price-value">0 ₽</span></div>\n'
html = html.replace(old_line, '')
# Also handle case without newline
old_line2 = '<div class="price-row"><span class="price-name">Бесплатная Консультация</span><span class="price-dots"></span><span class="price-value">0 ₽</span></div>'
html = html.replace(old_line2, '')

# Find the start of the Волосы price list
# Specifically before AirTouch
airtouch_line = '<div class="price-row"><span class="price-name">AirTouch (аиртач)</span>'
new_line = '                  <div class="price-row"><span class="price-name">Консультация</span><span class="price-dots"></span><span class="price-value">0 р</span></div>\n'

html = html.replace(airtouch_line, new_line + '                  ' + airtouch_line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated consultation")
