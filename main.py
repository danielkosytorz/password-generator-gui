import tkinter as tk
import string
import random

HEIGHT = 250
WIDTH = 400


def random_letter():
    rand = random.randint(0, len(LETTERS)-1)
    return rand


def random_digit():
    rand = random.randint(0, len(NUMBERS)-1)
    return rand


def random_special_sign():
    rand = random.randint(0, len(SPECIAL_SIGNS)-1)
    return rand


def random_number():
    return random.randint(0,2)


LETTERS = string.ascii_letters
NUMBERS = string.digits
SPECIAL_SIGNS = string.punctuation


def generate_password(pass_length):
    try:
        generated_password = tk.StringVar()
        password = ''
        # 0 - random letter, 1 - random digit, 2 - random special sign
        for i in range(int(pass_length)):
            sign = random_number()
            if sign == 0:
                password += LETTERS[random_letter()]
            elif sign == 1:
                password += NUMBERS[random_digit()]
            elif sign == 2:
                password += SPECIAL_SIGNS[random_special_sign()]
            else:
                print('Error')
    except:
        generated_password.set('Error 404')
        entry_output['textvariable'] = generated_password

    #label_pass_output['text'] = generated_password
    generated_password.set(password)
    entry_output['textvariable'] = generated_password

root = tk.Tk()
root.title("Password generator")
# root.iconbitmap('./hacker.ico')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='./wallpaper.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

top_frame = tk.Frame(root, bd=5)
top_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.3, anchor='n')

label_pass_len = tk.Label(top_frame, bg='#cccccc',text='How long the password should be?', font=("Helvetica", "12"),
                          justify='left', anchor='nw')
label_pass_len.place(relx=0, rely=0,relwidth=0.8, relheight=0.4)

entry = tk.Entry(top_frame, font=("Helvetica", "12"), bg='#cccccc')
entry.place(relx=0.8, rely=0, relwidth=0.15, relheight=0.4)

button = tk.Button(top_frame, text='Generate password', bg='grey',font=("Helvetica", "12"), command=lambda:
generate_password(entry.get()))
button.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.3, anchor='n')

lower_frame = tk.Frame(root, bg='#808080', bd=5)
lower_frame.place(relx=0.5, rely=0.6, relwidth=0.9, relheight=0.15, anchor='n')

# label_pass_output = tk.Label(lower_frame, bg='#cccccc')
# label_pass_output.place(relx=0, rely=0, relwidth=1, relheight=1)

entry_output = tk.Entry(lower_frame,font=("Helvetica", "12"), bd=0, state='readonly')
entry_output.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()