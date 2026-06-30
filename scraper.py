# ==========================================
# Amazon Review Scraper
# ==========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

import time


PRODUCT_URL = "https://www.amazon.in/dp/B08WKFSN84"


def get_reviews():

    reviews = []

    options = Options()

    options.add_argument("--start-maximized")

    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = None

    try:

        driver = webdriver.Chrome(

            service=Service(
                ChromeDriverManager().install()
            ),

            options=options

        )

        driver.get(PRODUCT_URL)

        WebDriverWait(driver,20).until(

            EC.presence_of_element_located(

                (By.ID,"productTitle")

            )

        )

        time.sleep(2)

        soup = BeautifulSoup(

            driver.page_source,

            "html.parser"

        )

        title = "Unknown Product"

        title_tag = soup.find(

            "span",

            id="productTitle"

        )

        if title_tag:

            title = title_tag.get_text(strip=True)

        review_blocks = soup.select(

            "div[data-hook='review']"

        )

        for block in review_blocks[:10]:

            review = ""

            rating = 0

            review_body = block.select_one(

                "span[data-hook='review-body']"

            )

            if review_body:

                review = review_body.get_text(

                    " ",

                    strip=True

                )

            rating_tag = block.select_one(

                "i[data-hook='review-star-rating'] span"

            )

            if rating_tag:

                try:

                    rating = float(

                        rating_tag.text.split()[0]

                    )

                except:

                    rating = 0

            reviews.append({

                "product": title,

                "review": review,

                "rating": rating

            })

        print("Reviews Scraped :",len(reviews))

        return reviews

    except Exception as e:

        print(e)

        return []

    finally:

        if driver:

            driver.quit()

if __name__ == "__main__":
    reviews = get_reviews()

    print(f"\nTotal Reviews: {len(reviews)}\n")

    for i, review in enumerate(reviews, start=1):
        print(f"Review {i}")
        print("Product :", review["product"])
        print("Rating  :", review["rating"])
        print("Review  :", review["review"])
        print("-" * 50)