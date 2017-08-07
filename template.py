#!/usr/bin/env python

#############################################################
# A template for feature extraction for functions with joern.
# Author: Fabian Yamaguchi
#############################################################

from joern.all import JoernSteps

j = JoernSteps()
j.connectToDatabase()

j.addStepsDir('steps/')

statementIds = j.runGremlinQuery("queryNodeIndex('type:Function').id")

for chunk in j.chunks(statementIds, 256):
    query = """
    idListToNodes(%s).transform{ [it.id, it.name, it.functionToFeatureVec() ] }
    """ % (chunk)

    X = j.runGremlinQuery(query)
    for x in X:
        print '==='
        print 'FunctionId: %d' % (x[0]) 
        print 'FunctionName: %s' % (x[1])
        print 'Features (list): %s' % (x[2])
        print '==='
