import tkinter as tkinter

tk = tkinter.Tk()

has_prev_key_release = None

'''
When holding a key down, multiple key press and key release events are fired in
succession. Debouncing is implemented in order to squash these repeated events
and know when the "real" KeyRelease and KeyPress events happen.
'''

def on_key_release(event):
    global has_prev_key_release
    has_prev_key_release = None
    print("on_key_release", repr(event.char))

def on_key_press(event):
    print("on_key_press", repr(event.char))

def on_key_release_repeat(event):
    global has_prev_key_release
    has_prev_key_release = tk.after_idle(on_key_release, event)
    print("on_key_release_repeat", repr(event.char))

def on_key_press_repeat(event):
    global has_prev_key_release
    if has_prev_key_release:
        tk.after_cancel(has_prev_key_release)
        has_prev_key_release = None
        print("on_key_press_repeat", repr(event.char))
    else:
        on_key_press(event)

frame = tkinter.Frame(tk, width=100, height=100)
frame.bind("<KeyRelease-a>", on_key_release_repeat)
frame.bind("<KeyPress-a>", on_key_press_repeat)
frame.bind("<KeyRelease-s>", on_key_release_repeat)
frame.bind("<KeyPress-s>", on_key_press_repeat)
frame.pack()
frame.focus_set()

tk.mainloop()
