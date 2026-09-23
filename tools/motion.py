import sys, time, json
sys.path.insert(0, 'tools')
import cdp, chrome

URL = "https://axiondetailing.framer.website/"
W = int(sys.argv[1]) if len(sys.argv) > 1 else 1440
H = int(sys.argv[2]) if len(sys.argv) > 2 else 900

port = chrome.free_port(9333)
proc, profile = chrome.start(port=port, width=W, height=H)
try:
    ws = cdp.connect(port)
    ws.cmd("Page.enable"); ws.cmd("Runtime.enable")
    ws.cmd("Emulation.setDeviceMetricsOverride",
           {"width": W, "height": H, "deviceScaleFactor": 1, "mobile": W < 810})
    ws.cmd("Page.navigate", {"url": URL})
    time.sleep(8)
    js = open('tools/probe_motion.js').read()
    print(json.dumps(cdp.evaluate(ws, js, timeout=180), indent=1))
finally:
    chrome.stop(proc, profile)
