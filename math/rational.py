class Rational:
	def __init__(self,numinator,denominator):
		self.numinator = numinator
		self.denominator = denominator


	def __cmp__(self, other):
		other.numinator = numinator
		if(self.numinator * other.denominator / (self.denominator * other.denominator) > other.numinator * self.denominator / (other.denominator * self.denominator)):
			return self
		else:
			return other

	def __add__(self, other):
		it = Rational(1, 1)
		it.numinator = self.numinator * other.denominator + other.numinator * self.denominator
		it.denominator = self.denominator * other.denominator
		print(it.numinator)
		print(it.denominator)
	def __str__(self):
		return '{}/{}'.format(self.numinator, self.denominator)

a = Rational(2, 3)
b = Rational(2, 3)
print(a)
print(b)
it = a + b