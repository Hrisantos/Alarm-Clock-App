import pygame
import time


class AlarmClock:

    def __init__(self):
        self.alarm_time = None

    pygame.mixer.init()

    def set_alarm(self, hour, minute):
        self.alarm_time = (hour, minute)
        print(f"Alarm set for {hour}:{minute}")

    def check_alarm(self):
        while True:
            current_time = time.localtime(time.time())
            current_hour = current_time.tm_hour
            current_minute = current_time.tm_min

            if self.alarm_time[0] == current_hour and self.alarm_time[1] == current_minute:
                self.trigger_alarm()
                break

            time.sleep(1)

    def trigger_alarm(self):
        print("Alarm! It's time to wake up!")
        pygame.mixer.music.load("Alarm-clock-ringing-sound-effect.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
