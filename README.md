# Car Image Dataset Scraper

This project implements the “Web Scraping and Dataset Organization for Machine Learning” challenge.  
It scrapes car images for specific Iranian car models from **Divar** and organizes them into a directory structure suitable for machine learning tasks.

**Author:** Kimiya Esmaeil Namazi

---

## Challenge Description

The goal of this project is to:

- Scrape car images and their labels for the following models:
  - 206, 206 SD, 207, 405, 504, Peride, Samand LX, Samand Soren, Tara, Dena, Rana, L90
- Organize images into a dataset structure, one folder per model, with at least ~200 images per class if possible.
- Store labels in a structured format (CSV/JSON).
- Provide clear documentation and a reproducible project structure.

---

## Supported Car Models

The dataset contains the following car models (each as a separate folder):



- 206  
- 206_SD  
- 207  
- 405  
- 504  
- Peride  
- Samand_LX  
- Samand_Soren  
- Tara  
- Dena  
- Rana  
- L90  


> ⚠️ For model 504, only ~90 images were available on Divar at scraping time.

---


## Project Structure


iranian-car-dataset-scraper/
├── scraper.py           
├── augment_simple.py     # Bonus: simple dataset expansion script
├── labels.csv            
├── requirements.txt
├── README.md
└── dataset/
    ├── 206/
    ├── 206_SD/
    ├── 207/
    ├── 405/
    ├── 504/
    ├── Peride/
    ├── Samand_LX/
    ├── Samand_Soren/
    ├── Tara/
    ├── Dena/
    ├── Rana/
    └── L90/

## scraper.py

Main script that:

1. Creates the `dataset/` directory and subfolders.
2. Opens the corresponding Divar search URL for each model.
3. Scrolls the page and collects image elements.
4. Downloads images into the correct model folder.
5. Writes metadata for each image into `labels.csv`.

**Key configuration:**

```python
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
    "Tara": "https://divar.ir/s/tehran/car?q=tara",
}
## augment_simple.py (Bonus)
augment_simple.py

Bonus script that duplicates existing images to expand the dataset without extra libraries.

Uses only Python standard library (shutil)

Controlled by:

DATASET_DIR = "dataset"
COPIES_PER_IMAGE = 1


Example:
image_95.jpg → image_95_copy1.jpg




## Requirements

- selenium
- webdriver-manager
- Google Chrome (required for Selenium WebDriver)


## Usage

### 1. Run the scraper
```bash
python scraper.py

# 2. Expand dataset (optional)
python augment_simple.py


Creates dataset/ folder and subfolders.

Visits each Divar URL.

Downloads up to 200 images per model (or fewer if not available).

Writes metadata to labels.csv.

2. Expand dataset (optional)
python augment_simple.py


Creates _copy1 duplicates for each original image.

Increases dataset size without extra libraries.

Dataset Format

Each subfolder in dataset/ represents a class (car model).

Image filenames: image_<index>.jpg (+ optional _copy1 for duplicates).

labels.csv maps each image to its label and source URL.

You can load it in ML frameworks either:

Directly from folders (folder-based datasets)

From labels.csv for custom data loaders

Course
This project was final project of the [Introduction to python](https://www.tahlildadeh.com/coursedetails/1165/%D8%AF%D9%88%D8%B1%D9%87-%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86.aspx) course.
