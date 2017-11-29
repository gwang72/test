# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 20:21:45 2017

@author: pfermat
"""

import xlrd
import xlwt
import sys


def ReadXlsFile(filepath: str):
    """
    通过xlrd读取excel文件
    :param filepath:文件完整路径，windows下参考格式 'D:\\src\\python\\Example.xlsx'
    :return:
    """
    try:
        data = xlrd.open_workbook(filepath)
    except IOError:
        return 1
    
    return data


def GetSize(data: 'xls data', index: int=0) -> tuple:
    """
    获取表格的行数与列数
    :param data:xlrd读取后返回的excel数据对象
    :param index:表格索引
    :return:(行数,列数)
    """
    table = data.sheets()[index]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    
    return (nrows, ncols)


def ReadSystemData(data: 'xls data') -> dict:
    """
    读取系统表格中的数据
    :param data:xlrd读取后返回的excel数据对象
    :return:{'学生姓名':['试卷id','学生id','学号']}
    """
    (nrows, ncols) = GetSize(data)
    table = data.sheets()[0]
    d = {}  # 存储返回的dict
    for i in range(2, nrows):  # 跳过第一行第二行的表头
        name = table.cell(i, 3).value
        paper_id = table.cell(i, 0).value
        stu_id = table.cell(i, 1).value
        stu_number = table.cell(i, 2).value
        if name not in d.keys():  # 已存数据中没有该学生姓名
            d[name] = [paper_id, stu_id, stu_number]
        
    return d


def ReadSystemOutline(data: 'xls data') ->  list:
    """
    读取系统表格中的第一行表头
    :param data: xlrd读取后返回的excel数据对象
    :return:list
    """
    (nrows, ncols) = GetSize(data)
    table = data.sheets()[0]
    l = []
    for i in range(4):  # 表头前4列
        l.append(table.cell(0,i).value)
    for i in range(4, ncols):  # 表头之后的列
        l.append(table.cell(1,i).value)

    return l


def ReadSchoolData(data: 'xls data') -> dict:
    """
    读取学校表格中的数据
    :param data:xlrd读取后返回的excel数据对象
    :return:{'学生姓名':[各小题得分]}
    """
    (nrows, ncols) = GetSize(data)
    table = data.sheets()[0]
    d = {}  # 存储返回的dict
    for i in range(1, nrows):  # 跳过第一行表头
        name = table.cell(i, 0).value
        scores = []
        for j in range(1, ncols):  # 读取每列对应的小题得分
            scores.append(0 if table.cell(i, j).value == '' else table.cell(i, j).value)
        if name not in d.keys():  # 已存数据中没有该学生姓名
            d[name] = scores
            
    return d


def Output(systemfile: str, schoolfile: str):
    """
    获取系统文件和学校文件，并按照格式输出成绩表
    :param systemfile: 系统文件
    :param schoolfile: 学校文件
    :return: 规定格式的学生成绩表
    """
    data_system = ReadXlsFile(systemfile)
    data_school = ReadXlsFile(schoolfile)
    d_system = ReadSystemData(data_system)
    d_school = ReadSchoolData(data_school)
    l = []  # 按行存放输出结果

    for k, v in d_system.items():
        if k in d_school.keys():
            line = []
            line.append(v[0])
            line.append(v[1])
            line.append(v[2])
            line.append(k)  # 依次添加 试卷id 学生id 学号 姓名
            for index in range(len(d_school[k])):
                line.append((d_school[k][index]))  # 加入小题得分数据
            l.append(line)

    workbook = xlwt.Workbook(encoding='utf8')
    worksheet = workbook.add_sheet('output')

    # 写入表头信息
    outline = ReadSystemOutline(data_system)
    for i in range(len(outline)):
        worksheet.write(0, i, label='')  # 第一行空行
        worksheet.write(1, i, label=outline[i])  # 第二行为表头信息

    # 写入每行学生的信息
    for i in range(len(l)):
        for index in range(len(l[i])):
            worksheet.write(i + 2, index, label=l[i][index])  # 真实数据从第三行开始写入

    workbook.save(str(sys.argv[1]) + '.output.xls')


def CheckNewStudent(systemfile: str, schoolfile: str) -> list:
    """
    根据学校文件比对系统文件，检查学校中新增的学生
    :param systemfile: 系统文件
    :param schoolfile: 学校文件
    :return: [学生姓名]
    """
    data_system = ReadXlsFile(systemfile)
    data_school = ReadXlsFile(schoolfile)
    d_system = ReadSystemData(data_system)
    d_school = ReadSchoolData(data_school)
    students = []  # 存放新增学生

    for k in d_school.keys():
        if k not in d_system.keys():
            students.append(k)

    return students


def CheckRename(schoolfile: str) -> dict:
    """
    根据学校文件，检查同名的学生
    :param schoolfile: 学校文件
    :return:{学生姓名:同名数量}
    """
    data_school = ReadXlsFile(schoolfile)
    students = {}  # 存放学生姓名及数量

    (nrows, ncols) = GetSize(data_school)
    table = data_school.sheets()[0]
    for i in range(1, nrows):  # 跳过第一行表头
        name = table.cell(i, 0).value
        if name not in students.keys():
            students[name] = 1
        else:  # 该学生姓名已存在
            students[name] += 1

    return students


def main():
    if len(sys.argv) <= 3:
        print("参数数量不正确")
        # print("使用方法 " + str(sys.argv[0]) + " 系统文件.xls" + " 学校文件.xls")
        sys.exit(1)

    option = str(sys.argv[1])
    systemfile = str(sys.argv[2])
    schoolfile = str(sys.argv[3])

    if option == 'o':  # 输出成绩表
        Output(systemfile, schoolfile)
    elif option == 'c':  # 检查学校文件中新增的学生
        students = CheckNewStudent(systemfile, schoolfile)
        if len(students) != 0:
            for i in range(len(students)):
                print(students[i])
    elif option == 'r':  # 检查学校文件中的同名学生
        students = CheckRename(schoolfile)
        for k, v in students.items():
            if v > 1:
                print(k, v)
    else:
        pass

    
if __name__ == "__main__":
    main()
