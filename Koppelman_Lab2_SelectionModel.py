#Matt Koppelman
#GIS 501
#Lab 2 Python Export - Part 3




# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# SelectionModel.py
# Created on: 2014-10-13 20:25:03.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
AMLInventoryPoints2014_10 = "AMLInventoryPoints2014_10"
Bituminous_coal_mine_permits_update_122112 = "Bituminous_coal_mine_permits_update_122112"
Anthracite_coal_mine_permits_update_122112 = "Anthracite_coal_mine_permits_update_122112"
Selection = "C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Selection"
AMLInventoryPoints2014_10__2_ = "AMLInventoryPoints2014_10"
AMLInventoryPoints2014_10__4_ = "AMLInventoryPoints2014_10"

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(AMLInventoryPoints2014_10, "INTERSECT", Bituminous_coal_mine_permits_update_122112, "", "NEW_SELECTION")

# Process: Select Layer By Location (2)
arcpy.SelectLayerByLocation_management(AMLInventoryPoints2014_10__2_, "INTERSECT", Anthracite_coal_mine_permits_update_122112, "", "ADD_TO_SELECTION")

# Process: Feature Class to Feature Class
arcpy.FeatureClassToFeatureClass_conversion(AMLInventoryPoints2014_10__4_, Selection, "AMLInventoryPoints2014_10_Selection.shp", "", "SF_ID \"SF_ID\" true true false 9 Long 0 9 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_ID,-1,-1;OTHER_ID \"OTHER_ID\" true true false 15 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,OTHER_ID,-1,-1;SF_NAME \"SF_NAME\" true true false 60 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_NAME,-1,-1;SF_TYPE_CD \"SF_TYPE_CD\" true true false 5 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_TYPE_CD,-1,-1;SF_TYPE \"SF_TYPE\" true true false 40 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_TYPE,-1,-1;SF_STATUS_ \"SF_STATUS_\" true true false 5 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_STATUS_,-1,-1;SF_STATUS \"SF_STATUS\" true true false 40 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_STATUS,-1,-1;SF_PRIORIT \"SF_PRIORIT\" true true false 5 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_PRIORIT,-1,-1;SF_PRIOR_1 \"SF_PRIOR_1\" true true false 60 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_PRIOR_1,-1,-1;SF_PROBLEM \"SF_PROBLEM\" true true false 5 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_PROBLEM,-1,-1;SF_PROBL_1 \"SF_PROBL_1\" true true false 56 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,SF_PROBL_1,-1,-1;HEIGHT_FT \"HEIGHT_FT\" true true false 9 Long 0 9 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,HEIGHT_FT,-1,-1;VOLUME_CY \"VOLUME_CY\" true true false 9 Long 0 9 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,VOLUME_CY,-1,-1;FLOW_GPM \"FLOW_GPM\" true true false 9 Long 0 9 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,FLOW_GPM,-1,-1;KEYWORDS \"KEYWORDS\" true true false 254 Text 0 0 ,First,#,C:\\Users\\Matt\\Documents\\UWTacoma\\GIS501\\GitHub\\Lab_2\\LabData\\Projected\\AMLInventoryPoints2014_10.shp,KEYWORDS,-1,-1", "")

