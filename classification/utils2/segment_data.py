import os
from remove_background import remove_bg
from tqdm import tqdm

def Data_Segmentation(src_folder_path, des_folder_path):    
    # Create the new folder if it doesn't exist
    os.makedirs(des_folder_path, exist_ok=True)
    
    # Loop through the subfolders in the old folder
    for subfolder in (os.listdir(src_folder_path)):
        print(subfolder)
        subfolder_path = os.path.join(src_folder_path, subfolder)        
        # Skip if the item is not a folder
        if not os.path.isdir(subfolder_path):
            continue
        
        new_subfolder = os.path.join(des_folder_path, subfolder)
        os.makedirs(new_subfolder, exist_ok=True)
        
        for file in tqdm(os.listdir(subfolder_path)):
            file_path = os.path.join(subfolder_path, file)
            if os.path.isfile(file_path):
                input_img_path = file_path
                file_types = ['.jpeg', '.png', '.jpg', '.webp']
                if '.jpeg' in file or '.webp' in file:
                    file = file[:-5]
                else:
                    file = file[:-4]
                output_img_path = os.path.join(new_subfolder, file)
                output_img_path = output_img_path+".png"
                if not os.path.isfile(output_img_path):
                    remove_bg(input_img_path, output_img_path)
                
                
                
                
                
                
class DataSegmentation:
    def __init__(self, src_folder_path, des_folder_path):
        self.src_folder_path = src_folder_path
        self.des_folder_path = des_folder_path
        # Create the new folder if it doesn't exist
        os.makedirs(des_folder_path, exist_ok=True)
        
    def bg_remover(self, src, des):
        for file in os.listdir(src):
            file_path = os.path.join(src, file)
            if os.path.isfile(file_path):
                input_img_path = file_path
                file_types = ['.jpeg', '.png', '.jpg', '.webp']
                if '.jpeg' in file or '.webp' in file:
                    file = file[:-5]
                else:
                    file = file[:-4]
                output_img_path = os.path.join(des, file)
                remove_bg(input_img_path, output_img_path)
    
    
    def all_species(self, species_list=[]):        
        if len(species_list)==0:
            l = os.listdir(self.src_folder_path)
        else:
            l = species_list
            
        # Loop through the subfolders in the old folder
        for subfolder in tqdm(l):
            subfolder_path = os.path.join(self.src_folder_path, subfolder)        
            # Skip if the item is not a folder
            if not os.path.isdir(subfolder_path):
                continue
            
            new_subfolder = os.path.join(self.des_folder_path, subfolder)
            os.makedirs(new_subfolder, exist_ok=True)
                    
            # bg_remover(src=subfolder_path, des=new_subfolder)
        
        
    def one_species(self):    
        # bg_remover(src=self.src_folder_path, des=self.des_folder_path)
        pass
        
src_folder_path = r"C:\Users\sowmy\Downloads\Fish Classification\Dataset\train_data\warehouse_data\classification_data"
des_folder_path = r"C:\Users\sowmy\Downloads\Fish Classification\Dataset\train_data\warehouse_data\bg_removed_Data"

Data_Segmentation(src_folder_path, des_folder_path)

    
    
    
        