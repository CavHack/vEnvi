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


class State:
    """
    A stateful semaphore implemented as a set, in this case we are abstracting the concept of
    a resource container with state

    """

    def __init__(self, namespace, zero, cost, prev = None, action = None, depth = 0):