<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head><body><article id="566ec3ca-586b-492c-ba22-d14742f2d8bb" class="page sans"><header><h1 class="page-title">Download_Auto_Calssification</h1></header><div class="page-body"><h1 id="fbf41188-e07b-41db-942e-a5552c157b56" class="">Application</h1><h2 id="a3b11936-7de6-4287-af2c-8d58eb133ea0" class="">Automatically move resources downloaded from the Internet
to D: devices (data devices) and classified following the file extension, and then save C: devices (system devices).</h2><hr id="839d0a09-943c-4689-a6ae-41d14c3f2eab"/><h1 id="d9cbf6a9-2e95-48b4-a6fc-0bb48240ebcf" class="">Step1. Coding Environment</h1><h3 id="9d753156-849e-4969-a795-4823dbdc0c06" class="">Python 3.8.5
Libs:</h3><ul id="8e01a93a-9e41-4074-a0b8-f362ac312093" class="bulleted-list"><li>os</li></ul><ul id="b9f37987-a492-4f16-81ee-b6096de37bea" class="bulleted-list"><li>time</li></ul><ul id="4e273d66-ae79-4526-9333-8fbf06e24b80" class="bulleted-list"><li>shutil</li></ul><ul id="205127f3-d7c5-4b91-9a24-43145f7dab39" class="bulleted-list"><li>watchdog</li></ul><hr id="cce46c53-55e3-47bb-910d-780ff1ba835b"/><h1 id="aded4726-d408-497d-a979-8844167e0f05" class="">Step 2. Write Code</h1><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="4b76721c-3054-4e25-b3e9-f35952e8e27b"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">import libs we need</div></figure><pre id="60355191-c187-4a89-b098-8b0ce11a4061" class="code"><code>
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import shutil
import time</code></pre><p id="aea53daf-19ed-48e5-9b1a-35f6d8ab3b0a" class="">
</p><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="c60ae1d0-a458-4544-a90f-c165688aee3a"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">create a list to save files extension we need to skip</div></figure><pre id="06bfe840-63ee-4b2f-b7bc-cad6094ca6ce" class="code"><code>skip = skip = [&#x27;crdownload&#x27;, &#x27;tmp&#x27;]</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="41644cba-6ad2-4c61-8abc-db2019361b7b"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">make a class. when downloading&#x27;s must to do</div></figure><pre id="164fa7f0-0b82-4807-9808-935e6cf8c643" class="code"><code>#to monitor the device
class Myhandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
						#get the file extension name
            file_type = filename.split(&#x27;.&#x27;)[-1].lower()
            time.sleep(1)
						#skip until the file name doesn&#x27;t in list &#x27;skip&#x27;
            if file_type not in skip:
                if file_type not in os.listdir(folder_destimation):
                    os.mkdir(folder_destimation + &quot;/&quot; + file_type + &quot;&quot;)
                src = folder_to_track + &quot;/&quot; + filename
                new_destinmation = folder_destimation + &quot;/&quot; + file_type + &quot;/&quot; + filename
                shutil.move(src, new_destinmation)</code></pre><pre id="c856a853-ed68-4722-b3b9-c0a291af020f" class="code"><code>folder_to_track = &#x27;C:/Users/smallwind/Downloads&#x27;
folder_destimation = &#x27;D:/Downloads&#x27;
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join</code></pre></div></article></body></html>
