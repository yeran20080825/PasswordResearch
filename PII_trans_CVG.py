# -*- coding:utf-8 -*-

from xpinyin import Pinyin
import operator
from functools import reduce
import numpy

class CVG:

	# def __init__(self):
	# 	self.name = []
	# 	self.birthday = []

	def setpassword(self, psw):
		self.password = psw.lower()

	def setname(self, name):
		transname = repr(Pinyin().get_pinyin(name, ' '))
		namelist = transname.split(" ")
		self.name = []
		self.name.append(''.join(namelist))			#1: the usages of full name(e.g. lei wang)
		self.name.append(''.join([c[0] for c in namelist]))			#2: the abbr. of full name(e.g. lw)
		# self.name.append(namelist[0])		#3: family name(e.g. wang)
		# self.name.append(''.join(namelist[1:]))			#4: given name(e.g. lei)
		self.name.append(namelist[0][0]+''.join(namelist[1:]))		#5:the 1st letter of the given name + family name
		self.name.append(''.join(namelist[1:])+namelist[0][0])    # 6:the 1st letter of the given name + family name
		# print  self.name

	def setbirthday(self, bir):
		self.birthday = []
		self.birthday.append(bir)
		self.birthday.append(bir[4:8]+bir[0:4])
		self.birthday.append(bir[6:8]+bir[4:6]+bir[0:4])
		self.birthday.append(bir[4:6]+bir[0:4])
		self.birthday.append(bir[4:6]+bir[6:8]+bir[2:4])
		self.birthday.append(bir[6:8] + bir[4:6] + bir[2:4])


	def calletterlens(self):
		# self.password = password
		letters = "".join(a for a in self.password if a.isalpha())  # 提取保存口令中的字符字段
		llens = []
		i = 0
		if self.password.find(self.name[1]) >= 0 :
			llens.append(len(self.name[1]))
		elif self.password.find(self.name[2]) >= 0 :
			llens.append(len(self.name[2]))
		elif self.password.find(self.name[3]) >= 0 :
			llens.append(len(self.name[3]))
		else:
			while i < len(letters) - 1:
				matched = False
				pattern = letters[i:i + 2]
				pos = i + 2  # 保存当前滑动窗口的位置
				while self.name[0].find(pattern) >= 0:
					matched = True
					pos += 1
					if pos <= len(letters):
						pattern = letters[i:pos]
					else:
						break

				if matched:
					llens.append(pos - i - 1)
				i = pos - 1


		if len(llens) == 0:
			return [0]
		else:
			return  llens

	def caldatalens(self):
		numbers = "".join(a for a in self.password if a.isdigit())  # 提取保存口令中的数字字段
		dlens = []
		i = 0

		if numbers.find(self.birthday[1]) >= 0:
			dlens.append(8)

		elif numbers.find(self.birthday[2]) >= 0:
			dlens.append(8)

		elif numbers.find(self.birthday[3]) >= 0:
			dlens.append(6)

		elif numbers.find(self.birthday[4]) >= 0:
			dlens.append(6)

		elif numbers.find(self.birthday[5]) >= 0:
			dlens.append(6)

		else:
			while i < len(numbers) - 1:
				matched = False
				pattern = numbers[i:i + 2]
				pos = i + 2
				while self.birthday[0].find(pattern) >= 0:
					matched = True
					pos += 1
					if pos <= len(numbers):
						pattern = numbers[i:pos]
					else:
						break

				if matched:
					dlens.append(pos - i - 1)


				i = pos - 1

		if len(dlens) == 0:
			return [0]
		else:
			return  dlens


	def cvg(self):

		a = reduce(operator.add, [x * x for x in self.calletterlens()])
		b = reduce(operator.add, [y * y for y in self.caldatalens()])
		print self.calletterlens(),self.caldatalens()
		# print self.password,'\t' ,  self.birthday,'\t' ,a ,'\t',b,'\t',len(self.password),'\t', len(self.birthday)
		print float(a + b)/numpy.square(len(self.password))
		return float(a + b)/numpy.square(len(self.password))






def main():
	passwordfile = open('E:\\AvailablePasswors\\12306\\password.txt', 'r')
	namefile = open('E:\\AvailablePasswors\\12306\\username.txt', 'r')
	birthdayfile = open('E:\\AvailablePasswors\\12306\\birthday.txt', 'r')

	c = CVG();
	cvglist = []
	#
	#
	passwordline = passwordfile.readline().strip('\n')
	nameline = namefile.readline().strip('\n')
	birthdayline = birthdayfile.readline().strip('\n')
	while passwordline:

		# c = CVG(repr(passwordline), unicode(repr(nameline), "utf-8"), repr(idline))		#没用
		c.setpassword(passwordline)
		c.setname(unicode(nameline, "gb2312", 'ignore'))

	# c.setpassword('jiangljnnan19820607')
	# c.setname(unicode('刘江南', 'utf-8'))
	# c.setbirthday('19820607')
	# c.cvg()

		c.setbirthday(birthdayline)
		cvglist.append(c.cvg())
		passwordline = passwordfile.readline().strip('\n')
		nameline = namefile.readline().strip('\n')
		birthdayline = birthdayfile.readline().strip('\n')

	passwordfile.close()
	namefile.close()
	birthdayfile.close()
	s = '\n'.join(str(num)[:] for num in cvglist)
	myfile = open('E:\\AvailablePasswors\\12306\\cvgfileNew1214.txt', 'w')
	myfile.write(s)


if __name__ == '__main__':
	main()