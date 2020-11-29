import json
from os import path
import math

def writeJson(fName, data):
    with open(fName, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def cleanUpDataset(fDir, fName, limit=math.inf):
    reviews = []
    cleanName = "cleanData"
    if path.exists("./%s/%s" % (cleanName, fName)):
        return
    num = 0

    with open("./%s/%s" % (fDir, fName)) as f:
        for line in f:
            temp = json.loads(line)
            temp['reviewText'] = temp['reviewText'].lower()
            reviews.append(json.loads(line))
            num = num + 1
            if num > limit:
                break

        jsonReviews = { "reviews": reviews }
        writeJson("./%s/%s" % (cleanName, fName), jsonReviews)