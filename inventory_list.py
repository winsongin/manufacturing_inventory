import tkinter as tk

# Inventory List

# Create the window first
win = tk.Tk()
mainHome = tk.Frame(win)
mainHome.pack()

# Create the labels below
lTitle = tk.Label(win, text = 'Inventory')
lSearch = tk.Label(win, text = 'Search')
lPartName = tk.Label(win, text = 'Part Name')
lPartNum = tk.Label(win, text = 'Part No.')
lManufact = tk.Label(win, text = 'Manufacturer')
lQuantity = tk.Label(win, text = 'Quantity')

# Entry object is for search
#eSearch = tk.Entry(win, textvariable = search)

# Now place all the parts in the GUI
lTitle.pack(padx=0, pady=10, side=tk.TOP)
lSearch.pack(padx=0, pady=10, side=tk.TOP)
lPartName.pack(padx=5, pady=20, side=tk.LEFT)
lPartNum.pack(padx=5, pady=20, side=tk.LEFT)
lManufact.pack(padx=5, pady=20, side=tk.LEFT)
lQuantity.pack(padx=5, pady=20, side=tk.LEFT)

win.mainloop()
