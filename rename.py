#-*- coding:utf-8
import os
import sys
import codecs
import string

def load_file(name):
    """载入配置"""
    f = open(name, 'r')
    dic = {}
    for line in f.readlines():
        key= line.split(',')
        key[0] = key[0].strip().lstrip().rstrip(' ')
        key[1] = key[1].strip().lstrip().rstrip(' ')
        dic[key[0]] = key[1]
    f.close()
    return dic
    
def batch_rename(cfgname):
    #得到所有配置文件中的内容
    des_dic = load_file(cfgname)
    print(des_dic)
    
    #获得当前文件下的所有文件
    src_list = os.listdir('./')
    print(src_list)
    
    #获得当前路径
    path = os.getcwd()
    print('current path --'+path)
    
    #改名
    for name in src_list:
        new_name = des_dic.get(name)
        if new_name != None:
            os.rename(os.path.join(path,name),os.path.join(path,new_name))
            print(name + '-->'+ new_name + finish)
        else:
            print(name + ' not rename!')

if __name__=='__main__':
    batch_rename('./config.cfg')