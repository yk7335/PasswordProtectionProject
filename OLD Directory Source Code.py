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

if Question == "n":
    Password = str(input("Create a new password:"))
    pickle.dump(Password, open("Password.dat", "wb"))
else:
    Password = str(input("Enter your Password:"))
    PasswordCheck = pickle.load(open("Password.dat", "rb"))
    while Password != PasswordCheck:
        print("Incorrect Password Try Again!")
        Password = str(input("Enter your Password:"))


Task = str(input("What do you want to do (press m for Menu):"))
Images = []
ImagesName = []

while Task != "q":
    if Task == "m":
        print("q to Quit **** m for Menu *** a to add a picture *** s to Show picture")
        Task = str(input("What do you want to do (press m for Menu):"))
    elif Task == "a":
        Name = str(input("Enter Name of file:"))
        NameOfDirectory = str(input("Name of file directory:"))
        Images.append(PicDatabase(Name))
        ImagesName.append(Name)
        index2 = ImagesName.index(Name)
        Images[index2].SaveImage(NameOfDirectory)
        pickle.dump(Images, open("ImageObject.dat", "wb"))
        pickle.dump(ImagesName, open("ImageName.dat", "wb"))
        print("Picture Saved under name:", Name)
        Task = str(input("What do you want to do (press m for Menu):"))
    elif Task == "s":
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

print("Quiting.....")
sys.exit(0)
