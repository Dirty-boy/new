import os
Main_dir = os.getcwd()  #当前项目路径

Key_text = os.path.join(Main_dir,'url_set.text')  # 读取文件
download = os.path.join(Main_dir,'download')  # 下载文件夹

chrome_path = os.path.join(Main_dir,'main\chromedriver.exe')
