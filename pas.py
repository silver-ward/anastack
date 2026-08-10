# formula: MA - MI
# MI = numero de erros * 2 / total de linhas
while True:

    def infer_decimal(entry):
        entry = entry.strip()
        if "," in entry:
            entry = entry.replace(",", ".")
        if len(entry) > 1 and '.' not in entry:
            whole, decimal = entry[0], entry[1:]
            return float(f"{whole}.{decimal}")
        return float(entry)

    print("\nASPECTOS MACROESTRUTURAIS\n")
    nota1 = infer_decimal(input("1 Apresentação textual: "))
    nota21 = infer_decimal(input("2.1 Apreensão e desenvolvimento do tema: "))
    nota22 = infer_decimal(input("2.2 Adequação ao tipo textual artigo de opinião: "))
    nota23 = infer_decimal(input("2.3 Coesão e coerência textuais: "))

    MA = (nota1 + nota21 + nota22 + nota23)

    print('----------')

    print("\nASPECTOS MICROESTRUTURAIS\n")
    erros = (int(input("Número de erros: "))) * 2
    linhas = int(input("Total de linhas: "))

    MI = erros / linhas

    print(f"MA: {MA}")
    print(f"MI: {MI}")
    print("\n==============================")
    print(f"||||| Nota Final: {MA - MI} |||||")
    print("==============================\n")