##################################################
# UI Module Class
#
#
##################################################
import maya.cmds as mc

class Ui(object) :
	def __init__(self, name = '') :
		self.name = name
		
	def __str__(self) :
		name = self.name
		return name
   
	def __repr__(self) :
		name = self.name
		return name
	
	def setAnnotation(self, description = '') :
		annTmp = 'mc.%s("%s", e = True, ann = description)' % (self.type, self.name)
		
		exec annTmp
	
	ann = property(None, setAnnotation, None, 'set annotation')

#####################		
#		window		#
#####################
class Window(Ui) :
	def __init__(self, name = 'defaultWindow', titleName = '', width = 100, height = 100) :
		self.name = name
		self.tittleName = titleName
		self.width = width
		self.height = height
       
		if mc.window(self.name, q = True, exists = True) :
			mc.deleteUI(self.name, window = True)
           
		mc.window(self.name)
		mc.showWindow(self.name)
	
	def __str__(self) :
		titleName = self.titleName
		return titleName
		
	def __repr__(self) :
		titleName = self.titleName
		return titleName
	
	def __int__(self) :
		width = self.width
		height = self.height
		return width, height
   
	def getWindowName(self) :
		name = self.name
		return name
   
	def getTitle(self) :
		self.titleName = mc.window(self.name, q = True, title = True)
		return self.titleName
   
	def setTitle(self, titleName = '') :
		self.titleName = mc.window(self.name, e = True, title = titleName)
	
	title = property(getTitle, setTitle, None, 'get and set window titleName')
	
	def getWidth(self) :
		self.width = mc.window(self.name, q = True, w = True)
		return self.width
	       
	def setWidth(self, width = 100) :
		self.width = mc.window(self.name, e = True, w = width)
	
	w = property(getWidth, setWidth, None, 'get and set window width')
	
	def getHeight(self) :
		self.height = mc.window(self.name, q = True, h = True)
		return self.height
   
	def setHeight(self, height = 100) :
		self.height = mc.window(self.name, e = True, h = height)
	
	h = property(getHeight, setHeight, None, 'get and set window height')
	

#####################	
#		layout		#
#####################
class Layout(Ui) :
	def __init__(self, name = '', type = '', width = 100, height = 100) :
		self.name = name
		self.type = type
		self.width = width
		self.height = height
       
	def __str__(self) :
		name = self.name
		type = self.type
		return name, type
   
	def __repr__(self) :
		name = self.name
		type = self.type
		return name, type
	
	def __int__(self) :
		width = self.width
		height = self.height
		return width, height
   
	def getName(self) :
		return self.name
   
	def getType(self) :
		return self.type
	
	def getWidth(self) :
		wid = 'wid'
		loWidth = '%s = mc.%s("%s", q = True, w = True)' % (wid, self.type, self.name)
		
		exec loWidth
		self.width = wid
		
		return self.width
       
	def setWidth(self, width = 100) :
		wid = 'wid'
		loWidth = '%s = mc.%s("%s", e = True, w = width)' % (wid, self.type, self.name)
		
		exec loWidth
		self.width = wid
	
	w = property(getWidth, setWidth, None, 'get and set layout width')
	
	def getHeight(self) :
		hgt = 'hgt'
		loHeight = '%s = mc.%s("%s", q = True, h = True)' % (hgt, self.type, self.name)
		
		exec loHeight
		self.height = hgt
		
		return self.height
       
	def setHeight(self, height = 100) :
		hgt = 'hgt'
		loHeight = '%s = mc.%s("%s", e = True, h = height)' % (hgt, self.type, self.name)
		
		exec loHeight
		self.height = hgt
		
	h = property(getHeight, setHeight, None, 'get and set layout height')
       
	def upStep(self) :
		mc.setParent('..')

#-- menuLayout --#
class MenuBarLayout(Layout) :
	def __init__(self, name = 'menuBarLayoutName', type = 'menuBarLayout') :
		self.name = name
		self.type = type
		mc.menuBarLayout(self.name)
       
#-- columnLayout --#     
class ColumnLayout(Layout) :
	def __init__(self, name = 'columnLayoutName', type = 'columnLayout') :
		self.name = name
		self.type = type
		mc.columnLayout(self.name)
   
	def adjustableColumn(self, val = True) :
		mc.columnLayout(self.name, e = True, adjustableColumn = val)

#-- rowLayout --#
class RowLayout(Layout) :
	def __init__(self, name = 'rowLaoutName', type = 'rowLayout') :
		self.name = name
		self.type = type
		mc.rowLayout(self.name)
       
#-- frameLayout --# 
class FrameLayout(Layout) :
	def __init__(self, name = 'frameLayoutName', type = 'frameLayout') :
		self.name = name
		self.type = type
		mc.frameLayout(self.name)
   
	def setLabel(self, label = 'FramLayout') :
		mc.frameLayout(self.name, e = True, l = label)

#-- formLayout --#
class FormLayout(Layout) :
	def __init__(self, name = 'formLayoutName', type = 'formLayout') :
		self.name = name
		self.type = type
		mc.formLayout(self.name)
   
	def setPosition(self, control = '', position = 'top', distance = 1) :
		mc.formLayout(self.name, e = True, attachForm = [(control, position, distance)])
		
#-- gridLayout --#		
class GridLayout(Layout) :
	def __init__(self, name = 'gridLayoutName', type = 'gridLayout') :
		self.name = name
		self.type = type
		mc.gridLayout(self.name)
	
	def setNumberOfColumns(self, val = 1) :
		mc.gridLayout(self.name, e = True, nc = val)
		
	def setCellWidthHeight(self, width = 1, height = 1) :
		mc.gridLayout(self.name, e = True,cwh = (width, height))

