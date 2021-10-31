import os

eng = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?.()“”:,+/*'-%~＆♪"
jp_eng = "０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ！？．（）“”：，＋／＊’―％～＆♪"
save_path = './converted'
dir = os.path.join("converted")

if not os.path.exists(dir):
    os.mkdir(dir)




def convert(filename):
    switch = True
    completeName = os.path.join(save_path, filename)
    openFile = open(filename, 'r+', encoding='utf-8')
    data = openFile.read()
    jp_str = ""
    for en_char in data:
        if en_char == "[":
            switch = False
            jp_char = en_char
        elif en_char == "]":
            switch = True
            jp_char = en_char
        else:
            if not switch:
                jp_char = en_char
            else:
                try:
                    index = eng.index(en_char)
                    jp_char = jp_eng[index]
                except ValueError:
                    jp_char = en_char

        jp_str += jp_char
    openFile.close()
    createFile = open(completeName, 'w', encoding = "utf-8")
    createFile.write(jp_str)
    createFile.close()

for filename in os.listdir():
        if filename.endswith('.txt'):
            convert(filename)