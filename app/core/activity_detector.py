from datetime import datetime
import time
from app.core.window_tracker import get_active_window_info
from app.config import WORK_APPS


previous_window = None
started_at = None

while True:
    current_window = get_active_window_info()
    now_time = datetime.now()

    if current_window != previous_window:
        if previous_window is not None:
            ended_at = now_time
            duration =  int(round((ended_at - started_at).total_seconds()))

            print("Завершена активность:")
            print(previous_window)
            print("Длительность:", duration, "сек.")

        previous_window = current_window
        started_at = now_time

    time.sleep(3)