#-- tabLayout --#
class TabLayout(Layout) :
	def __init__(self, name = 'tabLayoutName', type = 'tabLayout') :
		self.name = name
		self.type = type
		
		mc.tabLayout(self.name)
		
	def setTabLabel(self, chld = '', tabLabel = 'defaultTab') :
		mc.tabLayout(self.name, e = True, tabLabel = (chld, tabLabel))
				
#####################		
#		control		#
#####################
class Control(Ui) :
	def __init__(self, name = '', type = '') :
		self.name = name
		self.type = type
   
	def __str__(self) :
		name = self.name
		type = self.name
		label = self.label
		image = self.image
		
		return name, type, label, image
   
	def __repr__(self) :
		name = self.name
		type = self.type
		label = self.label
		image = self.image
		
		return name, type, label, image
   
	def getName(self) :
		return self.name
		
	def getLabel(self) :
		labelTmp = 'labelTmp'
		label = '%s = mc.%s("%s", q = True, l = True)' % (labelTmp, self.type, self.name)
		
		exec label
		self.label = labelTmp
		
		return self.label
       
	def setLabel(self, label = 'ButtonLabel') :
		labelTmp = 'mc.%s("%s", e = True, l = label)' % (self.type, self.name)
		
		exec labelTmp
	
	label = property(getLabel, setLabel, None, 'set control label')
	
	def command(self, cmdExc = '') :
		cmd = 'mc.%s("%s", e = True, c = cmdExc)' % (self.type, self.name)
		
		exec cmd
	
	c = property(None, command, None, 'execute command')
	
	def getWidth(self) :
		widthTmp = 'widthTmp'
		width = '%s = mc.%s("%s", q = True, w = True)' % (widthTmp, self.type, self.name)
		
		exec width
		self.width = widthTmp
		
		return self.width
	
	def setWidth(self, width = 50) :
		widthTmp = 'mc.%s("%s", e = True, w = width)' % (self.type, self.name)
		
		exec widthTmp
	
	w = property(getWidth, setWidth, None, 'set control height')
	
	def getHeight(self) :
		heightTmp = 'heightTmp'
		height = '%s = mc.%s("%s", q = True, h = True)' % (heightTmp, self.type, self.name)
		
		exec height
		self.width = heightTmp
		
		return self.width	
       
	def setHeight(self, height = 10) :
		heightTmp = 'mc.%s("%s", e = True, h = height)' % (self.type, self.name)
		
		exec heightTmp
	
	h = property(getHeight, setHeight, None, 'set control height')

	def setImage(self, img = 'image') :	
		setImg = 'mc.%s("%s", e = True, i = img)' % (self.type, self.name)
		
		exec setImg
	
	image = property(None, setImage, None, None)

	def getText(self) :
		textTmp = 'textTmp'
		txt = '%s = mc.%s("%s", q = True, tx = True)' % (textTmp, self.type, self.name)
		
		exec txt
		
		return textTmp
	
	def setText(self, text = '') :
		txt = 'mc.%s("%s", e = True, tx = text)' % (self.type, self.name)
		exec txt
	
	text = property(getText, setText, None, 'get and set text to control textField')

#-- Menu --#
class Menu(Control) :
	def __init__(self, name = 'menuName', type = 'menu') :
		self.name = name
		self.type = type
		
		mc.menu(self.name)
		
#-- MenuItem --#
class MenuItem(Control) :
	def __init__(self, name = 'menuItemName', type = 'menuItem') :
		self.name = name
		self.type = type
		
		mc.menuItem(self.name)

#-- Button --#
class Button(Control) :
	def __init__(self, name = 'buttonName', type = 'button') :
		self.name = name
		self.type = type
		
		mc.button(self.name, l = 'Button', w = 50)
		
#-- SymbolButton --#	
class SymbolButton(Control) :
	def __init__(self, name = 'symbolButtonName', type = 'symbolButton') :
		self.name = name
		self.type = type
		
		mc.symbolButton(self.name)
		

#-- TextScrollList --#		
class TextScrollList(Control) :
	def __init__(self, name = 'textScrollListName', type = 'textScrollList') :
		self.name = name
		self.type = type
		
		mc.textScrollList(self.name)
		
#-- TextFieldButtonGrp --#		
class TextFieldButtonGrp(Control) :
	def __init__(self, name = 'textFieldButtonGrpName', type = 'textFieldButtonGrp') :
		self.name = name
		self.type = type
		
		mc.textFieldButtonGrp(self.name, tx = 'text', l = 'textFieldButtonGrp', bl = 'Button', bc = '')
	
	def buttonLabel(self, label = 'Button') :
		mc.textFieldButtonGrp(self.name, e = True, buttonLabel = label)
	
	bl = property(None, buttonLabel, None, 'set TextFieldButtonGrp buttonLabel')
	
	def setButtonCommand(self, bttnCmd = '') :
		cmd = 'mc.%s("%s", e = True, bc = bttnCmd)' % (self.type, self.name)
		
		exec cmd
		
	bc = property(None, setButtonCommand, None, 'execute command')
		
#-- TextFieldGrp --#
class TextFieldGrp(Control) :
	def __init__(self, name = 'textFieldName', type = 'textFieldGrp') :
		self.name = name
		self.type = type
		
		mc.textFieldGrp(self.name, l = 'textFieldGrp')
		
#-- PopupMenu --#   
class PopupMenu(Control) :
	def __init__(self, name = 'popupMenuName', type = 'popupMenu') :
		self.name = name
		self.type = type
		
		mc.popupMenu(self.name)
		
#-- MenuItem --#
class MenuItem(Control) :
	def __init__(self, name = 'menuItemName', type = 'menuItem') :
		self.name = name
		self.type = type
		
		mc.menuItem(self.name)