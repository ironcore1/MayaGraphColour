import maya.cmds as cmds

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
controllerNameList =[]

for controllerName in nurbsTransList:


    #get all attribute which are visible to the user and are also keyable
    AllControlsWithAndWithoutKeyable = cmds.listAttr(controllerName,visible=True, keyable=True, scalar=True, unlocked=True)

    #check to see if controllers have keys which can be used by animators
    if AllControlsWithAndWithoutKeyable == None or len(AllControlsWithAndWithoutKeyable) == 0:

        #print 'Non-Keyable', controllerName
        pass
    else:
        #print 'this is keyable', controllerName, 'number', len(AllControlsWithAndWithoutKeyable)
        controllerNameList.append(controllerName)



for eachControl in controllerNameList:


    #if eachControl is not empty get all animCurve types
    if len(eachControl) != 0:

        #check and see if it is connected to a characterSet Node

        characterNodesNotSet = cmds.listConnections(eachControl, source=True, type='character')
        characterNodesSetRemoved = set(characterNodesNotSet)
        characterNodes = list(characterNodesSetRemoved)
        charType = cmds.nodeType(characterNodes)
        print type(charType)

        if cmds.nodeType(characterNodes) == 'character':


            #get connections of the controller of a character type
            connections = cmds.listConnections(eachControl, source=True, type='character')

            #remove duplicate names in the list of connections
            setConnections = set(connections)

            #turn it back into a list so it can be itteratred upon
            listedConnections = list(setConnections)

            #look through each character type node
            for eachCharacterSet in listedConnections:

                finalConnections = cmds.listConnections(eachCharacterSet, source=True, type='animCurve')

                if finalConnections == None:
                    pass
                else:
                    for individualCurves in finalConnections:

                        #Enable the attribute to be true so the grapgh editor can be altered colour
                        cmds.setAttr(individualCurves+".useCurveColor", 1)
                        #print 'individualCurves', individualCurves
                        cmds.setAttr(individualCurves+".curveColor", 1.0, 0.0, 0.0, type='double3')
                        print 'it works on', eachControl
            else:
                for eachCharacterSet in listedConnections:

                    finalConnections = cmds.listConnections(eachCharacterSet, source=True, type='animCurve')

                if finalConnections == None:
                    pass
                else:
                    for individualCurves in finalConnections:

                        #Enable the attribute to be true so the grapgh editor can be altered colour
                        cmds.setAttr(individualCurves+".useCurveColor", 1)
                        #print 'individualCurves', individualCurves
                        cmds.setAttr(individualCurves+".curveColor", 1.0, 0.0, 0.0, type='double3')





