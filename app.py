import tkinter as tk
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class BlindBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("抽盲盒")
        
        # 设置窗口大小和位置
        self.root.geometry("300x200")
        
        # 创建抽盲盒按钮
        self.draw_button = tk.Button(root, text="抽盲盒啦", command=self.draw_blind_box)
        self.draw_button.pack(pady=50)
        
        # 创建结果显示标签
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()
        
    def draw_blind_box(self):
        # 随机选择角色
        characters = ["基德", "小兰"]
        result = random.choice(characters)
        
        # 显示结果
        self.result_label.config(text=f"恭喜你抽到了：{result}")
        
        # 发送邮件
        self.send_email(result)
    
    def send_email(self, result):
        # 邮件服务器配置
        smtp_server = "smtp.qq.com"
        sender = "452285059@qq.com"  # 需要替换成你的QQ邮箱
        password = "sanlxlfxljhnbgca"  # 需要替换成你的QQ邮箱授权码
        receiver = "452285059@qq.com"
        
        # 构建邮件内容
        message = MIMEText(f"抽盲盒结果：{result}", "plain", "utf-8")
        message["Subject"] = Header("抽盲盒结果通知", "utf-8")
        message["From"] = sender
        message["To"] = receiver
        
        try:
            # 连接服务器并发送邮件
            server = smtplib.SMTP_SSL(smtp_server, 465)
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            server.quit()
            print("邮件发送成功！")
        except Exception as e:
            print(f"邮件发送失败：{str(e)}")

# 创建并运行应用
if __name__ == "__main__":
    root = tk.Tk()
    app = BlindBoxApp(root)
    root.mainloop()
