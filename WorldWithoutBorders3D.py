"""
World Without Borders 3D - Windows launcher.
Serves the game from a private local web server and opens it in its own app window
(Microsoft Edge or Google Chrome in "app mode"). Standard library only.
"""
import functools
import http.server
import os
import shutil
import socket
import subprocess
import sys
import threading
import webbrowser

PORT = 47820          # fixed so your save (browser storage) is found every time
TITLE = "World Without Borders 3D"


def base_dir():
    return getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))


GAME_DIR = os.path.join(base_dir(), "game")
URL = f"http://127.0.0.1:{PORT}/index.html"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


def port_in_use():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
        return s.connect_ex(("127.0.0.1", PORT)) == 0


def start_server():
    handler = functools.partial(QuietHandler, directory=GAME_DIR)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def find_browser():
    env = os.environ
    candidates = [
        os.path.join(env.get("ProgramFiles(x86)", r"C:\Program Files (x86)"), r"Microsoft\Edge\Application\msedge.exe"),
        os.path.join(env.get("ProgramFiles", r"C:\Program Files"), r"Microsoft\Edge\Application\msedge.exe"),
        os.path.join(env.get("ProgramFiles", r"C:\Program Files"), r"Google\Chrome\Application\chrome.exe"),
        os.path.join(env.get("ProgramFiles(x86)", r"C:\Program Files (x86)"), r"Google\Chrome\Application\chrome.exe"),
        os.path.join(env.get("LOCALAPPDATA", ""), r"Google\Chrome\Application\chrome.exe"),
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    for name in ("msedge", "google-chrome", "chromium", "chrome"):
        p = shutil.which(name)
        if p:
            return p
    return None


def profile_dir():
    root = os.getenv("APPDATA") or os.path.join(os.path.expanduser("~"), ".config")
    path = os.path.join(root, "WorldWithoutBorders3D", "window")
    os.makedirs(path, exist_ok=True)
    return path


def fallback_window():
    """Default browser + a small window that keeps the game server running."""
    webbrowser.open(URL)
    try:
        import tkinter as tk
        root = tk.Tk()
        root.title(TITLE)
        root.geometry("380x140")
        tk.Label(root, text="World Without Borders 3D is running\nin your web browser.", font=("Segoe UI", 12)).pack(pady=14)
        tk.Button(root, text="Open the game again", command=lambda: webbrowser.open(URL)).pack()
        tk.Label(root, text="Close this window to quit.", fg="#666").pack(pady=6)
        root.mainloop()
    except Exception:
        input("Game running at " + URL + " - press Enter to quit.")


def main():
    if "--serve-only" in sys.argv:          # for testing
        start_server().serve_forever()
        return
    httpd = None if port_in_use() else start_server()
    browser = find_browser()
    if browser:
        proc = subprocess.Popen([browser, f"--app={URL}", f"--user-data-dir={profile_dir()}", "--window-size=1366,820",
                                 "--no-first-run", "--no-default-browser-check", "--disable-features=Translate"])
        proc.wait()
    else:
        fallback_window()
    if httpd:
        httpd.shutdown()


if __name__ == "__main__":
    main()
