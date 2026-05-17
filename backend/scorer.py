def classify(score):
    if score < 0.30:
        return "SAFE"
    elif score < 0.65:
        return "SUSPICIOUS"
    else:
        return "MALICIOUS"
