from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    male = gender_var_male.get();
    age = int(age_spinbox.get())
    
    bmi = kg/(m*m)
    bmi = round(bmi, 1)

    if male == True:
        if bmi < 18.5:
            messagebox.showinfo('bmi-pythonguides', f'ИМТ={bmi} соответствует недостаточному весу \nВы мужчина, ваш возраст - {age}')
        elif (bmi > 18.5) and (bmi < 24.9):
            messagebox.showinfo('bmi-pythonguides', f'ИМТ={bmi} соответствует нормальному весу \nВы мужчина, ваш возраст - {age}')
        elif (bmi > 24.9) and (bmi < 29.9):
            messagebox.showinfo('bmi-pythonguides',f'ИМТ={bmi} соответствует избыточному весу \nВы мужчина, ваш возраст - {age}')
        else:
            messagebox.showinfo('bmi-pythonguides', f'ИМТ={bmi} соответствует ожирению \nВы мужчина, ваш возраст - {age}')
    else:
        if bmi < 18.5:
            messagebox.showinfo('bmi-pythonguides', f'ИМТ={bmi} соответствует недостаточному весу \n Вы женщина, ваш возраст - {age}')
        elif (bmi > 18.5) and (bmi < 24.9):
            messagebox.showinfo('bmi-pythonguides', f'ИМТ={bmi} соответствует нормальному весу \n Вы женщина, ваш возраст - {age}')
        elif (bmi > 24.9) and (bmi < 29.9):
            messagebox.showinfo('bmi-pythonguides',f'ИМТ={bmi} соответствует избыточному весу \n Вы женщина, ваш возраст - {age}')
        else:
            messagebox.showinfo('bmi-pythonguides', f'ИМТ={bmi} соответствует ожирению \n Вы женщина, ваш возраст - {age}')

window = Tk()
window.title('Калькулятор индекса массы тела (ИМТ)')
window.geometry('400x300')
frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)
height_lb = Label(
    frame,
    text="Введите свой рост (в см) "
)
height_lb.grid(row=3, column=1)
weight_lb = Label(
    frame,
    text="Введите свой вес (в кг) ",
)
weight_lb.grid(row=4, column=1)
height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)
weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)
cal_btn = Button(
    frame,
    text='Рассчитать ИМТ',
    command=calculate_bmi
)
cal_btn.grid(row=11, column=2)

# Добавление новых виджетов:
age_lb = Label(frame, text="Введите свой возраст:")
age_lb.grid(row=5, column=1)
age_spinbox = Spinbox(frame, from_=1, to=120)
age_spinbox.grid(row=5, column=2, pady=5)

gender_lb = Label(frame, text="Выберите свой пол:")
gender_lb.grid(row=6, column=1)
gender_var_male = BooleanVar()
male_cb = Checkbutton(frame, text="Я мужчина", variable=gender_var_male)
male_cb.grid(row=6, column=2)


window.mainloop()
