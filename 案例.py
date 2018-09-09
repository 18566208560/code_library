import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


#读取待处理的文件内容
with open("file.txt","r",encoding="utf-8") as f:
    msg = f.read()

#读取停用词库
with open("files.txt","r",encoding="utf-8") as f:
    files = f.read()

#分词
seg_list = jieba.cut(msg, cut_all=False)

#去除停用词库
seg_list = [i for i in seg_list if i not in files]
# print(len(seg_list))

#进行统计、排序
list_num = sorted(list(map(lambda x:(x, seg_list.count(x)),set(seg_list))),key=lambda i:i[1],reverse=True)
print(list_num)

#拼接字符串
text = " ".join([i[0] for i in list_num])
print(text)


#创建词云蒙板
img = Image.open("timg.jpg").resize((720,405))
mask = np.array(img)

#词云设置
wc = WordCloud(font_path="c:/Windows/Fonts/simhei.ttf",
               width=800,
               height=600,
               max_font_size=50,
               min_font_size=10,
               background_color="rgba(0,0,0,0)",
               mask=mask,
               mode="RGBA"

               )

wc = wc.generate(text)   #返回<class 'wordcloud.wordcloud.WordCloud'> 可以直接转为np
print(np.array(wc))

#wordcloud保存图片
# wc_img.to_file(r".\bbb.png")

#wc转为Image
wc_img = Image.fromarray(np.array(wc))
wc_img.show()
wc_img.save("wc_img.png")


#将图片转为灰度，得到二维数组，再二值化，得到图片蒙板图片（只有0和255，0不显示，255显示）
#注：这里用到Image的paste,文档上用rgba的alpha通道可以做为蒙板，待以后再测试
#注：二值化得到（0和255）Image还可以有更简单的方法 ，待以后再查
wc_mask = np.array(wc_img.convert("L"))
a = (wc_mask > 0)
wc_mask[a] = 255
wc_mask = Image.fromarray(wc_mask)


#打开背景图
bg = Image.open("bg2.jpg")


#将词云图片粘贴在背景图上，(0,0,1376,843)为词云图片大小位置，mask为蒙板
bg.paste(wc_img,(200,100,920,505),mask=wc_mask)
bg.show()

#..........................
plt.figure("abc")

plt.imshow(wc_img)

plt.axis("off")

plt.show()