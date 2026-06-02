from app.core.activity_detector import track_session
from app.storage.json_storage import add_activity


def main():

    for one_session in track_session():
        add_activity(one_session)


if __name__ == "__main__":
    main()