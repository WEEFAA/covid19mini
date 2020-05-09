# Tkinter module
from tkinter import *
from tkinter import ttk
from utils.req import *
from PIL import Image, ImageTk

# Function definitions
def make_request(country):
	error_label.pack_forget() # clear error message
	response = request_api(country)
	if response.get('success'):
		data = response.get('data')
		for field, value in data.items():
			# update fields
			information_labels.get(field).set(f'{field}: <{value}>') 
	else:
		error_label.pack(fill="both", expand=True)

# resize image, responsive to window's dimension
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    main_background.config(image = photo)
    main_background.image = photo #avoid garbage collection

# Definitions
SCREEN_FRAME_HEIGHT = 1
SCREEN_FRAME_WIDTH = 1
SCREEN_FRAME_COLOR = "#2c3e50"
HEIGHT = 425
WIDTH = 640
MAIN_FRAME_HEIGHT = 0.75
MAIN_FRAME_WIDTH = 0.80
MAIN_FRAME_SPACE = 0.10
MAIN_FRAME_COLOR = "#e8daef"

BOTTOM_FRAME_COLOR = "gray"
# root master
root = Tk()
# App title
root.title("Covid 19 | Mini")
root.geometry('640x425') # delete later

# information frame labels
information_labels = {
	"Active Cases_text": StringVar(),
	"Country_text":StringVar(),
	"Last Update":StringVar(),
	"New Cases_text":StringVar(),
	"New Deaths_text":StringVar(),
	"Total Cases_text":StringVar(),
	"Total Deaths_text":StringVar(),
	"Total Recovered_text":StringVar()
}

# define a canvas
canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

# WHOLE SCREEN FRAME
screen_frame = Frame(root, bg=SCREEN_FRAME_COLOR)
screen_frame.place(relx=0, rely=0, relheight=SCREEN_FRAME_HEIGHT, relwidth=SCREEN_FRAME_WIDTH)

# TITLE FRAME
title_frame = Frame(screen_frame, bg=SCREEN_FRAME_COLOR)
title_frame.place(relx=0, rely=0, relwidth=1, relheight=.10)

# Title frame label
title_label = Label(title_frame,text="We care, save the World!", fg="#f4f6f7", bg=SCREEN_FRAME_COLOR)
title_label.pack(fill="y", expand=True)

# MAINFRAME
main = Frame(screen_frame, bg=MAIN_FRAME_COLOR)
main.place(rely = MAIN_FRAME_SPACE, relx = MAIN_FRAME_SPACE, relwidth = MAIN_FRAME_WIDTH, relheight = MAIN_FRAME_HEIGHT)

# Mainframe background image
image = Image.open('images/earth.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)

main_background = Label(main, image=photo)
main_background.place(x=0,y=0, relwidth=1,relheight=1)

main_background.bind('<Configure>', resize_image)
main_background.pack(fill="both", expand = "yes")

# Input Entry
INPUT_REL_X_OFFSET = 0.25 
INPUT_REL_Y_OFFSET = 0.05

input_entry = Entry(main, bg="#f4f6f7", justify="center")
input_entry.place(relx=INPUT_REL_X_OFFSET, rely=INPUT_REL_Y_OFFSET, height=30, relwidth=0.50)

# Input button
main_button = Button(main, text="Search", bg="#196f3d",
 	fg="#f8c471", activebackground="#2ecc71", activeforeground="#d68910",
 	command = lambda: make_request(input_entry.get())
)
main_button.place(relx=0.33, rely= INPUT_REL_Y_OFFSET + 0.13, height=25, relwidth=0.33)

# MAIN INFORMATION FRAME
LABEL_WIDTH = 0.50 # 2X4 
LABEL_HEIGHT = 0.25 #  LAYOUT
LABEL_FG = "#34495e"
INFORMATION_BG = "white"

information_frame = Frame(main, bg=INFORMATION_BG)
information_frame.place(relx=0, rely=0.30, relwidth=1, relheight=0.70)

label_actives = Label(information_frame, textvariable=information_labels.get("Active Cases_text"), bg=INFORMATION_BG, fg=LABEL_FG)
label_actives.place(relx=0, rely=0, relheight=LABEL_HEIGHT, relwidth=LABEL_WIDTH)

label_country = Label(information_frame, textvariable=information_labels.get("Country_text"), bg=INFORMATION_BG, fg=LABEL_FG)
label_country.place(relx=LABEL_WIDTH, rely=0, relheight=LABEL_HEIGHT, relwidth=LABEL_WIDTH)

label_last_update = Label(information_frame, textvariable=information_labels.get("Last Update"), bg=INFORMATION_BG, fg=LABEL_FG)
label_last_update.place(relx=0, rely=0.25, relheight=LABEL_HEIGHT, relwidth=LABEL_WIDTH)

label_new_cases = Label(information_frame, textvariable=information_labels.get("New Cases_text"), bg=INFORMATION_BG, fg=LABEL_FG)
label_new_cases.place(relx=0.50, rely=0.25, relheight=LABEL_HEIGHT, relwidth=LABEL_WIDTH)

label_new_deaths = Label(information_frame, textvariable=information_labels.get("New Deaths_text"), bg=INFORMATION_BG, fg=LABEL_FG)
label_new_deaths.place(relx=0, rely=0.50, relheight=LABEL_HEIGHT, relwidth=LABEL_WIDTH)

label_total_cases = Label(information_frame, textvariable=information_labels.get("Total Cases_text"), bg=INFORMATION_BG, fg=LABEL_FG)
label_total_cases.place(relx=0.50, rely=0.50, relheight=LABEL_HEIGHT, relwidth=LABEL_WIDTH)

label_total_deaths = Label(information_frame, textvariable=information_labels.get("Total Deaths_text"), bg=INFORMATION_BG, fg=LABEL_FG)
label_total_deaths.place(relx=0, rely=0.75, relheight=LABEL_HEIGHT, relwidth=LABEL_WIDTH)

label_total_recovered = Label(information_frame, textvariable=information_labels.get("Total Recovered_text"), bg=INFORMATION_BG, fg=LABEL_FG)
label_total_recovered.place(relx=0.50, rely=0.75, relheight=LABEL_HEIGHT, relwidth=LABEL_WIDTH)

error_label = Label(information_frame, bg="#f0b27a", text='Something went wrong, please try again!')

# BOTTOM FRAME
bottom_frame = Frame(screen_frame, bg = BOTTOM_FRAME_COLOR)
bottom_frame.place(relx=0, rely=0.95, relheight=0.05, relwidth=1)
# Bottom frame label
bottom_label = Label(bottom_frame, text="Covid 19 | Mini App 🤙 Stay safe!",fg="white", bg=BOTTOM_FRAME_COLOR)
bottom_label.pack(fill="y",expand=True)

root.mainloop()



