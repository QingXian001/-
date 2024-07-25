import tkinter as tk
from tkinter import messagebox  
#function
def p():
    e_passwd=entry_passwd.get()
    e_tlim=entry_tlim.get()
    print(e_passwd,e_tlim)

def dis():
    tk.messagebox.showinfo('关不掉的','关不掉我吧!哈哈哈哈!\n没有办法,就是这么强大!\n啦啦啦啦啦啦啦啦啦啦')

#窗口
root=tk.Tk()
root.title('time-limit')
root.geometry('9999x9999')
#标签
label_welcome=tk.Label(root,text='hello 小孩!')
label_welcome.place(x=2,y=2)
label_passwd=tk.Label(root,text='密码:')
label_passwd.place(x=2,y=50)
label_tlim=tk.Label(root,text='计时时间:')
label_tlim.place(x=2,y=100)
#输入框
entry_passwd=tk.Entry(root)
entry_passwd.place(x=80,y=50)
entry_tlim=tk.Entry(root)
entry_tlim.place(x=80,y=100)
#按钮
button_passwd=tk.Button(root,text='确定',command=p)
button_passwd.pack(padx=120,pady=150)
button_break=tk.Button(root,text='退出',command=root.destroy)
button_break.place(x=50,y=150)

#额外设置
# 设置窗口置顶
root.attributes('-topmost', True)
#禁用最大最小化
root.resizable(False,False)
#设置窗口透明度
root.attributes('-alpha', 0.5)
# 禁用关闭按钮（窗口右上角的关闭按钮）


root.protocol("WM_DELETE_WINDOW", dis)
#主循环
root.mainloop()