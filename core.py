import maya.cmds as mc

def lsSel() :
	return mc.ls(sl = True)
	
def getSelShape() :
	return mc.listRelatives(lsSel(), s = True)

class Node(object) :
	def __init__(self, name = 'defaultName') :
		self.name = name

	def __str__(self) :
		name = self.name
		return name

	def __repr__(self) :
		name = self.name
		return name
	
	def rename(self, newName = 'newName') :
		self.name = mc.rename(self.name, newName)
		
	def prefix(self, pref = 'prefix_') :
		self.name = mc.rename(self.name, '%s%s' % (pref, self.name))
		
	def suffix(self, suf = '_suffix') :
		self.name = mc.rename(self.name, '%s%s' % (self.name, suf))

class Dag(Node) :
	def translate(self, axis = 'X', value = 0) :
		mc.setAttr('%s.translate%s' % (self.name, axis.upper()), value)

	def rotate(self, axis = 'X', value = 0) :
		mc.setAttr('%s.rotate%s' % (self.name, axis.upper()), value)

	def scale(self, axis = 'X', value = 1) :
		mc.setAttr('%s.scale%s' % (self.name, axis.upper()), value)
		
	def rotateOrder(self, rtod = 'xyz') :
		rotateOrder_dic = {'xyz' : 0, 'yzx' : 1, 'zxy' : 2, 'xzy' : 3, 'yxz' : 4, 'zyx' : 5, '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5}
		
		mc.setAttr('%s.rotateOrder' % self.name, rotateOrder_dic['%s' % rtod])

class Transform(Dag) :
	def rotatePivot(self, valueX = 0, valueY = 0, valueZ = 0) :
		mc.move(valueX, valueY, valueZ, '%s.rotatePivot' % self)
		
	def scalePivot(self, valueX = 0, valueY = 0, valueZ = 0) :
		mc.move(valueX, valueY, valueZ, '%s.scalePivot' % self)
		
	def rotateScalePivot(self, valueX = 0, valueY = 0, valueZ = 0) :
		mc.move(valueX, valueY, valueZ, '%s.rotatePivot' % self.name)
		mc.move(valueX, valueY, valueZ, '%s.scalePivot' % self.name)
		
class Shape(Dag) :
	def __init__(self, shapeName = 'defaultShape') :
		shapeName = mc.listRelatives(self.name, s = True)[0]
		self.shapeName = shapeName
	
	def __str__(self) :
		shapeName = self.shapeName
		return shapeName
	
	def __repr__(self) :
		shapeName = self.shapeName
		return shapeName

	def color(self, usedColor = 'navy') :
		print usedColor + '  ' + self.shapeName

class Joint(Dag) :
	def __init__(self, name = 'jointName') :
		name = mc.createNode('joint', n = name)
		self.name = name
	
	def radius(self, value = 1) :
		mc.setAttr('%s.radius' % self.name, value)
		
	def jointOrientX(self, valueX = 0) :
		mc.setAttr('%s.jointOrientX' % self.name, valueX)
		
	def jointOrientY(self, valueY = 0) :
		mc.setAttr('%s.jointOrientY' % self.name, valueY)
	
	def jointOrientZ(self, valueZ = 0) :
		mc.setAttr('%s.jointOrientZ' % self.name, valueZ)
		
	def jointOrient(self, valueX = 0, valueY = 0, valueZ = 0) :
		mc.setAttr('%s.jointOrientX' % self.name, valueX)
		mc.setAttr('%s.jointOrientY' % self.name, valueY)
		mc.setAttr('%s.jointOrientZ' % self.name, valueZ)

class Locator(Transform, Shape) :
	def __init__(self, name = 'locatorName') :
		name = mc.spaceLocator(n = name)[0]
		self.name = name
		
class Curve(Transform, Shape) :
	def __init__(self, crvType = 'circle') :
		if crvType == 'circle' :
			name = 'circleCrv'
			
			mc.curve(d = 1.0, p = [(0, 0, 1.579482), (0, 0, 1.004121), (0.157079, 0, 0.991758), (0.31029, 0, 0.954976), (0.31029, 0, 0.954976), (0.455861, 0, 0.894678), (0.590207, 0, 0.812351), (0.710021, 0, 0.710021), (0.812351, 0, 0.590207), (0.894678, 0, 0.455861), (0.954976, 0, 0.31029), (0.991758, 0, 0.157079), (1.004121, 0, 0), (1.579482, 0, 0), (1.004121, 0, 0), (0.991758, 0, -0.157079), (0.954976, 0, -0.31029), (0.894678, 0, -0.455861), (0.812351, 0, -0.590207), (0.710021, 0, -0.710021), (0.590207, 0, -0.812351), (0.455861, 0, -0.894678), (0.31029, 0, -0.954976), (0.157079, 0, -0.991758), (0, 0, -1.004121), (0, 0, -1.579482), (0, 0, -1.004121), (-0.157079, 0, -0.991758), (-0.31029, 0, -0.954976), (-0.455861, 0, -0.894678), (-0.590207, 0, -0.812351), (-0.710021, 0, -0.710021), (-0.812351, 0, -0.590207), (-0.894678, 0, -0.455861), (-0.954976, 0, -0.31029), (-0.991758, 0, -0.157079), (-1.004121, 0, 0), (-1.579482, 0, 0), (-1.004121, 0, 0), (-0.991758, 0, 0.157079), (-0.954976, 0, 0.31029), (-0.894678, 0, 0.455861), (-0.812351, 0, 0.590207), (-0.710021, 0, 0.710021), (-0.590207, 0, 0.812351), (-0.455861, 0, 0.894678), (-0.31029, 0, 0.954976), (-0.157079, 0, 0.991758), (0, 0, 1.004121)], n = name)
			
			self.name = name
		
		elif crvType == 'sphere' :
			name = 'sphereCrv'
			
			mc.curve(d = 1, p = [(0, 0, -1.5), (0, 0, -1), (-0.309017, 0, -0.951057), (-0.587785, 0, -0.809017), (-0.809017, 0, -0.587785), (-0.951057, 0, -0.309017), (-1, 0, 0), (-1.5, 0, 0), (-1, 0, 0), (-0.951057, 0, 0.309017), (-0.809017, 0, 0.587785), (-0.587785, 0, 0.809017), (-0.309017, 0, 0.951057), (-2.98023e-008, 0, 1), (0, 0, 1.5), (-2.98023e-008, 0, 1), (0.309017, 0, 0.951057), (0.587785, 0, 0.809017), (0.809017, 0, 0.587785), (0.951057, 0, 0.309017), (1, 0, 0), (1.5, 0, 0), (1, 0, 0), ( 0.951057, 0, -0.309017), (0.809018, 0, -0.587786), (0.587786, 0, -0.809017), (0.309017, 0, -0.951057), (0, 0, -1), (0, 0.258819, -0.965926), (0, 0.5, -0.866026), (0, 0.707107, -0.707107), (0, 0.866025, -0.5), (0, 0.965926, -0.258819), (0, 1, 0), (0, 1.5, 0), (0, 1, 0), (-7.71341e-009, 0.965926, 0.258819), (-1.49012e-008, 0.866025, 0.5), (-2.10734e-008, 0.707107, 0.707107), (-2.58096e-008, 0.5, 0.866026), (-2.87868e-008, 0.258819, 0.965926), (-2.98023e-008, 0, 1), (-2.87868e-008, -0.258819, 0.965926), (-2.58096e-008, -0.5, 0.866026), (-2.10734e-008, -0.707107, 0.707107), (-1.49012e-008, -0.866025, 0.5), (-7.71341e-009, -0.965926, 0.258819), (0, -1, 0), (0, -1.5, 0), (0, -1, 0), (0, -0.965926, -0.258819), (0, -0.866025, -0.5), (0, -0.707107, -0.707107), (0, -0.5, -0.866026), (0, -0.258819, -0.965926), (0, 0, -1), (0, 0.258819, -0.965926), (0, 0.5, -0.866026), (0, 0.707107, -0.707107), (0, 0.866025, -0.5), (0, 0.965926, -0.258819), (0, 1, 0), (0.258819, 0.965926, 0), (0.5, 0.866025, 0),  (0.707107, 0.707107, 0), (0.866025, 0.5, 0), (0.965926, 0.258819, 0), (1, 0, 0), (1.5, 0, 0), (1, 0, 0), (0.965926, -0.258819, 0), (0.866025, -0.5, 0), (0.707107, -0.707107, 0), (0.5, -0.866025, 0), ( 0.258819, -0.965926, 0), (0, -1, 0), (-0.258819, -0.965926, 0), (-0.5, -0.866025, 0), (-0.707107, -0.707107, 0), (-0.866026, -0.5, 0), (-0.965926, -0.258819, 0), (-1, 0, 0), (-0.965926, 0.258819, 0), (-0.866026, 0.5, 0), (-0.707107, 0.707107, 0), (-0.5, 0.866025, 0), (-0.258819, 0.965926, 0), (0, 1, 0)], n = name)
			
			self.name = name
		
		


