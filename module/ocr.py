# 截图、保存、识别
from PIL import Image
import pytesseract
import mss
import mss.tools
import random
import data.audios

# 传入某个识别的屏幕范围，并进行OCR输出
def strTextOcr():
    with mss.mss() as sct:
        # monitor = sct.monitors[1]  # 使用监视器编号，通常0是主显示器
        monitor = {"top": 0, "left": 0, "width": 500, "height": 800}
        print("开始截图→→")
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        # 保存为图像 调试使用 看识别准确率
        # mss.tools.to_png(screenshot.rgb, screenshot.size, output="audio/screenshot.png")
        print("截图完成")

    # 将图像转换为灰度图像，有时有助于提高识别率
    img = img.convert('L')

    # # 进行OCR识别
    print("开始OCR")
    text = pytesseract.image_to_string(img, lang='chi_sim')
    print("OCR完成")
    # print("\n\n\n\n————————————准备打印文字——————————————\n\n\n\n")
    # print(text)
    return text

# 根据弹幕评论选择应该播放的音频文件，返回文件目录
def selectReplyAudio(text):
    QA = data.audios.audios['QA']
    if text not in QA:
        return False
    item = random.choice(QA[text])
    return item