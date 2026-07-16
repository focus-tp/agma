import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

lashes_section = """
            <!-- Ресницы -->
            <div class="accordion-item">
              <button class="accordion-header">
                <h3>Ресницы</h3>
                <span class="accordion-icon"></span>
              </button>
              <div class="accordion-content">
                <div class="price-list">
                  <div class="price-row"><span class="price-name">1,5D наращивание ресниц</span><span class="price-dots"></span><span class="price-value">2 600 ₽</span></div>
                  <div class="price-row"><span class="price-name">2D наращивание ресниц</span><span class="price-dots"></span><span class="price-value">2 800 ₽</span></div>
                  <div class="price-row"><span class="price-name">3D наращивание ресниц</span><span class="price-dots"></span><span class="price-value">3 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Классическое наращивание ресниц</span><span class="price-dots"></span><span class="price-value">2 400 ₽</span></div>
                  <div class="price-row"><span class="price-name">Комплекс «ЛАМИНИРОВАНИЕ РЕСНИЦ»</span><span class="price-dots"></span><span class="price-value">от 2 200 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция наращивания ресниц 2Д (в течении 2-х недель)</span><span class="price-dots"></span><span class="price-value">2 300 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция ресниц по гарантии (7 дней)</span><span class="price-dots"></span><span class="price-value">0 ₽</span></div>
                  <div class="price-row"><span class="price-name">Лучики</span><span class="price-dots"></span><span class="price-value">500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Мокрый эффект</span><span class="price-dots"></span><span class="price-value">500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Наращивание внешних уголков ресниц</span><span class="price-dots"></span><span class="price-value">1 800 ₽</span></div>
                  <div class="price-row"><span class="price-name">Окрашивание ресниц</span><span class="price-dots"></span><span class="price-value">500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Снятие наращенных ресниц</span><span class="price-dots"></span><span class="price-value">500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Цветное наращивание</span><span class="price-dots"></span><span class="price-value">3 200 ₽</span></div>
                  <div class="price-row"><span class="price-name">Цветные ресницы (добавление к наращиванию)</span><span class="price-dots"></span><span class="price-value">500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Экспресс наращивание ресниц</span><span class="price-dots"></span><span class="price-value">3 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция наращивания ресниц 3D (в течении 2-х недель после наращивания)</span><span class="price-dots"></span><span class="price-value">2 500 ₽</span></div>
                </div>
              </div>
            </div>
"""

# Insert after Брови (and before Макияж)
insert_point = '<!-- Макияж -->'
html = html.replace(insert_point, lashes_section + '\n            ' + insert_point)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added lashes")
