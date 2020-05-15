
from .moudle import ChromeWeb,Downloads
import time
from lxml import etree
class Video_url(ChromeWeb):
    def get_url(self,url):
        self.slm.get(url=url)
        self.slm.find_element_by_class_name("play-btn").click()

        time.sleep(0.5)
        video_url = self.slm.page_source
        tree = etree.HTML(video_url)
        finish_url = tree.xpath('//video[@class="player"]//@src')[0]
        self.slm.close()
        return finish_url

import os,re,random
class Video_download(Downloads):
    def get_url(self, url):
        self.url = url
    # def get_file_path(self, file_path):
    #     self.file_path = file_path
    def get_name(self,name=None):
        try:
            self.video_name = re.findall('video_id=(.*?)&',self.url)[0] + '.mp4'
        except Exception:
            self.video_name = f'{random.randint(200)}{random.randint(200)}{random.randint(200)}{random.randrange(800,1400)}.mp4'


