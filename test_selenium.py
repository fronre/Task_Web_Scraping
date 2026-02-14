from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.dfrobot.com/category-202.html")

time.sleep(5)

products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/product-']")

print("عدد المنتجات:", len(products))

for p in products[:10]:
    print("•", p.text)

driver.quit()
