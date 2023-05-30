from keras.preprocessing.image import ImageDataGenerator

class Data_augmentation:
    def __init__(self):
        # Create an ImageDataGenerator with data augmentation transformations
        self.datagen = ImageDataGenerator(
                        rotation_range=20,
                        width_shift_range=0.2,
                        height_shift_range=0.2,
                        shear_range=0.2,
                        zoom_range=0.2,
                        horizontal_flip=True,
                        vertical_flip=True
                        )
        