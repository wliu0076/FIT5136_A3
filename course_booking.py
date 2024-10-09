from datetime import datetime, timedelta

class Course:
    def __init__(self, name, instructor, date, time, duration, frequency, credits, location, capacity, category, feedback, difficulty):
        self.name = name
        self.instructor = instructor
        self.date = date
        self.time = time
        self.duration = duration
        self.frequency = frequency
        self.credits = credits
        self.location = location
        self.capacity = capacity
        self.category = category
        self.feedback = feedback
        self.difficulty = difficulty
        self.booked = 0  # 当前预订人数
        self.booked_users = []  # 已预订该课程的用户

    def display_details(self):
        return f"""
课程名称: {self.name}
教练名称: {self.instructor}
日期: {self.date}
时间: {self.time}
时长: {self.duration} 分钟
课程频率: {self.frequency}
学分: {self.credits}
地点: {self.location}
容量: {self.capacity} 人
类别: {self.category}
反馈: {self.feedback}
难度级别: {self.difficulty}
"""

# 模拟的课程数据
courses = [
    Course('瑜伽', '张老师', '2024-10-10', '10:00', 60, '每周', 20, '1号健身房', 25, '健身', '非常棒的课程', '初级'),
    Course('普拉提', '李老师', '2024-10-12', '14:00', 90, '特殊', 30, '2号健身房', 20, '健身', '锻炼核心力量', '中级'),
]

# 学分余额（初始1000）
user_balance = 1000
user_bookings = []  # 用户已预订课程

def display_prompt():
    print("""
--------------------------------
|   Monash 健身课程预订系统     |
|                              |
|      1. 返回主界面            |
|      0. 退出系统              |
--------------------------------
""")

def display_confirmation_prompt():
    print("""
--------------------------------
|   Monash 健身课程预订系统     |
|                              |
|      1. 确认预订              |
|      2. 取消预订              |
|      0. 返回主界面            |
--------------------------------
""")

def view_courses():
    print("以下是可用的课程列表：")
    for idx, course in enumerate(courses, start=1):
        print(f"{idx}. {course.name} - 教练: {course.instructor}, 日期: {course.date}, 时间: {course.time}, 学分: {course.credits}, 容量: {course.capacity} 人")

    display_prompt()
    choice = input("请输入您的选择：")
    if choice == '1':
        return
    elif choice == '0':
        exit()

def display_course_numbers():
    print("以下是可用课程的编号：")
    for idx, course in enumerate(courses, start=1):
        print(f"{idx}. {course.name}")

def view_course_details():
    # 显示课程编号的提示框
    display_course_numbers()

    course_number = input("请输入要查看详情的课程编号（输入 0 返回主界面）：")
    if course_number == '0':
        return
    try:
        course = courses[int(course_number) - 1]
        print(course.display_details())
    except (ValueError, IndexError):
        print("无效的课程编号！")

    display_prompt()
    choice = input("请输入您的选择：")
    if choice == '1':
        return
    elif choice == '0':
        exit()


def check_time_conflict(new_course):
    new_course_time = datetime.strptime(f"{new_course.date} {new_course.time}", '%Y-%m-%d %H:%M')
    for course in user_bookings:
        existing_course_time = datetime.strptime(f"{course.date} {course.time}", '%Y-%m-%d %H:%M')
        if new_course_time == existing_course_time:
            return True
    return False

def book_course():
    global user_balance
    course_number = input("请输入要预订的课程编号（输入 0 返回主界面）：")
    if course_number == '0':
        return
    try:
        course = courses[int(course_number) - 1]
        # 检查是否已预订该课程
        if course in user_bookings:
            print("您已经预订了此课程，不能重复预订。")
            return
        # 检查时间冲突
        if check_time_conflict(course):
            print("您已经预订了同一时间段的课程，请选择其他时间的课程。")
            return
        # 检查课程预订是否在开始前2小时
        course_time = datetime.strptime(f"{course.date} {course.time}", '%Y-%m-%d %H:%M')
        if datetime.now() > course_time - timedelta(hours=2):
            print("课程预订已截止，您不能在课程开始前2小时内预订。")
            return
        # 检查课程容量
        if course.booked >= course.capacity:
            print("课程已满，请选择其他课程。")
            return
        # 检查学分余额
        if user_balance < course.credits:
            print("学分不足，请联系管理员增加学分。")
            return

        # 显示确认框
        display_confirmation_prompt()
        choice = input("请输入您的选择：")
        if choice == '1':
            course.booked += 1
            user_balance -= course.credits
            user_bookings.append(course)
            print(f"预订成功！您已成功预订 {course.name}，学分扣除 {course.credits}，剩余学分 {user_balance}")
        elif choice == '2':
            print("预订已取消。")
        elif choice == '0':
            print("返回主界面。")
            return
        else:
            print("无效选择，请重试。")
    except (ValueError, IndexError):
        print("无效的课程编号！")

def main_menu():
    while True:
        print("""
--------------------------------
|   Monash 健身课程预订系统     |
|                              |
|      1. 查看课程列表          |
|      2. 查看课程详情          |
|      3. 预订课程              |
|      0. 退出系统              |
--------------------------------
""")
        choice = input("请输入您的选择：")
        if choice == '1':
            view_courses()
        elif choice == '2':
            view_course_details()
        elif choice == '3':
            book_course()
        elif choice == '0':
            print("退出系统。")
            break
        else:
            print("无效选择，请重试。")

# 测试
if __name__ == "__main__":
    main_menu()
