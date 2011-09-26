########## fix cloth shape per frame ##########
###############################################
import sys
import maya.cmds as mc
import maya.mel as mm
import ui

reload(ui)

##########################################################################
### UI Creature ###
win = ui.Window('PangoClohtToolsWindow')
mainLyt_clm = ui.ColumnLayout('mainLyt_clm')

orig_txtFld = ui.TextFieldButtonGrp('orig_txtFld')
dummyMsh_bttn = ui.Button('dummyMsh_bttn')
fin_bttn = ui.Button('fin_bttn')
swtMsh_bttn = ui.Button('swtMsh_bttn')
gphEdt_bttn = ui.Button('gphEdt_bttn')

mainLyt_clm.upStep()

### UI Edit ###
win.title = 'Pango Cloth Tools     \(>///<)/'
win.w = 200
win.h = 180

orig_txtFld.bl = '   Get Original Mesh   '
orig_txtFld.label = 'Original Mesh : '
orig_txtFld.text = 'SelectOriginalMesh'

mainLyt_clm.adjustableColumn(1)

bttn_height = 35

dummyMsh_bttn.label = 'Dummy Mesh'
fin_bttn.label = 'Finalize'
swtMsh_bttn.label = 'Switch Mesh'
gphEdt_bttn.label = 'Graph Editor'

dummyMsh_bttn.h = bttn_height
fin_bttn.h = bttn_height
swtMsh_bttn.h = bttn_height
gphEdt_bttn.h = bttn_height

##########################################################################
### mesh object ###
class Mesh(object) :
    '''
    ********************
    ***** Document *****
    ********************
    Class : Mesh
    Description : this script use for fix error shape from cloth simulation per frame
                  by blendshape
    view document by help()
    '''
    def __init__(self, name = '', visibility = 1) :
        self.name = name
        self.visibility = visibility
        
    def __str__(self) :
        name = self.name
        return name
        
    def __repr__(self) :
        name = self.name
        return name
        
    def __int__(self) :
        visibility = self.visibility
        return visibility
        
    def getName(self) :
        return self.name
        
    def setName(self, newName = '') :
        self.name = mc.rename(self.name, newName)
        
    def delName(self) :
        del self.name
        
    n = property(getName, setName, delName, 'use for get and set name to mesh')
    
    def getVisibility(self) :
        visVal = mc.getAttr('%s.visibility' % self.name)
        visVal_dic = {'True' : 1, 'False' : 0}
        self.visibility = visVal_dic['%s' % visVal]
        
        return self.visibility
    
    def setVisibility(self, visVal = 1) :
        mc.setAttr('%s.visibility' % self.name, visVal)
        
    vis = property(getVisibility, setVisibility, None, 'use for visibility function')
        
class OrigMesh(Mesh) :    
    '''
    ********************
    ***** Document *****
    ********************
    Class : Mesh --> OrigMesh
    Description : get original shape by selected cloth's mesh
    '''
    def __ini__(self, name = '') :
        self.name = name
    
class FixMesh(Mesh) :
    '''
    ********************
    ***** Document *****
    ********************
    Class : Mesh --> FixMesh
    Description : get edit shape mesh by duplicate original mesh
    '''    
    def __init__(self, name = '') :
        self.name = name

##########################################################################
def setInputFixShape(*args) :
	curFrm = int(mc.currentTime(q = True)) 
	
	origMsh = OrigMesh(orig_txtFld.text)
	fixMsh_tmp = mc.duplicate(origMsh.n)[0]
	fixMsh = FixMesh(fixMsh_tmp)
	fixMsh.n = '%s_%sx' % (origMsh.n, curFrm)
                   
	curBsh = mc.blendShape(fixMsh.n, origMsh.n, n = '%s_BSH' % fixMsh, origin = 'world')[0]
	mc.setKeyframe('%s.%s' % (curBsh, fixMsh.n), t = curFrm, v = 1)
	mc.setKeyframe('%s.%s' % (curBsh, fixMsh.n), t = curFrm - 1, v = 0)
	mc.setKeyframe('%s.%s' % (curBsh, fixMsh.n), t = curFrm + 1, v = 0)
    
	origMsh.vis = 0
	fixMsh.vis = 1
		    
def finalizeFunction(*args) :
	curFrm = int(mc.currentTime(q = True))
	
	origMsh = OrigMesh(orig_txtFld.text)
	fixMsh = FixMesh('%s_%sx' % (origMsh.n, curFrm))
	origMsh.vis = 1
	fixMsh.vis = 0
    
def switchEditShape(origVis = 1) :
	curFrm = int(mc.currentTime(q = True))
	
	origMsh = OrigMesh(orig_txtFld.text)
	fixMsh = FixMesh('%s_%sx' % (origMsh.n, curFrm))
    
	if origMsh.vis == 1 :
		origMsh.vis = 0
		fixMsh.vis = 1
        
	else :
		origMsh.vis = 1
		fixMsh.vis = 0

def getOriginalMesh(*args) :
	orig_txtFld.text = mc.ls(sl = True)[0]
	
def graphEditorPanel(*args) :
	mm.eval('tearOffPanel "Graph Editor" graphEditor true;')
    
# button set command #
orig_txtFld.bc = getOriginalMesh
dummyMsh_bttn.c = setInputFixShape
fin_bttn.c = finalizeFunction
swtMsh_bttn.c = switchEditShape
gphEdt_bttn.c = graphEditorPanel

