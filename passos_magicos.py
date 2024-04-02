# Importe outras bibliotecas necessárias
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from datetime import date, timedelta
import toml
from googleapiclient.discovery import build

st.title('Datathon - Grupo 02')
st.write("***Integrantes:***")
st.write("*Bárbara Pereira Godoi*")
st.write("*Fernando Correia do Nascimento*")
st.write("*Guilherme Gentil Da Silva*")
st.write("*João Vitor Lopes Arruda*")
st.write("*William Fernandes Bento*")
st.write("---")
st.write('')

image_passos_magicos = "PassosMagicos.png"
image_missao_visao_pm = "MissaoVisaoPM.png"
image_aceleracao_conhecimento_pm = "aceleracao_conhecimento.png"
image_depoimento_01 = "depoimento_01.png"
image_depoimento_02 = "depoimento_02.png"
image_depoimento_03 = "depoimento_03.png"
image_depoimento_04 = "depoimento_04.png"
image_depoimento_intrevistador_pse_01 = "depoimento_intrevistador_pse_01.png"
image_depoimento_intrevistador_pse_02 = "depoimento_intrevistador_pse_02.png"
file_path = 'PEDE_PASSOS_DATASET_FIAP.csv'

# Carregar a chave de API do arquivo secrets.toml
secrets = toml.load('secrets.toml')
api_key = secrets['youtube']['api_key']
# Inicializar o serviço da API do YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

#Otendo o total de inscritos no canal do YouTube https://www.youtube.com/@passosmagicos700
channel_id = 'UChYs-rE3RMxFfHj47oOiOBA'
channel_response = youtube.channels().list(part='statistics', id=channel_id).execute()
total_inscritos700 = channel_response['items'][0]['statistics']['subscriberCount']

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image_passos_magicos)

st.markdown("<h1 style='text-align: center; color: Blue;'>Associação Passos Mágicos</h1>", unsafe_allow_html=True)
st.write("Rua Francisco Volante, 13 - Jd. Brasil, Embu-Guaçu – SP | CEP: 06.900-530")
st.write("**Cel:** (11) 98208-3282 | **e-mail:** passosmagicos@passosmagicos.org.br")
st.write("**Site:** https://passosmagicos.org.br/")
st.write("**Instagram:** https://www.instagram.com/passosmagicos/")
st.write("**LinkedIn:** https://www.linkedin.com/company/passosmagicos/")
st.write("**Canal do YouTube:** https://www.youtube.com/@passosmagicos700",f" (**{total_inscritos700} Inscritos.**)")
st.write("")

msg_vamos_conhecer_pm = '<p style="font-family:Arial; color:Red; font-size: 15px">Vamos conhecer um pouco sobre a ONG Passos Mágicos</p>'
st.markdown(msg_vamos_conhecer_pm, unsafe_allow_html=True)

st.image(image_missao_visao_pm)
st.write()

msg_nossa_historia_titulo = '<p style="font-family:Arial; text-align: center; color:Red; font-size: 20px;"><b>Nossa história</b></p>'
st.markdown(msg_nossa_historia_titulo, unsafe_allow_html=True)

msg_nossa_historia_texto = '<p style="font-family:Arial; text-align: center; color:black; font-size: 15px;">'
msg_nossa_historia_texto += 'A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.'
msg_nossa_historia_texto += '<br>A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.'
msg_nossa_historia_texto += '<br><i><b>Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação</b></i> que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.</p>'
st.markdown(msg_nossa_historia_texto, unsafe_allow_html=True)

st.write("---")
msg_depoimentos = '<p style="font-family:Arial; text-align: center; color:Black; font-size: 15px;"><i><b>Depoimentos enviados pelos pais após uma reunião</b></i></p>'
st.markdown(msg_depoimentos, unsafe_allow_html=True)

col1, col2  = st.columns(2)
with col1:
    st.image(image_depoimento_01)

with col2:
    st.image(image_depoimento_02)

col1, col2  = st.columns(2)
with col1:
    st.image(image_depoimento_03)

with col2:
    st.image(image_depoimento_04)    

st.write("---")
msg_depoimentos = '<p style="font-family:Arial; text-align: center; color:Black; font-size: 15px;"><i><b>Depoimentos de intrevistadores do PSE em 2020</b></i</p>'
st.markdown(msg_depoimentos, unsafe_allow_html=True)
st.image(image_depoimento_intrevistador_pse_01)
st.image(image_depoimento_intrevistador_pse_02)    
st.write("---")

