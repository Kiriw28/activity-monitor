import psutil
import win32gui, win32process



# Получение данных об активном окне
def get_active_window_info():

    hwnd = win32gui.GetForegroundWindow() # Получение HWND
    title_window = win32gui.GetWindowText(hwnd) # Данные окна
    getting_pid_win_process = win32process.GetWindowThreadProcessId(hwnd) # Получение идентификатора потока и процесса
    pid_win_process = getting_pid_win_process[1]
    piece_title_window = title_window.split(" - ")
    app_name = piece_title_window[-1]

    return pid_win_process, app_name


# Получение списка активных процессов
def get_all_pids_and_names_peocesses():
    activities = []
    for proc in psutil.process_iter(['pid', 'name']):
        activities.append({proc.pid: proc.name()})
    
    return activities






