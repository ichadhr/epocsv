import os
import xlrd
import re
import yaml
import io
import sys


def main() :
    # load config
    config = conf()

    if config['stsb'] != False :
        stsb()
        sys.exit()
    else :
        normal()
        sys.exit()


def stsb() :
    # load config
    config = conf()

    # file config value
    if isNotBlank(config["file"]) :
        File = config["file"]
    else :
        print("file can't blank")
        sys.exit()

    # regex po config
    regex_po = "[^A-Za-z0-9]"

    # delimiter config
    Delim = ';'

    # file config value
    if isNotBlank(config["file"]) :
        File = config["file"]
    else :
        print("file can't blank")
        sys.exit()

    # PO number config
    # if isNotBlank(config["stsb_po_no"]["row"]) :
    #     row = config["stsb_po_no"]["row"]

    # if isNotBlank(config["stsb_po_no"]["column"]) :
    #     column = config["stsb_po_no"]["column"]

    DocN = DocNum(File, config["stsb_po_no"]["row"], config["stsb_po_no"]["column"])
    # DocN = str(DocN).split('.')[0]
    DocN = re.sub("[^0-9]", "", DocN)

    loopA = getRange(File, config["stsb_page1"]["startRow"], config["stsb_page1"]["endRow"], config["stsb_page1"]["column"])

    loopB = getRange(File, config["stsb_page2"]["startRow"], config["stsb_page2"]["endRow"], config["stsb_page2"]["column"])

    loopC = loopA.extend(loopB)

    for resA in zip(loopA)  :
        resA = formatSTSB(resA)

        print(resA)

def formatSTSB(soh) :
    soh = str(soh)
    soh = soh[:-3] #remove 3 char from last string
    soh = soh[3:] # remove 3 char from first string
    soh = re.split(r'\s{3,}', soh)
    barcode = re.split(r'\s{2,}', soh[0])
    tmp = re.split(r'\s{2,}', soh[2])
    qty = tmp[1]
    price = tmp[0].replace(".",'')

    result = barcode[0]+';'+price+';'+qty

    return result

def getRange(FilePath, startX, endX, y) :
    book = xlrd.open_workbook(FilePath)
    sheet = book.sheet_by_index(0)

    sX = startX - 1
    eX = endX

    data = sheet.col_values(y, start_rowx=sX, end_rowx=eX)

    return data

def normal() :
    # load config
    config = conf()

    # file config value
    if isNotBlank(config["file"]) :
        File = config["file"]
    else :
        print("file can't blank")
        sys.exit()


    # regex po config
    regex_po = "[^A-Za-z0-9]"

    # delimiter config
    Delim = ';'

    a = code_store(File, config['code_store']['row'], config['code_store']['column'])
    b = po(File, config['po_no']['row'], config['po_no']['column'])
    c = barcode(File, config['barcode']['row'], config['barcode']['column'])
    d = qty(File, config['qty']['row'], config['qty']['column'])
    e = modal_karton(File, config['modal_karton']['row'], config['modal_karton']['column'])

    DocN = DocNum(File, config['dokumen_no']['row'], config['dokumen_no']['column'])

    DocN = str(DocN).split('.')[0]
    DocN = re.sub(regex_po, "_", DocN)

    ResFile = DocN + '.csv'

    if os.path.exists(ResFile) :
        os.remove(ResFile)

    # create and open .csv file
    csv = open(ResFile, 'w+')

    # write first header
    csv.write(config['main']['code_store']+Delim+config['main']['po_no']+Delim+config['main']['barcode']+Delim+config['main']['qty']+Delim+config['main']['modal_karton'])
    csv.write('\n')

    for resA, resB, resC, resD, resE in zip(a, b, c, d, e) :
        resA = str(resA).split('.')[0]
        resB = str(resB).split('.')[0]
        resB = re.sub(regex_po, "_", resB)
        resC = str(resC).split('.')[0]
        resD = str(resD).split('.')[0]
        resE = str(resE).split('.')[0]
        print(resA+Delim+resB+Delim+resC+Delim+resD+Delim+resE)
        csv.write(resA+Delim+resB+Delim+resC+Delim+resD+Delim+resE)
        csv.write("\n")

    csv.close()


def DocNum(FilePath, x, y) :
    book = xlrd.open_workbook(FilePath)
    sheet = book.sheet_by_index(0)

    data = sheet.cell_value(rowx=x, colx=y)

    return data


def code_store(FilePath, x, y) :
    book = xlrd.open_workbook(FilePath)
    sheet = book.sheet_by_index(0)

    data = sheet.col_values(y, start_rowx=x, end_rowx=None)

    return data

def po(FilePath, x, y) :
    book = xlrd.open_workbook(FilePath)
    sheet = book.sheet_by_index(0)

    data = sheet.col_values(y, start_rowx=x, end_rowx=None)

    return data

def barcode(FilePath, x, y) :
    book = xlrd.open_workbook(FilePath)
    sheet = book.sheet_by_index(0)

    data = sheet.col_values(y, start_rowx=x, end_rowx=None)

    return data

def qty(FilePath, x, y) :
    book = xlrd.open_workbook(FilePath)
    sheet = book.sheet_by_index(0)

    data = sheet.col_values(y, start_rowx=x, end_rowx=None)

    return data

def modal_karton(FilePath, x, y) :
    book = xlrd.open_workbook(FilePath)
    sheet = book.sheet_by_index(0)

    data = sheet.col_values(y, start_rowx=x, end_rowx=None)

    return data

def conf() :
    if os.path.exists('config.yaml') :
        stream = open('config.yaml', 'r')
        config = yaml.load(stream)
        return config

    else :
        conf = open('config.ini', 'w+')
        conf.write(_config)
        conf.close()

def isNotBlank(myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return True
    #myString is None OR myString is empty or blank
    return False

if __name__== "__main__":
  main()