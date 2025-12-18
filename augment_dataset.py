"""
Kimiya Esmaeil Namazi
Simple dataset expansion script (bonus).

This script duplicates some images in each class folder with new filenames
to simulate dataset augmentation, without external libraries.
"""

import os
import shutil

DATASET_DIR = "dataset"

# how many extra copies per original image (max)
COPIES_PER_IMAGE = 1  # start with 1

def expand_folder(model_folder: str):
    folder_path = os.path.join(DATASET_DIR, model_folder)
    if not os.path.isdir(folder_path):
        return

    print(f"\n=== Expanding model: {model_folder} ===")

    images = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
           and "_copy" not in f
    ]

    for name in images:
        base, ext = os.path.splitext(name)
        src = os.path.join(folder_path, name)

        for i in range(COPIES_PER_IMAGE):
            new_name = f"{base}_copy{i+1}{ext}"
            dst = os.path.join(folder_path, new_name)

            if os.path.exists(dst):
                continue

            shutil.copy2(src, dst)
            print(f"  [OK] {model_folder}/{new_name}")

def main():
    if not os.path.isdir(DATASET_DIR):
        print(f"{DATASET_DIR} not found")
        return

    for model in os.listdir(DATASET_DIR):
        if os.path.isdir(os.path.join(DATASET_DIR, model)):
            expand_folder(model)

if __name__ == "__main__":
    main()
