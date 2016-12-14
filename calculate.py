# -*- coding:utf-8 -*-
class calculate:
	def cal(self):
		myfile = open('E:\\AvailablePasswors\\12306\\cvgfileNew1214.txt', 'r')
		cvg = []
		for line in myfile.readlines():
			line = float(line.strip('\n'))
			cvg.append(line)
		# print cvg , '\n', len(cvg)
		myfile.close()
		cvgset = set(cvg)  # myset是另外一个列表，里面的内容是mylist里面的无重复 项
		for item in cvgset:
			print(" %f , %d,  %f" % (item, cvg.count(item), cvg.count(item)*100/131653.0))
			# print (" %f " % (item))
			# print (" %d " % (cvg.count(item)))
			# print (" %f " %(cvg.count(item)*100/131653.0))


if __name__ == '__main__':
	caldemo = calculate()
	caldemo.cal()