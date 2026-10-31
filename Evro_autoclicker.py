import keyboard
import threading
import pyautogui as pag
import customtkinter as ctk
import time
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("Light")

is_clicking = False

app=ctk.CTk(fg_color="white")
app.geometry("800x600")
app.title("Evro autoclicker")

cliks=ctk.CTkEntry(app,width=100,height=50,fg_color="white",placeholder_text="Кол-во кликов",text_color="black",border_color="white")
intervale=ctk.CTkEntry(app,width=160,height=50,fg_color="white",placeholder_text="Интервал меж кликами",text_color="black",border_color="white")
duratione=ctk.CTkEntry(app,width=130,height=50,fg_color="white",placeholder_text="Время до начала",text_color="black",border_color="white")
oror=ctk.CTkEntry(app,width=100,height=50,fg_color="white",placeholder_text="Вид клика",text_color="black",border_color="white")
binde=ctk.CTkEntry(app,width=150,height=50,fg_color="white",placeholder_text="Бинд на тормоз",text_color="black",border_color="white")
whenclick=ctk.CTkEntry(app,width=250,height=50,fg_color="white",placeholder_text="Вид клика 2 правый или левый",text_color="black",border_color="white")
bendi=ctk.CTkEntry(app,width=100,height=50,fg_color="white",placeholder_text="бинд на старт",text_color="black",border_color="white")

bendi.place(y=180,x=5)
whenclick.place(y=120,x=260)
binde.place(y=120,x=5)
oror.place(y=120,x=150)
duratione.place(y=5,x=285)
intervale.place(y=5,x=115)
cliks.place(y=5,x=5)

# def lock(event=None):
#     cliks.configure(state="disabled")
# def lock1(event=None):
#     intervale.configure(state="disabled")
# def lock2(event=None):
#     duratione.configure(state="disabled")
# def lock3(event=None):
#     oror.configure(state="disabled")

def stop_by_key():
    global is_clicking,binder
    is_clicking = False

def start():
    global is_clicking
    if is_clicking:
        return
    is_clicking = True
    threading.Thread(target=run_clicker_logic, daemon=True).start()

def run_clicker_logic():
    global is_clicking,binder
    
    pag.PAUSE=0.001

    bendir=str(bendi.get())
    whenclicke=str(whenclick.get())
    binder=str(binde.get())
    orore_str = str(oror.get())
    durati = float(duratione.get())
    clicke = int(cliks.get())
    interva = float(intervale.get()) 
    keyboard.add_hotkey(bendir,start)
    keyboard.add_hotkey(binder, stop_by_key)
    time.sleep(durati)
    if whenclicke == "left":
        if orore_str == "click":
            for i in range(clicke):
                if not is_clicking: break  
                pag.click(clicks=1)
                start_delay = time.perf_counter()
                if interva <= 0.001:
                    time.sleep(0.001) 
                else:
                    start_delay = time.perf_counter()
                    while time.perf_counter() - start_delay < interva:
                        pass
                
        elif orore_str == "doubleclick":
            for i in range(clicke):
                if not is_clicking: break
                pag.doubleClick() 
                start_delay = time.perf_counter()
                if interva <= 0.001:
                    time.sleep(0.001) 
                else:
                    start_delay = time.perf_counter()
                    while time.perf_counter() - start_delay < interva:
                        pass

        elif orore_str == "tripleclick":
            for i in range(clicke):
                if not is_clicking: break
                pag.tripleClick()     
                start_delay = time.perf_counter()
                if interva <= 0.001:
                    time.sleep(0.001) 
                else:
                    start_delay = time.perf_counter()
                    while time.perf_counter() - start_delay < interva:
                        pass
        else:
            pass
    elif whenclick == "right":
        if orore_str == "click":
            for i in range(clicke):
                if not is_clicking: break  
                pag.click(clicks=1,button="right")
                start_delay = time.perf_counter()
                if interva <= 0.001:
                    time.sleep(0.001) 
                else:
                    start_delay = time.perf_counter()
                    while time.perf_counter() - start_delay < interva:
                        pass
                
        elif orore_str == "doubleclick":
            for i in range(clicke):
                if not is_clicking: break
                pag.doubleClick(button="right") 
                start_delay = time.perf_counter()
                if interva <= 0.001:
                    time.sleep(0.001) 
                else:
                    start_delay = time.perf_counter()
                    while time.perf_counter() - start_delay < interva:
                        pass

        elif orore_str == "tripleclick":
            for i in range(clicke):
                if not is_clicking: break
                pag.tripleClick(button="right")     
                start_delay = time.perf_counter()
                if interva <= 0.001:
                    time.sleep(0.001) 
                else:
                    start_delay = time.perf_counter()
                    while time.perf_counter() - start_delay < interva:
                        pass
        else:
            pass
    is_clicking = False

# cliks.bind("<Return>",lock)
# intervale.bind("<Return>",lock1)
# duratione.bind("<Return>",lock2)
# oror.bind("<Return>",lock3)

Buttone=ctk.CTkButton(app,width=100,height=50,fg_color="white",text=f"Начать",text_color="gray",border_color="white",command=start,hover_color="white")
Buttone.place(y=60,x=150)

app.mainloop()
