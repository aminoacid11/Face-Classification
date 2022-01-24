from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from predict import *
import tkinter.messagebox as msgbox
from PIL import ImageTk, Image

root = Tk()
root.title("Face classification APP")
root.geometry("1250x770+70+20")
root.configure(bg='#3b5998')

global panel
temp_list = []

# Insert photo to canvas
def input_picture(size):
    for i,pht in enumerate(list_file.get(0,END)):
        temp_img = Image.open("images/predict/cat/{}.jpg".format(i))
        temp_img = temp_img.resize((size,size), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(temp_img)
        temp_list.append(img)       
    panel.config(image=temp_list[-1])
    panel.pack(side = LEFT, fill = "both", expand = "yes")
# View selected image command
def view():
    all_files = list_file.get(0, END)
    image_path_ind = list_file.curselection()
    sel_path = [all_files[item] for item in image_path_ind]
    opened_img = Image.open(sel_path[0])
    opened_img = opened_img.resize((550,550), Image.ANTIALIAS)
    fin_img = ImageTk.PhotoImage(opened_img)
    panel.config(image=fin_img)
    panel.image = fin_img
    panel.pack(side = LEFT, fill = "both", expand = "yes")
# Find prediction
def pred_photo():
    if os.path.isdir('images') is False:
        os.makedirs('images')
    if os.path.isdir('images/predict') is False:
        os.makedirs('images/predict')
        os.makedirs('images/predict/cat')
        os.makedirs('images/predict/dog')
        os.makedirs('images/predict/rabbit')
        os.makedirs('images/predict/horse')
        os.makedirs('images/predict/fox')
        os.makedirs('images/predict/squirrel')
        os.makedirs('images/predict/bear')
        os.makedirs('images/predict/wolf')
        os.makedirs('images/predict/monkey')
        os.makedirs('images/predict/turtle')
        os.makedirs('images/predict/pig')
        os.makedirs('images/predict/deer')
        os.makedirs('images/predict/frog')
    pred_path = 'images/predict'
    for index,x in enumerate(list_file.get(0,END)):
        image = Image.open(x)
        temp_path = 'images/predict/cat'
        predict_path = os.path.join(temp_path, '{}.jpg'.format(index))
        image.save(predict_path)
    pred_batches= ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
                .flow_from_directory(directory=pred_path, target_size=(224,224), classes=['bear','cat','deer','dog','fox','frog','horse','monkey','pig','rabbit','squirrel','turtle','wolf'], batch_size=10, shuffle=False)
    pred_result = predict_animal(pred_batches)
    size=550
    input_picture(size)
    for file in os.listdir(temp_path):
        if file.endswith('.jpg'):
            os.remove(os.path.join(temp_path,file))
    total_resp = ''
    for p_ind,pr in enumerate(pred_result):
        if pr == 0:
            response = 'The animal in image {} is predicted to be "Bear"'.format(p_ind+1)
        elif pr == 1:
            response = 'The animal in image {} is predicted to be "Cat"'.format(p_ind+1)
        elif pr == 2:
            response = 'The animal in image {} is predicted to be "Deer"'.format(p_ind+1)
        elif pr == 3:
            response = 'The animal in image {} is predicted to be "Dog"'.format(p_ind+1)
        elif pr == 4:
            response = 'The animal in image {} is predicted to be "Fox"'.format(p_ind+1)
        elif pr == 5:
            response = 'The animal in image {} is predicted to be "Frog"'.format(p_ind+1)
        elif pr == 6:
            response = 'The animal in image {} is predicted to be "Horse"'.format(p_ind+1)
        elif pr == 7:
            response = 'The animal in image {} is predicted to be "Monkey"'.format(p_ind+1)
        elif pr == 8:
            response = 'The animal in image {} is predicted to be "Pig"'.format(p_ind+1)
        elif pr == 9:
            response = 'The animal in image {} is predicted to be "Rabbit"'.format(p_ind+1)
        elif pr == 10:
            response = 'The animal in image {} is predicted to be "Squirrel"'.format(p_ind+1)
        elif pr == 11:
            response = 'The animal in image {} is predicted to be "Turtle"'.format(p_ind+1)
        elif pr == 12:
            response = 'The animal in image {} is predicted to be "Wolf"'.format(p_ind+1)
        total_resp += response + '\n'
    result_wind.config(state=NORMAL)
    result_wind.insert(END, total_resp)
    result_wind.config(foreground='#000000',font=("Helvetica", 14))
    result_wind.config(state=DISABLED)
# Add photo
def add_photo():
    photos = filedialog.askopenfilenames(title="Please select image files", \
            filetypes=(("JPG file", "*.jpg"), ("All types", "*.*")), \
            initialdir="C:/")
    for photo in photos:
        list_file.insert(END, photo)
# Delete photo
def del_photo():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
# Clear All
def clear_all():
    list_file.delete(0,END)
    result_wind.config(state=NORMAL)
    result_wind.delete("1.0",END)
    result_wind.config(state=DISABLED)
    panel.config(image='')
# Start command
def start():
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add photos")
        return
    pred_photo()

# Top button frame
photo_frame = Frame(root,bg='#3b5998')
photo_frame.pack(fill='x', padx=5, pady=5)
btn_photo_add = Button(photo_frame, padx=5, pady=5, width=12, text="Choose photo", command=add_photo)
btn_photo_add.pack(side='left')
btn_photo_clear = Button(photo_frame, padx=5, pady=5, width=12, text="Clear All", command=clear_all)
btn_photo_clear.pack(side='right')
btn_photo_del = Button(photo_frame, padx=5, pady=5, text="Delete selected image", command=del_photo)
btn_photo_del.pack(side='right')

# List frame
list_label = Label(root, text="Selected Images",bg='#3b5998',fg='#ffffff',font='Helvetica 18 bold')
list_label.place(x=10,y=40)
scroll_window1 = Text(root, bd=0, bg='#dfe3ee')
scroll_window1.place(x=557,y=80,height=250,width=20)
scroll_window2 = Text(root, bd=0, bg='#dfe3ee')
scroll_window2.place(x=10,y=330,height=20,width=567)
scrollbar = Scrollbar(scroll_window1)
scrollbar.pack(side=LEFT, fill=Y)
scrollbar1x = Scrollbar(scroll_window2, orient=HORIZONTAL)
scrollbar1x.pack(fill=X)
list_file = Listbox(root, selectmode='extended', height=15, yscrollcommand=scrollbar.set, bg='#dfe3ee')
list_file.config(yscrollcommand=scrollbar.set, xscrollcommand=scrollbar1x.set)
scrollbar1x.config(command=list_file.xview)
scrollbar.config(command=list_file.yview)
list_file.place(x=10,y=80, height=250, width=550)

# Result frame
label_book = Label(root,text="Predicted Results:", font='Helvetica 18 bold',bg='#3b5998',fg='#ffffff')
label_book.place(x=10,y=380)
result_wind = Text(root,bg='#dfe3ee',fg='#ffffff',font='Helvetica 14 bold')
scroll_window = Text(root, bd=0, bg='#dfe3ee')
scroll_window.place(x=560,y=421,height=299,width=20)
scrollbar2 = Scrollbar(scroll_window)
scrollbar2.pack(side=LEFT, fill=Y)
result_wind.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=result_wind.yview)
result_wind.config(state=DISABLED)
scroll_window.config(state=DISABLED)
result_wind.place(x=10, y=420, height=300, width=550)

# Canvas
canvas = Canvas(root,bg='#dfe3ee',bd=1)
panel = Label(canvas, bg='#dfe3ee')
canvas.create_window(650, 150, window=panel)
canvas.place(x=650, y=130, height=550, width=550)

# View photo Button
btn = Button(root,padx=5, pady=9,bg='#dfe3ee',text="View Selected Image",command=view)
btn.place(x=860,y=70)

# Run frame
btn_close = Button(root, padx=5, pady=9, text="Close", width=12, command=root.quit)
btn_close.place(x=1130,y=708)
btn_start = Button(root, padx=5, pady=9, text="Start", width=12, command=start)
btn_start.place(x=1000,y=708)

root.resizable(False,False)
root.mainloop()