# coding=utf-8
#%%
import  arcpy

lyrName=r'Тектоническая карта\TK2500.BASEA'
wsNew=r'Database Connections\gdb2012_tk2500_user_PROD.sde'

lyr=arcpy.mapping.Layer(lyrName)
wsOld= lyr.workspacePath
mxd = arcpy.mapping.MapDocument('current')
mxd.findAndReplaceWorkspacePaths(wsOld,wsNew)

#%%
import  arcpy

lyrName=r'Тектоничес\кая карта\TK2500.BASEA'
wsNew=r'Database Connections\gdb2012_tk2500_user_TEST.sde'

lyr=arcpy.mapping.Layer(lyrName)
wsOld= lyr.workspacePath
mxd = arcpy.mapping.MapDocument('current')
mxd.findAndReplaceWorkspacePaths(wsOld,wsNew)
