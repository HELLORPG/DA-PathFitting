import matplotlib.pyplot as plt

# plt.scatter([1, 2, 3], [2, 3, 4], alpha=0.6)  # 绘制散点图，透明度为0.6（这样颜色浅一点，比较好看）
# plt.show()


def GetScatterPlot(x: list, y: list, annotate_point_num = 0):
    """通过整个方法返回散点图"""
    plt.axis('equal')   # 保证XY轴的单位长度是一致的
    plt.scatter(x, y, alpha=0.6, s=0.4)
    plt.title("Raw Data")
    """x y为点的坐标序列 alpha为颜色的深浅 s为点的大小"""

    if annotate_point_num == 1:
        for i in range(0, len(x)):
            plt.annotate(i, (x[i], y[i]))
    plt.show()
