import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import urllib.request
import ssl

# 定义文件分类规则
RULES = {
    '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'],
    '文档': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
    '压缩包': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '音频': ['.mp3', '.wav', '.flac', '.aac'],
    '视频': ['.mp4', '.avi', '.mkv', '.mov', '.flv'],
    '代码': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.php', '.go', '.rs'],
}

# 项目信息
AUTHOR = 'com-in'
LICENSE = 'GPL-v3'
PROJECT_URL = 'https://github.com/com-in/AutoFilesOrganizer'
VERSION = 'v1.0.0'
UPDATE_LOG = """v1.0.0 (2026-02-28)
- 初始版本发布
- 实现文件分类整理功能
- 支持多种文件类型分类
- 添加图形用户界面
- 支持自定义整理路径和输出路径
"""

def organize_folder(source_path, output_path):
    """整理指定目录下的文件到输出目录"""
    for item in os.listdir(source_path):
        item_path = os.path.join(source_path, item)
        
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            
            moved = False
            for category, extensions in RULES.items():
                if ext in extensions:
                    target_dir = os.path.join(output_path, category)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(item_path, os.path.join(target_dir, item))
                    print(f'移动文件: {item} -> {category}/')
                    moved = True
                    break
            
            if not moved:
                other_dir = os.path.join(output_path, '其他')
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(item_path, os.path.join(other_dir, item))
                print(f'移动文件: {item} -> 其他/')

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('文件整理工具')
        self.root.geometry('500x400')
        self.root.resizable(False, False)
        
        self.source_path = tk.StringVar()
        self.output_path = tk.StringVar()
        
        self.create_main_menu()
    
    def create_main_menu(self):
        """创建主菜单界面"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill='both')
        
        # 标题
        tk.Label(frame, text='AutoFilesOrganizer', font=('Arial', 20, 'bold')).pack(pady=20)
        tk.Label(frame, text=f'版本: {VERSION}', font=('Arial', 10)).pack()
        
        # 按钮区域
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text='整理文件', font=('Arial', 12), width=15, height=2,
                  command=self.show_organize_page).pack(pady=5)
        tk.Button(btn_frame, text='关于', font=('Arial', 12), width=15,
                  command=self.show_about_page).pack(pady=5)
        tk.Button(btn_frame, text='退出', font=('Arial', 12), width=15,
                  command=self.root.quit).pack(pady=5)
        
        # 底部信息
        tk.Label(frame, text=f'© {AUTHOR} | {LICENSE}', font=('Arial', 9)).pack(side='bottom')
    
    def show_organize_page(self):
        """显示整理页面"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill='both')
        
        tk.Label(frame, text='文件整理', font=('Arial', 16, 'bold')).pack(pady=10)
        
        # 整理路径
        tk.Label(frame, text='整理路径:', font=('Arial', 11)).pack(anchor='w')
        path_frame = tk.Frame(frame)
        path_frame.pack(fill='x', pady=5)
        tk.Entry(path_frame, textvariable=self.source_path).pack(side='left', fill='x', expand=True, padx=(0, 5))
        tk.Button(path_frame, text='浏览', command=self.browse_source).pack(side='right')
        
        # 输出路径
        tk.Label(frame, text='输出路径:', font=('Arial', 11)).pack(anchor='w')
        out_frame = tk.Frame(frame)
        out_frame.pack(fill='x', pady=5)
        tk.Entry(out_frame, textvariable=self.output_path).pack(side='left', fill='x', expand=True, padx=(0, 5))
        tk.Button(out_frame, text='浏览', command=self.browse_output).pack(side='right')
        
        tk.Label(frame, text='提示: 路径为空时使用默认路径', font=('Arial', 9), fg='gray').pack(pady=10)
        
        # 按钮
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text='开始整理', font=('Arial', 11), width=12,
                  command=self.start_organize).pack(side='left', padx=5)
        tk.Button(btn_frame, text='返回', font=('Arial', 11), width=12,
                  command=self.create_main_menu).pack(side='left', padx=5)
    
    def show_about_page(self):
        """显示关于页面"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill='both')
        
        tk.Label(frame, text='关于软件', font=('Arial', 16, 'bold')).pack(pady=10)
        
        tk.Label(frame, text=f'作者: {AUTHOR}').pack(pady=2)
        tk.Label(frame, text=f'版本: {VERSION}').pack(pady=2)
        tk.Label(frame, text=f'许可证: {LICENSE}').pack(pady=2)
        
        link = tk.Label(frame, text=PROJECT_URL, fg='blue', cursor='hand2')
        link.pack(pady=2)
        link.bind('<Button-1>', lambda e: webbrowser.open(PROJECT_URL))
        
        tk.Label(frame, text='更新日志:', font=('Arial', 11, 'bold')).pack(anchor='w', pady=10)
        
        log = tk.Text(frame, height=6, width=50)
        log.pack()
        log.insert('1.0', UPDATE_LOG)
        log.config(state='disabled')
        
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text='检查更新', font=('Arial', 10), width=10,
                  command=self.check_update).pack(side='left', padx=5)
        tk.Button(btn_frame, text='返回', font=('Arial', 10), width=10,
                  command=self.create_main_menu).pack(side='left', padx=5)
    
    def browse_source(self):
        """选择整理路径"""
        path = filedialog.askdirectory(title='选择要整理的文件夹')
        if path:
            self.source_path.set(path)
    
    def browse_output(self):
        """选择输出路径"""
        path = filedialog.askdirectory(title='选择输出文件夹')
        if path:
            self.output_path.set(path)
    
    def check_update(self):
        """检查更新"""
        try:
            # 创建SSL上下文，忽略证书验证
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            # 请求服务器获取最新版本
            req = urllib.request.Request(
                'https://afo.acmcdev.top/version.html',
                headers={'User-Agent': 'AutoFilesOrganizer'}
            )
            
            with urllib.request.urlopen(req, context=ssl_context, timeout=5) as response:
                latest_version = response.read().decode('utf-8').strip()
            
            # 比较版本
            if latest_version != VERSION:
                result = messagebox.askyesno(
                    '发现新版本',
                    f'当前版本: {VERSION}\n'
                    f'最新版本: {latest_version}\n\n'
                    f'发现新版本，是否前往下载页面？'
                )
                if result:
                    webbrowser.open(PROJECT_URL)
            else:
                messagebox.showinfo('检查更新', f'当前版本: {VERSION}\n\n已是最新版本！')
                
        except Exception as e:
            messagebox.showerror('检查更新失败', f'无法连接到更新服务器\n\n请检查网络连接或访问:\n{PROJECT_URL}')
    
    def start_organize(self):
        """开始整理"""
        source = self.source_path.get().strip()
        output = self.output_path.get().strip()
        
        if not source:
            source = os.getcwd()
        
        if not output:
            output = os.path.join(source, 'after')
        
        if not os.path.exists(source):
            messagebox.showerror('错误', f'整理路径不存在: {source}')
            return
        
        if not os.path.exists(output):
            os.makedirs(output, exist_ok=True)
        
        try:
            organize_folder(source, output)
            messagebox.showinfo('完成', f'文件整理完成！\n\n整理路径: {source}\n输出路径: {output}')
        except Exception as e:
            messagebox.showerror('错误', f'整理过程中出错: {str(e)}')

if __name__ == '__main__':
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
