import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cookie_html = """
    <!-- Cookie Banner -->
    <div class="cookie-banner" id="cookie-banner">
      <p>Мы используем файлы cookie для улучшения работы сайта. Оставаясь на сайте, вы соглашаетесь с нашей <a href="#">политикой обработки данных</a>.</p>
      <button class="btn btn-primary cookie-btn" id="cookie-accept">Понятно</button>
    </div>
"""
if '<div class="cookie-banner"' not in html:
    html = html.replace('</body>', cookie_html + '\n</body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

cookie_css = """
/* Cookie Banner */
.cookie-banner {
  position: fixed;
  bottom: 24px;
  left: 24px;
  max-width: 400px;
  background: rgba(18, 18, 18, 0.95);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 24px;
  border-radius: 8px;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  transform: translateY(150%);
  transition: transform 0.6s cubic-bezier(0.19, 1, 0.22, 1);
}
.cookie-banner.show {
  transform: translateY(0);
}
.cookie-banner p {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.5;
  margin: 0;
}
.cookie-banner a {
  color: var(--color-accent);
  text-decoration: underline;
}
.cookie-banner .cookie-btn {
  padding: 10px 24px;
  font-size: 12px;
  align-self: flex-start;
}

@media (max-width: 768px) {
  .cookie-banner {
    bottom: 80px; /* Above mobile nav bar */
    left: 16px;
    right: 16px;
    max-width: none;
  }
}
"""
if '.cookie-banner {' not in css:
    css += "\n" + cookie_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 3. Update main.js
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

cookie_js = """
  // Cookie Banner Logic
  const cookieBanner = document.getElementById('cookie-banner');
  const cookieAcceptBtn = document.getElementById('cookie-accept');

  if (cookieBanner && cookieAcceptBtn) {
    // Check if user already accepted
    if (!localStorage.getItem('cookiesAccepted')) {
      setTimeout(() => {
        cookieBanner.classList.add('show');
      }, 2000); // Show after 2 seconds
    }

    cookieAcceptBtn.addEventListener('click', () => {
      localStorage.setItem('cookiesAccepted', 'true');
      cookieBanner.classList.remove('show');
    });
  }
"""
if 'cookie-banner' not in js:
    # insert before end
    js = js + '\n' + cookie_js
    with open('main.js', 'w', encoding='utf-8') as f:
        f.write(js)

print("Cookie banner added.")
