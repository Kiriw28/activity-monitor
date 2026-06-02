from datetime import datetime
import time
from app.core.window_tracker import get_active_window_info
# from app.config import WORK_APPS # отложено по соображениям логики



def track_session():

    previous_window = None
    started_at = None
    one_session = None

    while True:
        current_window = get_active_window_info()
        now_time = datetime.now()

        if current_window != previous_window:
            if previous_window is not None:
                ended_at = now_time
                duration =  int(round((ended_at - started_at).total_seconds()))

                one_session = previous_window
                one_session["duration_one_session"] = duration
                yield one_session
                
                # print("Завершена активность:")
                # print(previous_window)
                            
            previous_window = current_window
            started_at = now_time

        time.sleep(3)
