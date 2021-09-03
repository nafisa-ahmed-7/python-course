from training import *
######################### SVM ##########################

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

x_train, x_test, y_train, y_test = train_test_split(data_X, labels, test_size=0.2)

pca = PCA(n_components=5)
x_train = pca.fit_transform(x_train) # data converted into 3 cols. Eigen values, eigen vectors (dimensionality reduction)

svm = SVC() #(gamma='auto')   #Initialize
svm.fit(x_train, y_train) #Fitting the model with our data

x_test = pca.transform(x_test)
y_pred = svm.predict(x_test)
acc = accuracy_score(y_test,y_pred)
print("Accuracy value is "+ str(acc))
print(confusion_matrix(y_test,y_pred))
plot_confusion_matrix(svm,x_test,y_test)
plt.show()



##switch case: press 1 for webcam testing 2 for image testing
################# Live Testing on Webcam #############

haar_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    flag, img = capture.read()
    if flag:
        faces = haar_data.detectMultiScale(img, minNeighbors=6, minSize=(300,300))
        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
            face = img[int(y+h/2):y+h,x:x+w,:]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            face = cv2.resize(face,(200,100))
            face = face.reshape(1,-1)
            face = pca.transform(face)
            pred = svm.predict(face)[0]
            mask_pred = mask_flag[int(pred)]
            cv2.putText(img,mask_pred, (x,y), font, 1, (244,250,250),2)
            print(mask_pred)
        cv2.imshow('abc', img)
        if cv2.waitKey(5) ==27:
            break

capture.release()
cv2.destroyAllWindows()



'''
############ Predict using an Image ###############
img_path = 'all_pics/pics/test/with_mask/1.jpg'
img = cv2.imread(img_path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_data = face_classifier.detectMultiScale(img) #Detect
for x,y,w,h in face_data:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,255),2)
        face_crop = img[y:y+h, x:x+w]
        face_crop = cv2.resize(face_crop,(200,200))

face_crop = face_crop.reshape(1,-1)
face_crop = pca.transform(face_crop)
pred = svm.predict(face_crop)
print("Prediction: " + mask_flag[int(pred)])
'''