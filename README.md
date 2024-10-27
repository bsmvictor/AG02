# Classificação de Canais de Vendas com Machine Learning
Este projeto aplica técnicas de aprendizado de máquina para classificar transações de clientes de um distribuidor atacadista, identificando o canal de vendas ao qual cada transação pertence: HoReCa (hotel, restaurante ou café) ou Retail (varejo).

## Descrição do Projeto
Usando o conjunto de dados "Wholesale Customers", o modelo utiliza os gastos anuais dos clientes em diversas categorias de produtos (como frescos, laticínios, mercearia, etc.) para prever o canal de vendas da transação. Este projeto usa o classificador k-Nearest Neighbors (k-NN) com k=7, que foi testado como o valor que produz a maior precisão neste caso.

## Video de apresentação:

## Estrutura do Projeto
- **AG2.py**: Script principal que:
  - Carrega e processa o conjunto de dados.
  - Treina o modelo de classificação.
  - Avalia a precisão do modelo.
  - Permite a classificação de novos dados inseridos pelo usuário.

- **wholesale.csv**: Conjunto de dados contendo informações sobre transações de clientes e o canal de vendas associado.


## Instalação
1. Clone este repositório. 
2. Instale as bibliotecas necessárias:
```
pip install pandas scikit-learn termcolor
```
3. Execute o script:
```
python Victor_Boaventura_GEC_1807.py
```

## Uso
1. Execute o script principal `Victor_Boaventura_GEC_1807.py`.
2. O modelo exibirá as métricas de avaliação (como precisão e recall) para o conjunto de teste.
3. Em seguida, o script permitirá que você insira detalhes de uma transação para classificação. Insira os valores conforme solicitado, e o modelo retornará o canal de vendas previsto (HoReCa ou Retail).
   
## Estrutura dos Dados de Entrada
- Region: Região onde a venda foi realizada (0 = Lisbon, 1 = Oporto, 2 = Other).
- Fresh: Gasto anual em produtos frescos.
- Milk: Gasto anual em laticínios.
- Grocery: Gasto anual em produtos de mercearia.
- Frozen: Gasto anual em produtos congelados.
- Detergents_Paper: Gasto anual em detergentes e papel.
- Delicatessen: Gasto anual em delicatessen.
  
## Exemplo de Execução
```
Insira os detalhes da transação:
Região (0 para Lisbon, 1 para Oporto, 2 para Other): 1
Gasto anual em produtos frescos (em u.m.): 3000
Gasto anual em produtos de laticínios (em u.m.): 8000
Gasto anual em produtos de mercearia (em u.m.): 12000
Gasto anual em produtos congelados (em u.m.): 500
Gasto anual em detergentes e papel (em u.m.): 3000
Gasto anual em produtos de delicatessen (em u.m.): 1000

O canal de vendas previsto para a transação é: Retail
```
## Casos de Teste
### 1. HoReCa:
- Região: 2
- Fresh: 15000
- Milk: 3000
- Grocery: 2000
- Frozen: 5000
- Detergents_Paper: 600
- Delicatessen: 1000
- Resultado Esperado: HoReCa
  
 ### 2. Retail:
- Região: 1
- Fresh: 2000
- Milk: 7000
- Grocery: 12000
- Frozen: 800
- Detergents_Paper: 3500
- Delicatessen: 800
- Resultado Esperado: Retail
  
## Modelo Utilizado
Este projeto utiliza o algoritmo `k-Nearest Neighbors (k-NN)` com `k=7`, escolhido após testar diferentes valores para `k` e comparar a precisão resultante. O modelo foi avaliado com uma precisão de 88% no conjunto de dados de teste.

## Referências
Conjunto de Dados: [Wholesale Customers Data Set](https://archive.ics.uci.edu/dataset/292/wholesale+customers)

Documentação do scikit-learn: [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
