import math


class Cylinder():
    """A cylinder."""

    def __init__(self, height, radius, thickness=None):
        self.height = height
        self.radius = radius
        self.thickness = thickness
        if thickness == None:
            self.capacity = 0
        else:
            innerradius = self.radius - self.thickness
            self.capacity = math.pi * innerradius ** 2 * self.height
        self.contents = 0

    def addLiquid(self, amount):
        self.contents += amount
        if self.contents > self.capacity:
            print("uh oh I overflowed.")
            self.contents = self.capacity

    def removeLiquid(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            print("sorry, you were %0.2f short." % abs(self.contents))
            self.contents = 0
            ## add a string method here

            ## add a comparison method here. Have it compare on
            ## total volume, capacity, contents, or remaining capacity.

    def __str__(self):
        """Called whenever a printed representation is needed"""
        return  "Thickness is " + str(self.thickness) + " Capacity is " + str(self.capacity) + " Contents is " + str(self.contents)

    def __lt__(self, other):
        """Return true if self.capacity is less than other.capcity"""
        return self.capacity < other.capacity

    def __eq__(self,other):
        """Return true if they are the same capacity"""
        return self.capacity == other.capacity

mycylinder = Cylinder(10, 2)
# let's instead create classses for each of these types of cylinders.
# for the mug, we might have a handle or set the material, or if it has a lid
# for the cup, we might also define the material
# and the for the oil barrel, we might pick a number of chines
class Mug(Cylinder):
    def __init__(self,height = 3.75, radius = 1.62, thickness=.12, handle = True):
        Cylinder.__init__(self,height,radius,thickness)
        self.handle = handle
        def __str__(self):
            return "Mug with capacity %.2f, and containing %.2f"%(self.capcity,self.contents)
class Cup(Cylinder):
    def __init__(self,height = 6, radius = 1.5, thickness=.05, material = "Glass"):
        Cylinder.__init__(self,height,radius,thickness)
        self.material = material
        def __str__(self):
            return "Cup with capacity %.2f, and containing %.2f, material is %.2f"%(self.capcity,self.contents,self.material)
class Barrel(Cylinder):
    def __init__(self,height = 3.75, radius = 1.62, thickness=.12, color = "Black"):
        Cylinder.__init__(self,height,radius,thickness)
        self.color = color
        def __str__(self):
            return "Barrel with capacity %.2f, and containing %.2f, color is %.2f"%(self.capcity,self.contents, self.color)

mug = Cylinder(3.75, 1.62, .12)
cup = Cylinder(6, 1.5, .05)
barrel = Cylinder(35, 12, 0.06)
myMug = Mug()
myCup = Cup()
print(myCup)
print(myMug)
print(cup)
print(barrel)

print("Can mug store less than barrel?", mug < barrel)
print("Can cup store more than barrel?", cup > barrel)