############ FUNÇÕES ##############
def mediaUnisinos(grauA, grauB):
    media = (grauA + 2* grauB) / 3.0
    return media


################ PROGRAMA PRINCIPAL ###############

grauA = float(input('Digite sua media do grau A: '))
grauB = float(input('Digite sua media do grau B: '))

grauFinal = mediaUnisinos(grauA, grauB)
print('Grau final é: ', grauFinal)
# print('Grau final é ', mediaUnisinos(grauA, grauB))