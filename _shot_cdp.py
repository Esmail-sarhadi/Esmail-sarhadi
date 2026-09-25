"""Render index.html / index_fa.html at specific scroll positions via Chrome DevTools Protocol.

Launches Chrome with --remote-debugging-port=9222, connects via WebSocket,
navigates, scrolls, screenshots. Reliable — no --virtual-time-budget shenanigans.
"""
import json
import os
import subprocess
import time
import base64
import socket
import urllib.request

from simple_websocket import Client

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = r"C:\Users\esmail\WorkBuddy AI\2026-09-25-04-39-46\github-profile"
PREV = os.path.join(BASE, "_preview2")
os.makedirs(PREV, exist_ok=True)

PAGES = [("en", "index.html"), ("fa", "index_fa.html")]
# At viewport 1280x1200, after we force hero to 1200px:
#   hero: 1200
#   profile block: ~700-900 (terminal svg is ~600px)
#   boot block: ~700
#   wall-wrap: 4560
#   stack section: ~700
#   timeline section: ~1200
#   lab/bench: ~1000
#   network section: ~1000
#   code-window: ~800
#   contact: ~700
#   footer: ~200
SCROLL_Y = [0, 1300, 2200, 3200, 4800, 6200, 7600, 9000, 10500, 12000]
LABELS = ["01-hero", "02-profile", "03-boot", "04-wall-top", "05-wall-mid",
          "06-wall-end", "07-stack", "08-timeline", "09-lab-net", "10-contact"]

DEBUG_PORT = 9222


def wait_for_port(port, timeout=20):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), 1):
                return True
        except OSError:
            time.sleep(0.2)
    return False


def cdp_ws():
    # get the first tab's webSocketDebuggerUrl
    with urllib.request.urlopen(f"http://127.0.0.1:{DEBUG_PORT}/json", timeout=10) as r:
        tabs = json.loads(r.read())
    page_tab = next((t for t in tabs if t.get("type") == "page"), tabs[0])
    return Client(page_tab["webSocketDebuggerUrl"])


class CDP:
    def __init__(self):
        self.ws = cdp_ws()
        self.id = 0

    def call(self, method, params=None):
        self.id += 1
        msg = {"id": self.id, "method": method, "params": params or {}}
        self.ws.send(json.dumps(msg))
        while True:
            resp = json.loads(self.ws.receive())
            if resp.get("id") == self.id:
                return resp.get("result", {})

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass


def render_page(tag, page):
    """Open page in Chrome, screenshot at multiple scroll positions."""
    src_url = "file:///" + os.path.join(BASE, page).replace(os.sep, "/").replace(" ", "%20")

    for y, lbl in zip(SCROLL_Y, LABELS):
        cdp = CDP()
        try:
            # enable Page + Runtime
            cdp.call("Page.enable")
            cdp.call("Runtime.enable")
            cdp.call("Network.enable")
            # Navigate
            cdp.call("Page.navigate", {"url": src_url})
            # Wait for load
            time.sleep(2.0)
            # Force hero to fixed 1200px so wall-wrap renders predictably
            cdp.call("Runtime.evaluate", {
                "expression": """
                  (() => {
                    const s = document.createElement('style');
                    s.textContent = 'section.hero{min-height:1200px!important;height:1200px!important;}';
                    document.head.appendChild(s);
                  })();
                """
            })
            time.sleep(0.5)
            # Scroll to target
            cdp.call("Runtime.evaluate", {
                "expression": f"window.scrollTo(0, {y});",
                "awaitPromise": False
            })
            time.sleep(1.0)
            # Re-scroll after layout settles (some browsers ignore first scrollTo before layout)
            cdp.call("Runtime.evaluate", {
                "expression": f"window.scrollTo(0, {y}); window.scrollY;",
                "returnByValue": True
            })
            time.sleep(0.6)
            # Screenshot
            res = cdp.call("Page.captureScreenshot", {"format": "png"})
            data = base64.b64decode(res["data"])
            out = os.path.join(PREV, f"{tag}_{lbl}.png")
            with open(out, "wb") as f:
                f.write(data)
            print(f"{tag} {lbl} (y={y}): {out} ({len(data)} bytes)")
        finally:
            cdp.close()


def main():
    user_data = os.path.join(PREV, ".cdp")
    os.makedirs(user_data, exist_ok=True)
    proc = subprocess.Popen([
        CHROME,
        "--headless=new", "--no-sandbox", "--disable-gpu",
        "--hide-scrollbars",
        f"--remote-debugging-port={DEBUG_PORT}",
        f"--user-data-dir={user_data}",
        "--window-size=1280,1200",
        "about:blank"
    ])
    try:
        if not wait_for_port(DEBUG_PORT):
            print("Chrome didn't open debug port")
            return
        time.sleep(0.5)
        for tag, page in PAGES:
            render_page(tag, page)
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


if __name__ == "__main__":
    main()