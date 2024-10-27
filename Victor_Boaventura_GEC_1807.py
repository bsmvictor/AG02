import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from termcolor import colored

# Carregar o conjunto de dados de clientes atacadistas
data = pd.read_csv("wholesale.csv", encoding="utf-8")

# Mapear valores de texto para valores numéricos nas colunas 'Channel' e 'Region'
data["Channel"] = data["Channel"].replace({"HoReCa": 0, "Retail": 1})
data["Region"] = data["Region"].replace({"Lisbon": 0, "Oporto": 1, "Other": 2})

# Reordenar colunas conforme o formato especificado
data = data[['Region', 'Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicatessen', 'Channel']]

# Dividir o conjunto de dados em conjuntos de treinamento (80%) e teste (20%)
train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)

# Separar atributos (características) e rótulos (classes) para treinamento e teste
X_train = train_set.drop("Channel", axis=1)
y_train = train_set["Channel"]
X_test = test_set.drop("Channel", axis=1)
y_test = test_set["Channel"]

# Inicializar o classificador k-Nearest Neighbors com k=7
knn_classifier = KNeighborsClassifier(n_neighbors=7)

# Treinar o modelo k-NN com os dados de treinamento
knn_classifier.fit(X_train, y_train)

# Fazer previsões usando o conjunto de teste
y_pred = knn_classifier.predict(X_test)

# Exibir o relatório de desempenho do classificador k-NN
print(colored("\nRelatório de Desempenho do k-NN com k=7:\n", 'red'))
print(colored(classification_report(y_test, y_pred), 'green'))

# Função para inserir dados personalizados e prever o canal de vendas
def classify_custom_transaction():
    print(colored("\nInsira os detalhes da transação para classificação:", 'red'))

    # Função para validar a entrada da região
    def get_valid_region():
        while True:
            try:
                region = int(input(colored("\n\tRegião (0 para Lisbon, 1 para Oporto, 2 para Other): ", 'blue')))
                if region in [0, 1, 2]:
                    return region
                else:
                    print(colored("\tPor favor, insira um valor válido (0, 1 ou 2).", 'red'))
            except ValueError:
                print(colored("\n\tEntrada inválida. Por favor, insira um número inteiro.", 'red'))	

    # Receber valores de entrada do usuário para cada atributo
    region = get_valid_region()
    def get_valid_float(prompt):
        while True:
            try:
                return float(input(colored(prompt, 'blue')))
            except ValueError:
                print(colored("\n\tEntrada inválida. Por favor, insira um número." + '\n', 'red'))

    fresh = get_valid_float("\tGasto anual em produtos frescos (em u.m.): ")
    milk = get_valid_float("\tGasto anual em produtos de laticínios (em u.m.): ")
    grocery = get_valid_float("\tGasto anual em produtos de mercearia (em u.m.): ")
    frozen = get_valid_float("\tGasto anual em produtos congelados (em u.m.): ")
    detergents_paper = get_valid_float("\tGasto anual em detergentes e papel (em u.m.): ")
    delicatessen = get_valid_float("\tGasto anual em produtos de delicatessen (em u.m.): ")

    # Organizar os dados de entrada em um DataFrame para previsões
    user_data = pd.DataFrame([[region, fresh, milk, grocery, frozen, detergents_paper, delicatessen]],
                             columns=['Region', 'Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicatessen'])

    # Fazer a previsão com o modelo treinado
    prediction = knn_classifier.predict(user_data)

    # Mapear a previsão para o nome do canal de vendas
    channel_mapping = {0: "HoReCa", 1: "Retail"}
    predicted_channel = channel_mapping[prediction[0]]

    # Exibir o resultado da previsão ao usuário
    print(colored("\nO canal de vendas previsto para a transação é: ", 'red') + colored(predicted_channel, 'white') + "\n")

# Chamar a função para permitir a entrada de dados pelo usuário
classify_custom_transaction()
