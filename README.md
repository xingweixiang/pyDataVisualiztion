python数据可视化
=========
## 运行环境
     python 3.7.*
## 目录
* [python数据可视化](#python数据可视化)
	* [一、准备工作](#一准备工作)
		* [1、安装](#1安装)
		* [2、设置matplotlib参数](#2设置matplotlib参数)
	* [二、数据处理](#二数据处理)
		* [1、导入数据](#1导入数据)
		* [2、导出数据](#2导出数据)
		* [3、清理异常值](#3清理异常值)
		* [4、数据噪声平滑处理](#4数据噪声平滑处理)
	* [三、绘制并定制化图表](#三绘制并定制化图表)
		* [1、常用图](#1常用图)
		* [2、更多图表和定制化](#2更多图表和定制化)
    * [四、3D可视化图表](#四3D可视化图表)
        * [1、创建3D图表](#1创建3D图表)
### 一、准备工作
### 1、安装
- 安装matplotlib、Numpy、Scipy、图像库(PIL)等。
### 2、设置matplotlib参数
- 配置模板以方便各项目共享：有三种方式:当前工作目录，用户级和安装级配置文件
### 二、数据处理
### 1、导入数据
- 从csv文件导入数据：[源码](/example/02_Code/ch02-csvread.py)
- 从excel文件导入数据：[源码](/example/02_Code/ch02-xlsxread.py)
- 从定宽数据文件导入数据：[源码](/example/02_Code/ch02-fixedwidth-read.py)
- 从制表符分割的文件中导入数据：[源码](/example/02_Code/ch02-tabread.py)
- "脏数据"清理：[源码](/example/02_Code/ch02-tabread-split.py)
- 从JSON数据源导入数据：[源码](/example/02_Code/ch02-jsonread-github.py)
- 从数据库导入数据：[源码](/example/02_Code/ch02-sqlite-import.py)
- 读取大块数据文件：[源码](/example/02_Code/ch02-chunk-read.py)
- 读取流数据源：[源码](/example/02_Code/ch02-stream-read-1.py)
- 读取图像数据：[源码](/example/02_Code/ch02-imgshow.py)
### 2、导出数据
- 导出数据到JSON、CSV、Excel：[源码](/example/02_Code/ch02-export.py)
### 3、清理异常值
- 在统计学上，中位数绝对偏差(MAD)是用来描述单变量样本在定量数据中可变性的一种标准。常用来度量统计分布，对异常值有抵抗能力。[源码](/example/02_Code/ch02-clean-mad.py)<br>
![MAD](/example/02_Code/img/clean-mad.jpg)<br>
第一幅图除了一个最大的异常值之外什么都没有。<br>
第二幅图中剔除掉了异常值，显示了多样化的数据。
- 识别异常值的方法还有创建散点图，能轻易看到偏离簇中心的值。也可以绘制一个箱线图，就能显示出中值、上四分位数和下四分位数，以及远离箱体的异常值点。[源码](/example/02_Code/ch02-clean-boxplot.py)<br>
![箱线图](/example/02_Code/img/clean-boxplot.jpg)<br>
第二幅图以散点图的形式显示了相似的集合。数据的X轴都是25，看起来不直观<br>
第三幅图中，在X轴上生成的值分布在0-50的范围内，更能看出值与值间不同，也能够在Y轴上看出哪些值是异常值。
### 4、数据噪声平滑处理
- 对样本求平均值。[源码](/example/02_Code/ch02-noise-moving-average.py)<br>
![样本平均值](/example/02_Code/img/moving-average.jpg)
- ScpPy基于信号（数据原点）窗口的卷积（函数的总和）。[源码](/example/02_Code/ch02-noise-scipy-smooth-1d.py)<br>
![ScpPy](/example/02_Code/img/scipy-smooth.jpg)
- 中值滤波：用相邻信号项的中值替换当前项。[源码](/example/02_Code/ch02-noise-median-filter.py)<br>
![中值滤波](/example/02_Code/img/median-filter.jpg)
### 三、绘制并定制化图表
### 1、常用图
- 线、柱状图、水平柱状图、叠加柱状图、箱线图、散点图
```
from matplotlib.pyplot import *
x = [1,2,3,4]
y = [5,4,3,2]
figure()#建新图表
subplot(231)#把图表分割成2X3的网格,subplot(2,3,1)，第一个参数是行数，第二个是列数，第三个表示图形的标号
plot(x, y)#线
subplot(232)
bar(x, y)#柱状图
subplot(233)
barh(x, y)#水平柱状图
#叠加柱状图
subplot(234)
bar(x, y)
y1 = [7,8,5,3]
bar(x, y1, bottom=y, color = 'r')
subplot(235)
boxplot(x)#箱线图
subplot(236)
scatter(x,y)#散点图
savefig('./img/plotting.jpg')#保存成图片
show()
```
![常用图](/example/03_Code/img/plotting.jpg)
- 直方图
```
dataset = [113, 115, 119, 121, 124, 
           124, 125, 126, 126, 126,
           127, 127, 128, 129, 130,
           130, 131, 132, 133, 136]
subplot(121)
boxplot(dataset, vert=False)#箱线图
subplot(122)
hist(dataset)#直方图
show()
```
![直方图](/example/03_Code/img/historgram.jpg)
- 正弦、余弦图
```
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.cos(x)
y1 = np.sin(x)
pl.plot(x, y)
pl.plot(x, y1)
# 图表名称
pl.title("Functions $\sin$ and $\cos$")
# x,y轴坐标范围
pl.xlim(-3, 3)
pl.ylim(-1, 1)
# 坐标上刻度
pl.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
pl.yticks([-1, 0, 1],
       [r'$-1$', r'$0$', r'$+1$'])
# 网格
pl.grid()
show()
```
![正弦、余弦图](/example/03_Code/img/sin-cos.jpg)
- 饼图。[源码](/example/03_Code/ch03-rec04-pie.py)<br>
![饼图](/example/03_Code/img/pie.jpg)
- 设置图表的线型、属性和格式化字符串。[源码](/example/03_Code/ch03-rec05.py)<br>
![设置图表的线型、属性和格式化字符串](/example/03_Code/img/rec05.jpg)
- 设置刻度、时间刻度标签、网格。[源码](/example/03_Code/ch03-rec06.py)<br>
![设置刻度、时间刻度标签、网格](/example/03_Code/img/rec06.jpg)
- 添加图例和注释。[源码](/example/03_Code/ch03-rec07.py)<br>
![添加图例和注释](/example/03_Code/img/rec07.jpg)
- 设置坐标轴。[源码](/example/03_Code/ch03-rec08.py)<br>
![设置坐标轴](/example/03_Code/img/rec08.jpg)
- 误差条形图。[源码](/example/03_Code/ch03-rec09.py)<br>
![误差条形图](/example/03_Code/img/rec09.jpg)
- 带填充区域的图表。[源码](/example/03_Code/ch03-rec10.py)<br>
![带填充区域的图表](/example/03_Code/img/rec10.jpg)
### 2、更多图表和定制化
- 向图表添加数据表。[源码](/example/03_Code/ch03-rec11.py)<br>
![向图表添加数据表](/example/03_Code/img/rec11.jpg)
- 向图表添加数据表。[源码](/example/03_Code/ch03-rec12.py)<br>
![向图表添加数据表](/example/03_Code/img/rec12.jpg)
- 使用subplots。[源码](/example/03_Code/ch03-rec13.py)<br>
![使用subplots](/example/03_Code/img/rec13.jpg)
- 创建等高线图。[源码](/example/03_Code/ch03-rec14.py)<br>
![创建等高线图](/example/03_Code/img/rec14.jpg)
- 填充图表底层区域。[源码](/example/03_Code/ch03-rec15.py)<br>
![填充图表底层区域](/example/03_Code/img/rec15.jpg)
### 四、3D可视化图表
### 1、创建3D图表
- 3D柱状图。[源码](/example/04_Code/ch04-rec01.py)<br>
![3D柱状图](/example/04_Code/img/rec01.jpg)
- 曲面图。[源码](/example/04_Code/ch04-rec02.py)<br>
![曲面图](/example/04_Code/img/rec02.jpg)
- 3D直方图。[源码](/example/04_Code/ch04-rec03.py)<br>
![3D直方图](/example/04_Code/img/rec03.jpg)
- 三翼面图。[源码](/example/04_Code/ch04-rec04.py)<br>
![三翼面图](/example/04_Code/img/rec04.jpg)