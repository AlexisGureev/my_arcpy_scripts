# coding=utf-8
import  arcpy

lyrName=r'Тектоничес\кая карта\TK2500.BASEA'
wsNew=r'Database Connections\gdb2012ks2_work_TEST.sde'

lyr=arcpy.mapping.Layer(lyrName)
wsOld= lyr.workspacePath
mxd = arcpy.mapping.MapDocument('current')
mxd.findAndReplaceWorkspacePaths(wsOld,wsNew)
