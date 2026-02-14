import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from domain.product import Product


class Scraper:

    def __init__(self, driver):
        self.driver = driver

    def scrape_all(self, base_url, max_pages=120):

        all_products = []

        for page in range(1, max_pages + 1):

            url = f"{base_url}?page={page}"
            print(f"[INFO] Scraping page {page}...")

            self.driver.get(url)

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "div.product-inner")
                    )
                )
            except:
                print("[INFO] No more products.")
                break

            cards = self.driver.find_elements(By.CSS_SELECTOR, "div.product-inner")

            print(f"[INFO] Found {len(cards)} products.")

            if not cards:
                break

            for c in cards:

                try:
                    link = c.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                except:
                    link = ""

                try:
                    price = c.find_element(By.CSS_SELECTOR, ".price").text
                except:
                    price = ""

                title = link.split("/")[-1].replace("-", " ") if link else ""

                sku = ""
                description = ""
                image = ""

                if link:
                    try:
                        self.driver.get(link)
                        time.sleep(1)

                        # ✅ SKU
                        try:
                            sku = self.driver.find_element(
                                By.XPATH,
                                "//*[contains(text(),'SKU')]"
                            ).text
                        except:
                            sku = ""

                        # ✅ DESCRIPTION من meta
                        try:
                            description = self.driver.find_element(
                                By.CSS_SELECTOR,
                                "meta[itemprop='description']"
                            ).get_attribute("content")
                        except:
                            description = ""

                        # ✅ IMAGE
                        try:
                            image = self.driver.find_element(
                                By.CSS_SELECTOR,
                                "img[src*='products']"
                            ).get_attribute("src")
                        except:
                            image = ""

                    except:
                        pass

                product = Product(
                    sku=sku,
                    title=title,
                    description=description,
                    price=price,
                    product_url=link,
                    image_url=image,

                )

                all_products.append(product)

                # 🔄 رجوع لصفحة category
                self.driver.back()
                time.sleep(0.5)

        return all_products
