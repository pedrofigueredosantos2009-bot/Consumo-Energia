nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo medio de uso diario em horas: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

custo = consumo_mensal * 0.75

print("Resultado")
print("Aparelho:", nome_aparelho)
print("Consumo mensal:", consumo_mensal, "kWh")
print("valor: RS",custo)