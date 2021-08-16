import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
import wordcloud
import numpy as np
from PIL import Image
words='港话 现世 阔 切饭 照 搭将 更着 哈掉扯 大大 奶奶 噶气 不搭嘎 小鬼 阔法子 发狠'
wordlist=jieba.lcut(words)
wordlist=" ".join(wordlist)
# mask=np.array(Image.open(r'E:\ceshi\code\池州.jpg'))
wc=wordcloud.WordCloud(background_color='white',font_path=r'E:\ceshi\code\msyh.ttc',mode='RGB')
wc=wc.generate(wordlist)
plt.imshow(wc)
plt.axis('off')
plt.show()