col1, col2, col3  = st.columns(3)

video_urls =[
    'https://youtu.be/hT_jOmLzpH4',
    'https://youtu.be/FrbnXv8aCV4',
    'https://youtu.be/2ONPDnXCJiw'
]

with col1:
    video_id = 'hT_jOmLzpH4'
    video_response = youtube.videos().list(part='statistics', id=video_id).execute()
    total_views = video_response['items'][0]['statistics']['viewCount']
    st.video(video_urls[0])
    st.write(f'{total_views} Visualizações.')

with col2:
    video_id = 'FrbnXv8aCV4'
    video_response = youtube.videos().list(part='statistics', id=video_id).execute()
    total_views = video_response['items'][0]['statistics']['viewCount']    
    st.video(video_urls[1])
    st.write(f'{total_views} Visualizações.')

with col3:
    video_id = '2ONPDnXCJiw'
    video_response = youtube.videos().list(part='statistics', id=video_id).execute()
    total_views = video_response['items'][0]['statistics']['viewCount']       
    st.video(video_urls[2])
    st.write(f'{total_views} Visualizações.')


st.video('https://youtu.be/36ZfZQa68og')


# ID do vídeo do YouTube
video_id = '36ZfZQa68og'
video_response = youtube.videos().list(part='statistics', id=video_id).execute()
total_views = video_response['items'][0]['statistics']['viewCount']
st.write(f'{total_views} Visualizações.')

# Capturar os comentários do vídeo
response = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    maxResults=100
).execute()

# Exibir os comentários
st.title('Comentários do Vídeo')
for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']
    st.markdown(f"*{comment['authorDisplayName']}* - {comment['textOriginal']}")
    st.write('---')


st.write("")
st.image(image_aceleracao_conhecimento_pm)
url_fonte = f'[{'*Fonte: Site Passos Magicos Relatorio_de_atividades_2022*'}]({'https://passosmagicos.org.br/wp-content/uploads/2023/04/relatorio_de_atividades_2022_passosmagicos_compressed.pdf'})'
st.markdown(url_fonte, unsafe_allow_html=True)
st.write("")
st.write("---")






st.write("Analisando o arquivo PEDE_PASSOS_DATASET_FIAP.csv disponibilizado pela ONG para realização do Datathon")

font_grafico = {'family':'serif','color':'black','size':20}

df_orig = pd.read_csv(file_path, sep=';')

# Retirando da base uma linha de sujeira
df = df_orig[(df_orig.INSTITUICAO_ENSINO_ALUNO_2020 != 'V202')]

st.write("***Verificando a porcentagem de valores faltantes por coluna***")
st.write(df.isnull().mean() * 100)
st.write("---")

# Removendo duplicatas
df = df.drop_duplicates() 

# Convertendo tipos de dados, por exemplo, convertendo uma coluna para numérico
# Substitua 'IDADE_ALUNO_2020' por outras colunas conforme necessário
df['IDADE_ALUNO_2020'] = pd.to_numeric(df['IDADE_ALUNO_2020'], errors='coerce')

st.write("")
st.write("")
grafico = plt.figure(figsize=(10, 6))
sns.histplot(df['IDADE_ALUNO_2020'], kde=True, binwidth=1)
plt.title("Distribuição da Idade dos Alunos em 2020", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1, 1), ncol = 8)
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.xticks(rotation=35)
st.pyplot(grafico) 

# Convertendo INDE para numérico e tratando valores faltantes
for ano in ['2020', '2021', '2022']:
    coluna_inde = f'INDE_{ano}'
    df[coluna_inde] = pd.to_numeric(df[coluna_inde], errors='coerce').fillna(0)

# Calculando a média do INDE por ano
media_inde_por_ano = df[['INDE_2020', 'INDE_2021', 'INDE_2022']].mean()

# Plotando a evolução do INDE
st.write("")
st.write("---")

st.write("***INDE***: *Indice do Desenvolvimento Educacional – Metrica de Processo Avaliativo Geral do Aluno; Dado pela Ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV. A queda do indice em 2021 pode ter relação ao periodo de pandemia da COVID-19.*")

