import tkinter as tk

#创建主窗口
root = tk.Tk()
#设置标题
root.title("hello tk")
#设置标签和他的边距
label=tk.Label(root, text="hello world")
label.pack(padx=10, pady=10)
#设置按钮,按钮文字,命令.设置垂直边距
button=tk.Button(root, text="click me", command=lambda:print("button clicked"))
button.pack(pady=10)













#开启窗口循环(不开启看不见窗口)
root.mainloop()