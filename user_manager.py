class User:
    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

# 预定义的登录凭据
valid_users = {
    'member@student.monash.edu': User('member@student.monash.edu', 'Monash1234!', '成员'),
    'admin@monash.edu': User('admin@monash.edu', 'Admin1234!', '管理员')
}

def print_message(message):
    # 直接输出格式化内容
    print(message)

def login():
    # 显示欢迎界面并输入邮箱
    while True:
        print_message("""
-------------------------------        
|     Monash 健身课程预订系统     |
|                              |
|           ======             |
|            登录               |
|           ======             |
|                              |
|     请输入您的 Monash 邮箱:     |
|      ______@monash.edu       |
|                              |
|输入 # 继续                     |
|输入 0 返回                     |
-------------------------------|
""")

        email_input = input(">>> ")

        # 检查输入是否选择返回
        if email_input == '0':
            print("返回上一级菜单")
            return None

        # 允许两种邮箱
        if email_input not in valid_users:
            print("请输入正确的 monash.edu 邮箱地址！")
            input("按任意键继续...")
            continue

        # 显示密码输入界面
        print_message("""
-------------------------------        
|     Monash 健身课程预订系统     |
|                              |
|           ======             |
|            登录               |
|           ======             |
|                              |
|     请输入您的账户密码:         |
|      __________              |
|                              |
|输入 # 继续                     |
|输入 0 返回                     |
-------------------------------|
""")
        password_input = input(">>> ")

        # 检查输入是否选择返回
        if password_input == '0':
            print("返回上一级菜单")
            return None

        # 验证登录
        user = valid_users.get(email_input)
        if user.password == password_input:
            print_message(f"""
-------------------------------
|      登录成功！               |
|  欢迎 {user.role} 用户: {email_input}   |
-------------------------------|
""")
            return user.role
        else:
            print_message("""
-------------------------------
|       密码错误，请重试！       |
-------------------------------|
""")
            input("按任意键继续...")

# 测试
if __name__ == "__main__":
    role = login()

    if role == '成员':
        print("你已成功以成员身份登录系统。")
    elif role == '管理员':
        print("你已成功以管理员身份登录系统。")
    else:
        print("登录失败。")
