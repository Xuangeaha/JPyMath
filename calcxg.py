"""
轩氏智能计算器 XG Xuan-Intelligent-Calculator-XG
Copyright (c) 2022-2023 轩哥啊哈OvO
"""

while True:
    print("--------------------------------------------------")
    print("""1加法 2减法 3乘法 4除法 5次方 6开根 7阶乘
    8最大公因数 9最小公倍数 10解三角形 11质数判断
    12进制转换 13一元一次方程 14一元二次方程 15三角函数
    16乘法表生成 17月份日历生成""")
    print("--------------------------------------------------")
    num = input("请选择：")
    print("--------------------------------------------------")

    import math

    if int(num) == 1:
        a = input("请输入加数1：")
        b = input("请输入加数2：")
        ans = int(a) + int(b)
        print("两数和为：" + str(ans))

    elif int(num) == 2:
        a = input("请输入被减数：")
        b = input("请输入减数：")
        ans = int(a) - int(b)
        print("两数差为：" + str(ans))

    elif int(num) == 3:
        a = input("请输入乘数1：")
        b = input("请输入乘数2：")
        ans = int(a) * int(b)
        print("两数乘积为：" + str(ans))

    elif int(num) == 4:
        a = input("请输入被除数：")
        b = input("请输入除数：")
        ans = int(a) / int(b)
        print("两数之商为：" + str(ans))

    elif int(num) == 5:
        a = input("请输入底数：")
        b = input("请输入指数：")
        ans = int(a) ** int(b)
        print("两数之幂为：" + str(ans))

    elif int(num) == 6:
        a = input("请输入被开方数：")
        ans = math.sqrt(int(a))
        print("该数开根为：" + str(ans))

    elif int(num) == 7:
        def jc(k):
            if (k > 1):
                result = k * jc(k - 1)
            else:
                result = 1
            return result

        a = input("请输入计算数：")
        ans = jc(int(a))
        print("该数阶乘为：" + str(ans))

    elif int(num) == 8:
        a = input("请输入数1：")
        b = input("请输入数2：")

        def hcf(x, y):
            if x > y:
                smaller = y
            else:
                smaller = x
            for i in range(1, smaller + 1):
                if ((x % i == 0) and (y % i == 0)):
                    hcf = i
            return hcf

        ans = hcf(int(a), int(b))
        print("两数最大公因数为：" + str(ans))

    elif int(num) == 9:
        a = input("请输入数1：")
        b = input("请输入数2：")

        def lcm(x, y):
            if x > y:
                greater = x
            else:
                greater = y
            while (True):
                if ((greater % x == 0) and (greater % y == 0)):
                    lcm = greater
                    break
                greater += 1
            return lcm


        ans = lcm(int(a), int(b))
        print("两数最小公倍数为：" + str(ans))

    elif int(num) == 10:
        a = int(input("请输入最短边的长度:"))
        b = int(input("请输入另一条边的长度:"))
        c = int(input("请输入最长边的长度:"))
        if (a + b) > c:
            if a ** 2 + b ** 2 == c ** 2:
                print("它是一个直角三角形")
            else:
                if a ** 2 + b ** 2 > c ** 2:
                    print("它是一个锐角三角形")
                else:
                    if a ** 2 + b ** 2 < c ** 2:
                        print("它是一个钝角三角形")
        else:
            print("它不能构成一个三角形")

    elif int(num) == 11:
        a = int(input("请输入需判断的数字: "))
        if a > 1:
            for i in range(2, a):
                if (a % i) == 0:
                    print(a, "不是质数")
                    print(i, "乘以", a // i, "是", a)
                    break
            else:
                print(a, "是质数")
        else:
            print(a, "不是质数")

    elif int(num) == 12:
        a = int(input("输入数字："))
        print("")
        print("二进制：" + bin(a)[2:])
        print("十进制：" + str(a))
        print("八进制：" + oct(a)[2:])
        print("十六进制：" + hex(a)[2:].upper())

    elif int(num) == 13:
        print("解方程：ax+b=0")
        a = input("输入a的值：")
        b = input("输入b的值：")
        try:
            ans = (int(b) * (-1)) / int(a)
            print("解得：x=" + str(ans))
        except:
            print("原方程无实数根、无解、有无数根或表达式错误")

    elif int(num) == 14:
        print("解方程：ax²+bx+c=0")
        a = input("输入a的值：")
        b = input("输入b的值：")
        c = input("输入c的值：")
        import math

        try:
            x1s = ((int(b) * -1) + (math.sqrt(int(b) ** 2 - 4 * int(a) * int(c)))) / (int(a) * 2)
            x2s = ((int(b) * -1) - (math.sqrt(int(b) ** 2 - 4 * int(a) * int(c)))) / (int(a) * 2)
            print("解得：x₁=" + str(x1s) + ",x₂=" + str(x2s))
        except:
            print("原方程无实数根、无解、有无数根或表达式错误")

    elif int(num) == 15:
        a = int(input("请输入角度："))
        sin = math.sin(a)
        cos = math.cos(a)
        tan = math.tan(a)
        sinh = math.sinh(a)
        cosh = math.cosh(a)
        tanh = math.tanh(a)
        print("sin(a) = " + str(sin))
        print("cos(a) = " + str(cos))
        print("tan(a) = " + str(tan))
        print("sinh(a) = " + str(sinh))
        print("coah(a) = " + str(cosh))
        print("tanh(a) = " + str(tanh))

    elif int(num) == 16:
        a = int(input("几乘几的乘法表？: "))
        for i in range(1, a + 1):
            for j in range(1, i + 1):
                print('{}x{}={}\t'.format(j, i, i * j), end='')
            print()

    elif int(num) == 17:
        import calendar

        yy = int(input("输入年份: "))
        mm = int(input("输入月份: "))
        print(calendar.month(yy, mm))

    Stop = input()
