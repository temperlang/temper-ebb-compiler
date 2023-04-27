import logging
import sys
import faulthandler

faulthandler.enable(file=sys.stderr, all_threads=True)

logging.basicConfig(filename="/dev/stdout", level=logging.DEBUG, format="%(message)s")

from ebb.interp import Env

def read(name):
    with open(name) as f:
        return f.read()

env = Env()

env.source(read("ebb.ebb"))
env.call("main-lang", (sys.argv[1], read(sys.argv[2])))
