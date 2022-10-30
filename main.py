from tkinter import *
from container_canvas import ContainerCanvas


root = Tk()
# root.attributes("-fullscreen", True)
root.geometry("800x500")

management_map = ContainerCanvas(root)


root.mainloop()