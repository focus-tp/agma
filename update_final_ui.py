import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the button
button_str = '<p style="margin-top:24px; text-align:center;"><a href="https://vk.com/bsekat?w=app5688600_-222253395" target="_blank" class="btn btn-outline" style="font-size: 12px; padding: 10px 20px;">Смотреть полный прайс</a></p>'
html = html.replace(button_str, '')

# 2. Replace the map placeholder with Yandex map iframe
map_regex = r'<div class="map-placeholder">.*?</div>'
yandex_map = '<iframe src="https://yandex.ru/map-widget/v1/?mode=search&text=Екатеринбург,+ул.+Начдива+Васильева,+14/2&z=16" width="100%" height="400" frameborder="1" allowfullscreen="true" style="position:relative; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);"></iframe>'
html = re.sub(map_regex, yandex_map, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated UI")
