#__author__ = 'Caleb'

import csv
import os
import path

def convertToJson(relFilePath):
    with open(path.getPath(relFilePath),'r') as f:
    #rows=[map(float,L.strip().split(','))
        columns = {}
        resultList = []
        jsonResult = {}
        for idx, L in enumerate(f):
            if idx in [0,1,2]:
                columns[idx] = L
            else:
                row = L.strip().split('\t')
                for index, value in enumerate(row):
                    jsonResult[columns[index]] = value
                resultList.append(jsonResult)
        return resultList

def convertToKeyedArrays(relFilePath):
    with open(path.getPath(relFilePath),'r') as f:
        results  = {}
        for idx, L in enumerate(f):
            if idx in [0,1,2]:
                results[idx] = {'name': L.strip(), 'data': []}
            else:
                row = L.strip().split('\t')
                for index, value in enumerate(row):
                    ((results[index])['data']).append(float(value))
        return results

def test():
    results = convertToKeyedArrays('\data\MOST2014.dat')
    print "result keys are ", results.keys()
    print "first column name", results[0]['name']
    print "first column first value ", results[0]['data'][0]
    print "second column name", results[1]['name']
    print "second column first value ", results[1]['data'][0]
    print "third column name", results[2]['name']
    print "third column first value ", results[2]['data'][0]