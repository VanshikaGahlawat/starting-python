class Cylinder:

	pi=3.14

	def __init__ (self,radius,height):
		self.radius=radius
		self.height=height

	def volume (self):
		return Cylinder.pi*(self.radius**2)*(self.height)

	def surface_area(self):
		return 2*Cylinder.pi*self.radius*(self.radius+self.height)


cyl1=Cylinder(2,4)
s=cyl1.surface_area()
v=cyl1.volume()
print("volume=",v)
print("surface area=",s)				