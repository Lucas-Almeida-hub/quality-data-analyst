from Class.Controle_arquivo import File_read
from Class.Analise_result import Analise_result


dir='/home/lucas/Helem/BD/Review.xlsx'



Arquivos=File_read()
Analisador = Analise_result()
 
for i in range( 3,3000):
    print (Analisador.analise(Arquivos.read(i)))
