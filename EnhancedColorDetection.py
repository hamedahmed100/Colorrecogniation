import cv2
import numpy as np
from pygame import mixer
from tkinter import *
import time



#Colors in BGR 
TARGET_COLORS = {"Blue": (255, 0, 0),"Yellow": (0, 255, 255), "Green": (0, 255, 0), "Red": (0, 0, 255),
                 "White": (255, 255, 255), "Black": (0, 0, 0)}


def soundPlay(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()
    time.sleep(1)

def color_difference (color1, color2):
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

#initial WebCam

cap =cv2.VideoCapture(0)



#Section of Form
ROOT = Tk()
ROOT.geometry('400x400')
ROOT.title("Color Recognition")
#End form

#Label for Showing Colors
label_2 = Label(ROOT, text="....",fg='Red',bg='white', font=("bold", 30))
label_2.place(x=0, y=0)
label_2.config(height=400, width=400)


label_1 = Label(ROOT, text="",fg='Red',bg='white', font=("bold", 20))
label_1.place(x=150, y=150)
#End Title


#Color Dictionary to Holds Colors Values
Colors = dict()

#Counters for each Color Value
global  rc, bc, yc, blc, gc, grc


while True:
    ROOT.update()
    ret, frame = cap.read()
    if not ret:
        break
    if cv2.waitKey(1) == 27:
        break

    rc = 0 #red
    bc = 0 #blue
    gc = 0 #green
    yc = 0 #Yellow
    blc = 0 #Black
    wc = 0  #White

    #Get the count of Colors in a specific Porotion of Image taken by Web Cam
    for x in range(150,200):
        for y in range(150,200):

            my_color=frame[x,y]
            differences = [[color_difference(my_color, target_value), target_name] for target_name, target_value in
                           TARGET_COLORS.items()]
            differences.sort()  # sorted by the first element of inner lists
            my_color_name = differences[0][1]


            #Blue Part
            if my_color_name == "Blue":
                bc += 1
                # Red Part
            elif my_color_name == "Red":
                rc += 1
         # Green Part
            elif my_color_name == "Green":
                gc += 1

            # Yello Part
            elif my_color_name == "Yellow":
                yc += 1

                # Gray Part
            elif my_color_name == "White":
                wc += 1
            elif my_color_name == "Black":
                blc += 0





    #Filling the Dictionary with Color Values
    Colors['Red']=rc
    Colors['Green'] = gc
    Colors['Yellow'] = yc
    Colors['Blue'] = bc
    Colors['White']=wc
    #print(Colors)


  #Arrange Colors and get the Max counter to Know which Color in front of the Camera
    kay_List=list(Colors.keys())
    val_List = list(Colors.values())
    getColorName = kay_List[val_List.index(max(Colors.values()))]
    getColorValue = max(Colors.values())

    #print(getColorName,getColorValue)

#Blue Part
    if getColorName=="Blue" and label_1['text']!=getColorName and getColorValue>200:
        label_1['text']="Blue"
        label_1['fg']="white"
        label_1['bg']="blue"
        label_2['bg']="blue"
        PLAYERPATH = 'Blue.mp3'
        soundPlay(PLAYERPATH);


#Red Part
    elif getColorName=="Red" and label_1['text']!=getColorName and getColorValue>200:
        label_1['text'] = "Red"
        label_1['fg'] = "white"
        label_1['bg'] = "red"
        label_2['bg'] = "red"
        PLAYERPATH = 'Red.mp3'
        soundPlay(PLAYERPATH);



#Green Part
    elif getColorName=="Green" and label_1['text']!=getColorName and getColorValue>200:
        label_1['text'] = "Green"
        label_1['fg'] = "white"
        label_1['bg'] = "green"
        label_2['bg'] = "green"
        PLAYERPATH = 'green.mp3'
        soundPlay(PLAYERPATH);


#Yello Part
    elif getColorName=="Yellow" and label_1['text']!=getColorName and getColorValue>200:
        label_1['text'] = "Yellow"
        label_1['fg'] = "white"
        label_1['bg'] = "Yellow"
        label_2['bg'] = "Yellow"
        PLAYERPATH = 'Yellow.mp3'
        soundPlay(PLAYERPATH)

# White Part
    elif getColorName == "White" and label_1['text']!=getColorName and getColorValue>200:
        label_1['text'] = "White"
        label_1['fg'] = "black"
        label_1['bg'] = "white"
        label_2['bg'] = "white"
        PLAYERPATH = 'White.mp3'
        soundPlay(PLAYERPATH)
# Black Part
    elif getColorName == "Black" and label_1['text']!=getColorName and getColorValue>200:
        label_1['text'] = "Black"
        label_1['fg'] = "white"
        label_1['bg'] = "black"
        label_2['bg'] = "black"
        PLAYERPATH = 'black.mp3'
        soundPlay(PLAYERPATH)




cap.release()
cv2.destroyAllWindows()
