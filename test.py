import matplotlib.pyplot as plt

x=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(x,squares,linewidth=5)
plt.title('数字',fontsize=18,fontweight='bold')
plt.xlabel('datas',fontsize=18,fontweight='bold')
plt.ylabel('Squares',fontsize=18,fontweight='bold')
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.show()




