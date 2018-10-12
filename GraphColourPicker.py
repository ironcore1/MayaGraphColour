import maya.cmds as cmds

rotateAtt = ['RotateX', 'RotateY', 'RotateZ']
transAtt = ['TranslateX', 'TranslateY', 'TranslateZ']
scaleAtt = ['ScaleX', 'ScaleY', 'ScaleZ']

removeTranslate = False
removeRotate = False
removeScale = False 

value = 0

#grab everything within Maya
allScene = cmds.ls()

#all objects selected, check relatives to see if there is a SHAPE and place them in the allShapes varible
allShapes = cmds.listRelatives(allScene, shapes=True)

#grab all Nurbs in the shapes
nurbs= cmds.ls(allShapes, type="nurbsCurve")

#this varible will hold all of the duplicate transforms
nurbsTransformDuplicateList = []

# go through nurbs variable and interate and add to the nurbsTransformDuplicateList array
for shape in nurbs:
    nurbsTransformDuplicateList.append(cmds.listRelatives(shape, parent=True)[0])


#quickly see how many items are in the nurbsTransformDuplicateList varible
print len(nurbsTransformDuplicateList)

#remove duplicates
nurbsTransList = set(nurbsTransformDuplicateList)


for i in nurbsTransList:

    #get all attribute which are visible to the user and are also keyable
    transformAttr = cmds.listAttr(i,visible=True, keyable=True, scalar=True, unlocked=True)
    print transformAttr
    
    #store all source nurb connections in connectionNurb
    connectionNurb =[]
    lengthAttr = len(transformAttr)
    
    #grab the name of the object currently selected and list all connecting within the node editor and be sure to only grab the source
    
    #while value != lengthAttr:
        #connectionNurb.append(cmds.listConnections(lengthAttr[value],source=True, type='animCurveTA'))
        #value = value + 1
    
   
'''    
   
    #connectionNurb.append(cmds.listConnections(i,source=True, type='animCurveTL' or 'animCurveTU' or 'animCurveTA')) 

    
   
    if connectionNurb[0] is not None:
        
    
        for x in connectionNurb[0]:
            print x
            
            cmds.setAttr(x+".useCurveColor",1)
            
            attributeName = cmds.listConnections(x,plugs=True)
            
            
            
            if '.rotate' in attributeName[0]:
                print attributeName
            
      '''      





