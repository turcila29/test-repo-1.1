import tkinter

def strip_vowels():
    global label
    label.destroy()
    label = tkinter.Label(root, text =  ''.join(char for char in string if char not in 'aeiouAEIOU'))
    label.grod(row=2, column=1)
root = tkinter.Tk()

label = tkinter.Label(root, text = "")
input1 = tkinter.Entry(root)
input1.grid(row=1, column=2)

submit = tkinter.Button(root, test = "strip vowels", command=strip_vowels)


if __name__ == '__main__':
    root.mainloop()
