import threading
from playsound import playsound
import time

def _play_audio():

    for key in ["1","2","3"]:
        filename = "audio/"+ key +".m4a"
        playsound(filename)
        print(filename+"播放完毕")

audio_thread = threading.Thread(target=_play_audio)
audio_thread.start()

print("计时开始...")
time.sleep(5)  # 暂停5秒
print("5秒后继续执行...")
