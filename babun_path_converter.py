"""
windows下babun挂载后路径不能用，所以做一个路径转换
"""
import os

from my_info import ROOT_PATH


def babun_path_convert(path):
    folders = path.split('/')[1:]
    # split后啥都没了，所以是当前路径下的图片
    if len(folders) == 0:
        return os.getcwd() + '\\' + path

    result = ''

    # 两种情况
    # 1.cygdrive开头，被挂载的磁盘
    if folders[0] == 'cygdrive':
        f_i = 0
        for f in folders:
            f_i += 1
            if f_i == 1:
                continue
            elif f_i == 2:
                result += '{}:\\'.format(f.upper())
            else:
                result += '{}\\'.format(f)
    
    # 2.在babun路径下
    else:
        result = ROOT_PATH
        for f in folders:
            result += '{}\\'.format(f)
            
    # 去掉最后一个 '\'
    return result[:-1]


if __name__ == "__main__":
    a = babun_path_convert('2.jpg')
    print(a)

