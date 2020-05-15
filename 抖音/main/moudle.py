import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import download,chrome_path,Key_text

class OpenTxt:
    '''
    便捷读写,记得close
    '''
    f = None
    def __init__(self,file_path=Key_text,mode='r',encoding='utf-8'):
        self.f = open(file_path,mode,encoding=encoding)
    def read(self):
        '''
        :return:
        '''
        return self.f.read()
    def read_list(self):
        '''
        :return:
        '''
        return self.f.readlines()
    def read_set(self):
        '''
        :return: 将配置url去重后返回
        '''
        l  = []
        for i in self.f.readlines():
            i = i.split()[0]
            l.append(i)
        return list(set(l))
    def close(self):
        '''
        :return:
        '''
        self.close()




class ChromeWeb:
    '''
    谷歌浏览器
    '''
    slm = None
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--mute-audio")  # 静音
        try:
            self.slm = webdriver.Chrome(options=chrome_options)
        except Exception:
            self.slm = webdriver.Chrome(executable_path=chrome_path,options=chrome_options)
    def  close(self):
        self.slm.quit()





class Downloads:
    url = None
    file_path = None
    random_head = {'User-Agent':'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)'}
    video_name = None
    def __init__(self):
        self.get_file_path()
    def get_url(self,url):
        self.url = url
    def get_file_path(self,file_path=download):
        self.file_path = file_path
    def get_name(self,name):
        self.video_name = name
    def video(self):
        data = requests.get(self.url,headers =self.random_head)
        down_path = self.file_path + '/' + self.video_name
        with open(down_path,'ab') as f:
            f.write(data.content)








