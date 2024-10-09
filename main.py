# main.py

from user_manager import login
from course_booking import main_menu as course_booking_menu

def display_main_menu():
    print("""
--------------------------------
Monash 健身课程预订系统
--------------------------------

==========
主页
==========

1. 注册和登录
2. 课程安排和预订
3. 会员资料和课程管理
4. 支付管理
5. 管理管理
0. 返回主界面

----------------------------------------
请输入 1-5 选择功能
输入 0 返回上一级
----------------------------------------
>>> """)

def main():
    while True:
        display_main_menu()
        choice = input("请输入您的选择：")
        if choice == '1':
            # 进行登录操作
            role = login()
            if role == '成员':
                print("您已登录为成员。")
            elif role == '管理员':
                print("您已登录为管理员。")
            else:
                print("登录失败，返回主页。")
        elif choice == '2':
            # 进入课程安排和预订菜单
            course_booking_menu()
        elif choice == '3':
            print("会员资料和课程管理功能开发中...")
        elif choice == '4':
            print("支付管理功能开发中...")
        elif choice == '5':
            print("管理管理功能开发中...")
        elif choice == '0':
            print("退出系统。")
            break
        else:
            print("无效选择，请重试。")

# 启动主程序
if __name__ == "__main__":
    main()
