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
