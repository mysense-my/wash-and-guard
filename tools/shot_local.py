import sys, time, base64, json
sys.path.insert(0,'tools')
import cdp, chrome
URL="http://127.0.0.1:9788/index.html"
W=int(sys.argv[1]); OUT=sys.argv[2]
port=chrome.free_port(9400)
proc,profile=chrome.start(port=port,width=W,height=900)
try:
    ws=cdp.connect(port); ws.cmd("Page.enable"); ws.cmd("Runtime.enable")
    ws.cmd("Emulation.setDeviceMetricsOverride",{"width":W,"height":900,"deviceScaleFactor":1,"mobile":W<810})
    ws.cmd("Page.navigate",{"url":URL}); time.sleep(8)
    # scroll through so every reveal has fired and lazy images load
    h=cdp.evaluate(ws,"document.body.scrollHeight")
    y=0
    while y < h:
        cdp.evaluate(ws,f"scrollTo(0,{y})"); time.sleep(0.5); y+=700
    cdp.evaluate(ws,"scrollTo(0,0)"); time.sleep(1.5)
    h=cdp.evaluate(ws,"document.body.scrollHeight")
    time.sleep(2.0)
    r=ws.cmd("Page.captureScreenshot",{"format":"jpeg","quality":72,"captureBeyondViewport":True},timeout=180)
    open(OUT,"wb").write(base64.b64decode(r["data"]))
    print(OUT,"height",h)
finally:
    chrome.stop(proc,profile)
