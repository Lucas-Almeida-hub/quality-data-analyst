


negativa=['Horrível','negativo','ruin','feia','barulho','Barulho','mancha','frágil','sujeira']
positivo=['ótima','melhor','otima','Ótimo','indico','expectativa','Superou','Recomendo','bom','boa','gostei','excelente','Adorei','completa','Bom','recomendo','rápido','silenciosa','satisfeito','Excelente']
invertida=['não']



class Analise_result:
       
        def __init__(self) -> None:
            pass
    
        
        def analise(self,frase):

            global negativa
            global positivo

            ResultAnalise=0

            for i in range(len(negativa)):
                if negativa[i] in frase:
                    ResultAnalise=ResultAnalise-1

            for i in range(len(positivo)):
                if positivo[i] in frase:
                    ResultAnalise=ResultAnalise+1
                

            if (ResultAnalise >0):
                return("Positivo")
            elif(ResultAnalise < 0):
                return("Negativo")
            elif(ResultAnalise==0):
                return("Indefinido")
        


# teste=Analise_result()

# kkk = 'Lavadora excelente, cumpre o que promete.'


# print(teste.analise())
