class Line:
	def __init__ (self,coordinate1,coordinate2):
		self.coordinate1=coordinate1
		self.coordinate2=coordinate2

	def distance (self):
		x1,y1=self.coordinate1
		x2,y2=self.coordinate2

		return ((x2-x1)**2 - (y2-y1)**2)**0.5

	def slope (self):
		x1,y1=self.coordinate1
		x2,y2=self.coordinate2

		return (y2-y1)/(x2-x1)


l1=Line((0,4),(2,4))
m=l1.slope()
d=l1.distance()
print("slope is=" ,m)
print("distance is=" ,d)		