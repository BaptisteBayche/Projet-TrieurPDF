from parse_pdf import parse_pdf


def nom(data):
    no_repeat = True
    caract = None
    i = 0
    nom = []
    for lettre in range(len(data)):
        if data[lettre] == 'M':
            if data[lettre+1] == ' ' and no_repeat:
                no_repeat = False
                while caract != ' ':
                    caract = data[lettre+2+i]
                    if  caract != ' ':
                        nom.append(caract)
                    i += 1
            elif (data[lettre+1] == 'M' and data[lettre+2] == 'E' and data[lettre+3] == ' ') or (data[lettre+1] == 'L' and data[lettre+2] == 'E' and data[lettre+3] == ' '):
                if no_repeat:
                    no_repeat = False
                    while caract != ' ':
                        caract = data[lettre + 4 + i]
                        if caract != ' ':
                            nom.append(caract)
                        i += 1
    return "".join(nom)

def annee(data):
    no_repeat = True
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for lettre in range(len(data)):
        if data[lettre] == '/':
            if data[lettre+1] in numbers and data[lettre+2] in numbers and data[lettre+3] in numbers and data[lettre+4] in numbers:
                if no_repeat:
                    no_repeat = False
                    annee = "".join([data[lettre+1],data[lettre+2],data[lettre+3],data[lettre+4]])
    return annee








