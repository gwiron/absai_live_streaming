import threading
from playsound import playsound
import time
import module.ocr as ocr
import data.audios
import random

queueReplyAudios = []
queueReplyAudiosDelay30s = []
queueRandomAudios = []

# 音频播放线程
def _playAudio():
    while(1):
        if len(queueRandomAudios) == 0:
            randomAudios() # 重新随机循环话术列表

        # 如果有QA优先回答问题
        if len(queueReplyAudios) != 0:
            filename = queueReplyAudios.pop(0)
        else:
            filename = queueRandomAudios.pop(0)
        
        # print("播放音频："+filename)
        # time.sleep(3)

        print("播放音频："+filename)
        playsound(filename)


# 轮询检测评论文案，并调用选择回复音频的函数
def pollingCommentDetection():
    QA = data.audios.audios['QA']
    while(1):
        # 获取屏幕上的文字
        ocrStr = ocr.strTextOcr()
        # print(ocrStr)

        # 查询是否匹配QA列表
        retOcr = [key for key in QA.keys() if key in ocrStr]
        print(retOcr)

        for key in retOcr:

            # 刚回答过的问题，30s后才可以继续回答 & 列表是否有语音
            if key not in queueReplyAudiosDelay30s and len(QA[key]) > 0:
                t = ocr.selectReplyAudio(key)
                t = 'audio/QA/'+ key +'/'+t
                queueReplyAudios.append(t)
                sleepCommentDetection(key)
                # print(key)
        
        time.sleep(3)  # 一秒检测一次

# 刚回答过的问题 30s后才可以继续回答
def _sleepCommentDetection():
    time.sleep(30)
    t = queueReplyAudiosDelay30s.pop(0)
    print('关键词【'+ t +'】上次回答超过30s → 解锁')
def sleepCommentDetection(filename):
    queueReplyAudiosDelay30s.append(filename)
    delay = threading.Thread(target=_sleepCommentDetection)
    delay.start()
    
        
# temp = ['audio/circulate/1.m4a','audio/circulate/2.m4a','audio/circulate/3.m4a','audio/circulate/4.m4a','audio/circulate/5.m4a']
# 新一轮循环开始初始化循环播放堆栈
def randomAudios():
    audios = data.audios.audios
    # 随机选择一个开场白，加入播放堆栈
    item = random.choice(audios['prologue'])
    filename = 'audio/prologue/'+item
    queueRandomAudios.append(filename)

    # 循环话术进行随机排列，加入播放堆栈
    adsCopy = audios['circulate'][:]
    random.shuffle(adsCopy)
    for i in adsCopy:
        # print('文件目录：'+i)
        queueRandomAudios.append('audio/circulate/'+i)
    # print(queueRandomAudios)
    # print('\n\n\n\n\n\n\n')
    

def start():

    randomAudios() # 初始化循环话术播放

    # 开启新线程，与屏幕识别同时进行不干扰
    audio_thread = threading.Thread(target=_playAudio)
    audio_thread.start()

    pollingCommentDetection() # 开始屏幕检测轮询

    print('——————程序已启动——————')



if __name__ == '__main__': 
    start()

