# Desafio do dia: Cálculo de Bônus com Entrada do Usuário
#### Instruções:

# 1. O programa deve começar solicitando ao usuário que insira seu nome.
# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.
# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, 
# que também pode ser um número decimal.
# 4. O cálculo do KPI do bônus de 2024 é de `1000 + salario * bônus`
# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: 
# "Olá [nome], o seu valor bônus foi de 5000".

#### Exemplo de Saída:

CONSTANTE_BONUS = 1000
nome = input("Digite seu nome: ");
salario = float(input("Digite seu salario: "));
porcentagem_bonus = float(input("Digite a portecentagem do seu bonus: "));
kpi = str((CONSTANTE_BONUS + salario * porcentagem_bonus));

#
print(kpi)
print("Olá "+ nome +", o seu valor bônus foi de "+ kpi);
print(f"O usuário {nome} possui o bonus de {kpi}");

