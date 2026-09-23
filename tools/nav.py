import sys, time, json
sys.path.insert(0,'tools')
import cdp, chrome
URL = sys.argv[1]; W = int(sys.argv[2])
port = chrome.free_port(9600)
proc, profile = chrome.start(port=port, width=W, height=900)
try:
    ws = cdp.connect(port); ws.cmd("Page.enable"); ws.cmd("Runtime.enable")
    ws.cmd("Emulation.setDeviceMetricsOverride", {"width":W,"height":900,"deviceScaleFactor":1,"mobile":W<810})
    ws.cmd("Page.navigate", {"url": URL}); time.sleep(7)
    cdp.evaluate(ws, "scrollTo(0,1200)"); time.sleep(1.5); cdp.evaluate(ws, "scrollTo(0,0)"); time.sleep(1)
    print(json.dumps(cdp.evaluate(ws, open("tools/probe_nav.js").read(), timeout=60), indent=1))
finally:
    chrome.stop(proc, profile)
