import numpy as np
import cv2 as cv
import glob
import os
import win32api
import win32con


z = 0
e = ""
c = ""
bt = [0, 0, 0, 0, 0, 0, 0, 0]
df = [0, 0, 0, 0, 0, 0, 0, 0]


def ud():
    global bt, df
    bt = [0, 0, 0, 0, 0, 0, 0, 0]
    df = [0, 0, 0, 0, 0, 0, 0, 0]

    def sd():
        if not os.path.exists('.psnj/'):
            os.mkdir(".psnj/")
            win32api.SetFileAttributes(
                '.psnj/', win32con.FILE_ATTRIBUTE_HIDDEN)

    def a(g, rt):
        rc = [0, 0, 0, 0, 0, 0, 0, 0]
        global bt, df
        g = cv.resize(cv.imread(g), (800, 400))[0:00 + 352, 215:215 + 560]

        def s(t, e):
            if t == 0:
                t = 25 * t + (t - 1) * 18 - 15
            else:
                t = 25 * t + (t - 1) * 18 - 9
            e = 18 * e + (e - 1) * 46 - 2
            p = g[t:t + 18, e:e + 46]
            f = 0
            for y in range(18):
                for x in range(46):
                    if p[y, x][0] > 100:
                        f += 1
            if f > 414:
                return 0
            else:
                return 1
        for i in range(8):
            for j in range(4):
                if s((i + 1), (j+1)) == 1:
                    if rt == 1:
                        bt[i] = j + 1
                    elif rt == 0:
                        df[i] = j + 1
                    elif rt == 2:
                        rc[i] = j + 1
        if rt == 2:
            return rc

    def eer():
        global bt
        print("- Preview with some changes :")
        for i in range(len(bt)):
            print("  "+str(i+1)+"."+str(bt[i]))

    def bdd():
        u = glob.glob(".psnj/*.psnj")
        print("- "+str(len(u))+" Saved Teskeys We Found :")
        for i in range(len(u)):
            print("  " + u[i])

    def x(o):
        global c, z, e
        c = input("> ")
        t = 0
        r = 0
        for i in range(len(o)):
            if c == o[i] or c == o[i] + " ":
                r = 1
                z = i
            elif c.startswith(o[i] + " "):
                t = 1
                z = i
                e = c[len(o[i]) + 1:]

        if t == 0:
            if r == 0:
                print("- Command is not allowed !")
                print("  Try another command")
            else:
                print("- \""+o[z]+"\" is an allowed command !")
                print("  Please type input of that too !")
            x(o)

    print("- Welcome to PySanj :")
    print("  Open exam file by \"open + filename\"")
    print("  Or open exam folder by \"fopen + foldername\"")
    print("  Only .jpg files allowed for exam file")
    print("  So use \"open\" command without file extension")
    x(["fopen", "open"])
    while z == 0 and not os.path.exists(e):
        print("- There is no folder with this path !")
        print("  Try Another Path")
        x(["fopen", "open"])
    while z == 1 and not os.path.exists(e + ".jpg"):
        print("- There is no file with this path !")
        if c.endswith(".jpg"):
            print("  This may be a problem with using the file extension")
        print("  Try Another Path")
        x(["fopen", "open"])
    if z == 0:
        m = e
        print("- \""+m+"\" selected successfully")
        ere = []
        print("- " + str(len(glob.glob(m+"/*.jpg", recursive=True))) +
              " Exam Files Found :")
        for er in glob.glob(m+"/*.jpg", recursive=True):
            print("  " + er.replace('\\', '/'))
            ere.append(a(er.replace('\\', '/'), 2))
        print("  Type \"corr + testkeyname\" to start correction by saved tests")
        print("  Or type \"fcorr + testkey location\" to start correction by file")
        print("  You can see avaiable testkeys by \"tklist show\"")
        x(["corr", "fcorr", "tklist"])
        while z == 0 and not os.path.exists(".psnj/"+e+".psnj"):
            print("- Testkey with this name not found!")
            if c.endswith(".psnj"):
                print("  This may be a problem with using the file extension")
            x(["save", "corr", "fcorr", "tklist"])
        while z == 1 and not os.path.exists(e+".jpg"):
            print("- Exam File with this name not found!")
            if c.endswith(".jpg"):
                print("  This may be a problem with using the file extension")
            x(["save", "corr", "fcorr", "tklist"])
        if z == 2:
            sd()
            bdd()
            ud()
        if z == 0:
            rty = open('.psnj/'+e+".psnj",
                       'r').read().replace('[', '').replace(']', '').split(', ')
            for j in range(len(ere)):
                no = 8
                for i in range(8):
                    if ere[j][i] != int(rty[i]):
                        if ere[j][i] == 0:
                            no -= 1
                        else:
                            no -= 1.25
                print("- (" + str(j + 1) + ") Result : " + str(no))
            ud()
        if z == 1:
            a(e+".jpg", 0)
            for j in range(len(ere)):
                no = 8
                for i in range(8):
                    if ere[j][i] != int(bt[i]):
                        if ere[j][i] == 0:
                            no -= 1
                        else:
                            no -= 1.25
                print("- (" + str(j) + ") Result : " + str(no))
            ud()
    else:
        m = e
        print("- \""+m+".jpg\" selected successfully !")
        a(e+".jpg", 1)
        eer()
        print("  Type \"save + testkey\" to save it as a test key")
        print("  Or type \"corr + testkeyname\" to start correction by saved tests")
        print("  Or type \"fcorr + testkey location\" to start correction by file")
        print("  You can see avaiable testkeys by \"tklist show\"")
        x(["save", "corr", "fcorr", "tklist"])
        while z == 0 and os.path.exists(".psnj/"+e+".psnj"):
            print("- Testkey with this name already exits")
            x(["save", "corr", "fcorr", "tklist"])
        while z == 1 and not os.path.exists(".psnj/"+e+".psnj"):
            print("- Testkey with this name not found!")
            if c.endswith(".psnj"):
                print("  This may be a problem with using the file extension")
            x(["save", "corr", "fcorr", "tklist"])
        while z == 2 and not os.path.exists(e+".jpg"):
            print("- Exam File with this name not found!")
            if c.endswith(".jpg"):
                print("  This may be a problem with using the file extension")
            x(["save", "corr", "fcorr", "tklist"])
        if z == 0:
            sd()
            open(".psnj/"+e+".psnj", "w").write(str(bt))
            print("- saved successfully")
            ud()
        if z == 3:
            sd()
            bdd()
            ud()
        if z == 1:
            rty = open('.psnj/'+e+".psnj",
                       'r').read().replace('[', '').replace(']', '').split(', ')
            no = 8
            for i in range(8):
                if bt[i] != int(rty[i]):
                    if bt[i] == 0:
                        no -= 1
                    else:
                        no -= 1.25

                print("  "+str(i + 1)+"."+str(bt[i])+":"+str(rty[i]))
            print("- Final Result : " + str(no))
            ud()
        if z == 2:
            a(e+".jpg", 0)
            no = 8
            for i in range(8):
                if bt[i] != df[i]:
                    if bt[i] == 0:
                        no -= 1
                    else:
                        no -= 1.25

                print("  "+str(i + 1)+"."+str(bt[i])+":"+str(df[i]))
            print("- Final Result : " + str(no))
            ud()
ud()
