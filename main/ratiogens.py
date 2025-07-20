# Projecto: DIMENSIONADOR DE GERADOR


# Importa bibliotecas necessárias
import datetime

def inserir_equipamento():
    equipamentos = []
    n = int(input("Quantos equipamentos deseja inserir? "))

    for i in range(n):
        print(f"\nEquipamento {i+1}:")
        nome = input("Nome: ")
        tipo = input("Tipo (iluminacao/motor/equipamento comum/sensível): ").lower()
        potencia = float(input("Potência (W): "))
        quantidade = int(input("Quantidade: "))
        tempo_uso = float(input("Horas de uso por dia (opcional - 0 se desconhecido): "))

         # Factor de arranque para motores (multiplica a potência por 2.5)
        if tipo == "motor":
            potencia *= 2.5

        equipamentos.append({
            "nome": nome,
            "tipo": tipo,
            "potencia": potencia,
            "quantidade": quantidade,
            "tempo_uso": tempo_uso
        })

    return equipamentos

def calcular_potencia_total(equipamentos):
    total = 0
    for e in equipamentos:
        total += e['potencia'] * e['quantidade']
    return total