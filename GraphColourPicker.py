import maya.cmds as cmds

#colours = {'Red': 0, 'Blue': 0, 'Green': 0, 'Purple': 0.551 0 0.336679}

removeTranslate = False
removeRotate = False
removeScale = False


#grab everything within Maya
allScene = cmds.ls()

#all objects selected, check relatives to see if there is a SHAPE and place them in the allShapes varible
allShapes = cmds.listRelatives(allScene, shapes=True)

#grab all Nurbs in the shapes
nurbs = cmds.ls(allShapes, type="nurbsCurve")

#this varible will hold all of the duplicate transforms
nurbsTransformDuplicateList = []

# go through nurbs variable and interate and add to the nurbsTransformDuplicateList array
for shape in nurbs:

    nurbsTransformDuplicateList.append(cmds.listRelatives(shape, parent=True)[0])


#quickly see how many items are in the nurbsTransformDuplicateList varible
print 'Number of controls which may have dupes:', len(nurbsTransformDuplicateList)

#remove duplicates and all controllers should now be in here
nurbsTransList = set(nurbsTransformDuplicateList)
print 'Number of controls:', len(nurbsTransList)

#store all source nurb connections in connectionNurb
editTrans =[]

for controllerName in nurbsTransList:


    #get all attribute which are visible to the user and are also keyable
    AllControlsWithAndWithoutKeyable = cmds.listAttr(controllerName,visible=True, keyable=True, scalar=True, unlocked=True)

    #check to see if controllers have keys which can be used by animators
    if AllControlsWithAndWithoutKeyable == None or len(AllControlsWithAndWithoutKeyable) == 0:

        #print 'Non-Keyable', controllerName
        pass
    else:
        #print 'this is keyable', controllerName, 'number', len(AllControlsWithAndWithoutKeyable)
        editTrans.append(controllerName)



for eachControl in editTrans:

    nurbsConnection = []
    #if eachControl is not empty get all animCurve types
    if len(eachControl) != 0:

        #grab all connections which have a similar name to animCurve*
        eachControlsConnections = cmds.listConnections(eachControl, destination=True, type='animCurve')

        print 'Control name ',eachControl, 'ITS CONNECTIONS ', eachControlsConnections


#if editrans is not empty get all animCurve types
#if len(editTrans) != 0:

    #grab all connections which have a similar name to animCurve*
    connections = cmds.listConnections(editTrans, destination=True)
    #print 'this is the name', editTrans, 'these are the connections', connections

    '''
    if connections == None:
        pass
    else:
        #print 'name', controllerName, 'name of connections', connections

        for individualCurves in connections:

            #Enable the attribute to be true so the grapgh editor can be altered colour
            cmds.setAttr(individualCurves+".useCurveColor", 1)
            #print 'individualCurves', individualCurves
            cmds.setAttr(individualCurves+".curveColor", 1.0, 0.0, 0.0, type='double3')
    '''

