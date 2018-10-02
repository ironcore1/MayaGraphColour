import maya.cmds as cmds

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


#transformAttr = cmds.listAttr('CtrlRig:AN_IK_R_Hand_Control',visible=True, keyable=True, scalar=True, unlocked=True)

for i in nurbsTransList:

    transformAttr = cmds.listAttr(i,visible=True, keyable=True, scalar=True, unlocked=True)
    #grab the name of the object currently selected and list all connecting within the node editor
    connections = cmds.listConnections(i, plugs=True,s=True)





