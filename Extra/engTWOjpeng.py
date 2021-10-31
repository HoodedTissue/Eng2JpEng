# Version to convert [] and everything side them into jp eng
import os

eng = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?.()“”:,+/*'-%~＆♪"
jp_eng = "０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ！？．（）“”：，＋／＊’―％～＆♪"
save_path = './converted'
dir = os.path.join("converted")

if not os.path.exists(dir):
    os.mkdir(dir)


def convert(filename):
    #opens file + converts text
    completeName = os.path.join(save_path, filename)
    openFile = open(filename, 'r+', encoding='utf-8')
    data = openFile.read()
    converted = data.maketrans(eng, jp_eng)
    openFile.close()
    #creates new file + writes converted text
    createFile = open(completeName, 'w', encoding = "utf-8")
    createFile.write(data.translate(converted))
    createFile.close()

for filename in os.listdir():
        if filename.endswith('.txt'):
            convert(filename)