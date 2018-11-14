import argparse
import base64
import json
import requests
import win32clipboard

from my_info import APP_ID, API_KEY, SECRET_KEY
from aip import AipOcr
from babun_path_converter import babun_path_convert

# 当前在babun环境下，开启路径转换
IS_BABUN_ENV = True


class PhotoScaner(object):
    """
    将图片OCR, 转base64, 上传到图床
    """
    def __init__(self, filepath):
        self.filePath = filepath
        self.img = self.get_file_content(filepath)

    def get_file_content(self, filepath):
        with open(filepath, 'rb') as f:
            return f.read()

    def img_ocr(self):
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        result = client.basicGeneral(self.img)
        text_line = result['words_result']
        res = ''
        for line in text_line:
            res += (line['words'])  # + '\n')
        msg = "OCR result:\n{}\n".format(res)
        self.set_clipboard(res)
        return msg

    def img_to_base64(self):
        msg = "base64 result:\n{}\n".format(base64.b64encode(self.img))
        self.set_clipboard(msg)
        return msg

    def upload_to_img_bank(self):
        # sm.ms
        # upload
        url = 'https://sm.ms/api/upload'

        # 好像全路径的上传会失败，只保留文件名上传
        simple_file_name = self.filePath.split('\\')[-1]

        files = {
            "smfile": (simple_file_name, self.img, "image/jpeg"),
        }

        res = requests.post(url, files=files)
        doc = json.loads(res.text)

        reply_data = {
            'status': '',
            'data': '',
        }

        # parse response
        if doc['code'] == 'error':
            reply_data['status'] = 'error'
            reply_data['data'] = "upload to Photo bank...\n" +\
                                 "Photo is FAIL to upload...\n" +\
                                 "Failure type:{}\n".format(doc['msg'])

        else:
            doc = doc['data']
            img_url = doc['url']
            img_fileName = doc['filename']
            md = "![{}]({})".format(img_fileName, img_url)

            self.set_clipboard(md)

            reply_data['status'] = 'ok'
            reply_data['data'] = "upload to Photo bank...\n" +\
                                 "Photo has been upload successfully...\n\n" +\
                                 "url:  {}\nmd :  {}\n".format(img_url, md)
        return reply_data

    # 设置剪贴板
    def set_clipboard(self, sourceStr):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(sourceStr)
        win32clipboard.CloseClipboard()


def main():
    parser = argparse.ArgumentParser()
    """
    method = [o, b, u]
    o -> image ocr
    b -> iamge to base64
    u -> upload iamge to image bank(only 'sm.ms' now)
    """
    parser.add_argument("method", help="use which method")
    parser.add_argument("filepath", help="the target photo path")
    args = parser.parse_args()

    try:
        if IS_BABUN_ENV:
            fp = babun_path_convert(args.filepath)
        else:
            fp = args.filepath

        ps = PhotoScaner(fp)

        if args.method == 'o':
            print(ps.img_ocr())
            print('ocr result has been set to clipboard...')

        elif args.method == 'b':
            print(ps.img_to_base64())
            print('base64 code has been set to clipboard...')

        elif args.method == 'u':
            rep = ps.upload_to_img_bank()
            print(rep['data'])
            if rep['status'] == 'ok':
                print('markdown text has been set to clipboard...')
        else:
            print('use -h for help')
    except Exception as e:
        print('catch exception:{}'.format(e))


if __name__ == "__main__":
    main()
