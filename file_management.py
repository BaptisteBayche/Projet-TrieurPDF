from data_useful import nom, annee
from parse_pdf import parse_pdf
import box_message
import os
import shutil


def file_management(pathfile,pathselect,name_file):

    message = box_message.Message()
    message.set_namefile(name_file)
    try:
        os.mkdir(pathselect + '\\'+  nom(parse_pdf(pathfile)))
    except:
        pass
    try:
        os.mkdir(pathselect + '\\'+ nom(parse_pdf(pathfile)) + '\\' + annee(parse_pdf(pathfile)))
    except:
        pass
    try:
        shutil.copy(pathfile,pathselect +'\\'+  nom(parse_pdf(pathfile)) + '\\' + annee(parse_pdf(pathfile)) + '\\' + name_file)
        message.box_succes()
    except:
        message.box_error()




