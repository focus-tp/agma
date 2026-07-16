import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Additional Hair services
additional_hair = """
                  <div class="price-row"><span class="price-name">Стрижка женская (короткие волосы, до линии подбородка)</span><span class="price-dots"></span><span class="price-value">3 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Стрижка женская (средние волосы, до лопаток)</span><span class="price-dots"></span><span class="price-value">от 2 800 ₽</span></div>
                  <div class="price-row"><span class="price-name">Стрижка женская (длинные волосы, от лопаток)</span><span class="price-dots"></span><span class="price-value">от 3 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Стрижка + салонный уход</span><span class="price-dots"></span><span class="price-value">4 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция челки</span><span class="price-dots"></span><span class="price-value">от 700 ₽</span></div>
                  <div class="price-row"><span class="price-name">Создание челки</span><span class="price-dots"></span><span class="price-value">от 1 200 ₽</span></div>
                  <div class="price-row"><span class="price-name">Тонирование, окрашивание тон в тон</span><span class="price-dots"></span><span class="price-value">от 5 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Тонирование. Топ мастер</span><span class="price-dots"></span><span class="price-value">от 7 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Трихоскопия</span><span class="price-dots"></span><span class="price-value">1 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Укладка волос на утюг и/или плойку</span><span class="price-dots"></span><span class="price-value">от 2 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция сложного окрашивания</span><span class="price-dots"></span><span class="price-value">от 11 000 ₽</span></div>
"""

# Append to Волосы list before its closing </div>
# Find the exact end of the Волосы list
match = re.search(r'(<div class="price-row"><span class="price-name">Сложное окрашивание. Мастер</span><span class="price-dots"></span><span class="price-value">от 13 000 ₽</span></div>\n\s*)(</div>\n\s*</div>\n\s*<!-- Ногти -->)', html, re.DOTALL)
if match:
    html = html.replace(match.group(0), match.group(1) + additional_hair + match.group(2))

# Nails replacement
new_nails = """
                <div class="price-list">
                  <div class="price-row"><span class="price-name">Френч/втирка/стемпинг ДИЗАЙН 1 шт (1 ноготь)</span><span class="price-dots"></span><span class="price-value">50 ₽</span></div>
                  <div class="price-row"><span class="price-name">ПЛЁНКИ (установка дизайна 1шт)</span><span class="price-dots"></span><span class="price-value">100 ₽</span></div>
                  <div class="price-row"><span class="price-name">Маникюр аппаратный /Комби (без покрытия)</span><span class="price-dots"></span><span class="price-value">от 1 800 ₽</span></div>
                  <div class="price-row"><span class="price-name">Маникюр мужской</span><span class="price-dots"></span><span class="price-value">от 1 800 ₽</span></div>
                  <div class="price-row"><span class="price-name">Маникюр с покрытием ГЕЛЬ ЛАК (укрепление включено)</span><span class="price-dots"></span><span class="price-value">от 2 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Маникюр Японский Masura /P.shine (+аппаратный)</span><span class="price-dots"></span><span class="price-value">от 2 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Наращивание сломанного ногтя 1 шт при выполнении маникюра</span><span class="price-dots"></span><span class="price-value">200 ₽</span></div>
                  <div class="price-row"><span class="price-name">Наращивание ногтей на верхние формы (средние/длинные) квадрат, миндаль, овал, балерина</span><span class="price-dots"></span><span class="price-value">от 3 800 ₽</span></div>
                </div>
                <p style="margin-top:24px; text-align:center;"><a href="https://vk.com/bsekat?w=app5688600_-222253395" target="_blank" class="btn btn-outline" style="font-size: 12px; padding: 10px 20px;">Смотреть полный прайс</a></p>
"""

match_nails = re.search(r'(<h3>Ногти</h3>\s*<span class="accordion-icon"></span>\s*</button>\s*<div class="accordion-content">).*?(</div>\n\s*</div>\n\s*<!-- Макияж -->)', html, re.DOTALL)
if match_nails:
    html = html.replace(match_nails.group(0), match_nails.group(1) + '\n' + new_nails + match_nails.group(2))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added additional services")
