import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Макияж
makiyazh = """
                <div class="price-list">
                  <div class="price-row"><span class="price-name">Вечерний макияж</span><span class="price-dots"></span><span class="price-value">от 2 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Дневной макияж</span><span class="price-dots"></span><span class="price-value">от 2 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Образ (макияж + укладка)</span><span class="price-dots"></span><span class="price-value">от 4 800 ₽</span></div>
                  <div class="price-row"><span class="price-name">Экспресс макияж</span><span class="price-dots"></span><span class="price-value">от 1 600 ₽</span></div>
                </div>
"""
match_makiyazh = re.search(r'(<h3>Макияж</h3>\s*<span class="accordion-icon"></span>\s*</button>\s*<div class="accordion-content">).*?(</div>\n\s*</div>\n\s*<!-- Перманентный макияж -->)', html, re.DOTALL)
if match_makiyazh:
    html = html.replace(match_makiyazh.group(0), match_makiyazh.group(1) + '\n' + makiyazh + '              ' + match_makiyazh.group(2))

# Лицо
litso = """
                <div class="price-list">
                  <div class="price-row"><span class="price-name">Карбоновый пилинг</span><span class="price-dots"></span><span class="price-value">1 500 ₽</span></div>
                </div>
"""
match_litso = re.search(r'(<h3>Лицо</h3>\s*<span class="accordion-icon"></span>\s*</button>\s*<div class="accordion-content">).*?(</div>\n\s*</div>\n\s*<!-- Обучение -->)', html, re.DOTALL)
if match_litso:
    html = html.replace(match_litso.group(0), match_litso.group(1) + '\n' + litso + '              ' + match_litso.group(2))

# Обучение
obuchenie = """
                <div class="price-list">
                  <div class="price-row"><span class="price-name">Курс педикюр - БАЗОВЫЙ - пальчики (1 день/2модели)</span><span class="price-dots"></span><span class="price-value">15 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Обучение «Базовый курс мастер бровист» Пакет #2</span><span class="price-dots"></span><span class="price-value">15 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Обучение «Повышение квалификации,ламинирование ресниц/бровей»</span><span class="price-dots"></span><span class="price-value">12 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Обучение "Базовый курс - мастер маникюра" 3 дня</span><span class="price-dots"></span><span class="price-value">20 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Обучение «Базовый курс мастер бровист» пакет #1</span><span class="price-dots"></span><span class="price-value">10 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Обучение «Базовый курс ламинирование ресниц»</span><span class="price-dots"></span><span class="price-value">20 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Обучение «Базовый курс мастер бровист» пакет #3</span><span class="price-dots"></span><span class="price-value">25 000 ₽</span></div>
                </div>
"""
match_obuchenie = re.search(r'(<h3>Обучение</h3>\s*<span class="accordion-icon"></span>\s*</button>\s*<div class="accordion-content">).*?(</div>\n\s*</div>\n\s*</div>)', html, re.DOTALL)
if match_obuchenie:
    html = html.replace(match_obuchenie.group(0), match_obuchenie.group(1) + '\n' + obuchenie + '              ' + match_obuchenie.group(2))

# Add the two random items from "Без категории" to the end of Hair
additional_hair = """
                  <div class="price-row"><span class="price-name">БИОзавивка волос (короткие волосы)</span><span class="price-dots"></span><span class="price-value">6 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Стрижка женская (длинные волосы, от лопаток)</span><span class="price-dots"></span><span class="price-value">2 700 ₽</span></div>
"""
volosy_end_match = re.search(r'(<div class="price-row"><span class="price-name">Коррекция сложного окрашивания</span><span class="price-dots"></span><span class="price-value">от 11 000 ₽</span></div>\n\s*)(</div>\n\s*</div>\n\s*</div>\n\s*<!-- Ногти -->)', html, re.DOTALL)
if volosy_end_match:
    html = html.replace(volosy_end_match.group(0), volosy_end_match.group(1) + additional_hair + volosy_end_match.group(2))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated final sections")
