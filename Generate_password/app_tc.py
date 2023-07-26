
# 引入所需模塊
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont

# 生成密碼的函數
def generate_passwoed():
    # 從輸入欄位獲取所需的密碼長度和字符類型
    length_str = entry_length.get()
    upper = bool_var_upper.get()
    lower = bool_var_lower.get()
    digits = bool_var_digits.get()
    symbols = bool_var_symbols.get()
    
    # 將密碼長度從字串轉換為整數
    length = int(length_str)

    # 根據用戶選擇的字符類型創建字符集
    characters = ""
    if upper:
        characters += string.ascii_uppercase  # 添加大寫字母
    if lower:
        characters += string.ascii_lowercase  # 添加小寫字母
    if digits:
        characters += string.digits  # 添加數字
    if symbols:
        characters += string.punctuation  # 添加符號

    # 如果字符集為空（即用戶沒有選擇任何字符類型），則顯示錯誤消息並返回
    if characters == "":
        messagebox.showerror("Error", "You must select at least one type of characters.")
        return

    # 生成並顯示密碼
    password = "".join(random.choice(characters) for _ in range(length))  # 生成密碼
    password_str.set(password)  # 將密碼顯示在GUI上

# 複製密碼到剪貼板的函數
def copy_password():
    # 清空剪貼板，然後添加新密碼
    window.clipboard_clear()
    window.clipboard_append(password_str.get())

# 創建GUI窗口
window = Tk()
window.title("Password Generator")  # 設置窗口標題
window.geometry("1000x340")  # 設置窗口大小
window.resizable(False, False)  # 禁止調整窗口大小
window.config(bg = "black")  # 設置窗口背景顏色

# 獲取屏幕寬度和高度，並計算出窗口的中心位置
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int((screen_width / 2) - (1000 / 2))
center_y = int((screen_height / 2) - (340 / 2))

# 將窗口移動到中心位置
window.geometry("+{}+{}".format(center_x, center_y))

# 設置字體樣式
fontStyle = tkFont.Font(family = "Arial", size = 20)

# 創建並配置各種控件，如標籤、輸入欄位、復選框和按鈕
Label(window, text = "Password length:",
      font = fontStyle,
      bg = "black").grid(row = 0,
                         column = 0,
                         sticky = W,
                         padx = 10,
                         pady = 10)
entry_length = Scale(window, 
                     from_ = 1, 
                     to = 100, 
                     orient = HORIZONTAL,
                     width = 20,
                     length = 800)
entry_length.grid(row = 0,
                  column = 1,
                  sticky = W,
                  padx = 10,
                  pady = 10)

bool_var_upper = BooleanVar()
Checkbutton(window, text = "Include uppercase letters",
            variable = bool_var_upper,
            font = fontStyle,
            bg = "black").grid(row = 1,
                               column = 0,
                               columnspan = 2,
                               sticky = W,
                               padx = 10)

bool_var_lower = BooleanVar()
Checkbutton(window, text="Include lowercase letters",
            variable = bool_var_lower,
            font = fontStyle,
            bg = "black").grid(row = 2,
                               column = 0,
                               columnspan = 2,
                               sticky = W,
                               padx = 10)

bool_var_symbols = BooleanVar()
Checkbutton(window, text="Include symbols",
            variable = bool_var_symbols,
            font = fontStyle,
            bg = "black").grid(row = 3,
                               column = 0,
                               columnspan = 2,
                               sticky = W,
                               padx = 10)

bool_var_digits = BooleanVar()
Checkbutton(window, text="Include digits",
            variable = bool_var_digits,
            font = fontStyle,
            bg = "black").grid(row = 4,
                               column = 0,
                               columnspan = 2,
                               sticky = W,
                               padx = 10)

Button(window, text = "Generate password",
       command = generate_passwoed,
       font = fontStyle).grid(row = 5,
                            column = 0,
                            columnspan = 2,
                            padx = 10,
                            pady = 10)

password_str = StringVar()
Label(window, textvariable = password_str,
      font = tkFont.Font(family = "Arial", size = 14),
      bg = "black").grid(row = 6,
                         column = 0,
                         columnspan = 2,
                         padx = 10,
                         pady = 10)

Button(window, text = "Copy",
       command = copy_password,
       font = fontStyle,
       bg = "black").grid(row = 7,
                               column = 0,
                               columnspan = 2,
                               padx = 10,
                               pady = 10)

# 啟動GUI主循環
window.mainloop()
