import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pm_services = """
                <div class="price-list">
                  <div class="price-row"><span class="price-name">Дополнительная коррекция перманентного макияжа (делается в течении 2-х месяцев после коррекции)</span><span class="price-dots"></span><span class="price-value">3 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Консультация по перманентному макияжу</span><span class="price-dots"></span><span class="price-value">0 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция перманентного макияжа (выполняется в течении 2-х месяцев после первичной процедуры)</span><span class="price-dots"></span><span class="price-value">4 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Лазерное удаление татуажа</span><span class="price-dots"></span><span class="price-value">2 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Перманентный макияж бровей</span><span class="price-dots"></span><span class="price-value">8 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Рефреш перманентного макияжа</span><span class="price-dots"></span><span class="price-value">6 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Удаление татуажа ремувером</span><span class="price-dots"></span><span class="price-value">2 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Перекрытие старого тутуажа</span><span class="price-dots"></span><span class="price-value">8 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Удаление мини татуировки</span><span class="price-dots"></span><span class="price-value">2 500 ₽</span></div>
                </div>
"""

# Replace the content of the PM section
match = re.search(r'(<h3>Перманентный макияж</h3>\s*<span class="accordion-icon"></span>\s*</button>\s*<div class="accordion-content">).*?(</div>\n\s*</div>\n\s*<!-- Лицо -->)', html, re.DOTALL)
if match:
    html = html.replace(match.group(0), match.group(1) + '\n' + pm_services + '              ' + match.group(2))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated PM services")
