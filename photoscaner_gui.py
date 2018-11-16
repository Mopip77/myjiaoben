import tkinter as tk
import pyautogui as pag
import os

from PIL import ImageGrab
from photoscaner import PhotoScaner


class PSWin(PhotoScaner):
    """
    PhotoScaner Window 候选提示窗
    """
    tmp_pic_path = '1.jpg'

    def __init__(self):
        # mouse position
        self.m_x, self.m_y = pag.position()

        self.window = tk.Tk()
        self.window.title('PhotoScaner')
        self.window.geometry('150x231+{}+{}'.format(self.m_x, self.m_y))

        if self.__get_clipboard() is True:
            super(PSWin, self).__init__(PSWin.tmp_pic_path)

    """
    原本设想用win32中的方法，结果获取的图片是DIB格式，缺少图片格式头，现改用PIL将图片保存再打开的方式
    """

    # 读取剪贴板图片
    # def __get_clipboard(self):
    #     win32clipboard.OpenClipboard()
    #     # 剪贴板是图片
    #     try:
    #         img_byte = win32clipboard.GetClipboardData(win32con.CF_DIB)
    #         win32clipboard.CloseClipboard()
    #         self.img = img_byte
    #         return True
    #     except TypeError:
    #         self.text = tk.Text(self.window, font=("微软雅黑 15"))
    #         self.text.pack()
    #         self.text.insert(tk.INSERT, '当前剪贴板不是图片')
    #         return False

    def __get_clipboard(self):
        """
        读取剪贴板的图片，保存下来，名字为 PSWin.tmp_pic_path 的值
        """
        try:
            im = ImageGrab.grabclipboard()
            im.save(PSWin.tmp_pic_path)
            return True
        # 剪贴板不是图片
        except AttributeError:
            self.text = tk.Text(self.window, font=("微软雅黑 15"))
            self.text.pack()
            self.text.insert(tk.INSERT, '当前剪贴板不是图片')
            return False

    def __update_window_after_click(self, msg):
        self.lb1.pack_forget()
        self.b1.pack_forget()
        self.b2.pack_forget()
        self.b3.pack_forget()
        self.text = tk.Text(self.window, font=("微软雅黑 15"))
        self.text.pack()
        self.text.insert(tk.INSERT, msg)
        # 将保存的图片删了
        os.remove(PSWin.tmp_pic_path)

    def call_img_ocr(self):
        msg = self.img_ocr()
        self.__update_window_after_click(msg)

    def call_img_to_base64(self):
        msg = self.img_to_base64()
        self.__update_window_after_click(msg)

    def call_upload_to_img_bank(self):
        msg = self.upload_to_img_bank()
        msg = msg['data']
        self.window.geometry('650x300+{}+{}'.format(self.m_x, self.m_y))
        self.__update_window_after_click(msg)

    def run(self):

        if not self.__get_clipboard():
            pass
        else:
            self.lb1 = tk.Label(
                self.window,
                text='使用剪贴板的图片,  \n结果保存到剪贴板 ',
                font=('微软雅黑 12'),
                bg='yellow',
                height=2,
            )

            self.b1 = tk.Button(
                self.window,
                text='OCR',
                font=('微软雅黑 12 bold'),
                width=20,
                height=2,
                command=self.call_img_ocr)

            self.b2 = tk.Button(
                self.window,
                text='base64',
                font=('微软雅黑 12 bold'),
                width=20,
                height=2,
                command=self.call_img_to_base64)

            self.b3 = tk.Button(
                self.window,
                text='图床',
                font=('微软雅黑 12 bold'),
                width=20,
                height=2,
                command=self.call_upload_to_img_bank)

            self.lb1.pack()
            self.b1.pack()
            self.b2.pack()
            self.b3.pack()

        self.window.mainloop()


if __name__ == "__main__":
    w = PSWin()
    w.run()