anos = ['2020', '2021', '2022']
grafico = plt.figure(figsize=(10, 6))
plt.plot(anos, media_inde_por_ano, marker='o', linestyle='-', color='b')
plt.title("Evolução Média do INDE ao Longo dos Anos", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1, 1), ncol = 8)
plt.xlabel("Ano")
plt.ylabel("INDE Médio")
plt.xticks(rotation=35)
st.pyplot(grafico) 

st.write("---")
st.write("Matriz de Correlação entre os Indices do Desenvolvimento Educacional nos anos de 2020 a 2022 – Metrica de Processo Avaliativo Geral do Aluno; Dado pela Ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS")
# Selecionando subconjunto de INDE 2020 a 2022 para análise de correlação
indicadores = ['INDE_2020', 'INDE_2021','INDE_2022']
correlacoes = df[indicadores].corr()

grafico = plt.figure(figsize=(6, 6))
sns.heatmap(correlacoes, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlação entre Indicadores Educacionais (INDE)", fontdict=font_grafico, weight='bold', style='italic')
plt.legend(bbox_to_anchor = (1, 1), ncol = 8)
plt.xticks(rotation=35)
st.pyplot(grafico) 

st.write("---")

st.markdown("<h1 style='text-align: center; color: grey;'>Indicador de Ponto de Virada (IPV)</h1>", unsafe_allow_html=True)

st.write("Ponto de Virada é um estagio do desenvolvimento do aluno, no qual ele demostra de forma ativa, diversas dimensões da sua trajetória dentro da Associação. O Aluno precisa estar **consciente da importancia da educação**, do valor do saber e da importância de aprender. Ele também precisa estar **integrado aos valores da Associação**, expressos pelos seus Principios e tambem deve **demonstrar capacidade emocional e acadêmica** que lhe permita aproveitar novas oportunidade de aprendizado.")

df_pv20 = df[['NOME','PONTO_VIRADA_2020']]
df_pv20['ANO'] = '2020'
df_pv20.rename(columns={'PONTO_VIRADA_2020': 'PONTO_VIRADA'}, inplace = True)
df_pv20 = df_pv20[df_pv20['PONTO_VIRADA'].notnull()]

df_pv21 = df[['NOME','PONTO_VIRADA_2021']]
df_pv21['ANO'] = '2021'
df_pv21.rename(columns={'PONTO_VIRADA_2021': 'PONTO_VIRADA'}, inplace = True)
df_pv21 = df_pv21[df_pv21['PONTO_VIRADA'].notnull()]

df_pv22 = df[['NOME','PONTO_VIRADA_2022']]
df_pv22['ANO'] = '2022'
df_pv22.rename(columns={'PONTO_VIRADA_2022': 'PONTO_VIRADA'}, inplace = True)
df_pv22 = df_pv22[df_pv22['PONTO_VIRADA'].notnull()]

df_pv = pd.concat([df_pv20,df_pv21,df_pv22])

df_pv = pd.concat([df_pv20,df_pv21,df_pv22])
df_pv['PONTO_VIRADA'] = df_pv['PONTO_VIRADA'].replace('#NULO!', 'Não')

df_pv_grp = df_pv.groupby(['ANO','PONTO_VIRADA']).size().unstack(fill_value=0)
df_pv_grp['TOTAL'] = df_pv_grp.sum(axis=1)
df_pv_grp['Sim %'] = df_pv_grp['Sim'] / df_pv_grp['TOTAL'] * 100
df_pv_grp['Não %'] = df_pv_grp['Não'] / df_pv_grp['TOTAL'] * 100

grafico, ax = plt.subplots()
df_pv_grp[['Sim %','Não %']].plot(kind='bar',ax=ax)
ax.set_xlabel('Ano')
ax.set_ylabel('Percentual (%)')
ax.set_title('Percentual de alunos que atingiram o Ponto de Virada nos anos de 2020 a 2022')

for p in ax.patches:
  width, height = p.get_width(), p.get_height()
  x, y = p.get_xy()
  ax.annotate(f'{height:.1f}%', (x + width / 2, y + height / 2), ha='center', va='center', color='black', rotation=35)

plt.xticks(rotation=35)
plt.legend(bbox_to_anchor = (1, 1), ncol = 8, title='Atingiu o Ponto de Virada', labels=['Sim','Não'])

st.pyplot(grafico)

st.write("---")
