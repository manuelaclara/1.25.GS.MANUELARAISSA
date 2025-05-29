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

    # Armazenando as informações nas listas
    tipos_desastres.append(tipo)
    paises.append(pais)
    cidades.append(cidade)
    bairros.append(bairro)
    ruas.append(rua)
    total_afetados.append(total)

    criancas.append(criancas_qtd)
    adultos.append(adultos_qtd)
    idosos.append(idosos_qtd)
    mobilidade_reduzida.append(mobilidade_qtd)
    feridos.append(feridos_qtd)

# 3. Análise de Dados

# a. Total de desastres registrados
print(f"\nTotal de desastres registrados: {quantidade_desastres}")

# b. Calcular o total geral de pessoas afetadas
total_pessoas_geral = sum(total_afetados)

# c. Calcular o total de pessoas em cada categoria
total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mob_reduzida = sum(mobilidade_reduzida)
total_feridos = sum(feridos)

# d. Identificar a categoria mais afetada
categorias = {
    "Crianças": total_criancas,
    "Adultos": total_adultos,
    "Idosos": total_idosos,
    "Mobilidade reduzida": total_mob_reduzida,
    "Feridos": total_feridos
}

categoria_mais_afetada = max(categorias, key=categorias.get)
print(categoria_mais_afetada)

# e. Identificar o desastre com maior número de afetados
print(total_pessoas_geral)
indice_max_afetados = total_afetados.index(max(total_afetados))
print(indice_max_afetados)

# 4. Relatório de Resultados

# Exibindo o Relatório
print("\nRelatório de Resultados:")
print(f"\nTotal de desastres registrados: {quantidade_desastres}")
print(f"Total geral de pessoas afetadas: {total_pessoas_geral}")
print(f"\nResumo de pessoas afetadas por categoria:")
print(
    f"Crianças: {total_criancas} | Adultos: {total_adultos} | Idosos: {total_idosos} | Mobilidade reduzida: {total_mob_reduzida} | Feridos: {total_feridos}")
print(f"\nCategoria mais afetada: {categoria_mais_afetada}")
print(f"\nDesastre com maior número de afetados:")
print(f"Tipo: {tipos_desastres[indice_max_afetados]}")
print(
    f"Local: {ruas[indice_max_afetados]}, {bairros[indice_max_afetados]}, {cidades[indice_max_afetados]}, {paises[indice_max_afetados]}")


