from infrastructure.driver_factory import DriverFactory
from application.scraper import Scraper
from infrastructure.repositories.csv_repository import save


def main():
    driver = DriverFactory.create_driver()

    scraper = Scraper(driver)

    base_url = "https://aretronics.com/collections/all"

    products = scraper.scrape_all(base_url, max_pages=120)

    save(products, "products")

    driver.quit()


if __name__ == "__main__":
    main()
