import os
import subprocess as sp
import sys
import re




def cmd(command,cwdd): # cmd
    p = sp.run(command, shell=True,
                 cwd=cwdd,
                 encoding="UTF-8",stdout=sp.PIPE,stderr=sp.PIPE)

    return list(p.stdout)

def getnpmversion(bag): # 获取npm包的版本号 并加一
    str = cmd("C://WINDOWS//system32//WindowsPowerShell//v1.0//powershell.exe npm view "+bag+" version", "D://Windows//wd//GitHub//blog")
    str[len(str) - 2] = int(str[len(str) - 2]) + 1

    return str[0:len(str)-1]

if __name__ == '__main__':

    print(getnpmversion("wxydeimage"))









