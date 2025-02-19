import os
import random
import torch
from PIL import Image
from img_utils import resize_and_crop, img2tensor

# Set random seed for reproducibility
random.seed(42)

def process_and_save(image_path, out_path):
    try:
        with Image.open(image_path) as img:
            cropped = resize_and_crop(img)
            tensor = img2tensor(cropped)
            torch.save(tensor, out_path)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")



if __name__ == '__main__':
    dest_root = '/Users/jonhelgi/Projects/Ferr_classifier/data/dataset/'
    dest_subfolders = ['Train', 'Validation']
    raw_root = '/Users/jonhelgi/Projects/Ferr_classifier/data/dataset/raw_img/combined'
    raw_subfolders = ['calculus_equation','connected_graph', 'lewis_structure_diagram' ]

    # for base_dir in [train_dir, val_dir]:
    #     os.makedirs(base_dir, exist_ok=True)

    for raw_subfolder in raw_subfolders:
        raw_folder_path = os.path.join(raw_root, raw_subfolder)
        print(f"working on {raw_folder_path}")
        #iterate through the specific folder, apply 

        # Get list of image files
        images_files = [f for f in os.listdir(raw_folder_path)]
        random.shuffle(images_files)
    
        # Split list into 80% training and 20% validation
        split_idx = int(len(images_files) * 0.8)
        train_images = images_files[:split_idx]
        val_images = images_files[split_idx:]

        # Create label directories for train and val
        train_label_dir = os.path.join(dest_root, 'Train', raw_subfolder)
        val_label_dir = os.path.join(dest_root, 'Validation', raw_subfolder)
        os.makedirs(train_label_dir, exist_ok=True)
        os.makedirs(val_label_dir, exist_ok=True)

        # Process and save training images
        for img_name in train_images:
            img_path = os.path.join(raw_folder_path, img_name)
            out_name = os.path.splitext(img_name)[0] + ".pt"
            out_path = os.path.join(train_label_dir, out_name)
            process_and_save(img_path, out_path)

        # Process and save validation images
        for img_name in val_images:
            img_path = os.path.join(raw_folder_path, img_name)
            out_name = os.path.splitext(img_name)[0] + ".pt"
            out_path = os.path.join(val_label_dir, out_name)
            process_and_save(img_path, out_path)
