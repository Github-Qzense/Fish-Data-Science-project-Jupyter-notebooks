import os
import shutil
from datetime import date
from tqdm import tqdm


'''
Collects data from drive folder to a new folder
where all the images in the good and bad folders 
of each species are stored in the final folder 
'''

src_folder = r"C:\Users\sowmy\Downloads\Fish Classification\Dataset\train_data\warehouse_data\Data\s3_data"
des_folder = r"C:\Users\sowmy\Downloads\Fish Classification\Dataset\train_data\warehouse_data\Data\Final_Data"

def update_final_data(src_folder, des_folder, date_folder=''):
    today = date.today()
    today = str(today)
    if date_folder=='':
        today = date.today()
        date_folder = str(today)
    src_folder = src_folder+"\\"+date_folder
    des_folder = des_folder
        
    # Create the new folder if it doesn't exist
    os.makedirs(des_folder, exist_ok=True)

    # Loop through the subfolders in the old folder
    for subfolder in tqdm(os.listdir(src_folder)):
        subfolder_path = os.path.join(src_folder, subfolder)
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
            
            
            # Copy the image files from 'Good' folder to the new folder
            if os.path.exists(good_folder):
                new_subfolder = os.path.join(des_folder, subfolder)
                os.makedirs(new_subfolder, exist_ok=True)
                
                new_good_folder = os.path.join(new_subfolder, "Good")
                os.makedirs(new_good_folder, exist_ok=True)
                for file in os.listdir(good_folder):
                    file_path = os.path.join(good_folder, file)
                    if os.path.isfile(file_path):
                        shutil.copy2(file_path, new_good_folder)

            # Copy the image files from 'Bad' folder to the new folder
            if os.path.exists(bad_folder):
                new_subfolder = os.path.join(des_folder, subfolder)
                os.makedirs(new_subfolder, exist_ok=True)
                new_bad_folder = os.path.join(new_subfolder, "Bad")
                os.makedirs(new_bad_folder, exist_ok=True)
                for file in os.listdir(bad_folder):
                    file_path = os.path.join(bad_folder, file)
                    if os.path.isfile(file_path):
                        shutil.copy2(file_path, new_bad_folder)
                        
            # Copy the image files from 'Ok' folder to the new folder
            if os.path.exists(ok_folder):
                new_subfolder = os.path.join(des_folder, subfolder)
                os.makedirs(new_subfolder, exist_ok=True)
                new_ok_folder = os.path.join(new_subfolder, "Ok")
                os.makedirs(new_ok_folder, exist_ok=True)
                for file in os.listdir(ok_folder):
                    file_path = os.path.join(ok_folder, file)
                    if os.path.isfile(file_path):
                        shutil.copy2(file_path, new_ok_folder)


update_final_data(src_folder, des_folder)



class update_final_data_folder:
    def __init__(self, src_folder, des_folder, date_folder=''):
        if date_folder=='':
            today = date.today()
            date_folder = str(today)
        
        self.src_folder = src_folder+"\\"+date_folder
        self.des_folder = des_folder
        
        # Create the new folder if it doesn't exist
        os.makedirs(des_folder, exist_ok=True)
        
        
    def get_images(self, next_folder, subfolder, folder_type):
        # Copy the image files from 'Good', 'Bad' and 'Ok' folders to the new folder
        type_folder = os.path.join(next_folder, folder_type)
        if os.path.exists(type_folder):
            new_subfolder = os.path.join(self.des_folder, subfolder)
            os.makedirs(new_subfolder, exist_ok=True)
            
            new_type_folder = os.path.join(new_subfolder, folder_type)
            os.makedirs(new_type_folder, exist_ok=True)
            for file in os.listdir(type_folder):
                file_path = os.path.join(type_folder, file)
                if os.path.isfile(file_path):
                    shutil.copy2(file_path, new_type_folder)
        
            
    
    def final_data(self):
        # Loop through the subfolders in the old folder
        for subfolder in tqdm(os.listdir(src_folder)):
            subfolder_path = os.path.join(src_folder, subfolder)
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
                
                # get_images(next_folder, subfolder, folder_type='Good')
                # get_images(next_folder, subfolder, folder_type='Bad')
                # get_images(next_folder, subfolder, folder_type='Ok')
 
 
                
            
                