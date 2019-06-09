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
### 2、导出数据
- 导出数据到JSON、CSV、Excel：[源码](/example/02_Code/ch02-export.py)
### 3、清理异常值
- 在统计学上，中位数绝对偏差(MAD)是用来描述单变量样本在定量数据中可变性的一种标准。常用来度量统计分布，对异常值有抵抗能力。：[源码](/example/02_Code/ch02-clean-mad.py)<br>
![MAD](/example/02_Code/img/clean-mad.jpg)
