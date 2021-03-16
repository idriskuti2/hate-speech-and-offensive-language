import tkinter as tk

root = tk.Tk()
canvas  = tk.Canvas(root , height =700  , width = 800)
frame = tk.Frame(root , bg = '#80c1ff')
frame.place(relx = 0.1 , rely = 0.1 , relwidth = 0.8 , relheight = 0.8)
button = tk.Button(frame , text = 'Test button')
canvas.pack()
button.grid(row = 0 , column = 0)

label = tk.Label(frame , text = 'This is a label' , bg = 'yellow')
label.grid(row = 0 , column = 1)

entry = tk.Entry(frame , bg = 'green')
entry.grid(row = 0 , column = 2)
root.mainloop()
