import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Additional items for Ногти
more_nails = """
                  <div class="price-row"><span class="price-name">Маникюр детский (5-12 лет)</span><span class="price-dots"></span><span class="price-value">1 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Омбре/градиент/кошачий глаз 10 ногтей</span><span class="price-dots"></span><span class="price-value">от 300 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр экспресс (пальчики без покрытия)</span><span class="price-dots"></span><span class="price-value">1 900 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр экспресс (пальчики) + покрытие ГЕЛЬ ЛАК - АКЦИЯ 🔥-10%</span><span class="price-dots"></span><span class="price-value">2 160 ₽</span></div>
                  <div class="price-row"><span class="price-name">Реставрация ногтей верхними формами (короткие/средние)</span><span class="price-dots"></span><span class="price-value">3 500 ₽</span></div>
"""

nails_end = '</div>\n                <p style="margin-top:24px; text-align:center;">'
html = html.replace(nails_end, more_nails + '\n                ' + nails_end)

# New section for Брови
brovi_section = """
            <!-- Брови -->
            <div class="accordion-item">
              <button class="accordion-header">
                <h3>Брови</h3>
                <span class="accordion-icon"></span>
              </button>
              <div class="accordion-content">
                <div class="price-list">
                  <div class="price-row"><span class="price-name">Ботокс для бровей/ресниц (Доп услуга к окрашиванию или ламинированию)</span><span class="price-dots"></span><span class="price-value">500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Комплекс «ЛАМИНИРОВАНИЕ БРОВЕЙ»</span><span class="price-dots"></span><span class="price-value">от 2 200 ₽</span></div>
                  <div class="price-row"><span class="price-name">Комплекс «ЛАМИНИРОВАНИЕ РЕСНИЦ И БРОВЕЙ»</span><span class="price-dots"></span><span class="price-value">от 4 400 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция +прореживание+ окрашивание бровей</span><span class="price-dots"></span><span class="price-value">от 1 600 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция бровей (воск+пинцет)</span><span class="price-dots"></span><span class="price-value">1 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция+окрашивание бровей</span><span class="price-dots"></span><span class="price-value">от 1 600 ₽</span></div>
                  <div class="price-row"><span class="price-name">Ламинирование бровей (без окрашивания и коррекции)</span><span class="price-dots"></span><span class="price-value">1 400 ₽</span></div>
                  <div class="price-row"><span class="price-name">Мужская коррекция бровей</span><span class="price-dots"></span><span class="price-value">1 200 ₽</span></div>
                  <div class="price-row"><span class="price-name">Окрашивание бровей (краска/хна)</span><span class="price-dots"></span><span class="price-value">1 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Осветление бровей+ тонирование</span><span class="price-dots"></span><span class="price-value">1 600 ₽</span></div>
                  <div class="price-row"><span class="price-name">Удаление волос на лице (1 зона)</span><span class="price-dots"></span><span class="price-value">500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Ламинирование бровей+ коррекция (без окрашивания)</span><span class="price-dots"></span><span class="price-value">1 800 ₽</span></div>
                </div>
              </div>
            </div>
"""

# Insert Брови after Ногти (and before Макияж)
insert_point = '<!-- Макияж -->'
html = html.replace(insert_point, brovi_section + '\n            ' + insert_point)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added brovi and more nails")
