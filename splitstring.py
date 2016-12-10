class splitstring:
	def splitbirthday(self):
		myfile = open('//Users//Aran//Documents//AvailablePasswors//12306//ID.txt','r')
		birthday = []
		line = myfile.readline()
		while line:
			if len(line) == 20:
				birthday.append (line[6:14])
			else:
				birthday.append (line.strip('\n'))
			line = myfile.readline()

		myfile.close()
		s = '\n'.join(num[:] for num in birthday)
		f = open('//Users//Aran//Documents//AvailablePasswors//12306//birthday.txt','w')
		f.write(s)

if __name__ == '__main__':
	split = splitstring()
	split.splitbirthday()