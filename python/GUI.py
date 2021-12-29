import tkinter as tk
from tkinter import messagebox
from CLI import GPANormalizer, AverageCalculator

def main():
    scores_list = ["N/A"]
    units_list = ["N/A"]
    
    window = tk.Tk()
    window.geometry("450x250")
    
    frame_top = tk.Frame(window)
    frame_top.pack()
    
    label_lastScore = tk.Label(window, text=('last score: ' + str(scores_list[-1])))
    label_lastScore.place(x=80, y=20)
    
    label_lastUnit = tk.Label(window, text=('last unit: ' + str(units_list[-1])))
    label_lastUnit.place(x=280, y=20)

    label_score = tk.Label(window, text='Score:')
    label_score.place(x=80, y=80)
    
    entry_score = tk.Entry(window)
    entry_score.place(x=150, y=80)
    
    label_unit = tk.Label(window, text='Unit:')
    label_unit.place(x=80, y=120)
    
    entry_unit = tk.Entry(window)
    entry_unit.place(x=150, y=120)
       
    def Push():
        if (entry_score.get() != '') and (entry_unit.get() != ''):
            try:
                score = float(entry_score.get())
                unit = int(entry_unit.get())
                scores_list.append(score)
                units_list.append(unit)
                entry_score.delete(0, 'end')
                entry_unit.delete(0, 'end')
                label_lastScore.configure(text=('last score: ' + str(scores_list[-1])))
                label_lastUnit.configure(text=('last unit: ' + str(units_list[-1])))
            except:
                messagebox.showerror('Error', 'Invalid inputs')
        else:
            messagebox.showerror('Error', 'Input box is empty')
        
    def Pop():
        if(len(scores_list) > 1):
            scores_list.pop()
            units_list.pop()
            entry_score.delete(0, 'end')
            entry_unit.delete(0, 'end')
            label_lastScore.configure(text=('last score: ' + str(scores_list[-1])))
            label_lastUnit.configure(text=('last unit: ' + str(units_list[-1])))
        else:
            messagebox.showerror('Error', 'List is empty')
    
    
    def Calculate():
        scores = scores_list[1 : ]
        units = units_list[1 : ]
        scores = GPANormalizer(scores)
        average = AverageCalculator(scores, units)
        messagebox.showinfo('GPA', 'Your GPA is: ' + str(average)[ : 3])
        
        
    button_push = tk.Button(window, text='PUSH', width=10, command=Push)
    button_push.place(x=30, y=200)
    
    button_calculate = tk.Button(window, text='CALCULATE', width=10, command=Calculate)
    button_calculate.place(x=160, y=200)
    
    button_pop = tk.Button(window, text='POP', width=10, command=Pop)
    button_pop.place(x=300, y=200)


    window.mainloop()
    
if __name__ == "__main__":
    main()