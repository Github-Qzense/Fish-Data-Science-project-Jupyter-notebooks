import os
import cv2
import numpy as np
from tqdm import tqdm

class preprocessing:
    def __init__(self, dataset_folder, IMAGE_SIZE, fish_species=[], test_data=False):
        self.dataset_folder = dataset_folder
        self.fish_species = fish_species
        self.IMAGE_SIZE = IMAGE_SIZE
        self.test_data = test_data
        self.label_map = {species: i for i, species in enumerate(fish_species)}

        
    def preprocess(self):
        # Create a dictionary to map each species to a numerical label
        images = []
        labels = []

        IMAGE_SIZE = self.IMAGE_SIZE

        # Load the images and labels
        if len(self.fish_species)==0:
            l = os.listdir(self.dataset_folder)
            print("All fish")
        else:
            l = self.fish_species
            print("fish species : ",self.fish_species,"\n")
            
        for species in tqdm(l):
            folder_path = os.path.join(self.dataset_folder, species)
            for filename in tqdm(os.listdir(folder_path), desc=f"Loading {species}"):
                if filename.endswith((".jpg",".jpeg", ".webp", ".png", ".JPEG")):
                    image_path = os.path.join(folder_path, filename)
                    image = cv2.imread(image_path)
                    if image is not None:
                        # Resize the image to a consistent size
                        image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))  
                        images.append(image)
                        labels.append(self.label_map[species])
                        
        images = np.array(images)
        labels = np.array(labels)
        
        if self.test_data:
            print("\ntest data preprocessed\n")
            images = images/255.0
        else:
            print("\ntrain data preprocessed\n")
        return images, labels
    
    
    def preprocess_image(self, img_path):
        # Load and preprocess the new image
        image = cv2.imread(img_path)
        image = cv2.resize(image, (self.IMAGE_SIZE, self.IMAGE_SIZE))  # Resize the image to match the input size of the CNN model
        image = image / 255.0  # Normalize the image

        # Expand dimensions to match the input shape of the CNN model
        image = np.expand_dims(image, axis=0)
        return image