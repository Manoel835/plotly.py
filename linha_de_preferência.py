#bibliotecas, 
import plotly.graph_objects as go
import pandas as pd 

#criando os dados de preferência
nivel = ['insuportável', 'não gosto', 'aceito','gosto','apaixono']
altura = ['150', '160', '165', '170', '175']

#variável que armazena as configurações da linha de acordo com os dados
linha1 = go.Scatter(
    x = nivel,
    y = altura
    )

#nova variável para armazenar a figura do gráfico
grafico = go.Figure(linha1)

grafico.show()
