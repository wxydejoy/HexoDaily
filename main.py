import os
import subprocess as sp
import sys
import re
import string



def cmd(command,cwdd): # cmd
    command = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe " + command
    p = sp.run(command, shell=True,
                 cwd=cwdd,
                 encoding="UTF-8",stdout=sp.PIPE,stderr=sp.PIPE)

    return list(p.stdout)

def cmd(command): # cmd
    command = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe " + command
    p = sp.run(command, shell=True,
                 encoding="UTF-8",stdout=sp.PIPE,stderr=sp.PIPE)

    return list(p.stdout)


def getnpmversion(bag): # 获取npm包的版本号 并加一

    strr = cmd("npm view "+bag+" version")
    strr[-2] = int(strr[-2]) + 1
    return ''.join(list(map(str, strr)))



def get_file_path(root_path,file_list,dir_list): #遍历文件
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)

def urlreplace(root_path,git_name,git_re,domain,npm_name,version):
    file_list = []
    # 用来存放所有的目录路径
    dir_list = []
    get_file_path(root_path, file_list, dir_list)
    
    for i in file_list:
        fopen = open(filename, 'r+')
        str = fopen.read()
        str.replace(. xxx,xxx)
    fopen.close()
    


if __name__ == '__main__':
    ps = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe " #powershell
    git_name = "wxydejoy"
    git_re = "image"
    domain = "unpkg.zhimg.com"
    npm_name = "wxydejoy"
    version = getnpmversion("wxydeimage")
    print(version)
    root_path = r"D:\Windows\wd\GitHub\blog\source\_posts"
    # 用来存放所有的文件路径
    mdreplace(root_path, git_name, git_re, domain, npm_name, version)
    #print(file_list)
    #print(dir_list)










