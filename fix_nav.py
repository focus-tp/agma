with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="#services_price"', 'href="#services"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Nav fixed")
