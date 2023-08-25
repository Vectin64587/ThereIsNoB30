import tkinter as tk
from tkinter import filedialog
import b30_reader,b30_generator,ast,SongInfoCon

selected = False
global st3file

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        text_box.delete(1.0, tk.END)  # 清空文本框
        st3file = file_path
        text_box.insert(tk.END, file_path)
        b30_reader.st3file = file_path
        
def show_help():
    print("Help")

def complete():
    print(b30_reader.start(b30_reader.st3file))
    modify_text(b30_reader.start(b30_reader.st3file))

def modify_text(new_ptt):
    ptt_output.config(state="normal")  # 将状态设置为可编辑
    ptt_output.delete("1.0", "end")     # 删除原有内容
    ptt_output.insert("1.0", new_ptt)  # 插入新内容
    ptt_output.config(state="disabled")

def generate():
    with open("all_song.txt", 'r') as f:
        content = f.read()
    new_content = ast.literal_eval(content)
    with open("new_all_song.txt", 'w') as f:
        f.write(str(SongInfoCon.b30_generate(new_content)))
        #print(SongInfoCon.b30_generate(new_content))

    with open("new_all_song.txt","r") as file:
        content = file.read()
        # print(ast.literal_eval(content))
        data_dict = ast.literal_eval(content)
    b30_generator.generate_image(data_dict)

# 创建主窗口
root = tk.Tk()
root.title("B30 Generator")

# 创建按钮并使用 grid() 放在左边
button_select = tk.Button(root, text="选择st3", command=open_file_dialog)
button_help = tk.Button(root, text="?", command=show_help)
button_generate = tk.Button(root, text="生成b30成绩图", command=generate)
button_select.grid(row=0, column=0, padx=10, pady=10)
button_help.grid(row=0, column=1, padx=10, pady=10)
button_generate.grid(row=1, column=3, padx=10, pady=10)

#创建文本控件
ptt_output = tk.Text(root, height=1, width=40)
ptt_output.insert(3.5,"Ptt")
ptt_output.configure(state="disabled")
ptt_output.grid(row=2, columnspan=3, padx=5, pady=5)

# 创建文本框放在按钮的右边
text_box = tk.Text(root, height=1, width=40)
text_box.grid(row=0, column=2, padx=10, pady=10)

# 创建一个完成按钮
button_complete = tk.Button(root, text="Complete",command = complete)
button_complete.grid(row=1, columnspan=3, padx=10, pady=10)

# 运行主循环
root.mainloop()