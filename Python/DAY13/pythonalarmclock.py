# Python Alarm Clock

import time
import datetime  # This allows us to manipulate dates and times
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().now().strftime("%H:%M:%S")
        print(current_time)


        if current_time == alarm_time:
            print("WAKE UP!")

            pygame.mixer.init() # Initialize , mixer is the main loop of the game 
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1) # Sleep

            is_running = False
        time.sleep(1) # sleep for 1 second      

if __name__ == "__main__":  # This script is run directly (not imported) then run the main function
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

