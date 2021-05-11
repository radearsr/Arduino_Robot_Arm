from tkinter import *
import serial
import time

port = False

# Coloring Style
background = "#262626"
foreground = "#fff"
font       = ("Times",13,"bold")
fgbutton   = "#FAF7FF"

def set_serial_port():
    global port,arduino

    com_port = port_input.get()
    arduino  = serial.Serial(com_port,9600)
    port     = True
    print ("COM Arduino : " + com_port)

def kirim_posisi(posisi):
    message = "{0:0=3d}".format(posisi[0])+"{0:0=3d}".format(posisi[1])+"{0:0=3d}".format(posisi[2])+"{0:0=3d}".format(posisi[3])+"\n"
    arduino.write(str.encode(message))
    print(message, end='')
    time.sleep(0.2)

rekaman_posisi = []

def rekam_posisi():
    rekaman_posisi.append([slider_servo1.get(), slider_servo2.get(), slider_servo3.get(), slider_servo4.get()])
    print("Posisi Tersimpan: "+str(rekaman_posisi))

def replay_posisi():
    for posisi in rekaman_posisi:
        print("playing: "+str(posisi))
        kirim_posisi(posisi)
        time.sleep(1)

def reset():
    slider_servo1.set(0)
    slider_servo2.set(0)
    slider_servo3.set(0)
    slider_servo4.set(0)
    x = int(len(rekaman_posisi))
    print(rekaman_posisi)
    for i in range(0, x):
        remove = rekaman_posisi[0]
        rekaman_posisi.remove(remove)
    print(rekaman_posisi)
    

root = Tk()
root.title("APRA")
root.geometry("600x400")
root.configure(bg="#262626")

title_label = Label(
    root,
    text="Pengontrol Robot Arm",
    font=("Times", 20,"bold"),
    bg=background,
    fg=foreground
    )
title_label.place(x=170, y=2)
subTitle_label = Label(root, text="DEVELOP BY RADEARSR", font=("Times", 10), bg=background, fg=foreground)
subTitle_label.place(x=230, y=38)


port_label=Label(root,text="Port Com Arduino:", font=("Times", 13,"bold"), bg=background, fg=foreground)
port_label.place(x=10,y=55);
port_input=Entry(root, font=("Times", 15), width=7, borderwidth=2, relief="solid", bg=fgbutton, justify="center")
port_input.place(x=10,y=85)
port_button=Button(root, text="KONEK", command=set_serial_port, bg="#8083FF", font=("Times", 10), pady=2, fg=foreground)
port_button.place(x=100,y=85)



# Slider Servo 1
slider_servo1 = Scale(
    root,
    from_=0,
    to=180,
    orient=HORIZONTAL,
    length=400,
    bg= background,
    troughcolor='#fccd59',
    fg="#fff",
    highlightthickness=0,
    activebackground="#007D5C"
)
slider_servo1.place(x=115, y=115)
label_servo1=Label(root,text="Pemutar", bg=background, fg=foreground, font=font)
label_servo1.place(x=1, y=130)


# Slider Servo 2 
slider_servo2 = Scale(
    root,
    from_=0,
    to=180,
    orient=HORIZONTAL,
    length=400,
    highlightthickness=0,
    bg=background,
    fg=foreground,
    troughcolor="#ffa95c",
    activebackground="#369093"
    
)
slider_servo2.place(x=115, y=165)
label_servo2=Label(root,text="Lengan Bawah", bg=background, fg=foreground, font=font)
label_servo2.place(x=1, y=180)


# Slider Servo 3
slider_servo3 = Scale(
    root,
    from_=0,
    to=180,
    orient=HORIZONTAL,
    length=400,
    highlightthickness=0,
    bg=background,
    fg=foreground,
    troughcolor="#d8717c",
    activebackground="#00B38F"
)
slider_servo3.place(x=115, y=215)
label_servo3=Label(root,text="Lengan Atas", bg=background, fg=foreground, font=font)
label_servo3.place(x=1, y=230)


# Slider Servo 4
slider_servo4 = Scale(
    root,
    from_=0,
    to=180,
    orient=HORIZONTAL,
    length=400,
    highlightthickness=0,
    bg=background,
    fg=foreground,
    troughcolor="#9f5b72",
    activebackground="#54ECC4"
)
slider_servo4.place(x=115, y=265)
label_servo4=Label(root,text="Pencapit", bg=background, fg=foreground, font=font)
label_servo4.place(x=1, y=280)

reset_button=Button(root, text="Reset Posisi", height=2, width=10, command=reset, bg="#FF00FF", font=font, fg=fgbutton)
reset_button.place(x=10,y=330)

save_button=Button(root, text="Rekam Posisi", command=rekam_posisi, height=2, width=10, bg="#068488", font=font, fg=foreground)
save_button.place(x=300,y=330)

play_button=Button(root, text="Replay Posisi", command=replay_posisi, height=2, width=10, bg="#00C6CF", font=font, fg=foreground)
play_button.place(x=470,y=330)

while True:
    root.update()
    if(port):
        message = kirim_posisi([slider_servo1.get(), slider_servo2.get(), slider_servo3.get(), slider_servo4.get()])

