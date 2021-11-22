import os
import subprocess as sp
from tkinter import *
import configparser
import tkinter.filedialog

import sys
import time
import string

global git_name, git_re, domain, npm_name, root_path, image_path
git_name = ""
git_re = ""
domain = ""
npm_name = ""

root_path = ""
image_path = ""

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
    # print(command)
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
    # print(''.join(list(map(str, strr))))
    return ''.join(list(map(str, strr[0:-1])))



def get_file_path(path,file_list,dir_list): #遍历文件
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)

def urlreplace(version):
    file_lists = []
    # 用来存放所有的目录路径
    dir_list = []
    # print(root_path)
    get_file_path(root_path, file_lists, dir_list)
    
    for file_list in file_lists:
        file = open(file_list, 'r+',encoding="UTF-8")
        s = file.read()
        file.seek(0, 0)
        s = s.replace("cdn.jsdelivr.net/gh/"+git_name+"/" + git_re, "unpkg.zhimg.com/"+npm_name + "@" + version)
        file.write(s)
    file.close()



def updateimage():
    cmd('git pull', image_path)
    cmd('git add .', image_path)

    cmd("git commit  -m ' npm 自动更新 '", image_path)

    cmd("npm version patch ", image_path)

    cmd("git push", image_path)

    # tk 相关


def mwindow():
    screenWidth = root.winfo_screenwidth()  # 屏幕宽度
    screenHeight = root.winfo_screenheight()  # 屏幕高度
    w = 300  # 窗口宽
    h = 160  # 窗口高
    x = (screenWidth - w) / 2  # 窗口左上角x轴位置
    y = (screenHeight - h) / 2  # 窗口左上角y轴位置
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))  # 表示距离屏幕左上角(400,200)
    # +x表示窗口左侧距离屏幕左侧距离, -x表示窗口右侧距离屏幕右侧的距离
    # +y与-y的含义类似，窗口上侧(下侧)距离屏幕上侧(下侧)的距离
    # 练习改函数


def unwindowset():
    # label = Label(root,text="前缀")
    # label.pack()
    # label = Label(root, text="前缀", fg="black", bg="#FFFFFF")
    # label.pack(anchor=N, side=LEFT, padx=10, pady=10)
    # label = Label(root, text="后缀", fg="black", bg="#FFFFFF")
    # label.pack(anchor=N, side=LEFT, padx=50, pady=10)
    # label = Label(root, text="自动序号", fg="black", bg="#FFFFFF")
    # label.pack(anchor=N, side=LEFT, padx=0, pady=10)

    btn = Button(root, padx=2, pady=2, bd=2, relief=GROOVE, bg="white", text="打开博客_posts", command=gitbutton)
    # btn.pack(side=BOTTOM,padx=10,pady=10)
    btn.place(x=20, y=10)
    btn = Button(root, padx=2, pady=2, bd=2, relief=GROOVE, bg="white", text="打开图床仓库", command=npmbutton)
    btn.place(x=20, y=50)

    global gitname, gitre, npmname
    gitname = Entry(root, width=6, bd=2, relief=GROOVE)
    gitre = Entry(root, width=6, bd=2, relief=GROOVE)
    npmname = Entry(root, width=6, bd=2, relief=GROOVE)
    label = Label(root, text="git name")
    label.place(x=145, y=10)
    label = Label(root, text="git repo")
    label.place(x=145, y=40)
    label = Label(root, text="npm repo")
    label.place(x=145, y=70)
    gitname.place(x=225, y=10)
    gitre.place(x=225, y=40)
    npmname.place(x=225, y=70)
    label = Label(root, text="--小魏", fg="blue", bg="#FFFFFF")
    label.place(x=240, y=120)
    btn = Button(root, padx=2, pady=2, bd=2, relief=GROOVE, bg="white", text="设置完成重启", command=init_run)
    btn.place(x=20, y=90)




def windowset():
    label = Label(root, text="--小魏", fg="blue", bg="#FFFFFF")
    label.place(x=220, y=120)
    btn = Button(root, padx=2, pady=2, bd=2, relief=FLAT, bg="white", text="替换链接", command=run)
    btn.place(x=120, y=20)
    # pb1 = Progressbar(root)
    # pb1.place(10,20)




def gitbutton():
    root_path = tkinter.filedialog.askdirectory()
    cf.set("Database", "root_path", root_path)
    # print(root_path)



def npmbutton():
    image_path = tkinter.filedialog.askdirectory()
    cf.set("Database", "image_path", image_path)
    # print(image_path)


def init_run():
    git_name = gitname.get()
    git_re = gitre.get()
    npm_name = npmname.get()
    cf.set("Database", "git_name", git_name)
    cf.set("Database", "git_re", git_re)
    cf.set("Database", "npm_name", npm_name)
    cf.set("Database", "init", "1")

    # Writing our configuration file to 'example.cfg'
    with open('config.ini', 'w') as configfile:
        cf.write(configfile)
    configfile.close()
    root.quit()


def run():

    urlreplace(getnpmversion(npm_name))
    updateimage()

if __name__ == '__main__':


    cf = configparser.ConfigParser()

    if os.path.exists("config.ini"):
        cf.read("config.ini")
        git_name = cf.get("Database", "git_name")
        git_re = cf.get("Database", "git_re")
        domain = cf.get("Database", "domain")
        npm_name = cf.get("Database", "npm_name")
        root_path = cf.get("Database", "root_path")
        image_path = cf.get("Database", "image_path")
        # 参数设置
    else:
        fp = open("config.ini", "w")
        fp.write(
            "[Database]\ninit = 0\ngit_name = \ngit_re = \ndomain = unpkg.zhimg.com\nnpm_name = \nroot_path = \nimage_path = \n")
        fp.close()
        cf.read("config.ini")


    # urlreplace(getnpmversion(npm_name))
    # updateimage()

    root = Tk()


    root.title("Hexo Tool")
    root.config(bg='#FFFFFF')
    root.resizable(0,0)
    #root.iconbitmap("x.ico")  # 不知道为什么，png和bmp无法显示，或许是我图片问题，但就先这样吧

    mwindow()
    if cf.get("Database", "init") == "0":
        unwindowset()
    else:
        windowset()




    # pyinstaller -F -w -i x.ico main.py --exclude-module _bootlocale


    root.mainloop()  # 让程序继续运行，同时进入等待与处理窗口事件，放在程序最后一行1





