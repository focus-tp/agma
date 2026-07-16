import re

html_to_insert = """
      <!-- Services Section -->
      <section class="services-section section-light" id="services_price">
        <div class="container">
          <div class="section-header animate-on-scroll">
            <h2 class="section-title">Услуги и Цены</h2>
            <p class="section-desc">Выберите категорию, чтобы ознакомиться с подробным прайс-листом.</p>
          </div>
          
          <div class="accordion-container animate-on-scroll">
            <!-- Волосы -->
            <div class="accordion-item">
              <button class="accordion-header">
                <h3>Волосы</h3>
                <span class="accordion-icon"></span>
              </button>
              <div class="accordion-content">
                <div class="price-list">
                  <div class="price-row">
                    <span class="price-name">Стрижка женская (короткие волосы, до подбородка)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">3 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Стрижка женская (средние волосы, до лопаток)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">2 800 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Стрижка женская (длинные волосы, от лопаток)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 2 700 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Стрижка + салонный уход</span>
                    <span class="price-dots"></span>
                    <span class="price-value">4 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Подравнивание кончиков</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 1 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Создание челки</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 1 200 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Сложное окрашивание. Мастер / Топ мастер</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 13 000 ₽ / 18 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Тонирование, окрашивание тон в тон. Мастер / Топ мастер</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 5 000 ₽ / 7 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">БИОзавивка волос (короткие волосы)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">6 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Укладка волос на утюг и/или плойку</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 2 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Профессиональный салонный уход для волос</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 2 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Трихоскопия</span>
                    <span class="price-dots"></span>
                    <span class="price-value">1 000 ₽</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Ногти -->
            <div class="accordion-item">
              <button class="accordion-header">
                <h3>Ногти</h3>
                <span class="accordion-icon"></span>
              </button>
              <div class="accordion-content">
                <div class="price-list">
                  <div class="price-row">
                    <span class="price-name">Маникюр аппаратный / Комби (без покрытия)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 1 800 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Маникюр мужской</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 1 800 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Маникюр с покрытием ГЕЛЬ ЛАК (укрепление включено)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 2 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Маникюр Японский Masura / P.shine (+аппаратный)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 2 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Наращивание ногтей на верхние формы</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 3 800 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Коррекция наращенных ногтей</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 3 300 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Педикюр экспресс (пальчики) без покрытия / с покрытием ГЕЛЬ ЛАК</span>
                    <span class="price-dots"></span>
                    <span class="price-value">1 900 ₽ / от 2 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Педикюр Kane professional ПОЛНЫЙ (стопа + пальцы) + ГЕЛЬ ЛАК</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 3 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Педикюр Smart (СМАРТ) ПОЛНЫЙ + покрытие ГЕЛЬ ЛАК</span>
                    <span class="price-dots"></span>
                    <span class="price-value">3 300 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Педикюр Golden trace ПОЛНЫЙ + покрытие ГЕЛЬ-ЛАК</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 4 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Дизайн (френч / втирка / кошка / омбре) на 10 ногтей</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 300 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">ПЛЁНКИ (установка дизайна на 10 пальцев ног)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">1 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Маникюр детский (5-12 лет)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">1 000 ₽</span>
                  </div>
                </div>
                <p style="margin-top:24px; text-align:center;"><a href="https://vk.com/bsekat?w=app5688600_-222253395" target="_blank" class="btn btn-outline" style="font-size: 12px; padding: 10px 20px;">Смотреть полный прайс</a></p>
              </div>
            </div>

            <!-- Макияж -->
            <div class="accordion-item">
              <button class="accordion-header">
                <h3>Макияж</h3>
                <span class="accordion-icon"></span>
              </button>
              <div class="accordion-content">
                <div class="price-list">
                  <div class="price-row">
                    <span class="price-name">Экспресс макияж</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 1 600 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Дневной макияж</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 2 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Вечерний макияж</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 2 500 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Образ (макияж + укладка)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">от 4 800 ₽</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Перманентный макияж -->
            <div class="accordion-item">
              <button class="accordion-header">
                <h3>Перманентный макияж</h3>
                <span class="accordion-icon"></span>
              </button>
              <div class="accordion-content">
                <div class="price-list">
                  <div class="price-row">
                    <span class="price-name">Перманентный макияж бровей</span>
                    <span class="price-dots"></span>
                    <span class="price-value">8 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Перекрытие старого татуажа</span>
                    <span class="price-dots"></span>
                    <span class="price-value">8 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Рефреш перманентного макияжа</span>
                    <span class="price-dots"></span>
                    <span class="price-value">6 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Коррекция перманентного макияжа</span>
                    <span class="price-dots"></span>
                    <span class="price-value">4 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Лазерное удаление татуажа / ремувером</span>
                    <span class="price-dots"></span>
                    <span class="price-value">2 500 ₽</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Лицо -->
            <div class="accordion-item">
              <button class="accordion-header">
                <h3>Лицо</h3>
                <span class="accordion-icon"></span>
              </button>
              <div class="accordion-content">
                <div class="price-list">
                  <div class="price-row">
                    <span class="price-name">Карбоновый пилинг</span>
                    <span class="price-dots"></span>
                    <span class="price-value">1 500 ₽</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Обучение -->
            <div class="accordion-item">
              <button class="accordion-header">
                <h3>Обучение</h3>
                <span class="accordion-icon"></span>
              </button>
              <div class="accordion-content">
                <div class="price-list">
                  <div class="price-row">
                    <span class="price-name">Обучение «Базовый курс мастер бровист» (от пакета #1 до #3)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">10 000 ₽ - 25 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Обучение "Базовый курс - мастер маникюра" 3 дня</span>
                    <span class="price-dots"></span>
                    <span class="price-value">20 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Курс педикюр - БАЗОВЫЙ - пальчики (1 день)</span>
                    <span class="price-dots"></span>
                    <span class="price-value">15 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Обучение «Базовый курс ламинирование ресниц»</span>
                    <span class="price-dots"></span>
                    <span class="price-value">20 000 ₽</span>
                  </div>
                  <div class="price-row">
                    <span class="price-name">Повышение квалификации, ламинирование ресниц/бровей</span>
                    <span class="price-dots"></span>
                    <span class="price-value">12 000 ₽</span>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert before Contact Section
if 'id="services_price"' not in html:
    html = html.replace('<section class="contact section-light" id="contact">', html_to_insert + '\n      <section class="contact section-light" id="contact">')

# Update nav menu to point to #services_price
if 'href="#services_price"' not in html:
    if 'href="#services"' in html:
        html = html.replace('href="#services"', 'href="#services_price"')
    else:
        html = html.replace('<li><a href="#team" class="nav-link">Мастера</a></li>',
                            '<li><a href="#team" class="nav-link">Мастера</a></li>\n            <li><a href="#services_price" class="nav-link">Услуги</a></li>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
