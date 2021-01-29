from bs4 import BeautifulSoup
import lxml



#This module parses any MENOTA XML file. You can use the "getInfo" function to get very basic info about the MS from the XML. The "getText" function returns all words of the text in their normalized, diplomatic and facsimile forms, as well as lemmatized.


def read_tei(tei_file):
    with open(tei_file, 'r', encoding="UTF-8") as tei:
        soup = BeautifulSoup(tei, from_encoding='UTF-8')
        return soup

def getInfo (soup):
    msInfo = soup.find("sourceDesc")
    msAbbreviation = msInfo.msDesc.idno.get_text()  # This is the shelfmark, signature or other identifier of the physical manuscript
    msAbbreviation = msAbbreviation.replace(" ", "")
    wittnessName = msInfo.msDesc.msName.get_text() # Name of the text witness, not the MS itself misleadingly
    return msAbbreviation, wittnessName

def getText(soup):
    allWords = soup.findAll('w')

    normList = []
    facsList = []
    diplList = []
    lemmaList = []

    for word in allWords:
        lemming = word.get('lemma')
        if lemming is not None:
            lemming = word.get('lemma')
        else:
            lemming = "-"
        facsRaw = word.find('me:facs')
        if facsRaw is not None:
            facsClean = facsRaw.get_text()
        else:
            facsClean = "-"
        diplRaw = word.find('me:dipl')
        if diplRaw is not None:
            diplClean = diplRaw.get_text()
        else:
            diplClean = "-"
        normRaw = word.find('me:norm')
        if normRaw is not None:
            normClean = normRaw.get_text()
        else:
            normClean = "-"

        normList.append(normClean)
        facsList.append(facsClean)
        diplList.append(diplClean)
        lemmaList.append(lemming)
    return normList, facsList, diplList, lemmaList