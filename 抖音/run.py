from main.video import *
from main.moudle import *
from threading import Thread
import queue
q=queue.Queue()

def get_urls():
    d = OpenTxt().read_set()
    for i in d:
        f = Video_url()
        url= f.get_url(i)
        q.put(url)

def put_video(url):
    d = Video_download()
    d.get_url(url)
    d.get_name()
    d.video()




if __name__ == '__main__':
    t = Thread(target=get_urls)
    t.setDaemon(True)  # 必须在t.start()之前设置
    t.start()
    t.join()
    choose =True
    while choose:
        try:
            q_get = q.get_nowait()
            print(q_get)
            A = Thread(target=put_video,args=(q_get,))
            A.start()
            A.join()
        except Exception:
            choose = False





