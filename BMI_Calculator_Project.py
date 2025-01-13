import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from csv import DictWriter
import os
import matplotlib.pyplot as plt

win = tk.Tk()       # win --> window
win.title('Adult and Child BMI Calculator')


# creating label frame
label_frame = ttk.LabelFrame(win, text = 'BMI Details')
label_frame.grid(row=0, column=0, padx=40, pady=10)

# creating labels
height_label = ttk.Label(label_frame, text = 'Please, Enter your height in meter: ', font =("Helvetica", 14))

weight_label = ttk.Label(label_frame, text = 'Please, Enter your weight in kg: ', font=("Helvetica", 14))

# entry box variables
height_var = tk.StringVar()
weight_var = tk.StringVar()

# enrty boxes
height_entry = ttk.Entry(label_frame, width = 36, textvariable = height_var)
weight_entry = ttk.Entry(label_frame, width = 36, textvariable = weight_var)

# grid
height_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
weight_label.grid(row=1, column=0, padx = 5, pady = 5, sticky=tk.W)

height_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
weight_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

height_entry.focus()

# Defining funcion for visulaising the BMI result
def plot_bmi_result(bmi,result):
    categories = ['Underweight','Normal','Overweight','Obese']
    values = [18.5,24.9,29.9,40]
    colors = ['lightblue','lightgreen','yellow','red']

    if bmi <= 18.5:
        color = colors[0]
    elif bmi <= 24.9:
        color = colors[1]
    elif bmi <= 29.9:
        color = colors[2]
    else:
        color = colors[3]

    plt.figure(figsize=(6,4))
    plt.bar(categories, values, color=colors)
    plt.axhline(y=bmi,color=color,linewidth=4,label=f'BMI :{bmi}')
    plt.legend()
    plt.title("BMI Categories")
    plt.ylabel("BMI Value")
    plt.show()


# defining function for bmi
def bmi_calc():
    height = height_var.get()
    weight = weight_var.get()
    result = ""

    if height == '' or weight == '':
        m_box.showerror('Error','Please fill both height and weight')
    else:
        try:
            height = float(height) 
            weight = float(weight) 
        except ValueError:
            m_box.showerror('Error', 'Only digits are allowed')
        else:
            bmi = (weight)/(height)**2
            if bmi <= 0:
                m_box.showwarning('Invalid Input', f'Error!! Enter a valid input...')
            elif bmi <= 18.5:
                # Updating the result
                result = "Underweight"
                m_box.showinfo('BMI Details',f'Your BODY MASS INDEX is {bmi:.2f}.\nOOP\'s!, You are {result}.')
            elif bmi <= 24.9:
                result = "Healthy"
                m_box.showinfo('BMI Details', f'Your BODY MASS INDEX is {bmi:.2f}.\nThat\'s good, You are {result}.')
            elif bmi <= 29.9:
                result = "Over weight"
                m_box.showinfo('BMI Details', f"Your BODY MASS INDEX is {bmi:.2f}.\nAhhh! You are {result}.")
            else:
                result = "Obese"
                m_box.showinfo('BMI Details', f"Your BODY MASS INDEX is {bmi:.2f}.\nOh my god! You are {result}.")

    # saving data in CSV file 
    with open('BMI Deatils.csv', 'a', newline='') as f:
        csv_dictwriter = DictWriter(f, fieldnames = ['Height','Weight','BMI','BMI Result'])

        # calling function to visualise the Bmi Category
        plot_bmi_result(bmi,result)
        
        if os.stat(r'C:\Users\Disha\Desktop\Internship Project\BMI Calculator\BMI Deatils.csv').st_size == 00:          # check size of file if 0 then write headings
            csv_dictwriter.writeheader()
        
        csv_dictwriter.writerow({
            'Height' : height,
            'Weight' : weight,
            'BMI': f"{bmi:.2f}",
            'BMI Result' : result,
            })

# removing data when added
    height_entry.delete(0,tk.END)
    weight_entry.delete(0,tk.END)


# Button for calculating the BMI
bmi_btn = ttk.Button(win, text = 'Calculate', command = bmi_calc)
bmi_btn.grid(row=1, columnspan = 2, padx=40)

win.mainloop()