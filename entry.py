import cv2
import tkinter as tk
import tkinter as ttk

r=tk.Tk()
r.title('SECURITY')
tLabel = tk.Label(r,padx=500, text="SANT LONGOWAL INSTITUTE OF ENGINEERING AND TECHNOLOGY",font = "Times")
tLabel.config(bg = 'white',fg='green')
tLabel.grid(row=0,padx=20,pady=20)






def entry():




    face_classifier = cv2.CascadeClassifier('C:/Users/Shubham kumar/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

    def face_extractor(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        if faces is ():
            return None

        for (x, y, w, h) in faces:
            cropped_face = img[y:y + h, x:x + w]

        return cropped_face

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            print('enter face name')
            name_of_user = input()


            file_name_path = 'C:/Users/Shubham kumar/Desktop/Security/images/' + str(name_of_user) + '.jpg'
            cv2.imwrite(file_name_path, face)

            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('FACE Cropper', face)
        else:
            print("FACE NOT FOUND")
            pass

        if cv2.waitKey(1) == 13 or count == 1:
            break

    cap.release()
    cv2.destroyAllWindows()
    #print(face)
    print('COLLECTING SAMPLES COMPLETED!!!!')



button=ttk.Button(r, text='ENTRY(capture)',width=100, command=entry)
button.grid(row=1,sticky='S')
eLabel=tk.Label(r,padx=100, text="First Name")
e1 = tk.Entry(r,bg='white',fg='black')
e1.grid(row=7, column=0)



eLabel.config(bg='red',fg='white')
eLabel.grid(row=2,padx=20,pady=20)

r.mainloop()

