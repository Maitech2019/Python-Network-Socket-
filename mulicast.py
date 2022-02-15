#multicast.py

import time
import threading

def Toothbrush(brand):
	for i in range(10):
		print("brushing teeth..." + brand)
		time.sleep(0.3) #run every 3 second

def Shower(soap,gel):
	for i in range(10):
		print("showering ...soap{} and gel{}".format(soap,gel))
		time.sleep(1)

task1 = threading.Thread(target=Toothbrush, args=('collgae',))  # one arg still need , after
task2 = threading.Thread(target=Shower, args=('dove', 'sunsilk'))

start = time.time() # stopwatch

#Toothbrush()
#Shower()
task1.start()
task2.start()
task1.join()
task2.join()

end = time.time()
print("All Time", end -start)
print("--------")
print("----go to school----")
