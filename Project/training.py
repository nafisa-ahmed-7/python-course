import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

############## Without Mask ###############

train_data_without = []
for filename in os.listdir('all_pics/pics/without_mask/'):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
        img = cv2.imread('all_pics/pics/without_mask/' + filename)
        '''
        while True:
            cv2.imshow('abc',img)
            if cv2.waitKey(2) == 27:
                break
        '''
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        '''
        while True:
            cv2.imshow('abc',img)
            key = cv2.waitKey(1)
            if key == ord("p"):
                break
        '''
        face_data = face_classifier.detectMultiScale(img,minNeighbors=5, minSize=(250,250)) #Detect
        for x,y,w,h in face_data:
            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,255),2)
            face_crop = img[int(y+h/2):y+h, x:x+w]
            face_crop = cv2.resize(face_crop,(200,100))
            '''
            while True:
                cv2.imshow('abc', img)
                key = cv2.waitKey(1)
                if key == ord("p"):
                    break

            while True:
                cv2.imshow('abc', face_crop)
                key = cv2.waitKey(1)
                if key == ord("p"):
                    break
            '''
            train_data_without.append(face_crop)
            break

    if len(train_data_without) == 54:
        break
np.save('without_mask.npy',train_data_without)

#~~~~~~~~~~~~~~~~~~~################################# With Mask #############################################~~~~~~~~~~~~~~~~~~


train_data_with = []
for filename in os.listdir('all_pics/pics/with_mask/'):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
        img = cv2.imread('all_pics/pics/with_mask/' + filename)
        '''
        while True:
            cv2.imshow('abc',img)
            if cv2.waitKey(2) == 27:
                break
        '''
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        '''
        while True:
            cv2.imshow('abc',img)
            key = cv2.waitKey(1)
            if key == ord("p"):
                break
        '''
        face_data = face_classifier.detectMultiScale(img, minNeighbors=4, minSize=(250,250)) #Detect
        for x,y,w,h in face_data:
            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,255),2)
            face_crop = img[int(y+h/2):y+h, x:x+w]
            face_crop = cv2.resize(face_crop,(200,100))
            train_data_with.append(face_crop)
            '''
            while True:
                cv2.imshow('abc', img)
                key = cv2.waitKey(1)
                if key == ord("p"):
                    break
        
            while True:
                cv2.imshow('abc', face_crop)
                #if cv2.waitKey(2) == 27:
                key = cv2.waitKey(1)
                if key == ord("p"):
                    break
            '''
            break
    if len(train_data_with) == 47:
        break
np.save('with_mask.npy',train_data_with)


########## Creating the dataset model #############

mask_data = np.load('with_mask.npy')
no_mask_data = np.load('without_mask.npy')

mask_data = mask_data.reshape(47,200*100)
no_mask_data = no_mask_data.reshape(54,200*100)

data_X = np.r_[mask_data,no_mask_data]
labels = np.zeros(data_X.shape[0])
labels[47:] = 1.0
mask_flag = {0 : 'Mask', 1: 'No Mask'}