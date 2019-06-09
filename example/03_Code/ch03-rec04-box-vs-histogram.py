from pylab import *
dataset = [113, 115, 119, 121, 124, 
           124, 125, 126, 126, 126,
           127, 127, 128, 129, 130,
           130, 131, 132, 133, 136]
subplot(121)
boxplot(dataset, vert=False)#箱线图
subplot(122)
hist(dataset)#直方图
savefig('./img/historgram.jpg')#保存成图片
show()
