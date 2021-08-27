import matplotlib.pyplot as plt
import numpy as np
from  wordcloud import WordCloud
import wordcloud
import jieba 
from PIL import Image
from wordcloud.color_from_image import ImageColorGenerator
from wordcloud.wordcloud import FONT_PATH
words='专注能提升一个人的幸福感,提升一个人的能力,这个世界上许多伟大的事情,都源于专注'
word_list=jieba.cut(words)
word_list=" ".join(word_list)
mask=np.array(Image.open(r'E:\ceshi\levi202108\run1.png'))
cd=wordcloud.WordCloud(contour_color='steelblue',font_path='E:\ceshi\levi202108\FZSTK.TTF',background_color='white',mask=mask,width=1000, height=800,random_state=1,mode='RGBA',scale=30.5,max_font_size=255,min_font_size=40)
cd=cd.generate(word_list)
plt.imshow(cd)
plt.axis('off')
plt.show()
