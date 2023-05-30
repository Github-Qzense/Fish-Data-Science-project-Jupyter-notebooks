from tqdm import tqdm
import os

# Files common to both folders are removed from folder2

folder1 = ""
folder2 = ""

subfolders = []
for species in subfolders:
    folder_path1 = os.path.join(folder1, species) # train data folder
    folder_path2 = os.path.join(folder2, species) # test data folder

    if os.path.isdir(folder_path1):
        for file in tqdm(os.listdir(folder_path1), desc = f'Loading {species} '):
            filepath1 = os.path.join(folder_path1, file)
            if os.path.isfile(filepath1):
                if file in os.listdir(folder_path2):
                    filepath2 = os.path.join(folder_path2, file)
                    os.remove(filepath2)