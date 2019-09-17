import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero

a = int(input("请输入点的个数:"))
x = list(range(a))
y = []
for i in range(len(x)):
    b = float(input("请输入第%d个点的纵坐标值:" % (i+1)))
    y.append(b)

print("\n------------图的设置------------\n")
fig_width = float(input("请输入您想设置的长度（如5）:"))
fig_height = float(input("请输入您想设置的宽度（如5）:"))
figsize = fig_width, fig_height
figure, ax = plt.subplots(figsize=figsize)
font1 = {}
font1['family'] = input("请输入您想设置的字体(如Arial):")
font1['weight'] = 'normal'
font1['size'] = float(input("请输入您想设置的字体大小如(18):"))
print("******坐标轴设置******")
axis_choice = input("您是否想隐藏某个坐标轴(y/n):")
if 'y' == axis_choice:
    axis_set = input("请输入您想隐藏的坐标轴\n（左:l, 右:r, 上:t, 下:b，如隐藏“上右”，输入“tr”即可）:")
    if 'l' in axis_set:
        ax.spines['left'].set_color('none')
        plt.yticks([])
    if 'r' in axis_set:
        ax.spines['right'].set_color('none')
    if 't' in axis_set:
        ax.spines['top'].set_color('none')
    if 'b' in axis_set:
        ax.spines['bottom'].set_color('none')
        plt.xticks([])
    if 'b' not in axis_set:
        x_name = input("请输入您想设置的x轴名称:")
        plt.xlabel(x_name, font1)
        tick_x = input("是否关闭x轴刻度，同意输入y,不同意输入n:")
        if 'y' == tick_x:
            plt.xticks([])
    if 'l' not in axis_set:
        y_name = input("请输入您想设置的y轴名称:")
        plt.ylabel(y_name, font1)
        tick_y = input("是否关闭y轴刻度，同意输入y,不同意输入n:")
        if 'y' == tick_y:
            plt.yticks([])
# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=font1['size'])
labels = ax.get_xticklabels() + ax.get_yticklabels()
# print labels
[label.set_fontname('Times New Roman') for label in labels]

print("\n------------能量势垒中曲线的设置------------\n")
T = 2 * 1  # 将要画的正弦曲线的周期
pi = math.pi    # π
w = 2 * pi / T  # y = Asin(wx + phi) + y0中的w
curve_type = input("请输入您想设置的曲线的线条格式（颜色及线条样式，如r-.  b--等）:")
curve_width = float(input("请输入您想设置的曲线的线宽大小:"))
for j in range(len(x)-1):
    A = (y[j + 1] - y[j])/2  # 某段正弦曲线的振幅(不取绝对值，是为了让其调控函数增减)
    sx1 = x[j]     # 正弦曲线的起点
    sx2 = x[j+1]   # 正弦曲线的终点
    sx = np.linspace(sx1, sx2, 1000)  # 为了在两点之间绘制正弦曲线，所以需要插点
    phi = (- pi / 2) - w * sx1   # y = Asin(wx + phi) + y0中的phi
    y_dif = (y[j] + y[j+1]) / 2  # y = Asin(wx + phi) + y0中的y0，实际上有-0
    sy = A * np.sin(w * sx + phi) + y_dif  # 生成这条曲线上的纵坐标的点
    plt.plot(sx, sy, curve_type, curve_width)

print("\n------------能量势垒中的短横的设置------------\n")
len_shortline = float(input("请输入您想设置的短横的长度:"))
line_color = input("请输入您想设置的短横的颜色\n(r:红色 b:蓝色 g:绿色 c:青色 m:洋红 y:红色 k:黑色 w:白色)\n其他颜色可参考网址https://www.cnblogs.com/darkknightzh/p/6117528.html:")
line_width = float(input("请输入您想设置的短横的线宽大小:"))
line_type = line_color
for i in range(len(x)):
    half_ls = len_shortline / 2
    x1 = x[i] - half_ls      # 短横连线的起点
    x2 = x[i] + half_ls      # 短横连线的中点
    y1 = y[i]
    y2 = y[i]
    m = [x1, x2]
    n = [y1, y2]
    plt.plot(m, n, line_type, linewidth = line_width)   # 两点连线，并设置好颜色、线型和线宽

print("\n------------坐标参数设置------------\n")
print("******设置坐标轴范围******")
print("x轴横坐标采取默认值，不可修改")
ylim_min = float(input("请输入您想设置的纵坐标范围的下限:"))
ylim_max = float(input("请输入您想设置的纵坐标范围的上限:"))
plt.ylim((ylim_min, ylim_max))

"""

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 30,
         }
#plt.xlabel('round', font2)
plt.ylabel(y_name, font2)
"""
print("\n------------横线上是否显示纵坐标值的文本设置------------")
text_choice = input("您是否想每个横线上显示其纵坐标值(y/n):")
if 'y' == text_choice:
    k = 0
    pianyi = float(input('请输入坐标值文本距离横线的偏移量(如0.005):'))
    color_text = input("请输入您想要的文本颜色\n(r:红色 b:蓝色 g:绿色 c:青色 m:洋红 y:红色 k:黑色 w:白色):")
    num_n =  int(input("请输入您想要保留的小数点后的位数(如1):"))
    for t_y in y:
        plt.text(x[k], t_y+0.1, '%.2f' % t_y, ha='center', va='bottom', color=color_text,fontsize=font1['size'])
        k += 1

plt.show()    # 图片显示
