class Rational:
	def __init__(self,numinator,denominator):
		self.__numinator = numinator
		self.__denominator = denominator

	@property
	def numinator(self):
		return self.__numinator

	@property
	def denominator(self):
		return self.__denominator

	@numinator.setter
	def numinator(self, value):
		self.__numinator = int(value)

	@denominator.setter
	def denominator(self, value):
		self.__denominator = int(value)

	def __lt__(self, other):
		num = self.denominator * other.denominator
		numcopy = other.numinator * self.denominator
		if(num > numcopy):
			return False
		else:
			return True


	def __gt__(self, other):
		num = self.denominator * other.denominator
		numcopy = other.numinator * self.denominator
		if(num < numcopy):
			return False
		else:
			return True


	def __add__(self, other):
		it = Rational(1, 1)
		if(self.denominator == other.denominator):
			it.numinator = self.numinator + other.numinator
			it.denominator = self.denominator
			per =  evklid(it.numinator, it.denominator)
			it.numinator /= per
			it.denominator /= per
			return it
		else:
			it.numinator = self.numinator * other.denominator + other.numinator * self.denominator
			it.denominator = self.denominator * other.denominator
			per =  evklid(it.numinator, it.denominator)
			it.numinator /= per
			it.denominator /= per
			return it


	def __str__(self):
		return '{}/{}'.format(self.numinator, self.denominator)


	def __sub__(self, other):
		antiit = Rational(1, 1)
		antiit.numinator = self.numinator * other.denominator - other.numinator * self.denominator
		antiit.denominator = self.numinator * other.denominator
		if(antiit.numinator == 0):
			return 0
		else:
			per =  evklid(antiit.numinator, antiit.denominator)
			antiit.numinator /= per
			antiit.denominator /= per
			return antiit

	def __mul__(self, other):
		mult = Rational(1,1)
		mult.numinator = self.numinator * other.numinator
		mult.denominator = self. denominator *  other.denominator
		per =  evklid(mult.denominator, mult.numinator)
		mult.numinator /= per
		mult.denominator /= per
		return mult

	def __truediv__(self, other):
		diver = Rational(1, 1)
		diver.numinator = self.numinator * other.denominator
		diver.denominator = self.denominator * other.numinator
		per =  evklid(diver.denominator, diver.numinator)
		diver.numinator /= per
		diver.denominator /= per
		return diver

	def __pow__(self, power):
		puff = Rational(1,1)
		puff.numinator = self.numinator ** power
		puff.denominator = self.denominator ** power
		return puff


	def __ne__(self, other):
		num = self.denominator * other.denominator
		numcopy = other.numinator * self.denominator
		if(num == numcopy):
			return False
		else:
			return True


	def __eq__(self, other):
		num = self.denominator * other.denominator
		numcopy = other.numinator * self.denominator
		if(num == numcopy):
			return True
		else:
			return False


	def __le__(self, other):
		num = self.denominator * other.denominator
		numcopy = other.numinator * self.denominator
		if(num <= numcopy):
			return True
		else:
			return False


	def __ge__(self, other):
		num = self.denominator * other.denominator
		numcopy = other.numinator * self.denominator
		if(num <= numcopy):
			return False
		else:
			return True

def evklid(den, noun):
	dencopy = den
	numcopy = noun
	while(dencopy != 0 and numcopy != 0):
		if(dencopy > numcopy):
			dencopy = dencopy % numcopy
		else:
			numcopy = numcopy % dencopy	
	return numcopy + dencopy
a = Rational(10, 5)
b = Rational(2, 3)
print(a)
print(b)
it = a + b
print('plus')
print(it)
antiit = a - b
print('antiplus')
print(antiit)
mult = a * b
print('multy')
print(mult)
diver = a / b
print('antimulty')
print(diver)		
print('srvnen')
srvn = a > b
print('a == b')
print(a == b)
print(a > b)
print('sravne')
srvne = b < a
if(b == a):
	print(b > a)
else:
	print(b < a) 
print('puff')
module = 2
print(a ** module)
print('neravn')
print(b != a)
print('ravn')
print(b == a)
print('ravnor')
ravn = a <= b
print(ravn)
print('ravnorobor')
ravnore = a >= b
print(ravnore)