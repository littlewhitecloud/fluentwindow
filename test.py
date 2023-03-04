from ctypes import windll, c_int, byref, sizeof
from tkinter import *

def dark_title_bar(window):
	window.update()
	DWMWA_USE_IMMERSIVE_DARK_MODE = 20
	set_window_attribute = windll.dwmapi.DwmSetWindowAttribute
	get_parent = windll.user32.GetParent
	hwnd = get_parent(window.winfo_id())
	rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
	value = 2
	value = c_int(value)
	set_window_attribute(hwnd, rendering_policy, byref(value), sizeof(value))

root = Tk()
dark_title_bar(root)
root.geometry("750x405")
root.attributes("-alpha", 0.64)
root["background"] = "black"
root.mainloop()
