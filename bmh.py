# @ name: Daisy StudentId: 202110701580008
# @ Date: 2022-11-29 22:36
import math


# 水质评估算法
# 输入水质测量值
def input_c():
    for i in range(4):
        c = input(f"{EQ.get(i)}请输入水质测量的数值").split()
        if len(c) != 6:
            print("输入有误")
            break
        else:
            for e in range(6):
                sz[e].append(eval(c[e]))


# 输入气象指标值
def input_qx():
    for i in range(len(EQ)):
        qx = input(f"请输入{EQ[i]}气象指标值").split()
        if len(qx) != 8:
            print("请检查数据")
            break
        else:
            qxzbsz.append(qx)
    for i in qxzbsz:
        fylz.append(eval(i[0]))
        gzqd.append(eval(i[1]))
        pm.append(eval(i[2]))
        fx.append(eval(i[3]))
        fs.append(eval(i[4]))
        qy.append(eval(i[5]))
        kqsd.append(eval(i[6]))
        kqwd.append(eval(i[7]))


# 计算sbz
def sbz_list():
    for i in sz:
        location = sz.index(i)
        lst = []
        if location <= 4:
            for j in i:
                value = j / bz[location]
                lst.append(value)
            sbz.append(lst)


# 查看水质情况
def _peek_(tp):
    index = tpList.index(tp)
    if index < 0:
        return print("没有该选项")
    for e in range(len(EQ)):
        station = EQ.get(e)
        zu = sbz[index]
        result = tp(zu[e])
        print(f"{station},{result[0]},{zu[e]},{result[2]},{result[1]}")


# 计算SBZI
def get_sbzi(_sbz_):
    sbzi = 0.0
    for i in _sbz_:
        for j in i:
            sbzi += (j / 5 / 4)
    return sbzi


# 计算SBZJ
def get_sbzj(_sbz_):
    sbzj = list(0 for _ in range(5))
    for s in range(len(sbzj)):
        sbzj[s] = sum(_sbz_[s]) / 4
    return sbzj


# 计算SBZM
def get_sbzm(_sbz_):
    return max(get_sbzj(_sbz_))


# 计算内梅罗指数
def get_nmdzs(_sbz_):
    return math.sqrt((get_sbzi(_sbz_) ** 2 + get_sbzm(_sbz_) ** 2) / 2.0)


# 打印水质量内梅罗指数
def print_nmdzs(_sbz_):
    nmlzs = get_nmdzs(_sbz_)
    if nmlzs < 1:
        print(f"内梅罗指数数值={nmlzs},水环境质量较好")
    else:
        print(f"内梅罗指数数值={nmlzs},水环境质量较差")


# 计算ph偏差值
def check_ph(indicators):
    if indicators > 7.5:
        if 6.5 <= (indicators - 7.0) / (9.0 - 7.0) < 8.5:
            return "达标"
        else:
            return "不达标"
    else:
        if 6.5 <= (7.0 - indicators) / (7.0 - 6.0) < 8.5:
            return "达标"
        else:
            return "不达标"


# 模拟输出
def analog_output(_qxzbsz_):
    for i in range(len(qxzbsz)):
        print(f"{EQ.get(i)}的负氧离子:{qxzbsz[i][0]}个/cm3")
        print(f'{EQ.get(i)}的光照强度:{qxzbsz[i][1]} LUX')
        print(f'{EQ.get(i)}的PM2.5:{qxzbsz[i][2]} ug/m3')
        print(f'{EQ.get(i)}的风向:{qxzbsz[i][3]}°')
        print(f'{EQ.get(i)}的风速:{qxzbsz[i][4]} m/s')
        print(f'{EQ.get(i)}的气压:{qxzbsz[i][5]} hPa')
        print(f'{EQ.get(i)}的空气湿度:{qxzbsz[i][6]} %')
        print(f'{EQ.get(i)}的空气温度:{qxzbsz[i][7]}℃')


# 评估算法
def get_iqaik(value):
    if 0 <= value < 35:
        k = 0
    elif value < 75:
        k = 1
    elif value < 115:
        k = 2
    elif value < 150:
        k = 3
    elif value < 250:
        k = 4
    elif value < 350:
        k = 5
    elif value < 500:
        k = 6
    else:
        return "出错了"
    k2 = k + 1
    return (iaqi[k2] - iaqi[k]) / (pm[k2] - pm[k]) * (value - pm[k] + iaqi[k])


# 评估pm2.5
def aqi25():
    for i in range(len(pm)):
        value = get_iqaik(pm[i])
        if 0 <= value < 50:
            print(f'{EQ.get(i)}的AQI-PM2.5: {value} 优')
        elif value < 100:
            print(f'{EQ.get(i)}的AQI-PM2.5: {value} 良')
        elif value < 150:
            print(f'{EQ.get(i)}的AQI-PM2.5:" {value} 轻度污染')
        elif value < 200:
            print(f'{EQ.get(i)}的AQI-PM2.5:" {value} 中度污染')
        elif value < 300:
            print(f'{EQ.get(i)}的AQI-PM2.5:" {value} 重度污染')
        elif value >= 300:
            print(f'{EQ.get(i)}的AQI-PM2.5:" {value} 严重污染')
        else:
            print("出错了")


# 评估负氧离子
def fylz_print():
    for i in range(len(fylz)):
        value = fylz[i]
        if value < 1000:
            print(f"{EQ.get(i)}空气污染")
        elif value <= 1500:
            print(f"{EQ.get(i)}清新空气")
        else:
            print(f"{EQ.get(i)}健康空气")


# 初始化
def init():
    input_c()
    input_qx()
    sbz_list()


# 菜单
def menu():
    print("1.查看水质")
    print("2.查看内梅罗指数")
    print("3.查看各项空气指数数值")
    print("4.查看空气质量指数评价")
    print("5.查看负氧离子指标")


tpList = [lambda indicators: ("蓝绿藻", "达标" if indicators <= 1 else "不达标", "cells/ml"),
          lambda indicators: ("叶绿素a", "达标" if indicators <= 1 else "不达标", "ug/L"),
          lambda indicators: ("溶解氧", "达标" if (1 / indicators) <= 1 else "不达标", "mg/L"),
          lambda indicators: ("浊度", "达标" if indicators <= 1 else "不达标", "NTU"),
          lambda indicators: ("PH:", check_ph(indicators), "Mol/L")]

qxzbsz = []
llz, yls, rjy, zd, ph, sw = [], [], [], [], [], []
fylz, gzqd, pm, fx, fs, qy, kqsd, kqwd = [], [], [], [], [], [], [], []
bz = [625, 10, 5, 3, 7]
sz = [llz, yls, rjy, zd, ph, sw]
qx_list = [fylz, gzqd, pm, fx, fs, qy, kqsd, kqwd]
sbz = []
EQ = {0: "综合监测点", 1: "保育区1", 2: "保育区2", 3: "入湖河道"}

# 空气质量评估算法

iaqi = [0, 50, 100, 150, 200, 300, 400, 500]
pm25 = [0, 35, 75, 115, 150, 250, 350, 500]

if __name__ == '__main__':
    init()
    while True:
        menu()
        user_input = eval(input("请输入操作序号"))
        if user_input == 1:
            for i in range(len(tpList)):
                _peek_(tpList[i])
        elif user_input == 2:
            print_nmdzs(sbz)
        elif user_input == 3:
            analog_output(qxzbsz)
        elif user_input == 4:
            aqi25()
        elif user_input == 5:
            fylz_print()
        else:
            break
