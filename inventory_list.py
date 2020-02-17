import tkinter as tk

# Inventory List

# Create the window first
win = tk.Tk()
win.geometry("1000x300") #Configure the width by height size
mainHome = tk.Frame(win)

# Create the labels below
lTitle = tk.Label(win, text = 'Inventory')
lSearch = tk.Label(win, text = 'Search')
lPartName = tk.Label(win, text = 'Part Name')
lPartNum = tk.Label(win, text = 'Part No.')
lManufact = tk.Label(win, text = 'Manufacturer')
lQuantity = tk.Label(win, text = 'Quantity')

# Create the entries below
eSearch = tk.Entry(win)
ePartName = tk.Entry(win)
ePartNum = tk.Entry(win)
eManufact = tk.Entry(win)
eQuantity = tk.Entry(win)

# Now place all the parts in the GUI
lTitle.pack(fill=tk.X, pady=10)
lSearch.pack(fill=tk.X, pady=10)
eSearch.pack(fill=tk.X, pady=10)
lPartName.pack(padx=10, pady=10, side=tk.LEFT)
lPartNum.pack(padx=10, pady=10, side=tk.LEFT)
lManufact.pack(padx=10, pady=10, side=tk.LEFT)
lQuantity.pack(padx=10, pady=10, side=tk.LEFT)
ePartName.pack(padx=10, pady=10, side=tk.LEFT)
ePartNum.pack(padx=10, pady=10, side=tk.LEFT)
eManufact.pack(padx=10, pady=10, side=tk.LEFT)
eQuantity.pack(padx=10, pady=10, side=tk.LEFT)

win.mainloop()
