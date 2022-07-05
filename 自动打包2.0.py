
import os
import tkinter as tk
from pathlib import Path
from tkinter import filedialog as fd
from tkinter import messagebox

window = tk.Tk()  #初始化
window.title("自动打包") #设置标题。
window.geometry("330x200")
file = ''
图标_=''
def i():
    return os.path.join(os.path.expanduser('~'),"Desktop")
file1=i()
file1 = file1.rstrip()
e_file = tk.Entry(window)
w_file = tk.Entry(window)
label_pixel= tk.Label(window, text='选择打包类型')
def mkdir(path):
    isExists=os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        print (path+' 创建成功')
def askfile():
    global file
    file = fd.askopenfilename()
    e_file.delete(0,'end')
    e_file.insert(0,file)
def askfile1():
    global file1
    file1 = fd.askdirectory()
def askfile2():
    global 图标_
    图标_ = fd.askopenfilename()
    w_file.delete(0,'end')
    w_file.insert(0,file)
def djalk():
    ttt=list_color.selection_get()
    os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller')
    file2=file1+'/exe文件所在地'
    mkdir(file2)
    if ttt=='有图标，隐藏界面':
        os.chdir(file2)
        os.system(f'pyinstaller -F -w -i{图标_} {file}')
    elif ttt=='有图标':
        os.chdir(file2)
        os.system(f'pyinstaller -F -i{图标_} {file}')
    elif ttt=='隐藏界面':
        os.chdir(file2)
        os.system(f'pyinstaller -F -w  {file}')
    elif ttt=='没有图标也不隐藏界面':
        os.chdir(file2)
        os.system(f'pyinstaller -F {file}')
def gg():
    messagebox.showinfo('使用须知',"""                   \t 自动打包器
      使用须知:
\t2.0版本自动pip pyinstaller!!!!!
\tpip uninstall pyinstaller 可以用这个卸载pyinstaller试一试。
\t保存在 D:/要改自己改。
\t打包完成后然后会出现两个文件夹: 'build','dist'
\texe文件保存在'dist'当中。
\t需要等一个大约120秒。
\t请不要看到未响应就把它关了。
\t喜欢这东西那下次上课的时候多夸我几次。！！！！！！！！！！！！！！！！！
""")
b1 = tk.Button(window, text='点击开始转换',command=djalk)
b2 = tk.Button(window, text='使用须知',command=gg)
Picture_location = tk.Button(window,text="选择py文件位置",command=askfile,cursor='hand2')
Picture_location2 = tk.Button(window,text=r"更改保存位置(默认是D:\)",command=askfile1,cursor='hand2')
Filter = tk.Button(window,text="选择图标位置",command=askfile2,cursor='hand2')
list_color = tk.Listbox(window,  height=4)
list_color.insert('end', '有图标，隐藏界面')
list_color.insert('end', '有图标')
list_color.insert('end', '隐藏界面')
list_color.insert('end', '没有图标也不隐藏界面')
Picture_location.grid(row=0,column=0,pady=5,padx=10)
e_file.grid(row=1,column=0,pady=5,padx=10)
Filter.grid(row=2,column=0,pady=5,padx=10)
w_file.grid(row=3,column=0,pady=5,padx=10)
label_pixel.grid(row=0,column=1)
Picture_location2.grid(row=3,column=1)
list_color.grid(row=1,column=1,rowspan=2,pady=5,padx=10)
b1.grid(row=5,column=1,pady=5,padx=10)
b2.grid(row=5,column=0,pady=5,padx=10)
window.mainloop()
#

