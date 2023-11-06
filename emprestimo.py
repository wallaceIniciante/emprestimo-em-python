from datetime import datetime
from dateutil.relativedelta import relativedelta


def tela(text):
    print('#'*20)
    print('#'*5,text,'#'*5)
    print('#'*20)

impostos = 3
emprestimo = 0
total_parcelas = 0
valor_parcela = 0
data_emprestimo = 0
data_final = 0
taxa_emprestimo = 10

dados_corretos = True

while dados_corretos:

    tela('VALOR DO EMPRESTIMO')

    emprestimo = float(input('Valor: '))

    if emprestimo <= 0:
        print('Digite um valor valido')
        continue

    tela('TOTAL DE ANOS')
    
    total_parcelas = int(input(': '))

    if total_parcelas < 0:
        print('Digite valor valido')
        continue

    data_emprestimo = datetime.now()

    break


percentual_taxa = (emprestimo / 100) * taxa_emprestimo
total_a_pagar = emprestimo + percentual_taxa
data_final = data_emprestimo + relativedelta(years=total_parcelas)
valor_parcela = total_a_pagar / (total_parcelas * 12)
lista_parcelas = []
data_parcela = data_emprestimo



while data_parcela < data_final:
    lista_parcelas.append(data_parcela.date()) 

    data_parcela += relativedelta(months=+1)


print()
print(f'EMPRESTIMO: {emprestimo}')
print(f'TOTAL A PAGAR: {total_a_pagar}')
print()

for data in lista_parcelas:
    print(f'Vencimento: {data} - Parcela: {valor_parcela:.2f}')






