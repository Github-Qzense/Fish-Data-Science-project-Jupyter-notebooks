from sklearn.model_selection import train_test_split

def train_test_data(images, labels):
    train_images, test_images, train_labels, test_labels = train_test_split(images, 
                                                                            labels, 
                                                                            test_size=0.2, 
                                                                            random_state=42, 
                                                                            stratify=labels)
    
    # Normalize the image data
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    
    return train_images, test_images, train_labels, test_labels