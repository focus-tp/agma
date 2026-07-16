import json
from bs4 import BeautifulSoup

html_file = "/Users/tanya/.gemini/antigravity-ide/brain/937f7bd0-3170-4bcd-8dd0-daf73ae69110/.system_generated/steps/508/content.md"
with open(html_file, "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")
services = soup.find_all("div", class_="service")
results = []
for s in services:
    title_el = s.find(class_="title")
    price_el = s.find(class_="price")
    type_el = s.find(class_="type")
    
    if title_el and price_el:
        cat = type_el.get_text(strip=True) if type_el else "Other"
        results.append({
            "category": cat,
            "name": title_el.get_text(strip=True),
            "price": price_el.get_text(strip=True)
        })

for r in results:
    print(f"[{r['category']}] {r['name']} - {r['price']}")
