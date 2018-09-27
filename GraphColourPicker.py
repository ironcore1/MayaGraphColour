import maya.cmds as cmds

#grab everything within Maya
allScene = cmds.ls()

#all objects selected, check relatives to see if there is a SHAPE and place them in the allShapes varible
allShapes = cmds.listRelatives(allScene, shapes=True)

#grab all Nurbs in the shapes 
nurbs= cmds.ls(allShapes, type="nurbsCurve")

nurbsTransformDuplicateList = []

# go through nurbs variable and interate and add to the nurbsTransformDuplicateList array
for shape in nurbs:
    nurbsTransformDuplicateList.append(cmds.listRelatives(shape, parent=True)[0]) 


#quickly see how many items are in the nurbsTransformDuplicateList varible
print len(nurbsTransformDuplicateList)

#remove duplicates    
nurbsTransList = set(nurbsTransformDuplicateList)
    
#derp = cmds.listAttr(nurbsTransformParent,visible=True, keyable=True, scalar=True, unlocked=True)
#   print derp

thisIsSet={1,2,3,4,5,2,3,4}

print thisIsSet