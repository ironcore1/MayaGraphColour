import maya.cmds as cmds

isMyCodeOn = 1

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


        if characterNodesNotSet != None:
            characterNodesSetRemoved = set(characterNodesNotSet)
            characterNodes = list(characterNodesSetRemoved)

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

                            #Enable the attribute to be true so the gr zapgh editor can be altered colour
                            cmds.setAttr(individualCurves+".useCurveColor", isMyCodeOn)
                            #print 'individualCurves', individualCurves
                            cmds.setAttr(individualCurves+".curveColor", 1.0, 0.0, 0.0, type='double3')
                            print 'it works on', eachControl





        else:

            finalConnections = cmds.listConnections(eachControl, source=True, type='animCurve')
            listWithoutTranRotScale = []

            if finalConnections == None:
                pass
            else:

                ######### remove Translate, Rotate and scale from the list to change colours as I don't want this to happen #########
                for checkTransRotScale in finalConnections:

                        #print checkTransRotScale, 'set to ', defaultControls
                        pass
                    else:
                        listWithoutTranRotScale.append(checkTransRotScale)



                    for idx,individualCurves in enumerate(listWithoutTranRotScale):
                        if idx == 0:

                            #Enable the attribute to be true so the grapgh editor can be altered colour
                            cmds.setAttr(individualCurves+".useCurveColor", isMyCodeOn)

                            #Colour Pale Yellow
                            cmds.setAttr(individualCurves+".curveColor", 1.0, 1.0, 0.5, type='double3')

                        elif idx == 1:

                            #Enable the attribute to be true so the grapgh editor can be altered colour
                            cmds.setAttr(individualCurves+".useCurveColor", isMyCodeOn)

                            #Colour Purple
                            cmds.setAttr(individualCurves+".curveColor", 1.0, 0.0, 1.0, type='double3')

                        elif idx == 2:
                            #Enable the attribute to be true so the grapgh editor can be altered colour
                            cmds.setAttr(individualCurves+".useCurveColor", isMyCodeOn)

                            #Colour Bright Orange
                            cmds.setAttr(individualCurves+".curveColor", 1.0, 0.331, 0.0, type='double3')

                        elif idx == 3:
                            #Enable the attribute to be true so the grapgh editor can be altered colour
                            cmds.setAttr(individualCurves+".useCurveColor", isMyCodeOn)

                            #Colour Pink
                            cmds.setAttr(individualCurves+".curveColor", 0.8, 0.397, 0.805, type='double3')

                        elif idx == 4:
                            #Enable the attribute to be true so the grapgh editor can be altered colour
                            cmds.setAttr(individualCurves+".useCurveColor", isMyCodeOn)

                            #Colour Pink
                            cmds.setAttr(individualCurves+".curveColor", 1.0, 0.841, 0.0, type='double3')


                        elif idx == 5:
                            #Enable the attribute to be true so the grapgh editor can be altered colour
                            cmds.setAttr(individualCurves+".useCurveColor", isMyCodeOn)

                            #Colour brown
                            cmds.setAttr(individualCurves+".curveColor", 0.610, 0.236, 0.0, type='double3')





























