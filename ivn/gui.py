from tkinter import*
from PIL import Image , ImageTk
import action 
import speak_to_text 


def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  
          

def ask():

    ask_val= speak_to_text.speak_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if bot_val != None:
       text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")


root = Tk()
#root.geometry("550x675")
root.geometry("550x700")

root.title("AI Assistant")
root.resizable(False,False)
root.config(bg="#BEBEBE")

  


# Main Frame
Main_frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
Main_frame.config(bg="#D3D3D3")
Main_frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)


# Text Lable 
Text_lable = Label(Main_frame, text = "AI Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#FFFFFF")
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)



# Charger et redimensionner l'image
original_image = Image.open("image/assistant.png")
resized_image = original_image.resize((240, 240))  # Modifier la taille (largeur, hauteur)
Display_Image = ImageTk.PhotoImage(resized_image)
Image_Lable = Label(Main_frame, image=Display_Image)
Image_Lable.grid(row=1, column=0, pady=20)
Image_Lable.image = Display_Image  

# Add a text widget

text=Text(root , font= ('Courier 10 bold') , bg = "#FFFFFF")
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100) 




# Add a entry widget
entry1 = Entry(root, justify = CENTER)
entry1.place(x=100 , y = 500 , width= 350, height= 30)



# Add a text button1
button1 =  Button(root,  text="ASK" , bg="#FFFFFF" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 575)

# Add a text button2
button2 =  Button(root,  text="Send" , bg="#FFFFFF" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 400, y= 575)

# Add a text button3
button3 = Button(root, text="Delete", bg="#FFFFFF" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 225, y= 575)
root.mainloop()