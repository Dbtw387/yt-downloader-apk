import os
import yt_dlp
import requests
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# --- Скачивание видео с поддержкой YouTube, X, Reddit ---
def download_video(url, folder, proxy=None):
    ydl_opts = {
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'format': 'mp4',
    }
    if proxy:
        ydl_opts['proxy'] = proxy

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# --- Интерфейс ---
def start_download():
    url = entry.get()
    folder = filedialog.askdirectory()
    if not url or not folder:
        messagebox.showerror("Ошибка", "Укажи ссылку и папку для сохранения!")
        return
    try:
        proxy = proxy_entry.get() if proxy_entry.get() else None
        download_video(url, folder, proxy)
        messagebox.showinfo("Успех", "Видео скачано!")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("Video Downloader")
root.geometry("400x500")
root.configure(bg="#2c2f33")

# Картинка (аниме-стиль, для примера онлайн)
try:
    img_url = "https://i.imgur.com/4AiXzf8.jpeg"
    img_data = requests.get(img_url).content
    with open("bg.jpg", "wb") as f:
        f.write(img_data)
    bg_image = Image.open("bg.jpg").resize((380, 200))
    bg_photo = ImageTk.PhotoImage(bg_image)
    label_img = tk.Label(root, image=bg_photo)
    label_img.pack(pady=10)
except:
    pass

tk.Label(root, text="Ссылка на видео:", fg="white", bg="#2c2f33").pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Label(root, text="Прокси (опц.):", fg="white", bg="#2c2f33").pack()
proxy_entry = tk.Entry(root, width=40)
proxy_entry.pack(pady=5)

btn = tk.Button(root, text="Скачать", command=start_download, bg="#7289da", fg="white")
btn.pack(pady=20)

root.mainloop()
