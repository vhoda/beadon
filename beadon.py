import sys
import os
import traceback
from tkinter import Tk, Label, messagebox
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip
import pygame

def play_video(video_path):
    try:

        pygame.mixer.init()
        
        # Cargar el video
        clip = VideoFileClip(video_path)


        audio_path = "temp_audio.mp3"
        clip.audio.write_audiofile(audio_path, logger=None)

        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        width, height = clip.size

        root = Tk()
        root.title("beadon")
        root.geometry(f"{width}x{height}")


        label = Label(root)
        label.pack()


        window_open = True


        def update_frame():
            if window_open:
                current_time = pygame.mixer.music.get_pos() / 1000  
                frame = clip.get_frame(current_time)
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image)
                label.config(image=photo)
                label.image = photo
                root.after(10, update_frame)
        update_frame()
        
        def on_close():
            nonlocal window_open
            window_open = False
            root.destroy()

            pygame.mixer.music.stop()

            os.remove(audio_path)

        root.protocol("WM_DELETE_WINDOW", on_close)
        root.mainloop()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}\n\n{traceback.format_exc()}")
        print(f"Ocurrió un error: {str(e)}")
        print(traceback.format_exc())

if __name__ == "__main__":
    video_path = "video.mp4"
    play_video(video_path)
