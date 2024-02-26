import datetime
import asyncio
import streamlink
import e-posta
import tkinter as tk
from tkinter import ttk, messagebox
import threading

sayac_h = 0
sayac_w = 0
hd_loop_flag = True
way_loop_flag = True


async def control_hd(url_hd):
    global sayac_h  # sayac_h değişkenini global olarak tanımlıyoruz
    global hd_loop_flag
    global time_eposta
    while hd_loop_flag:
        time = datetime.datetime.now().strftime("%H:%M:%S - %d:%m:%Y")
        try:
            # StreamLink ile canlı yayını al
            streams = streamlink.streams(url_hd)
            if not streams:
                sayac_h += 1
                message = f"Yayın Kontrol Et !  {time}"
                update_log(message)
                log_hd(url_hd)
                if sayac_h == 3:
                    message2 = f"E-posta Gönderiliyor = {time}"
                    update_log(message2)
                    log_hd(url_hd)
                    e-posta()

            else:
                sayac_h = 0
                time = datetime.datetime.now().strftime("%H:%M:%S - %d:%m:%Y")
                ms = f"Yayın Var  = {time}"
                update_log(ms)

        except Exception as e:
            time = datetime.datetime.now().strftime("%H:%M:%S - %d:%m:%Y")
            error = (f"Hata!!  = {time}",e)
            update_log(error)
            log_hd(url_hd)
        await asyncio.sleep(10)

async def control_way(url_way):
    global sayac_w  # sayac_h değişkenini global olarak tanımlıyoruz
    global way_loop_flag
    while way_loop_flag:
        time = datetime.datetime.now().strftime("%H:%M:%S - %d:%m:%Y")
        try:
            # StreamLink ile canlı yayını al
            streams = streamlink.streams(url_way)
            if not streams:
                sayac_w += 1
                time = datetime.datetime.now().strftime("%H:%M:%S - %d:%m:%Y")
                message = f"Yayın Sorunu!  = {time}"
                update_log(message)
                log_way(url_way)
                if sayac_w == 3:
                    message2 = f"E-posta Gönderiliyor! = {time}"
                    update_log(message2)
                    log_way(url_way)
                    e-posta()
            else:
                sayac_w = 0
                ms = f"Yayın Var  = {time}"
                update_log(ms)
        except Exception as e:
            error = (f"Hata !  = {time}", e )
            update_log(error)
            log_way(url_way)
        await asyncio.sleep(10)


def log_hd(url_hd):
    error_time = datetime.datetime.now().strftime("%H:%M:%S - %d:%m:%Y")
    with open('test', 'a', encoding='utf-8') as log_file:
        log_file.write(f'{url_hd}: Yayın Sorunu !! ={error_time}')
    log_file.close()

def log_way(url_way):
    error_time = datetime.datetime.now().strftime("%H:%M:%S - %d:%m:%Y")
    with open('way_youtube_log.txt', 'a', encoding='utf-8') as log_file :
        log_file.write(f'{url_way}: Yayın Sorunu !! ={error_time}')
    log_file.close()



# Arayüz

def start_stop_hd():
    global hd_loop_flag
    if hd_status.get() == "Başlat":
        hd_loop_flag = True
        hd_status.set("Durdur")
        hd_url = hd_entry.get()
        threading.Thread(target=run_start_stop_hd, args=(hd_url,)).start()
    else:
        hd_status.set("Başlat")
        hd_loop_flag = False
def run_start_stop_hd(hd_url):
    asyncio.run(control_hd(hd_url))

def start_stop_way():
    global way_loop_flag
    if way_status.get() == "Başlat":
        way_loop_flag = True
        way_status.set("Durdur")
        way_url = way_entry.get()
        threading.Thread(target=run_start_stop_way, args=(way_url,)).start()
    else:
        way_status.set("Başlat")
        way_loop_flag = False

def run_start_stop_way(way_url):
    asyncio.run(control_way(way_url))


def update_log(message):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)  # En son eklenen satıra odaklan
    log_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Youtube Yayın Kontrol Arayüzü")

# HD Yayını
hd_label = ttk.Label(root, text="HD Youtube Yayını URL:")
hd_label.grid(row=0, column=0, padx=5, pady=5)
hd_entry = ttk.Entry(root, width=40)
hd_entry.grid(row=0, column=1, padx=5, pady=5)
hd_status = tk.StringVar()
hd_status.set("Başlat")
hd_button = ttk.Button(root, textvariable=hd_status, command=start_stop_hd)
hd_button.grid(row=0, column=2, padx=5, pady=5)

# Way Yayını
way_label = ttk.Label(root, text="Way Youtube Yayını URL:")
way_label.grid(row=1, column=0, padx=5, pady=5)
way_entry = ttk.Entry(root, width=40)
way_entry.grid(row=1, column=1, padx=5, pady=5)
way_status = tk.StringVar()
way_status.set("Başlat")
way_button = ttk.Button(root, textvariable=way_status, command=start_stop_way)
way_button.grid(row=1, column=2, padx=5, pady=5)



# Log Paneli
log_label = ttk.Label(root, text="Log Kayıtları:")
log_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
log_text = tk.Text(root, width=60, height=10)
log_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
log_text.config(state=tk.DISABLED)

def on_key_press(event):
    if event.keysym == "Escape":
        if messagebox.askyesno("Çıkış", "Programdan çıkmak istediğinizden emin misiniz?"):
            root.destroy()
root.bind("<KeyPress>", on_key_press)
root.mainloop()
