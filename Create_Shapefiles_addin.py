import arcpy
import pythonaddins
arcpy.env.overwriteOutput = False
import os

class CircleTool(object):
    """Implementation for Create_Shapefiles_addin.tool (Tool)"""
    def __init__(self):
        global j
        self.enabled = True
        self.shape = "Circle" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
        j=1
   
    def onMouseDownMap(self, x, y, button, shift):
        global j
        filename1= "circle" + str(j)
        path1="in_memory"
        radius=str(value)
        fullpath1=os.path.join(path1, filename1)
        point=arcpy.Point(x,y)
        pointGeometry = arcpy.PointGeometry(point)  
        arcpy.Buffer_analysis(pointGeometry, fullpath1, radius)
        j=j+1
        
           
class Combo1(object):
    
    """Implementation for Create_Shapefiles_addin.combobox (ComboBox)"""
    def __init__(self):
        self.items = ["item1", "item2"]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
        
    def onSelChange(self, selection):
        pass
    def onEditChange(self, text):
        global value
        value=text
        print "The value you provided is" , value
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass

class SquareTool(object):
    """Implementation for Create_Shapefiles_addin.tool_1 (Tool)"""
    def __init__(self):
        global i
        self.enabled = True
        self.shape = "Rectangle" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
        i=1
    def onMouseDownMap(self, x, y, button, shift):
        global i
        print x,y
        mxd = arcpy.mapping.MapDocument("CURRENT")  
        df = arcpy.mapping.ListDataFrames(mxd, '')[0] 
        for layer in arcpy.mapping.ListLayers(mxd, None, df): # function variable elimination

            # Ignore layers without local data
            if (layer.isGroupLayer or layer.isServiceLayer):
                continue

            # Skip layers with invalid source
            if (layer.isBroken):
                print("Warning: Layer '{:s}' source is broken!".format(layer.name))
                continue

            sr = arcpy.Describe(layer).spatialReference
            # Avoid undefined variable
            if (sr.type == "Unknown"):
                # print is function at Python 3; use string.format()
                print("Warning: Layer '{:s}' has an unknown spatial reference\n".format(layer.name))
            else:
                # print is function at Python 3; use string.format()
                print("{:30s}: {:s}\n".format(layer.name,sr.name))

        del mxd

        arcpy.env.workspace = 'in_memory'

       
        val = int(value)
        if val%2==0:
            
            a = (val / 2)
            x = (x)
            y =(y)
            x1 = x - a
            y1 = y - a
            x2 = x1
            y2 = y+ a
            x3 = x+a
            y3 = y2
            x4 = x3
            y4 = y1
            
        else:
            a = (val / 2)
            x = (x)
            y =(y)
            x1 = x - a-0.5
            y1 = y - a -0.5
            x2 = x1
            y2 = y+ a+0.5
            x3 = x+a+0.5
            y3 = y2
            x4 = x3
            y4 = y1
       

        #feature_info = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]


        array = arcpy.Array([arcpy.Point(x1, y1),
                     arcpy.Point(x2, y2),
                     arcpy.Point(x3,y3),
                     arcpy.Point(x4,y4)
                     ])
        polygon = arcpy.Polygon(array, sr)
        #with arcpy.da.InsertCursor(r"in_memory\polygon", "SHAPE@") as cursor:
           #cursor.insertRow((polygon,))
        filename= "polygon" + str(i)
        path="in_memory"
        fullpath=os.path.join(path, filename)
        arcpy.CopyFeatures_management(polygon, fullpath)
        arcpy.RefreshActiveView()
        i=i+1
     
        
