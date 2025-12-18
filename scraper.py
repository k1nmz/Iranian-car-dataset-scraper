"""
Car Image Dataset Scraper
Author: Kimiya Esmaeil Namazi
"""
import os
import time
import csv
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ================= CONFIG =================
DATASET_DIR = "dataset"
IMAGES_PER_MODEL = 200  

CAR_URLS = {
    "206": "https://divar.ir/s/tehran/car?q=206",
    "206_SD": "https://divar.ir/s/tehran/car?q=206%20sd",
    "207": "https://divar.ir/s/tehran/car?q=207",
    "405": "https://divar.ir/s/tehran/car?q=405",
    "504": "https://divar.ir/s/tehran/car?q=504%20%D9%BE%DA%98%D9%88",
    "Dena": "https://divar.ir/s/tehran/car?q=dena",
    "L90": "https://divar.ir/s/tehran/car?q=L90",
    "Peride": "https://divar.ir/s/tehran/car?q=%D9%BE%D8%B1%D8%A7%DB%8C%D8%AF",
    "Rana": "https://divar.ir/s/tehran/car?q=rana",
    "Samand_LX": "https://divar.ir/s/tehran/car?q=Samand_LX",
    "Samand_Soren": "https://divar.ir/s/tehran/car?q=Samand_Soren",
    "Tara": "https://divar.ir/s/tehran/car?q=tara"
}


#Create dataset directory and subfolders for each car model.
def make_dirs():
    os.makedirs(DATASET_DIR, exist_ok=True)
    for model in CAR_URLS:
        os.makedirs(os.path.join(DATASET_DIR, model), exist_ok=True)

#Configure and return a Chrome WebDriver instance
def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

#Scrape images for each model from Divar and return CSV records
def scrape_divar():
    driver = setup_driver()
    csv_data = []

    for model, url in CAR_URLS.items():
        print(f"\n🔍 Scraping {model}")
        driver.get(url)
        time.sleep(5)

        downloaded = 0
        last_count = 0
        no_new_rounds = 0

        while downloaded < IMAGES_PER_MODEL and no_new_rounds < 3:
            images = driver.find_elements(
                By.CSS_SELECTOR,
                "img.kt-image-block__image"
            )

            if len(images) == last_count:
                no_new_rounds += 1
            else:
                no_new_rounds = 0

            last_count = len(images)

            for img in images:
                if downloaded >= IMAGES_PER_MODEL:
                    break

                src = img.get_attribute("src")
                if not src or "divarcdn.com" not in src:
                    continue

                filename = f"image_{downloaded + 1}.jpg"
                path = os.path.join(DATASET_DIR, model, filename)

                if os.path.exists(path):
                    continue

                try:
                    urllib.request.urlretrieve(src, path)
                    csv_data.append([model, filename, path, url])
                    downloaded += 1
                    print(f"  [OK] {model} image {downloaded}")
                    time.sleep(0.7)
                except:
                    continue

            
            driver.execute_script(
                "window.scrollBy(0, document.body.scrollHeight);"
            )
            time.sleep(3)

        if downloaded < IMAGES_PER_MODEL:
            print(f"  ⚠️ Only {downloaded} images found for {model}")

    driver.quit()
    return csv_data


def save_csv(data):
    with open("labels.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Label", "Filename", "Path", "Source"])
        writer.writerows(data)


# ================= MAIN =================
if __name__ == "__main__":
    make_dirs()
    records = scrape_divar()
    save_csv(records)
    print("\n DONE: Images downloaded successfully.")
