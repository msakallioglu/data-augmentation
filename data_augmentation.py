from keras_preprocessing.image import ImageDataGenerator,img_to_array, load_img

def generation(ID):
    name = input("Enter the name of the person to create the data set: ")
    for i in range(1,4):
        img = load_img(str(ID)+'_'+str(i)+'.jpg')
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        j = 0
        for batch in datagen.flow(x, batch_size=1,
                                  save_to_dir='dataset/'+name,
                                  save_prefix=str(ID) + '_' + str(j), save_format='jpg'):
            j += 1
            if j > 5:
                break

datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True)


x = int(input("For how many people the data set will be created: "))
for i in range(0,x):
    i=i+1
    generation(i)


