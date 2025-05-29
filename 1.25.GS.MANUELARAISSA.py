#Manuela Clara Jurgens - 563730 (representante)
#Raissa Neves Costa - 566323

# 1. Entrada de Dados
tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []

criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

quantidade_desastres = int(input("Insira a quantidade de desastres: "))

# 2. Coleta de Dados para Cada Desastre
for i in range(quantidade_desastres):
    print(f"\n--- Desastre {i + 1} ---")

    tipo = input("Tipo de desastre: ")
    pais = input("País: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")

    while True:
        total = int(input("Total de pessoas afetadas: "))
        criancas_qtd = int(input("Número de crianças: "))
        adultos_qtd = int(input("Número de adultos: "))
        idosos_qtd = int(input("Número de idosos: "))
        mobilidade_qtd = int(input("Número de pessoas com mobilidade reduzida: "))
        feridos_qtd = int(input("Número de feridos: "))

        # Vendo se a soma das categorias é igual ao total de pessoas afetadas
        if criancas_qtd + adultos_qtd + idosos_qtd + mobilidade_qtd + feridos_qtd == total:
            print('Informações armazenadas com sucesso')
            break
        else:
            print("\nA soma das categorias não é igual ao total de pessoas afetadas. Entre novamente com os dados.")

