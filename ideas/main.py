import json
import numpy as np
import tensorflow as tf
import time
from jsonHelpers import cleanUpDataset

start_time = time.time()
cleanUpDataset("data", "Electronics_5.json")
print("%s data read time seconds" % (time.time() - start_time))
