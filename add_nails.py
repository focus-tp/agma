import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

more_nails = """
                  <div class="price-row"><span class="price-name">Педикюр Golden trace (стопа+пальчики) без покрытия</span><span class="price-dots"></span><span class="price-value">от 3 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр Golden trace ПОЛНЫЙ (стопа, пальчики) + покрытие ГЕЛЬ-ЛАК</span><span class="price-dots"></span><span class="price-value">от 4 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр Kane professional ПОЛНЫЙ препаратный/дисковый (стопа + пальцы) + покрытие ГЕЛЬ ЛАК</span><span class="price-dots"></span><span class="price-value">от 3 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр Kane professional препаратный/дисковый (стопа + пальцы) без покрытия</span><span class="price-dots"></span><span class="price-value">от 3 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр Smart (СМАРТ) Мужской (обработка стопы smart дисками + пальцы аппарат)</span><span class="price-dots"></span><span class="price-value">от 3 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр Smart (СМАРТ) БЕЗ ПОКРЫТИЯ (обработка стопы дисками smart + пальчики аппарат)</span><span class="price-dots"></span><span class="price-value">от 2 800 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр Smart (СМАРТ) ПОЛНЫЙ + покрытие ГЕЛЬ ЛАК</span><span class="price-dots"></span><span class="price-value">3 300 ₽</span></div>
                  <div class="price-row"><span class="price-name">ПЛЁНКИ (установка дизайна на 10 пальцев ног)</span><span class="price-dots"></span><span class="price-value">1 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр экспресс (пальчики) + покрытие ГЕЛЬ ЛАК</span><span class="price-dots"></span><span class="price-value">от 2 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Педикюр экспресс (пальчики) без покрытия</span><span class="price-dots"></span><span class="price-value">от 1 900 ₽</span></div>
                  <div class="price-row"><span class="price-name">Покрытие обычным цветным лаком (Masura)</span><span class="price-dots"></span><span class="price-value">200 ₽</span></div>
                  <div class="price-row"><span class="price-name">Ремонт покрытия (не по гарантии, или работа стороннего мастера) 1 ноготь</span><span class="price-dots"></span><span class="price-value">от 500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Ремонт покрытия по гарантии (10 дней)</span><span class="price-dots"></span><span class="price-value">0 ₽</span></div>
                  <div class="price-row"><span class="price-name">Ремонт трещины (при выполнении полной процедуры маникюра)</span><span class="price-dots"></span><span class="price-value">от 100 ₽</span></div>
                  <div class="price-row"><span class="price-name">Снятие гель лака (без последующего покрытия) + опил формы</span><span class="price-dots"></span><span class="price-value">700 ₽</span></div>
                  <div class="price-row"><span class="price-name">Снятие гель-лака (с последующим покрытием, работа стороннего мастера)</span><span class="price-dots"></span><span class="price-value">200 ₽</span></div>
                  <div class="price-row"><span class="price-name">Работа с длинными ногтями (доп оплата за сложность работы/расход материала) при последующем покрытии</span><span class="price-dots"></span><span class="price-value">500 ₽</span></div>
                  <div class="price-row"><span class="price-name">Снятие наращенных ногтей (или длинных) + убрать длину + опил формы (без обработки кутикулы и покрытия)</span><span class="price-dots"></span><span class="price-value">1 000 ₽</span></div>
                  <div class="price-row"><span class="price-name">Френч/втирка/стемпинг/кошка ДИЗАЙН 10 ногтей (все ногти)</span><span class="price-dots"></span><span class="price-value">от 300 ₽</span></div>
                  <div class="price-row"><span class="price-name">Коррекция наращенных ногтей (верхние формы) - через месяц</span><span class="price-dots"></span><span class="price-value">от 3 300 ₽</span></div>
"""

# Append to Ногти list before its closing </div>
# Find the exact end of the Ногти list
nails_end = '</div>\n                <p style="margin-top:24px; text-align:center;">'
html = html.replace(nails_end, more_nails + '\n                ' + nails_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added nails")
