"""Launch and stop a headless Chrome with the DevTools protocol open.

Kept separate from cdp.py so the socket client stays dependency-free and
reusable. One Chrome per capture run; the profile is throwaway.
"""
import os, shutil, signal, subprocess, tempfile, time, urllib.request, json

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def start(port=9222, width=1440, height=900):
    if not os.path.exists(CHROME):
        raise SystemExit("Google Chrome not found at " + CHROME)
    profile = tempfile.mkdtemp(prefix="senseframe-chrome-")
    proc = subprocess.Popen([
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--mute-audio",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-background-timer-throttling",
        "--disable-renderer-backgrounding",
        "--force-device-scale-factor=1",
        f"--window-size={width},{height}",
        f"--remote-debugging-port={port}",
        f"--user-data-dir={profile}",
        "about:blank",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for _ in range(120):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=1).read()
            return proc, profile
        except Exception:
            time.sleep(0.25)
    stop(proc, profile)
    raise SystemExit("Chrome did not open a debugging port on %d" % port)


def stop(proc, profile):
    try:
        proc.send_signal(signal.SIGTERM)
        proc.wait(timeout=8)
    except Exception:
        try: proc.kill()
        except Exception: pass
    shutil.rmtree(profile, ignore_errors=True)


def free_port(start_port=9222):
    """Chrome left running from an earlier crashed run holds its port; step past it."""
    import socket as s
    for p in range(start_port, start_port + 40):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{p}/json/version", timeout=0.4).read()
            continue          # someone is already there
        except Exception:
            pass
        sock = s.socket()
        try:
            sock.bind(("127.0.0.1", p)); sock.close(); return p
        except OSError:
            sock.close()
    raise SystemExit("no free debugging port")
