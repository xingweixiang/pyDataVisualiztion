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