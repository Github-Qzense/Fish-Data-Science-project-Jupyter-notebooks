import os
import shutil
from tqdm import tqdm

'''
Collects data from drive folder to a new folder
where all the images in the good and bad folders 
of each species are stored in one folder 
'''
# Define the paths
old_folder = r"C:\Users\sowmy\Downloads\Fish Classification\Dataset\train_data\warehouse_data\Data\Final_Data"
new_folder = r"C:\Users\sowmy\Downloads\Fish Classification\Dataset\train_data\warehouse_data\classification_data"

# Create the new folder if it doesn't exist
os.makedirs(new_folder, exist_ok=True)

# Loop through the subfolders in the old folder
for subfolder in tqdm(os.listdir(old_folder)):
    subfolder_path = os.path.join(old_folder, subfolder)
    # Skip if the item is not a folder
    if not os.path.isdir(subfolder_path):
        continue
    
    # Find the date folder inside the subfolder
    for date_folder in os.listdir(subfolder_path):
        # Check if the folder name is a date type eg: "19-May" 
        if "-" in date_folder:
            date_folder_path = os.path.join(subfolder_path, date_folder)
            next_folder = date_folder_path
            # Skip if the item is not a folder
            if not os.path.isdir(date_folder_path):
                continue
        else:
            next_folder = subfolder_path
        
        # Find the 'good' and 'bad' folders inside the 'date' folder
        good_folder = os.path.join(next_folder, "Good")
        bad_folder = os.path.join(next_folder, "Bad")
        ok_folder = os.path.join(next_folder, "Ok")
        

        # Copy the image files from 'good' folder to the new folder
        if os.path.exists(good_folder):
            new_subfolder = os.path.join(new_folder, subfolder)
            os.makedirs(new_subfolder, exist_ok=True)
            for file in os.listdir(good_folder):
                file_path = os.path.join(good_folder, file)
                if os.path.isfile(file_path):
                    if file_path not in new_subfolder:
                        shutil.copy2(file_path, new_subfolder)

        # Copy the image files from 'bad' folder to the new folder
        if os.path.exists(bad_folder):
            new_subfolder = os.path.join(new_folder, subfolder)
            os.makedirs(new_subfolder, exist_ok=True)
            for file in os.listdir(bad_folder):
                file_path = os.path.join(bad_folder, file)
                if os.path.isfile(file_path):
                    if file_path not in new_subfolder:
                        shutil.copy2(file_path, new_subfolder)
                    
        # Copy the image files from 'ok' folder to the new folder
        if os.path.exists(ok_folder):
            new_subfolder = os.path.join(new_folder, subfolder)
            os.makedirs(new_subfolder, exist_ok=True)
            for file in os.listdir(ok_folder):
                file_path = os.path.join(ok_folder, file)
                if os.path.isfile(file_path):
                    if file_path not in new_subfolder:
                        shutil.copy2(file_path, new_subfolder)
