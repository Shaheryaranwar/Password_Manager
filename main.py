from tkinter import *
from tkinter import messagebox
import string
from random import choice,randint,shuffle
from PIL import Image, ImageTk  # Import Pillow for image handling
#__________________________PASSWORD GENERATOR_____________________________#
def pass_genrator():
    # List of numbers from 1 to 20
    numbers = list(range(1, 21))
    # List of letters A-Z
    letters = list(string.ascii_uppercase)  # Uppercase A-Z
    # List of special characters
    special_letters = ["!", "-", "+", "@", "$", "%", "^", "&", "*", "(", ")"]
    # Generate random parts of the password
    pass_num = [str(choice(numbers)) for _ in range(randint(5,8))]  # Convert numbers to strings
    pass_letter = [choice(letters) for _ in range(randint(13,17))]
    pass_syb = [choice(special_letters) for _ in range(randint(1,3))]
    # Combine and shuffle the password
    password_list = pass_syb + pass_letter + pass_num
    shuffle(password_list)
    # Convert list to a single string password
    my_password = "".join(password_list)
    # print(my_password)
    entery_password.insert(0, my_password)#use to insert  output in password section of gui
#__________________________ SAVE    PASSWORD _____________________________#
def save_password():
    website = entery_website.get()
    email = entery_website.get()
    password = entery_password.get()
    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showwarning(title="Error",message="Please enter Information Correctly...! ")
    else:
        is_ok = messagebox.askokcancel(title="Conformatio" ,message ="Do you want to save")
        if is_ok :
            with open("Data.txt",mode="a") as imp_file:
                imp_file.write(f"{website}                         |{email}                         |{password} \n")
                entery_password.delete(0,END)
                entery_website.delete(0,END)
                entery_email.delete(0,END)



#__________________________UI SETUP_____________________________#


# Initialize window
screen = Tk()
screen.title("CloudChain Protection")
screen.config(padx=40,pady=40)
screen.minsize(width=550, height=450)
image_path = "Comapny_logo.png"  # Ensure this file exists
image = Image.open(image_path)
image = image.resize((300, 300))  # Resize as needed
photo = ImageTk.PhotoImage(image)

# Create Label to display the image
image_label = Label(screen, image=photo)
image_label.grid(row = 0, column = 1 )  # Add padding for better layout
# Creating Lable
my_website = Label(text="Website:",font=("Arial",16,"bold"),fg="#f17024")
my_website.grid(row = 1,column = 0)
my_email = Label(text="Email/Username:",font=("Arial",16,"bold"),fg="#f17024")
my_email.grid(row = 2,column = 0)
my_pasword = Label(text="Password:",font=("Arial",16,"bold"),fg="#f17024")
my_pasword.grid(row = 3,column = 0)#imp to grid
#Enteries
entery_website = Entry(width=35)
entery_website.grid(row=1,column=1)
entery_website.focus()
entery_email = Entry(width=35)
entery_email.grid(row=2,column=1)
entery_password = Entry(width=35)
entery_password.grid(row=3,column=1)

#Buttons
gen_password = Button(text="Generate Password",width=18,command=pass_genrator)
gen_password.grid(row=4,column=1)
add_button = Button(text="Add" ,width=18 , command=save_password)
add_button.grid(row=5,column=1)
# Run the Tkinter main loop
screen.mainloop()
