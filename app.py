# Calculadora de Consumo Elétrico
# Programa para calcular o consumo mensal de energia de um aparelho

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Verificação dos dados
if potencia > 0 and horas_dia > 0:

    # Cálculo do consumo mensal em kWh
    consumo_mensal = (potencia * horas_dia * 30) / 1000

    # Cálculo do custo estimado
    valor_kwh = 0.75
    custo_mensal = consumo_mensal * valor_kwh

    # Exibição dos resultados
    print()
    print("=" * 45)
    print("       CONSUMO DE ENERGIA ELÉTRICA")
    print("=" * 45)
    print(f"Aparelho: {aparelho}")
    print(f"Potência: {potencia:.0f} W")
    print(f"Uso diário: {horas_dia:.1f} horas")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo_mensal:.2f}/mês")
    print("=" * 45)

else:
    print("A potência e o tempo de uso devem ser maiores que zero.")
    