import pandas as pd

#importar base de dados de irradiação
tabela_irradiacao = pd.read_excel('irradiacao.xlsx')
df = tabela_irradiacao

#visualizar base de dados de irradiação (FI)
pd.set_option('display.max_columns', None)

#inserir localização da residencia (cidade/uf)
state = (input('Qual o estado (UF) que você mora? '))

#localizar o valor de FI na tabela_irradiação com o nome da cidade
if state == 'ACRE':
    fator_irradiacao = df.loc[0, "ANNUAL"]
elif state == 'ALAGOAS':
    fator_irradiacao = df.loc[1, "ANNUAL"]
elif state == 'AMAPA':
    fator_irradiacao = df.loc[2, "ANNUAL"]
elif state == 'AMAZONAS':
    fator_irradiacao = df.loc[3, "ANNUAL"]
elif state == 'BAHIA':
    fator_irradiacao = df.loc[4, "ANNUAL"]
elif state == 'CEARA':
    fator_irradiacao = df.loc[5, "ANNUAL"]
elif state == 'DISTRITO FEDERAL':
    fator_irradiacao = df.loc[6, "ANNUAL"]
elif state == 'ESPIRITO SANTO':
    fator_irradiacao = df.loc[7, "ANNUAL"]
elif state == 'GOIAS':
    fator_irradiacao = df.loc[8, "ANNUAL"]
elif state == 'MARANHÃO':
    fator_irradiacao = df.loc[9, "ANNUAL"]
elif state == 'MATO GROSSO':
    fator_irradiacao = df.loc[10, "ANNUAL"]
elif state == 'MATO GROSSO DO SUL':
    fator_irradiacao = df.loc[11, "ANNUAL"]
elif state == 'MINAS GERAIS':
    fator_irradiacao = df.loc[12, "ANNUAL"]
elif state == 'PARÁ':
    fator_irradiacao = df.loc[13, "ANNUAL"]
elif state == 'PARAÍBA':
    fator_irradiacao = df.loc[14, "ANNUAL"]
elif state == 'PARANÁ':
    fator_irradiacao = df.loc[15, "ANNUAL"]
elif state == 'PERNAMBUCO':
    fator_irradiacao = df.loc[16, "ANNUAL"]
elif state == 'PIAUÍ':
    fator_irradiacao = df.loc[17, "ANNUAL"]
elif state == 'RIO DE JANEIRO':
    fator_irradiacao = df.loc[18, "ANNUAL"]
elif state == 'RIO GRANDE DO NORTE':
    fator_irradiacao = df.loc[19, "ANNUAL"]
elif state == 'RIO GRANDE DO SUL':
    fator_irradiacao = df.loc[20, "ANNUAL"]
elif state == 'RONDONIA':
    fator_irradiacao = df.loc[21, "ANNUAL"]
elif state == 'RORAIMA':
    fator_irradiacao = df.loc[22, "ANNUAL"]
elif state == 'SANTA CATARINA':
    fator_irradiacao = df.loc[23, "ANNUAL"]
elif state == 'SÃO PAULO':
    fator_irradiacao = df.loc[24, "ANNUAL"]
elif state == 'SERGIPE':
    fator_irradiacao = df.loc[25, "ANNUAL"]
else:
    fator_irradiacao = df.loc[26, "ANNUAL"]

#inserir quantos reais gasta com energia elétrica
conta_luz = float((input('Qual o valor da sua conta de Energia? ')))

#inserir taxa de iluminação pública
ip_luz = float((input('Qual o valor da sua Taxa de Iluminação Pública (IP)? ')))

#calculando quantidade de painéis (media de kwh/30*FI*0,98)
potencia_projeto = float((conta_luz*0.89))/(30*0.98*fator_irradiacao)

#calculando potencia kwp do sistema
qtde_paineis = float((potencia_projeto/0.545))

#calculando custo do projeto (4,9 R$/wp)
custo_projeto = round((potencia_projeto*4900))
print ('O custo do Projeto é de aproximadamente R$',custo_projeto)
