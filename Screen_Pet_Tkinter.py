from tkinter import Tk,HIDDEN,NORMAL,Canvas



def toggle_eyes():
    current_color = c.itemcget(eye_left,'fill')
    new_color = c.body_color if current_color =='white' else 'white'
    current_state = c.itemcget(pupil_left,'state')
    new_state =  NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfig(pupil_left,state = new_state)
    c.itemconfig(pupil_right, state=new_state)
    c.itemconfig(eye_left, fill = new_color)
    c.itemconfig(eye_left, fill = new_color)

def blink():
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(3000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(pupil_left, 10, -5)
        c.move(pupil_left, -10, -5)
        c.crossed_eyes = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_left, 10, 5)
        c.crossed_eyes = False


def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    win.after(1000,toggle_tongue)
    win.after(1000,toggle_pupils)
    return

def show_happy(event):
    if(20<= event.x and event.x < 350) and (20<= event.y and event.y <= 350):
        c.itemconfigure(cheek_left, state = NORMAL)
        c.itemconfigure(cheek_right, state = NORMAL)
        c.itemconfigure(mouth_happy, state = NORMAL)
        c.itemconfigure(mouth_normal, state = HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 10
    return

def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return


def sad():
    if c.happy_level ==0 :
        c.itemconfigure(mouth_happy,state = HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    win.after(500,sad)



win = Tk()

# canvas section

c = Canvas(win,width = 400,height = 400)
c.configure(bg = 'dark blue',highlightthickness = 0)
c.body_color = 'Skyblue1'
# pet body
body = c.create_oval(27,26,365,360,outline=c.body_color, fill=c.body_color)

#end pet body

# foot
foot_left = c.create_oval(65,320,145,360, outline = c.body_color, fill = c.body_color)
foot_right = c.create_oval(250,320,330,360, outline = c.body_color, fill = c.body_color)

# ear
ear_left = c.create_polygon(75,80,75,10,165,70,outline = c.body_color,fill = c.body_color)
ear_right = c.create_polygon(255,45,325,10,320,70,outline = c.body_color,fill = c.body_color)

# eyes

eye_left = c.create_oval(130,110,160,170,outline = 'black',fill = 'white')
pupil_left = c.create_oval(140,145,150,155,outline = 'black',fill = 'black')

eye_right = c.create_oval(230,110,260,170,outline = 'black',fill = 'white')
pupil_right = c.create_oval(240,145,250,155,outline = 'black',fill = 'black')

# mouth
mouth_normal = c.create_line(170,250,200,272,230,250,smooth=1,width = 2,state =NORMAL)
mouth_happy = c.create_line(170,250,200,282,230,250,smooth=1,width = 2,state = HIDDEN)
mouth_sad =c.create_line(170,250,200,232,230,250,smooth=1,width = 2,state = HIDDEN)




# cheeks

cheek_left = c.create_oval(70,180,120,230,outline = 'pink',fill = 'pink',state = HIDDEN)
cheek_right = c.create_oval(280,180,330,230,outline = 'pink',fill = 'pink',state = HIDDEN)


c.pack()

# cursor motion
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)

win.after(1000,blink)
win.after(5000,sad)

c.crossed_eyes = False
c.happy_level = 10
win.mainloop()


