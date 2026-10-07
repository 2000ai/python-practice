# 温度换算器 v2.0
print("=== 温度换算器 ===")
print("1. 摄氏度 -> 华氏度")
print("2. 华氏度 -> 摄氏度")

choice = input("请选择功能（输入 1 或 2）：")

try:
    if choice == "1":
        # 摄氏转华氏: F = C * 1.8 + 32
        c = float(input("请输入摄氏度："))
        f = c * 1.8 + 32
        print(f"{c}摄氏度 = {f:.2f}华氏度")
    elif choice == "2":
        # 华氏转摄氏: C = (F - 32) / 1.8
        f = float(input("请输入华氏度："))
        c = (f - 32) / 1.8
        print(f"{f}华氏度 = {c:.2f}摄氏度")
    else:
        print("输入错误：只能输入 1 或 2。")
except ValueError:
    print("输入错误：请输入有效的数字！")