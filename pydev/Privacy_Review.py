
# coding: utf-8

# In[79]:

#Outputs a crosstab report for privacy reviews

import json
from IPython.nbformat import current as nbf


# In[80]:

fxns = '''

# functions used throughout analysis

from __future__ import division
from IPython.core.display import HTML
import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import mode

pd.set_option('display.max_colwidth', 1)



def loadFiles(src_dir, fnName):
    fn = src_dir + fnName
    df = pd.read_csv(fn, delimiter=',')
    return df

def getDfColumns(df):
    return list(df.columns.values)

def columnString(dfList):
    return ','.join(dfList)

def findSingleCells (df):
    crossMatrix = df.as_matrix()
    single = len([ row[i] for row in crossMatrix for i in range(len(row)) if row[i] == 1 ])
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

def getSingleCellInfo( datasetName, crossTab, grpFieldList,  fieldListString):
    single, kplus, totalcells, percentsingle, minCell, maxCell, meanCell, medianCell = findSingleCells(crossTab)
    reportInfo =  "<div> *********************** </br>"
    reportInfo = reportInfo +  "<h3>" + datasetName +  ":</br>" + grpFieldList  + " By " + fieldListString + "</h3>"
    
    reportInfo = reportInfo + "<p><b> Total of number of cells in " + datasetName + "- " + fieldListString + " By " + grpFieldList +": " + str(totalcells) + "</br>" 
    reportInfo = reportInfo + "Number of Single Cells in " + datasetName + "- " + fieldListString  + " By " + grpFieldList +": " + str(single)+ "</br>"
    reportInfo = reportInfo + "Percentage of Single cells in "  + datasetName+  "- " + fieldListString +" By " + grpFieldList +": " + str( percentsingle) + "%" +"</b></br></p>"

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
    titleStuff  = titleStuff + "<p> Columns: "+":</p>"
    titleStuff = titleStuff + "<p>" + ", ".join(df_column_names) + "</p></H1>"
    titleStuff = HTML(titleStuff)
    return df, titleStuff

def makeCrossTabInfo( grpField, grpFieldList, fieldList, fieldListString,  datasetName):
    crossTab = getCrossTab( grpField, fieldList)
    single_cell_info = getSingleCellInfo( datasetName, crossTab, grpFieldList, fieldListString)
    return crossTab, single_cell_info

'''


# In[81]:

