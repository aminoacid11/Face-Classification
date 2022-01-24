import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import optimizers
from tensorflow.keras import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import itertools
import os
import shutil
import random
import glob
import matplotlib.pyplot as plt
import warnings
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
warnings.simplefilter(action='ignore', category=FutureWarning)

train_path = 'images/train'
valid_path = 'images/valid'

train_batches = ImageDataGenerator() \
                .flow_from_directory(directory=train_path, target_size=(224,224), classes=['bear','cat','deer','dog','fox','frog','horse','monkey','pig','rabbit','squirrel','turtle','wolf'], batch_size=10)
valid_batches= ImageDataGenerator() \
                .flow_from_directory(directory=valid_path, target_size=(224,224), classes=['bear','cat','deer','dog','fox','frog','horse','monkey','pig','rabbit','squirrel','turtle','wolf'], batch_size=10)

imgs, labels = next(train_batches)

# Make model
model = Sequential()
model.add(tf.keras.layers.Convolution2D(64, (3, 3), activation='relu', padding="SAME", input_shape=(224,224, 3)))
model.add(tf.keras.layers.Convolution2D(64, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)))
 
model.add(tf.keras.layers.Convolution2D(128, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.Convolution2D(128, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)))
 
model.add(tf.keras.layers.Convolution2D(256, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.Convolution2D(256, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.Convolution2D(256, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)))
 
model.add(tf.keras.layers.Convolution2D(512, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.Convolution2D(512, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.Convolution2D(512, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)))
 
model.add(tf.keras.layers.Convolution2D(512, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.Convolution2D(512, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.Convolution2D(512, (3, 3), activation='relu', padding="SAME"))
model.add(tf.keras.layers.MaxPooling2D((2,2), strides=(2,2)))

model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(4096, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(4096, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(2622, activation='relu'))
model.add(Dense(units=13, activation='softmax'))
for layer in model.layers[:-1]:
    layer.trainable = False
model.summary()

model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
# Fit the model
model.fit(x=train_batches, validation_data=valid_batches, epochs=2, verbose=1)

model.save('my_model_2.h5')

