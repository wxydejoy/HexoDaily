import os
import subprocess as sp
import sys
import time
import string



# 图床仓库自动更新版本并且推送到github
# md文件自动查找替换域名
# 自动推送博客


def cmd(command,cwdd): # cmd
    command = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe " + command
    p = sp.Popen(command, shell=True,
                 cwd=cwdd,
                 encoding="UTF-8",stdout=sp.PIPE,stderr=sp.PIPE)
    try:
        outs, errs = p.communicate(timeout=150)
    except p.TimeoutExpired:
        p.kill()
        outs, errs = p.communicate()
    p.wait(100)
    p.kill()
    return list(outs)

# def cmd(command): # cmd 其实是powershell
#     command = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe " + command
#     p = sp.Popen(command, shell=True,
#                  encoding="UTF-8",stdout=sp.PIPE,stderr=sp.PIPE)
#     try:
#         outs, errs = p.communicate(timeout=150)
#     except p.TimeoutExpired:
#         p.kill()
#         outs, errs = p.communicate()
#     p.wait(100)
#     p.kill()
#     return list(outs)
#

def getnpmversion(bag): # 获取npm包的版本号 并加一

    strr = cmd("npm view "+bag+" version",None)
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

def urlreplace(root_path,git_name,git_re,npm_name,version):
    file_lists = []
    # 用来存放所有的目录路径
    dir_list = []
    get_file_path(root_path, file_lists, dir_list)
    
    for file_list in file_lists:
        file = open(file_list, 'r+',encoding="UTF-8")
        s = file.read()
        file.seek(0, 0)
        s = s.replace("cdn.jsdelivr.net/gh/"+git_name+"/" + git_re, "unpkg.zhimg.com/"+npm_name + "@" + version)
        file.write(s)
    file.close()


def updateimage(image_path):
    cmd('git pull', image_path)
    cmd('git add .', image_path)

    cmd("git commit  -m ' npm 自动更新 '", image_path)

    cmd("npm version patch ", image_path)

    cmd("git push", image_path)



if __name__ == '__main__':

    # 参数设置

    git_name = "wxydejoy"
    git_re = "image"
    domain = "unpkg.zhimg.com"
    npm_name = "wxydeimage"
    version = getnpmversion("wxydeimage")
    root_path = r"D:\Windows\zm\source\_posts" # 用来存放所有的文件路径
    image_path = "D:\Windows\wd\GitHub\image"

    updateimage(image_path)
    # print(cmd("npm -version"))
    # 替换
    # urlreplace(root_path, git_name, git_re,  npm_name, version)
    #
    # updateimage(image_path)









