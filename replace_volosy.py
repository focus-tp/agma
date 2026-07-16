import re

new_volosy_html = """
                <div class="price-list">
                  <div class="price-row"><span class="price-name">AirTouch (аиртач)</span><span class="price-dots"></span><span class="price-value">от 14 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Бесплатная Консультация</span><span class="price-dots"></span><span class="price-value">0 ₽</span></div>
                  <div class="price-row"><span class="price-name">БИОзавивка волос</span><span class="price-dots"></span><span class="price-value">от 12 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Выход из темного</span><span class="price-dots"></span><span class="price-value">от 15 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Идеальный блонд. Мастер</span><span class="price-dots"></span><span class="price-value">от 6 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Идеальный блонд. Топ Мастер</span><span class="price-dots"></span><span class="price-value">от 9 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Контуринг. Мастер</span><span class="price-dots"></span><span class="price-value">от 7 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Контуринг. Топ Мастер</span><span class="price-dots"></span><span class="price-value">от 9 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Мытье головы и сушка по форме стрижки</span><span class="price-dots"></span><span class="price-value">от 1 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Мытье головы ПЕРЕД УКЛАДКОЙ</span><span class="price-dots"></span><span class="price-value">от 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Окрашивание в 1 тон. На тон светлее или темнее. Мастер</span><span class="price-dots"></span><span class="price-value">от 5 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Окрашивание в 1 тон. На тон светлее или темнее. Топ мастер</span><span class="price-dots"></span><span class="price-value">от 7 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Рассветление прядей (блики) - доп услуга к окрашиванию</span><span class="price-dots"></span><span class="price-value">от 2 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Окрашивание корней. Мастер</span><span class="price-dots"></span><span class="price-value">от 4 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Окрашивание корней. Топ Мастер</span><span class="price-dots"></span><span class="price-value">от 5 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Пилинг кожи головы (доп. услуга)</span><span class="price-dots"></span><span class="price-value">400 ₽</span></div>
                  <div class="price-row"><span class="price-name">Подравнивание кончиков</span><span class="price-dots"></span><span class="price-value">от 1 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Прическа</span><span class="price-dots"></span><span class="price-value">от 3 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Профессиональный салонный уход для волос</span><span class="price-dots"></span><span class="price-value">от 2 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Сложное окрашивание. Топ мастер</span><span class="price-dots"></span><span class="price-value">от 18 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Сложное окрашивание. Мастер</span><span class="price-dots"></span><span class="price-value">от 13 000 ₽</span></div>
                </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the content inside the "Волосы" accordion content div
html = re.sub(r'(<h3>Волосы</h3>\s*<span class="accordion-icon"></span>\s*</button>\s*<div class="accordion-content">).*?(</div>\n\s*</div>\n\s*<!-- Ногти -->)', 
              r'\1\n' + new_volosy_html + r'\2', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated volosy prices.")
