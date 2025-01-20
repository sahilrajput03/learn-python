import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RunScriptOnSaveHandler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name

    def on_modified(self, event):
        if event.src_path.endswith(self.script_name):
            print(f"Detected changes in {self.script_name}. Running script...")
            subprocess.run(["python", self.script_name], check=True)

if __name__ == "__main__":
    script_to_watch = "1.py"  # Replace with your Python file name
    path = "."  # Directory to watch

    event_handler = RunScriptOnSaveHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    print(f"Watching for changes in {script_to_watch}. Press Ctrl+C to stop.")
    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopped watching.")  
