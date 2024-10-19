import subprocess

# Run the service corresponding to the user_app
def run_user_service():
    subprocess.Popen([r"C:\Users\ragha\Downloads\version_2_social_media_app\version_2\social_media_app\venv\Scripts\python","user_app/app.py"])

# Run the service corresponding to the post_app
def run_post_service():
    subprocess.Popen([r"C:\Users\ragha\Downloads\version_2_social_media_app\version_2\social_media_app\venv\Scripts\python","post_app/app.py"])

def run_shared():
    subprocess.Popen([r"C:\Users\ragha\Downloads\version_2_social_media_app\version_2\social_media_app\venv\Scripts\python","shared/app.py"])

if __name__ == '__main__':
    run_user_service()
    run_post_service()
    run_shared()

    # Graceful Termination of the two subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating both the processes. Alvida!")
