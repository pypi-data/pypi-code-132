import nest_asyncio
nest_asyncio.apply()
import asyncio
from PIL import Image
from io import BytesIO
import time
import json
import sys
import random
import threading
from playwright.async_api import async_playwright
from unencryptedsocket import SS, SC


def playwright_worker():
    async def main():
        global tabs
        async def handle_popup(page):
            await page.wait_for_load_state()
            add_page_handlers(page)
        def add_page_handlers(page):
            global tab_index
            global tabs_lock
            global tabs
            with tabs_lock:
                tabs[tab_index] = page
                tab_index += 1
            page.on("popup", handle_popup)
        async with async_playwright() as pw:
            driver = await pw.webkit.launch(
                timeout=5000,
                headless= True,
            )
            context = await driver.new_context(
                viewport={"width": 1920, "height": 1200},
                ignore_https_errors=True,
                bypass_csp=True,
            )
            page = await context.new_page()
            add_page_handlers(page)
            # page.goto("https://colab.research.google.com")
            await page.goto("https://google.com")
            await page.screenshot(type="jpeg", quality=100, path="tmp.jpg")
            while True:
                try:
                    for _ in tbc_tabs:
                        tab = tabs.pop(_)
                        await tab.close()
                    tbc_tabs.clear()
                    for k in list(tabs.keys()):
                        v = tabs[k]
                        if v.is_closed():
                            tabs.pop(k)
                    if ctab in tabs:
                        page = tabs[ctab]
                    else:
                        if tabs:
                            page = next(iter(tabs.values()))
                        else:
                            page = await context.new_page()
                            await page.set_viewport_size({"width": 1920, "height": 1200})
                            add_page_handlers(page)
                            await page.goto("https://duckduckgo.com")
                    t = next(iter(jobs.keys()))
                    v = jobs.pop(t)
                    args = v[1:]
                    v = v[0]
                    try:
                        if v == "screenshot":
                            img = await page.screenshot(type="jpeg", quality=100)
                            open("tmp.jpg", "wb").write(img)
                            img = Image.open(BytesIO(img))
                            img = img.convert("RGB")
                            img = img.resize(tuple(map(lambda x: int(x*0.75), img.size)), resample=Image.Resampling.LANCZOS)
                            im = BytesIO()
                            img.save(im, format="JPEG", quality=66, subsampling="4:2:0", optimize=True, progressive=True)
                            result = im.getvalue()
                        elif v == "mouse":
                            x,y,w,h,d,b = args
                            width = page.viewport_size["width"]
                            height = page.viewport_size["height"]
                            x = width*x/w
                            y = height*y/h
                            await page.mouse.move(x, y)
                            if d == 1:
                                await page.mouse.down(button="left" if b == 1 else "right")
                            elif d == -1:
                                await page.mouse.up(button="left" if b == 1 else "right")
                            result = "ok"
                        elif v == "wheel":
                            d, = args
                            await page.evaluate("window.scrollTo((document.body.scrollLeft||window.scrollX), (document.body.scrollTop||window.scrollY){}100);".format(
                                "+" if d else "-"
                            ))
                            result = "ok"
                        elif v == "keyboard":
                            k,d = args
                            if d == 1:
                                await page.keyboard.down(k)
                            else:
                                await page.keyboard.up(k)
                            result = "ok"
                        else:
                            raise
                    except:
                        import traceback
                        result = traceback.format_exc()
                        traceback.print_exc()
                    job_results[t] = result
                except StopIteration:
                    time.sleep(1/1000)
                except:
                    import traceback
                    traceback.print_exc()
                    time.sleep(1/1000)
            await driver.close()
    asyncio.run(main())


jobs = dict()
job_results = dict()
tab_index = 0
tabs = {}
tabs_lock = threading.Lock()
ctab = 0
tbc_tabs = []


def close_tab(id):
    tbc_tabs.append(id)


def set_tab(id):
    global ctab
    ctab = id


def get_tabs():
    return [[k, v.url] for k, v in tabs.items()]


def add_job(t, v):
    global jobs
    jobs[t] = v


def get_job_result(t):
    try:
        return job_results.pop(t)
    except:
        return KeyError()


sc_port = '<sc_port>'
ss = SS(host="127.0.0.1", port=sc_port, silent=True, functions=dict(
    close_tab=close_tab,
    set_tab=set_tab,
    get_tabs=get_tabs,
    get_job_result=get_job_result,
    add_job=add_job,
))
p = threading.Thread(target=lambda: ss.start())
p.daemon = True
p.start()
playwright_worker()


