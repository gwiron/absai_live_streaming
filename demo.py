
# 文字识别
# from PIL import Image
# import pytesseract

# # 设置tesseract的路径（如果你没有将其添加到PATH环境变量中）
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows路径示例
# # 在Linux或Mac上通常不需要这一步，因为tesseract已经被添加到了PATH中

# # 打开图片文件
# img = Image.open('111.png')

# # 使用pytesseract进行OCR识别
# text = pytesseract.image_to_string(img, lang='chi_sim')

# # 打印识别的文本
# print(text)


# # 截图、保存、识别
# from PIL import Image
# import pytesseract
# import mss
# import mss.tools

# # 截取整个屏幕

# with mss.mss() as sct:
#     # monitor = sct.monitors[1]  # 使用监视器编号，通常0是主显示器
#     monitor = {"top": 0, "left": 0, "width": 500, "height": 800}
#     print("开始截图")
#     screenshot = sct.grab(monitor)
#     img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
#     mss.tools.to_png(screenshot.rgb, screenshot.size, output="audio/screenshot.png")
#     print("截图完成")

# # 将图像转换为灰度图像，有时有助于提高识别率
# img = img.convert('L')

# # # 进行OCR识别
# print("开始OCR")
# text = pytesseract.image_to_string(img, lang='chi_sim')
# print("OCR完成")
# print("\n\n\n\n————————————准备打印文字——————————————\n\n\n\n")
# print(text)

# from data.audios import audios

# print(audios)


# 播放音频

import threading
from playsound import playsound
import time

def _play_audio():

    for key in ["1","2","3"]:
        filename = "audio/"+ key +".m4a"
        playsound(filename)
        print(filename+"播放完毕")

# audio_thread = threading.Thread(target=_play_audio)
# audio_thread.start()
_play_audio()
print("计时开始...")
time.sleep(5)  # 暂停5秒
print("5秒后继续执行...")