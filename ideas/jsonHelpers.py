import json

def writeJson(fName, data):
    with open(fName, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def cleanUpDataset(fDir, fName):
    reviews = []
    cleanName = "cleanData"
    with open("./%s/%s" % (fDir, fName)) as f:
        for line in f:
            reviews.append(json.loads(line))
        jsonReviews = { "reviews": reviews }
        writeJson("./%s/%s" % (cleanName, fName), jsonReviews)