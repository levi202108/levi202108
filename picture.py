# import pandas as pd
# from pandas.io.formats.style_render import Subset
# df=pd.read_excel(r"E:\ceshi\levi202108\data.xlsx",'Sheet1')
# print(df.head(13))
# print(df.describe())
# print(df.info())
#生成pandas报告
# from pandas_profiling import ProfileReport
# prof=ProfileReport(df)
# prof.to_file(output_file='report_01.html')

from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family']=['sans-serif']
plt.rcParams['font.sans-serif']=['SimHei'] #中文
df=pd.read_excel(r"E:\ceshi\levi202108\data.xlsx",'Sheet1')
#折线图
# plt.title('人工智能的发展趋势')
# plt.xlabel('date',fontsize=15)
# plt.ylabel('数量',fontsize=15)
# # plt.plot(df['date'],df['data_science'],color='green',label='data_science')
# # plt.plot(df['date'],df['machine_learning'],color='red',label='machine_learning')
# # plt.plot(df['date'],df['deep_learning'],color='grey',label='deep_learing')
# # plt.plot(df['date'],df['categorical'],color='yellow',label='categorical')
# # plt.grid(True)
# # plt.legend(fontsize=10,loc='upper right',frameon=False)# loc:best,upper right,upper left,lower right, right,center left, center right,lower center,upper center,center
# # plt.show()
#散点图
# plt.title('data_science 与 machine_learning 的关系')
# plt.xlabel('data_science')
# plt.ylabel('machine_learning')
# plt.scatter(df['data_science'],df['machine_learning'],color='grey',edgecolor='none',linewidths=5)
# plt.show()
#柱状图
# plt.title('date 与 machine_learning 的关系')
# plt.xlabel('date')
# plt.ylabel('machine_learning')
# plt.bar(x=df['date'],height=df['machine_learning'],color='red',width=10)
# plt.show()
#直方图
# plt.title('deep_learning的分布')
# plt.xlabel('deep_learning')
# plt.ylabel('数量')
# plt.hist(x=df['deep_learning'], bins=8,color='pink')
# plt.show()
#直方图与正太分布图
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set()
# sns.distplot(df['deep_learning'],bins=8,color='red')
# sns.kdeplot(df['deep_learning'],color='green')
# plt.show()
#热图
# import seaborn as sns
# import  matplotlib.pyplot as plt
# plt.title('热图')
# sns.set()
# sns.heatmap(df.corr(),annot=True,square=True, xticklabels="auto",center=True)
# plt.show()
#配对图
# import matplotlib.pyplot as plt
# import seaborn as sns
# plt.title('配对图')
# sns.pairplot(df)
# plt.show()
#成对图
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.pairplot(df,hue='categorical')
# plt.show()
#联合图
# import matplotlib.pyplot as plt
# import seaborn as sns
# plt.title('联合图')
# sns.jointplot(x='deep_learning', y='machine_learning', data=df)
# plt.show()
#小提琴图
# import matplotlib.pyplot as plt
# import seaborn as sns
# plt.title('小提琴图')
# sns.catplot(y="data_science",x='categorical',kind='violin',data=df,color='red')
# plt.show()

