# 導入所需的庫
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

# 定義圖像轉換應用的類
class ImageConverter:
    def __init__(self, root):
        # 初始化實例變量
        self.image_files = []  # 存放選擇的圖像文件的列表
        self.root = root  # tkinter根窗口

        # 設定根窗口的屬性
        self.root.title('圖像轉換器')
        self.root.geometry('500x650')

        # 創建GUI控件
        self.create_widgets()
        self.root.resizable(False, False)

    # 創建GUI控件的方法
    def create_widgets(self):
        # 創建一個框架來存放控件
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # 創建一個用於選擇圖像的按鈕
        self.select_files_button = ttk.Button(frame, text="選擇圖像", command=self.select_files)
        self.select_files_button.pack(pady=10)

        # 創建一個列表框以顯示選擇的圖像文件
        self.listbox = tk.Listbox(frame, width=50, height=20)
        self.listbox.pack(pady=10)

        # 創建一個按鈕用於移除選定的圖像
        self.remove_button = ttk.Button(frame, text="移除選定", command=self.remove_selected)
        self.remove_button.pack(pady=10)

        # 創建一個標籤用於選擇輸出格式
        self.label = ttk.Label(frame, text="輸出格式：")
        self.label.pack(pady=10)

        # 創建一個變量用於保存選定的輸出格式
        self.format_var = tk.StringVar()
        self.format_var.set('jpeg')

        # 創建一個下拉菜單用於選擇輸出格式
        self.option_menu = ttk.OptionMenu(frame, self.format_var, 'jpeg', 'png', 'webp', 'jpeg')
        self.option_menu.pack(pady=10)

        # 創建一個按鈕用於開始轉換
        self.convert_button = ttk.Button(frame, text="轉換", command=self.convert_images)
        self.convert_button.pack(pady=10)

    # 選擇圖像文件的方法
    def select_files(self):
        # 打開文件對話框選擇圖像文件
        files = filedialog.askopenfilenames(filetypes=[('圖像文件', '*.png'), ('圖像文件', '*.jpg'), ('圖像文件', '*.webp'), ('圖像文件', '*.jpeg')])
        # 將選定的文件添加到列表中
        self.image_files.extend(files)
        # 更新列表框
        self.update_listbox()

    # 更新列表框的方法
    def update_listbox(self):
        # 刪除列表框中的所有現有項
        self.listbox.delete(0, tk.END)
        # 將當前的圖像文件添加到列表框中
        for file in self.image_files:
            self.listbox.insert(tk.END, os.path.basename(file))

    # 移除選定文件的方法
    def remove_selected(self):
        # 獲取選定的列表框項的索引
        selected_indices = self.listbox.curselection()
        # 從圖像文件列表中移除選定的項
        for index in selected_indices[::-1]:
            del self.image_files[index]
        # 更新列表框
        self.update_listbox()

    # 轉換圖像的方法
    def convert_images(self):
        # 獲取選定的輸出格式
        target_format = self.format_var.get()
        # 請用戶選擇一個輸出目錄
        output_dir = filedialog.askdirectory()
        output_dir = os.path.join(output_dir, '輸出圖像')
        # 如果輸出目錄不存在，則創建它
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 轉換每個圖像文件
        for file in self.image_files:
            # 打開圖像文件
            img = Image.open(file).convert("RGB")
            # 獲取不帶擴展名的文件名
            root, ext = os.path.splitext(os.path.basename(file))
            # 以新格式保存圖像
            img.save(os.path.join(output_dir, f"{root}.{target_format}"), target_format)

        # 顯示一個消息框表示轉換成功
        messagebox.showinfo("轉換成功", f"圖像已轉換為 {target_format} 格式！")
        # 打開輸出目錄
        subprocess.call(["open", output_dir])

# 運行應用
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverter(root)
    root.mainloop()