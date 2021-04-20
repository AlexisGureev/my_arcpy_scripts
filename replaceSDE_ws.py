# coding=utf-8
import  arcpy

lyrName=r'Тектоничес\кая карта\BASEA_KRAP_noflds_q'
wsNew=r'Database Connections\gdb2012ks2_work_TEST.sde'

lyr=arcpy.mapping.Layer(lyrName)
wsOld= lyr.workspacePath
mxd = arcpy.mapping.MapDocument('current')
mxd.findAndReplaceWorkspacePaths(wsOld,wsNew)