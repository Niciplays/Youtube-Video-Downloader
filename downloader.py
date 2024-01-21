import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def choose_directory():
    download_path = filedialog.askdirectory()
    download_path_entry.delete(0, tk.END)
    download_path_entry.insert(0, download_path)

def download_video():
    try:
        video_url = url_entry.get()
        download_path = download_path_entry.get()
        youtube = YouTube(video_url)
        video = youtube.streams.filter(progressive=True, file_extension="mp4").first()
        video.download(download_path)
        status_label.config(text="Download successful!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create and pack widgets
url_label = tk.Label(window, text="Enter YouTube Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=10)

download_path_label = tk.Label(window, text="Choose Download Directory:")
download_path_label.pack(pady=10)

download_path_entry = tk.Entry(window, width=50)
download_path_entry.pack(pady=10)

choose_directory_button = tk.Button(window, text="Choose Directory", command=choose_directory)
choose_directory_button.pack(pady=10)

download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack(pady=20)

status_label = tk.Label(window, text="")
status_label.pack()

# Run the main loop
window.mainloop()
