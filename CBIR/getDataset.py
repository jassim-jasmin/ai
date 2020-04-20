from keras.preprocessing.image import ImageDataGenerator
# from keras.preprocessing.sequence import


img_width, img_height = 28, 28

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
# nb_train_samples = 1
# nb_validation_samples = 2
epochs = 1
batch_size = 2

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

test_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')


validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

train_datagen = ImageDataGenerator(rescale=1. / 255)

itr = train_datagen.flow_from_directory(
train_data_dir,
target_size=(img_width, img_height),
batch_size=1,
class_mode='binary')

X, y = itr.next()

