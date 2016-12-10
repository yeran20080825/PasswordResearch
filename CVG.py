# -*- coding:utf-8 -*-

import operator
from functools import reduce
import numpy
class CVG:
	def __init__(self, password, name, birthday):
		self.password = password
		self.name = name
		self.birthday = birthday

	def calletterlens(self):
		# self.password = password
		letters = "".join(a for a in self.password if a.isalpha())  # 提取保存口令中的字符字段
		llens = []
		i = 0
		while i < len(letters)-1:
			matched = False
			pattern = letters[i:i + 2]
			pos = i + 2  # 保存当前滑动窗口的位置
			while self.name.find(pattern) >= 0:
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
		while i < len(numbers)-1:
			matched = False
			pattern = numbers[i:i + 2]
			pos = i + 2
			while self.birthday.find(pattern) >= 0:
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

		print a, '\t', b
		return float(a + b)/numpy.square(len(self.password))






def main():
	c = CVG('xujsh2012', 'xujiasheng', '19830307')
	print(c.cvg())


if __name__ == '__main__':
	main()
