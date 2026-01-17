#Contexto: Um casal está organizando sua festa de casamento e precisa consolidar a lista de convidados. No entanto, ambos têm listas separadas e alguns convidados são comuns a ambos, enquanto outros são exclusivos de um dos noivos.
#O Desafio: Crie um programa que receba diversas entradas no formato Nome;QuemConvidou (onde "QuemConvidou" pode ser "noivo" ou "noiva"). O programa deve parar de ler quando a palavra ACABOU for digitada.
#Ao final, o programa deve exibir 5 listas organizadas em ordem alfabética:
#Lista Final: Todos os convidados (sem duplicatas).
#Apenas Noiva: Convidados que estão na lista da noiva, mas não na do noivo.
#Apenas Noivo: Convidados que estão na lista do noivo, mas não na da noiva.
#Por Ambos: Convidados que foram chamados tanto pelo noivo quanto pela noiva.
#Por Apenas Um Deles: Convidados que são exclusivos (chamados ou só pelo noivo ou só pela noiva, excluindo os comuns).


def convidados_noivos():
    convidados_noivo = set()
    convidados_noiva = set()
    convite = input()
    while convite != 'ACABOU':
        convidado, convidou = convite.split(';')
        if convidou == 'noivo':
            convidados_noivo.add(convidado)
        else:
            convidados_noiva.add(convidado)
        convite = input()
    return (convidados_noivo, convidados_noiva)
 
def cabecalho(frase):
    print('-' * 20)
    print(frase)
    print('-' * 20)
 
def exibe_lista(convidados, asterisco=True):
    for convidado in convidados:
        print(convidado)
    if asterisco: print('*')
 
def main():
    convidados_noivo, convidados_noiva = convidados_noivos()
 
    cabecalho('LISTA FINAL')
    exibe_lista(sorted(convidados_noivo | convidados_noiva))
 
    cabecalho('APENAS NOIVA')
    exibe_lista(sorted(convidados_noiva - convidados_noivo))
 
    cabecalho('APENAS NOIVO')
    exibe_lista(sorted(convidados_noivo - convidados_noiva))
 
    cabecalho('POR AMBOS')
    exibe_lista(sorted(convidados_noivo & convidados_noiva))
 
    cabecalho('POR APENAS UM DELES')
    exibe_lista(sorted(convidados_noivo ^ convidados_noiva), False)
 
main()
