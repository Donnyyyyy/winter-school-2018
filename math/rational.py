class Rational:
	def __init__(self,numinator,denominator):
		self.numinator = numinator
		self.denominator = denominator

	def __it__(self, other):
		if(self.numinator * other.denominator / (self.denominator * other.denominator) > other.numinator * self.denominator / (other.denominator * self.denominator)):
			return self
		else:
			return other
	def __gt__(self, other):
		if(self.numinator * other.denominator / (self.denominator * other.denominator) < other.numinator * self.denominator / (other.denominator * self.denominator)):
			return other
		else:
			return self
	def __add__(self, other):
		it = Rational(1, 1)
		it.numinator = self.numinator * other.denominator + other.numinator * self.denominator
		it.denominator = self.denominator * other.denominator
		per =  evklid(it)
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
			per =  evklid(antiit)
			antiit.numinator /= per
			antiit.denominator /= per
			return antiit

	def __mul__(self, other):
		mult = Rational(1,1)
		mult.numinator = self.numinator * other.numinator
		mult.denominator = self. denominator *  other.denominator
		per =  evklid(mult)
		mult.numinator /= per
		mult.denominator /= per
		return mult

	def __truediv__(self, other):
		diver = Rational(1, 1)
		diver.numinator = self.numinator * other.denominator
		diver.denominator = self.denominator * other.numinator
		per =  evklid(diver)
		diver.numinator /= per
		diver.denominator /= per
		return diver
	def __pow__(self, power):
		puff = Rational(1,1)
		puff.numinator = self.numinator ** power
		puff.denominator = self.denominator ** power
		print(module)
		return puff
def evklid(den, noun):
	dencopy = den
	nouncopy = noun
	while(dencopy != 0 and nouncopy != 0):
		if(dencopy > nouncopy):
			dencopy = dencopy % nouncopy
		else:
			nouncopy = nouncopy % dencopy	
	return nouncopy + dencopy
a = Rational(2, 3)
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
print(srvnen)
srvn = a > b
if(srvn == a):
	print(a > b)
else:
	print(b > a)
print(sravne)
srvne = b > a
if(srvne == b):
	print(b > a)
else:
	print(b < a) 
print('puff')
module = input()
int(module)
puff = a ** module
print(puff)