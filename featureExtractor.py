from derivativeTrimmer import trim
from getBandPercentages import getSumOfBandsPercentages
from trimSides import trimSides


def extract(sig):
    sig = trimSides(sig, 2000, 2000)
    sig = trim(sig, 20)

    percentages = getSumOfBandsPercentages(sig)

    return percentages

def extractPercentages(sig):
    #sig = trimSides(sig, 2000, 2000)
    sig = trim(sig, 30)

    percentages = getSumOfBandsPercentages(sig)

    return percentages