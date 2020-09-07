import time


class Pomodoro:
    def __init__(self, focus_time: float or int,
                 pause_time: float or int) -> tuple:
        """
        :param focus_time: время фокусировки в минутах
        :param pause_time: время на паузу, в минутах
        """
        self.focus_time = focus_time
        self.pause_time = pause_time

    def focus(self):
        print('Start focus!')
        sec = self.focus_time * 60
        for _ in range(int(sec)):
            sec = sec - 1
            print(f'left time: {sec // 60} min, {sec % 60} sec')
            time.sleep(1)
        return 'End focus!'

    def pause(self):
        print('Start pause!')
        sec = self.pause_time * 60
        for _ in range(int(sec)):
            time.sleep(1)
        return 'End pause!'