class GenerateCrosstabReports:
    def __init__(self):

        self.fxns = '''

# functions used throughout analysis

from __future__ import division
from IPython.core.display import HTML
import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import mode

pd.set_option('display.max_colwidth', 1)



def loadFiles(src_dir, fnName):
    fn = src_dir + fnName
    df = pd.read_csv(fn, delimiter=',')
    return df

def getDfColumns(df):
    return list(df.columns.values)

def columnString(dfList):
    return ','.join(dfList)

def findSingleCells (df):
    crossMatrix = df.as_matrix()
    single = len([ row[i] for row in crossMatrix for i in range(len(row)) if row[i] == 1 ])
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

def getSingleCellInfo( datasetName, crossTab, grpFieldList,  fieldListString):
    single, kplus, totalcells, percentsingle, minCell, maxCell, meanCell, medianCell = findSingleCells(crossTab)
    reportInfo =  "<div> *********************** </br>"
    reportInfo = reportInfo +  "<h3>" + datasetName +  ":</br>" + grpFieldList  + " By " + fieldListString + "</h3>"
    
    reportInfo = reportInfo + "<p><b> Total of number of cells in " + datasetName + "- " + fieldListString + " By " + grpFieldList +": " + str(totalcells) + "</br>" 
    reportInfo = reportInfo + "Number of Single Cells in " + datasetName + "- " + fieldListString  + " By " + grpFieldList +": " + str(single)+ "</br>"
    reportInfo = reportInfo + "Percentage of Single cells in "  + datasetName+  "- " + fieldListString +" By " + grpFieldList +": " + str( percentsingle) + "%" +"</b></br></p>"

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
    titleStuff  = titleStuff + "<p> Columns: "+":</p>"
    titleStuff = titleStuff + "<p>" + ", ".join(df_column_names) + "</p></H1>"
    titleStuff = HTML(titleStuff)
    return df, titleStuff

def makeCrossTabInfo( grpField, grpFieldList, fieldList, fieldListString,  datasetName):
    crossTab = getCrossTab( grpField, fieldList)
    single_cell_info = getSingleCellInfo( datasetName, crossTab, grpFieldList, fieldListString)
    return crossTab, single_cell_info

'''
        self.nb = nbf.new_notebook()
        self.cells = []
        cell = nbf.new_code_cell(fxns )
        self.cells.append(cell)
    
    def generateListStrings(self, fieldStrings, stringTypeString, stringTypeList):
        fieldListString = stringTypeString + " = '" + fieldStrings + "'"
        fieldListDfString = ""
        fL = fieldStrings.split(",")
        for field in fL: 
            fieldDF = "df['" + field.strip() + "'],"
            fieldListDfString  = fieldListDfString + fieldDF
        fieldListDfString =  stringTypeList +   " = [ " + fieldListDfString[0:-1] + "]"
        return fieldListString, fieldListDfString
    
    def generateCells(self, crossTabList, grpFieldString, datasetName, grpField):
        for fieldList in crossTabList:
            fieldListString, fieldListDfString = self.generateListStrings(fieldList,  "fieldListString", "fieldList")
            crossStuff = grpField + "\n" + fieldListString + "\n" +   fieldListDfString + "\n" 
            crossStuff = crossStuff + "crossBy, single_cell_info = makeCrossTabInfo( grpField, grpFieldList, fieldList, fieldListString,  datasetName)" 
            crossStuff = crossStuff + "\n"+ "single_cell_info"
            cell = nbf.new_code_cell(crossStuff)
            self.cells.append(cell)
            cell = nbf.new_code_cell("crossBy")
            self.cells.append(cell)
    
    def generateCrossTabsReport(self, datasetName, src_dir, fnName, crossTabList, grpFieldString):
        dfcell = 'df, titleStuff = makeOutput(datasetName, src_dir , fnName )'
        grpFieldString, grpField = self.generateListStrings( grpFieldString, "grpFieldList", "grpField" )
        stuff = '''
datasetName = "%s"
src_dir = '%s'
fnName = '%s'
        ''' % (datasetName, src_dir, fnName )
        stuff = stuff + "\n" + grpFieldString+  "\n"  + dfcell + "\n" + "titleStuff"
        cell = nbf.new_code_cell(stuff)
        self.cells.append(cell)
        self.generateCells(crossTabList, grpFieldString, datasetName, grpField)
    
    def generateFinalCrossTabReport(self, output_dir, outputFname):
        self.nb['worksheets'].append(nbf.new_worksheet(cells=self.cells))
        with open(output_dir + outputFname, 'w') as f:
            nbf.write(self.nb, f, 'ipynb')


# In[82]:

class JsonConfigStuff:
    def __init__(self):
        self.initialized = 'true'
    
    @staticmethod
    def loadJsonFile(config_dir, config_fn):
        with open(config_dir+config_fn ) as data_file:    
            json_data = json.load(data_file)
            return json_data['all_items']
   
    @staticmethod
    def parseConfigVariables(jsonItem):
        src_dir = jsonItem['src_dir']
        output_fName = jsonItem['output_fName']
        output_dir = jsonItem['output_dir']
        crossTabReports = jsonItem['crossTabReports']
        return src_dir, output_fName, output_dir, crossTabReports

    @staticmethod
    def parseCrossTabReportVaribles(crossTabReportJsonConfig):
        fname = crossTabReportJsonConfig['fnName']
        grpFieldString = crossTabReportJsonConfig['grpFieldString']
        datasetName = crossTabReportJsonConfig['datasetName']
        crossTabList =  crossTabReportJsonConfig['crossTabList'].values()
        return fname, datasetName, grpFieldString, crossTabList

    def generateReports(self, jsonItem, rp):
        src_dir, outputFname, outputDir, crossTabReports = self.parseConfigVariables(jsonItem)
        for itemJson in crossTabReports:
            fName, datasetName, grpFieldString, crossTabList =  self.parseCrossTabReportVaribles(itemJson)
            rp.generateCrossTabsReport( datasetName, src_dir, fName, crossTabList, grpFieldString)
        rp.generateFinalCrossTabReport(outputDir, outputFname)


    def getListConfigFiles(self, config_dir, config_fn):
        jsonData = self.loadJsonFile(config_dir, config_fn)
        return jsonData[0].values()

