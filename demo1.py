# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-15 19:47
import os


def menu():  # 菜单
    print()
    print("0.唤出菜单"
          "\n1.添加学生信息模块",
          "\n2.添加学生成绩模块",
          "\n3.删除学生信息模块",
          "\n4.删除学生成绩模块"
          "\n5.修改信息模块",
          "\n6.修改成绩模块"
          "\n7.查询信息模块",
          "\n8.查询成绩模块"
          "\n9.遍历学生信息功能模块",
          "\n10.遍历学生成绩功能模块"
          "\n11.成绩升序排序"
          "\n12.成绩降序排序"
          "\n13.保存并退出")
    print()


def information():
    name = input("输入学生姓名")
    age = input("输入学生年龄")
    sex = input("输入学生性别")
    student_informations_dict = {"studentID": student_id, "name": name, "age": age, "sex": sex}
    student_dicte = {"studentID": student_id, "name": name}
    student_informations_list.append(student_informations_dict)
    student_list.append(student_dicte)


def add_student():  # 将学生信息以字典的形式添加到列表
    global student_id
    student_id = input("输入学生ID")
    if len(student_informations_list) != 0:
        for i in student_informations_list:
            if student_id in i["studentID"]:
                print("该生已存在")
                break
        else:
            information()
            print("添加成功")
    elif len(student_informations_list) == 0:
        information()
        print("添加成功")


def add_grades():  # 插入学生成绩
    student_id = input("请输入学生ID")
    for i in student_list:
        if student_id == i["studentID"]:
            for j in student_grades_list:
                if student_id == j["studentID"]:
                    print("该生成绩已录入")
                    break
            else:
                Chinese = input("请输入语文成绩")
                Math = input("请输入数学成绩")
                English = input("请输入英语成绩")
                student_grades_dicte = {"studentID": student_id, "name": i["name"], "Chinese": Chinese,
                                        "Math": Math,
                                        "English": English}
                student_grades_list.append(student_grades_dicte)
                print("添加成功")
                break
            break
    else:
        print("该生信息不存在，请检查")


def delete_student_informations():  # 删除学生信息
    student_id = input("请输入学生ID")
    for i in student_informations_list:
        if student_id == i["studentID"]:
            index = student_informations_list.index(i)
            student_informations_list.remove(i)
            print("操作成功")
            student_list.remove(student_list[index])
            student_grades_list.remove(student_grades_list[index])
            break
    else:
        print("该生信息不存在，请检查")


def delete_student_grades():  # 删除学生成绩
    student_id = input("请输入学生ID")
    for i in student_grades_list:
        if student_id == i["studentID"]:
            student_grades_list.remove(i)
            print("操作成功")
            break
    else:
        print("该生信息不存在，请检查")


def change_informations():  # 修改学生信息
    student_id = input("输入学生学号：")
    for i in student_informations_list:
        index = student_informations_list.index(i)
        if student_id == i["studentID"]:
            i["name"] = input("新的学生姓名：")
            i["age"] = input("新的学生年龄")
            student_list[index]["name"] = i["name"]
            student_grades_list[index]["name"] = i["name"]
            print("操作成功")
            break
    else:
        print("该生信息不存在！")


def change_grades():  # 修改学生成绩
    student_id = input("输入学生学号：")
    for i in student_grades_list:
        if student_id == i["studentID"]:
            i["Chinese"] = input("新的语文成绩：")
            i["Math"] = input("新的数学成绩：")
            i["English"] = input("新的英语成绩：")
            print("操作成功")
            break
    else:
        print("该生信息不存在！")


def search_informations():  # 查找单个学生信息
    student_id = input("输入学生学号：")
    for i in student_informations_list:
        if student_id == i["studentID"]:
            print(
                f'学号: {i["studentID"]} 姓名: {i["name"]} 性别：{i["sex"]} 年龄：{i["age"]}'
            )
            print("操作成功")
            break
    else:
        print("不存在！")


