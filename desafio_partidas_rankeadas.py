def fraseFinal(nivel):
    print(f'O Herói tem o saldo de {resultado} e está no nível de {nivel}.')

def saldoVitorias(vitorias, derrotas):
    saldo = vitorias - derrotas
    return saldo

resultado = saldoVitorias(150, 75)

if resultado < 10:
    fraseFinal('Ferro')
elif 10 < resultado <= 20:
    fraseFinal('Bronze')
elif 20 < resultado <= 50:
    fraseFinal('Prata')
elif 50 < resultado <= 80:
    fraseFinal('Ouro')
elif 80 < resultado <= 90:
    fraseFinal('Diamante')
elif 90 < resultado <= 100:
    fraseFinal('Lendário')
elif resultado > 100:
    fraseFinal('Imortal')