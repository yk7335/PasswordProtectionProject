from PIL import Image
import numpy as np
import sys
import pickle


class PicDatabase:
    def __init__(self, name):
        image = None
        name = name
        ImageArray = np.empty((0))

    def SaveImage(self, NameofDirectory):
        self.image = Image.open(NameofDirectory)
        self.ImageArray = np.asarray(self.image)
        self.image = Image.fromarray(self.ImageArray)

    def Show(self):
        self.image.show()


Question = str(input("Do you already have a password (y = yes / n = no): "))


try:
    PasswordCheck = pickle.load(open("Password.dat", "rb"))
    print("Password Exits!")
    Password = str(input("Enter Password:"))
    while Password != PasswordCheck:
        print("Incorrect Password Try Again!")
        Password = str(input("Enter your Password:"))
except:
    print("No Password Exists!")
    Password = str(input("Create a new password:"))
    print("Password Created! ", Password)
    pickle.dump(Password, open("Password.dat", "wb"))


Task = str(input("What do you want to do (press m for Menu):"))
Images = []
ImagesName = []

while Task != "q":
    if Task == "m":
        print("q to Quit **** m for Menu *** s to save a picture *** o to Show picture *** v to view saved files")
        Task = str(input("What do you want to do (press m for Menu):"))
    elif Task == "s":
        Name = str(input("Enter Name of file:"))
        NameOfDirectory = str(input('Name of file directory (EX: C:\\Users\\OneDrive\\Desktop\\Pictures\\Capture.jpg):'))
        Images.append(PicDatabase(Name))
        ImagesName.append(Name)
        index2 = ImagesName.index(Name)
        Images[index2].SaveImage(NameOfDirectory)
        pickle.dump(Images, open("ImageObject.dat", "wb"))
        pickle.dump(ImagesName, open("ImageName.dat", "wb"))
        print("Picture Saved under name:", Name)
        Task = str(input("What do you want to do (press m for Menu):"))
    elif Task == "o":
        ImagesName = pickle.load(open("ImageName.dat", "rb"))
        Images = pickle.load(open("ImageObject.dat", "rb"))
        NameOfFile = str(input("Which file do you want to see:"))
        if NameOfFile in ImagesName:
            print("Found Picture!")
            print("Opening Picture.....")
            index = ImagesName.index(NameOfFile)
            Images[index].Show()
        else:
            print("Image not saved yet")
        Task = str(input("What do you want to do (press m for Menu):"))
    elif Task == "v":
        try:
            ImagesName = pickle.load(open("ImageName.dat", "rb"))
            print(ImagesName)
        except:
            print("No image has been saved yet!")
        Task = str(input("What do you want to do (press m for Menu):"))

print("Quiting.....")
sys.exit(0)