def search_grades():  # 查找单个学生成绩
    student_id = input("输入学生学号：")
    for i in student_grades_list:
        if student_id == i["studentID"]:
            print(
                f'学号: {i["studentID"]} 姓名: {i["name"]} 语文: {i["Chinese"]} 数学: {i["Math"]} 英语: {i["English"]}'
            )
            print("操作成功")
            break
    else:
        print("不存在！")


def select_infromations():  # 遍历学生信息
    if len(student_informations_list) == 0:
        print("暂无数据")
    else:
        print("{:<15}{:<15}{:<15}{:<15}".format("studentID", "name", "sex", "age"))
        for i in student_informations_list:
            print(
                f'{i["studentID"]:<15}{i["name"]:<15}{i["sex"]:<15}{i["age"]:<15}'
            )
        print("操作成功")


def select_grades():  # 遍历学生成绩
    if len(student_grades_list) == 0:
        print("暂无数据")
    else:
        print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("studentID", "name", "Chinese", "Math", "English"))
        for i in student_grades_list:
            print(
                f'{i["studentID"]:<15}{i["name"]:<15}{i["Chinese"]:<15}{i["Math"]:<15}{i["English"]:<15}'
            )
        print("操作成功")


def grades_sort():  # 升序
    if len(student_grades_list) == 0:
        print("暂无数据")
    else:
        user_input = input("请输入排序关键字")
        for i in student_grades_list:
            if user_input in i:
                sort = sorted(student_grades_list, key=lambda x: x[user_input])
                print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("studentID", "name", "Chinese", "Math", "English"))
                for i in sort:
                    print(
                        f'{i["studentID"]:<15}{i["name"]:<15}{i["Chinese"]:<15}{i["Math"]:<15}{i["English"]:<15}'
                    )
                print("操作成功")
                break
        else:
            print("该排序关键字不存在")


def grade_resort():  # 降序
    if len(student_grades_list) == 0:
        print("暂无数据")
    else:
        user_input = input("请输入排序关键字")
        for i in student_grades_list:
            if user_input in i:
                sort = sorted(student_grades_list, key=lambda x: x[user_input], reverse=True)
                print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("studentID", "name", "Chinese", "Math", "English"))
                for i in sort:
                    print(
                        f'{i["studentID"]:<15}{i["name"]:<15}{i["Chinese"]:<15}{i["Math"]:<15}{i["English"]:<15}'
                    )
                print("操作成功")
                break

        else:
            print("该排序关键字不存在")


def save():  # 保存文件
    if os.path.exists(path1):
        os.remove(path1)
    file1 = open(path1, "w")
    file1.write(f"{student_informations_list}")
    file1.close()

    if os.path.exists(path2):
        os.remove(path2)
    file1 = open(path2, "w")
    file1.write(f"{student_grades_list}")
    file1.close()

    if os.path.exists(path3):
        os.remove(path3)
    file1 = open(path3, "w")
    file1.write(f"{student_list}")
    file1.close()


def input_data():  # 导入数据
    global student_informations_list
    global student_grades_list
    global student_list
    if os.path.exists(path1):
        student_informations_list = eval(open(path1, "r").read())
    else:
        student_informations_list = []
    if os.path.exists(path2):
        student_grades_list = eval(open(path2, "r").read())
    else:
        student_grades_list = []
    if os.path.exists(path2):
        student_list = eval(open(path3, "r").read())
    else:
        student_list = []


path1 = "student_information.txt"
path2 = "student_grades.txt"
path3 = "student_list.txt"

student_list = []
student_informations_list = []
student_grades_list = []

if __name__ == '__main__':
    menu()
    input_data()

    while True:
        user = eval(input("请输入对应序号"))
        choose_dict = {
            0: menu, 1: add_student, 2: add_grades, 3: delete_student_informations, 4: delete_student_grades,
            5: change_informations, 6: change_grades, 7: search_informations, 8: search_grades,
            9: select_infromations, 10: select_grades, 11: grades_sort, 12: grade_resort
        }
        if user in choose_dict:
            choose_dict[user]()
        elif user == 13:
            save()
            print("文件保存成功，正在退出")
            break
        else:
            print("操作失误")
