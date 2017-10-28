import os, requests, threading, datetime
from time import sleep
from selenium import webdriver

class Speaker():
    def __init__(self, interval):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while (True):
            print('{dt}'.format(dt=datetime.datetime.now()))
            sleep(self.interval)

#def send_finish(th, ah):
#    with open('id', 'r') as f:
#        worker_name = f.read()
#    requests.post('http://deepnet.duckdns.org:1783/cms/', {'worker': worker_name, 'th':th, 'ah':ah})

def start():
    #node = ''
    #with open('node', 'r') as f:
    #    node = f.read()
    driver = webdriver.Firefox()
    #driver.get(node)
    driver.get('http://deepnet1.epizy.com')
    sleep(3)
    Speaker(30)
    sleep(60*20)
    th = driver.find_element_by_id('th').text
    ah = driver.find_element_by_id('ah').text
    driver.close()
    #send_finish(th, ah)###
    print('FINISH!!!')

if __name__ == '__main__':
    start()
