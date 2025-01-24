while True:
    import requests


    # This function will pass your text to the machine learning model
    # and return the top result with the highest confidence
    def classify(text):
        key = "5b35d040-da10-11ef-8425-4bcff9655afc8d2f7eea-55d2-4540-9971-0f011aaf689d"
        url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

        response = requests.get(url, params={"data": text})

        if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
            return topMatch
        else:
            response.raise_for_status()

    # CHANGE THIS to something you want your machine learning model to classify
    demo = classify(input("input identifier"))

    label = demo["class_name"]
    confidence = demo["confidence"]

    # CHANGE THIS to do something different with the result
    print("'%s' with %d%% confidence" % (label, confidence))