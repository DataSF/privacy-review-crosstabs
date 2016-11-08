
# coding: utf-8
#!/usr/bin/python
from __future__ import division
from IPython.core.display import HTML
import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import mode

def loadFiles(src_dir, fnName):
    fn = src_dir + fnName
    df = pd.read_csv(fn, delimiter=',')
    return df

def getDfColumns(df):
    return list(df.columns.values)

def columnString(dfList):
    return ','.join(dfList)

def findSingleCells (df, k_anon_size):
    #finds cells with a k-anonymous group size EQUAL or LESS THAN the parameter value, k_annon_size
    crossMatrix = df.as_matrix()
    single = len([ row[i] for row in crossMatrix for i in range(len(row)) if row[i] <= k_anon_size ])
    totalcells  = len([ 1 for row in crossMatrix for i in range(len(row)) ])
    kplus = totalcells - single
    percentsingle = (single/totalcells )* 100
    maxCell  = np.amax(crossMatrix) 
    minCell = np.amin(crossMatrix)
    meanCell = np.mean(crossMatrix)
    medianCell =   np.median(crossMatrix)
    return single, kplus, totalcells, percentsingle, minCell, maxCell, meanCell, medianCell

def getCrossTab(grpField, fieldList, margin=False):
    crossTab= pd.crosstab(grpField, fieldList,  margins=margin)
    return crossTab

def getSingleCellInfo( datasetName, crossTab, grpFieldList,  fieldListString, k_anon_size):
    single, kplus, totalcells, percentsingle, minCell, maxCell, meanCell, medianCell = findSingleCells(crossTab, k_anon_size)
    reportInfo =  "<div> *********************** </br>"
    reportInfo = reportInfo +  "<h3>" + datasetName +  ":</br>" + grpFieldList  + " By " + fieldListString + "</h3>"
    reportInfo = reportInfo +  "<h4> k-anonomous group size: "   + str(k_anon_size) +"</h4>"
    
    reportInfo = reportInfo + "<p><b> Total of number of cells with values below the k-anonomous group size of " +str(k_anon_size)+ " in " + datasetName + "- " + fieldListString + " By " + grpFieldList +": " + str(totalcells) + "</br>" 
    reportInfo = reportInfo + "Number of Cells with values below the k-anonomous group size of " + str(k_anon_size) + " in " + datasetName + "- " + fieldListString  + " By " + grpFieldList +": " + str(single)+ "</br>"
    reportInfo = reportInfo + "Percentage of of cells with values below the k-anonomous group size of " +str(k_anon_size) + " in "  + datasetName+  "- " + fieldListString +" By " + grpFieldList +": " + str( percentsingle) + "%" +"</b></br></p>"

    reportInfo = reportInfo +  "<br> Min cell value in crossTabs: " + str(minCell) + "</br>" 
    reportInfo = reportInfo + "Max cell value in crossTabs: " + str(maxCell)+ "</br>" 
    reportInfo = reportInfo + "Mean cell value in crossTabs " + str(meanCell)+ "</br>" 
    reportInfo = reportInfo + "Median cell value in crossTabs: " + str(medianCell)+ "</br>" 
    reportInfo =  HTML( reportInfo )
    return reportInfo 
    
    
def makeOutput(datasetName, src_dir, fnName):
    df = loadFiles(src_dir, fnName) 
    df_column_names =  getDfColumns(df)
    titleStuff = "<H1>**************************************</br>" + "Dataset: " + datasetName  + "</br>"
    titleStuff  = titleStuff + "<p> Columns: "+"</p>"
    titleStuff = titleStuff + "<p>" + ", ".join(df_column_names) + "</p></H1>"
    titleStuff = HTML(titleStuff)
    return df, titleStuff

def makeCrossTabInfo( grpField, grpFieldList, fieldList, fieldListString,  datasetName, k_anon_size ):
    crossTab = getCrossTab( grpField, fieldList)
    single_cell_info = getSingleCellInfo( datasetName, crossTab, grpFieldList, fieldListString,  k_anon_size)
    return crossTab, single_cell_info

