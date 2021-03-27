#!/usr/bin/env python

import datetime
import time

def main():
	f = open('output.txt','a')
	f.write("Hello World! @ :" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " --> _the_finish_\n")
	print("Hello World! @ :" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " --> _the_finish_\n")
	f.close

if __name__ == '__main__':
	for i in range(2):
        	main()
        	time.sleep(5)