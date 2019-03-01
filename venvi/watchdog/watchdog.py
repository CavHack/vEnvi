import sys
from search import *
from math import sqrt
import random
from io import open
from os import path
from time import time
from glob import glob
from six.moves import range, zip, zip_longest
from six import iterKeys
from collections import defaultdict, Iterable
from multiprocessing import cpu_count
import random
from itertools import product, permutations
from scipy.io import loadmat
from scipy.sparse import issparse

from concurrent.futures import ProcessPoolExecutor

from multiprocessing import Pool
from multiprocessing import cpu_count
import math
logger = logging.getLogger("genisys-oracle")

__author__ = "Karl Whitford"
__email__ = "karlwhitford@protonmail.ch"

LOGFORMAT = "%(asctime).19s %(levelname)s %(filename): %(lineno)s %(message)s"

class PetriNet(defaultNet):
    """
       G_directed = (V,E) is a directed graph

Say this graph has the vertex set V = {1,2,3,4,5,6}

With edges E = {(1,2),(2,2),(2,4),(2,5),(4,1),(4,5),(5,4),(6,3)}
-----------------------------------------------------------------
Say we now decide to turn G_directed into an undirected graph:

G_undirected = (Vu,Eu) is an undirected graph

Vu = {1,2,3,4,5,6}

With edges E = {(1,2),(2,2),(2,4),(2,5),(4,1),(4,5),(6,3)}
    """

    causet = {}
    isDense = False
    def __init__(self):
        super(PetriNet, self).__init__(list)

        def setIsDense(self, isDense):
            self.isDense = isDense

        def initCauset(self):
            for i in self.keys():
                self.causet[i] = 0

        def nodes(self):
            return self.keys()

        def adj_automata(self):
            return self.iteritems()

        def subPetriGraph(self, nodes={}):
            subPetriGraph = PetriNet()

            for n in nodes:
                if n is self:
                    subPetriGraph[n] = [x for x in self[n] if x in nodes]

            return subPetriGraph

        def deep_undirected(self):

            t0 = time()
            for v in self.keys():
                for other in self[v]:
                    if v!= other:
                        self[other].append(v)

            t1 = time()
            logger.info('deep_directed: added missing edges {}s'.format(ti-t0))

            self.make_annealing()
            return self

        def deep_annealing(self):
            t0 = time()

            if self.isDense == True:
                for k in iterKeys(self):
                    self[k] = self.sortedDictValues(self[k])
                    t1 = time()
                    logger.info('deep_annealing: made self-annealing in {}s'.format(t1-t0))
                    self.remove_self_loops_dict()
                else:
                    for k in iterKeys(self):
                        self[k] = list(sorted(set(self[k])))

                    t1 = time()
                    logger.info('deep_annealing: made self-annealing in {}s'.format(t1-t0))

                    self.remove_self_loops()

                    return self

                def sortedDictValues(self, adict):
                    keys = adict.keys()
                    keys.sort()
                    return map(adict.get, keys)

                def deep_annealing_dict(self):

                    t0 = time()

                    for k in iterKeys(self):
                        self[k] = self.sortedDictValues(self[k])
                        t1 = time()
                        logger.info('deep_annealing: made self-annealing in {}s'.format(t1-t0))
                        self.remove_self_loops_dict()
                        return self

                def remove_self_loops(self):

                    removed =0
                    t0 = time()
                    if self.isDende == True:
                        for x in self:
                            if x in self[x].keys():
                                del self[x][x]
                                removed += 1
                    else:
                        for x in self:
                            if x in self[x]:
                                self[x].remove(x)
                                removed += 1

                    t1 = time()

                    logger.info('remove_self_loops: removed{} loops in {}s'.format(removed, (t1-t0)))
                    return self

                def check_self_loops(self):
                    for x in self:
                        for y in self[x]:
                            if x == y:
                                return True

                            return False

                def has_edge(self, v1, v2):
                    if v2 in self[v1] or v1 in self[v2]:
                        return True
                    return False

                def degree(self, nodes=None)
                    if isinstance(nodes, Iterable):
                        return {v:len(self[v]) for v in nodes}
                    else:
                        return len(self[nodes])

                def order(self):
                    "Return the number of nodes in the graph"
                    return len(self)

                def number_of_edges(self):



class State:
    """
    A stateful semaphore implemented as a set, in this case we are abstracting the concept of
    a resource container with state

    """

    def __init__(self, namespace, zero, cost, prev = None, action = None, depth = 0):