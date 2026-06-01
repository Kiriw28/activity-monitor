import psutil
import win32gui, win32process



# Получение данных об активном окне
def get_active_window_info():

    hwnd = win32gui.GetForegroundWindow() # Получение HWND
    title_window = win32gui.GetWindowText(hwnd) # Данные окна
    _, pid = win32process.GetWindowThreadProcessId(hwnd) # Получение идентификатора потока и процесса
    process = psutil.Process(pid)
    process_name = process.name()


    return {
        "process_name": process_name,
        "window_title": title_window
    }