import json, socket, base64, os, struct, time, urllib.request

class WS:
    def __init__(self, url):
        rest = url[5:]; hostport, path = rest.split("/", 1); path = "/" + path
        host, port = hostport.split(":")
        self.sock = socket.create_connection((host, int(port)))
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((f"GET {path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\n"
            f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        buf = b""
        while b"\r\n\r\n" not in buf: buf += self.sock.recv(4096)
        self.buf = buf.split(b"\r\n\r\n", 1)[1]; self._id = 0
    def _recv(self, n):
        while len(self.buf) < n:
            d = self.sock.recv(1 << 20)
            if not d: raise EOFError
            self.buf += d
        out, self.buf = self.buf[:n], self.buf[n:]; return out
    def send(self, data):
        payload = data.encode(); hdr = bytearray([0x81]); n = len(payload); mask = os.urandom(4)
        if n < 126: hdr.append(0x80 | n)
        elif n < 65536: hdr.append(0x80 | 126); hdr += struct.pack(">H", n)
        else: hdr.append(0x80 | 127); hdr += struct.pack(">Q", n)
        hdr += mask; hdr += bytes(b ^ mask[i % 4] for i, b in enumerate(payload)); self.sock.sendall(bytes(hdr))
    def recv(self):
        while True:
            b1, b2 = self._recv(2); op = b1 & 0x0F; ln = b2 & 0x7F
            if ln == 126: ln = struct.unpack(">H", self._recv(2))[0]
            elif ln == 127: ln = struct.unpack(">Q", self._recv(8))[0]
            data = self._recv(ln)
            if op == 1: return data.decode()
            if op == 8: raise EOFError("closed")
    def cmd(self, method, params=None, timeout=120):
        self._id += 1; i = self._id
        self.send(json.dumps({"id": i, "method": method, "params": params or {}}))
        self.sock.settimeout(timeout)
        while True:
            msg = json.loads(self.recv())
            if msg.get("id") == i:
                if "error" in msg: raise RuntimeError(msg["error"])
                return msg.get("result", {})

def connect(port=9222):
    for _ in range(80):
        try:
            tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json"))
            pages = [t for t in tabs if t["type"] == "page"]
            if pages: return WS(pages[0]["webSocketDebuggerUrl"])
        except Exception: pass
        time.sleep(0.5)
    raise RuntimeError("no chrome")

def evaluate(ws, expr, timeout=120):
    r = ws.cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True, "awaitPromise": True}, timeout)
    if "exceptionDetails" in r: raise RuntimeError(json.dumps(r["exceptionDetails"])[:1500])
    return r["result"].get("value")
