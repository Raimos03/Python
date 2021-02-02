
'''# -*- coding: utf-8 -*-
Created on Fri Nov 20 02:10:56 2020

@author: Pedro Henrique Lima

Executado em: Visual Code e Spyder

Análise de Carros na planilha DadosCarros2020
Todos os dados foram obtidos pela internet sedo assim, deve-se considerar uma margem de
erro das informações. O resultado é aproximado.
'''
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
#import matplotlib.pyplot as plt


pd.set_option("display.max_rows",300)
pd.set_option("display.max_columns",300)

dfCarros=pd.read_excel('DadosCarros2020.xlsx',header=0,index_col=0)


print("---------------------------------------------------------")

print('Tratando índices duplicados')
print("1) Renomeie os índices duplicados acrescentando a quantidade ao seu índice de ocorrência.")
print("Exiba os 5 primeiros elementos com o mesmo índice, corrija a repetição e depois mostra a tabela de frequencia novamente. \n")
print("\n-------------------------------------------------------")

#ex :
#   carro a: carro a 1
#   carro a: carro a 2
#   carro a: carro a 3


frind=dfCarros.index.value_counts()
print(frind.head(5))

lrep=list(frind.loc[frind>1].index.values)

dtfab=dfCarros['Fabricação']

lind=list(dfCarros.index.values)            

v=True
i=0

for el in lrep:
    
    while v==True:
        
        i+=1
        if el in lind:
            
            pos=lind.index(el)
            nind=el +' '+ str(i)
            lind[pos]=nind
            
        else:
            v=False
                
dfCarros.index=lind         
print(dfCarros.index.value_counts().head(5))


print("-------------------------------------------------------")

print("2) Quais os 5 primeiros e 5 ultimos itens da tabela ? \n")

print(dfCarros.head(5),dfCarros.tail(5))

print("-------------------------------------------------------")

print("\n-----------------------------------------------------")
print("3) Existem valores ausentes na tabela ? Como podemos trata-los?"
     ' Crie uma copia de dfCarros chamada dfCarse sem os veículos elétricos e preencha os valores ausentes de dfCarros com a media da categoria. \n')
#         Crie uma copia de dfCarros chamada dfCarse sem os veículos elétricos e preencha os valores ausentes de dfCarros com a media da categoria. \n")
#
#       Nas categorias Esportivo e Super esportivo os valores devem ter o valor da coluna
#       Alcool com NaN substituídos para o valor 0.
#       Para a categoria OffRoad o valor deve ser substituído pela média da categoria.
print("\n-----------------------------------------------------") 

def preenche(g):
    
    #print('------',g)
    
    if (g.name=='Esportivo') or (g.name=='Super Esportivo'):
    
        g.fillna({'Alcool':0},inplace=True)
    else:
        g.fillna(g.mean(),inplace=True)
    
    #print(g)
    return g



dfCarse=dfCarros.loc[(dfCarros['Combustivel']!='híbrido') & (dfCarros['Combustivel']!='eletricidade' )]
dfaCarros=dfCarse.copy()

agcat=dfCarse.groupby('Categoria')
dfCarse=agcat.apply(preenche)

dfCarse.fillna(0,inplace=True)

print("\n-------------------------------------------------------")
print("\n-------------------------------------------------------")

print("4) Qual a média de consumo dos carros e o combustivel predominante em cada categoria?")
#
#       Na categoria Offroad, exiba Diesel ao invés de gasolina por que o consumo 
#       foi representado na gasolina para nao ter que criar uma nova coluna
#
print("\n-----------------------------------------------------")
def combstpred(g):
    
    scombst=g['Combustivel'].value_counts()
    
    dtmedia=g.mean()
    #print(dtmedia)
    
    if dtmedia['Alcool']==0:
        print('\n----- Categoria :',g.name,'\n')
        dtmedia.drop(labels=['Alcool'],inplace=True)
    
        if g.name=='Offroad':
        
    
            dtmedia.rename({'Gasolina':'Diesel'},axis=0,inplace=True)
        
    else:
        print('\n----- Categoria :',g.name,'\n')
    
    print(scombst.idxmax())      
    print(dtmedia)
    
    return 


dfCarsesel=dfCarse[['Combustivel','Alcool','Gasolina','Categoria']]
agsel=dfCarsesel.groupby('Categoria')
agsel.apply(combstpred)


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")

print("5) Qual modelo de carro é mais econômico usando Alcool ? E usando Gasolina ? Mostre seus respectivos valores.")


dtcombst=dfCarsesel[['Alcool','Gasolina','Categoria']]
agc=dtcombst.groupby('Categoria')


print(agc.agg(['idxmax']))
print(agc.agg(['max']))


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")

print("6) Sabendo que o índice de velocidade/potência pode ser um indicador de desempenho, crie a series sVelPot e responda, qual a sua mediana?"
     "Exiba a series e coloque-a em ordem decrescente exibindo os 10 primeiros.")
print("\n-----------------------------------------------------")

sVelPot=dfCarros['VelMaxima']/dfCarros['Potencia']

print('\nMediana:',sVelPot.median(),'\n')

print(sVelPot.sort_values(ascending=False).head(10))


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("7) Crie uma coluna baseada na ordem da VelPot e a preencha com a respectiva categoria do modelo. Retire os NAN  e Exiba os 30 primeiros em ordem decrescente")
print("\n-----------------------------------------------------")

stemp=dfCarsesel['Categoria']
dfvelpot=pd.concat([sVelPot,stemp],axis=1).rename({0:'Vel/Pot'},axis=1)
dfvelpot.dropna(inplace=True)
print(dfvelpot.sort_values(by='Vel/Pot', ascending=False).head(30))


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")

print("8) Como sabemos a categoria, o valor médio, maximo e minimo de cada grupo?"
     ' Exiba o Data Frame anterior por categoria com o valor medio, maximo, minimo para cada grupo e o melhor modelo.')
print("\n-------------------------------------------------------")     
      
#dfvelpot.sort_values(by=['Categoria'], inplace=True)
def exibecat(g):
    
    sr=g.sort_values(by='Vel/Pot',ascending=False).drop('Categoria',axis=1)
   
    print('\n----- Categoria:', g.name,'\n')
    #print(sr,'\n')
    print(sr.agg(['mean','max','min']).T)   
    print('Melhor modelo:{}'.format(sr.idxmax().values[0]))
    return

agvelpot=dfvelpot.groupby('Categoria')
agvelpot.apply(exibecat)


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("9) Podemos categorizar os veiculos por desempenho?"
      'Categorize o dfCarros criando a serie sDesemp por potencia, utilizando:(0 a 200, 200 a 300 e 300 ou mais), use os nomes: Padrão, Desempenho e Super Desempenho respectivamente') 
print('Exiba os 20 ultimos')
print("\n-------------------------------------------------------")

sDesemp=pd.cut(dfCarse['Potencia'],bins=[0,200,300,dfCarse['Potencia'].max()],labels=['Padrão','Desempenho','Super Desempenho'])
print(sDesemp.tail(20))

print("\n-------------------------------------------------------")
print('----- Visualizações ------')

print("10) Exiba o grafico de frequencia por Desempenho dos carros") 
print("\n-------------------------------------------------------")

sDesemp.value_counts().plot.bar(figsize=(12,8), title=' Quantidade por Desempenho')
plt.show()

print("\n-------------------------------------------------------")


print("\n-------------------------------------------------------")
print("11) Podemos visualizar a porcentagem de cada combustível no total de carros?"
      " Exiba com grafico de pizza a porcentagem do tipo de combustivel por carros.")
print("\n Exiba tambem com grafico de barras o consumo de combustivel por categoria.")
print("\n-----------------------------------------------------")

print('----- Pelo total de carros -----')
print('--------------------------------')

dtcomb=dfCarros['Combustivel'].value_counts()
dtcomb.plot.pie(title='Combutivel Por Total de Carros',autopct="%.1f",figsize=(12,8))
plt.show()


def catcombustivel(g):
    
    g[['Alcool','Gasolina']]
   
    #print(g)   
    return g


srcomb_cat=agc.apply(catcombustivel)

srcomb_cat.reset_index(inplace=True)
srcomb_cat.set_index('Categoria',inplace=True)

srcomb_cat.sort_index().plot.bar(title='Combutivel por categoria',figsize=(12,8))
plt.show()


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("12) Exiba a  media, mediana, o valor maximo e modelo do veículo pelo Peso e  Potencia por tipo de desempenho") 
print("\n-------------------------------------------------------")


agDesemp=dfCarse.groupby(sDesemp)
#agDesemp.apply(pesocat)

print(agDesemp['Peso','Potencia'].agg(['mean','median','max','idxmax']))

print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("13)Como observamos o consumo médio das marcas?"
      " Mostre através do grafico de linha o consumo medio por cada marca.") 
print("\n-------------------------------------------------------")


def exibe2g(g):
    
    #print(g)
    gt=g[['Alcool','Gasolina','Marca']]
    
    gt.reset_index(inplace=True)
    gt.set_index(g['Fabricação'],inplace=True)
  
    #print('------',gt.mean())
    #print('*******',gt)
    return gt.mean()

agmarca=dfCarse.groupby('Marca')
smarcaconsumo=agmarca.apply(exibe2g)
smarcaconsumo.plot(figsize=(12,8))
plt.show()

print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("14) Mostre através do grafico de linhas o consumo das marcas por ano da categoria hatch."
      "Exiba também a madiana e o mais economico por marca.") 
print("\n-------------------------------------------------------")


def consumoanos(g):
    
    #print('________-----', g.name,type(g.name))
    #print(g)
    #print(g.agg('mean'))
    
    cat=g.name[1]
    
    if cat == 'Hatch':
        
        #print(g)
        g.sort_values('Fabricação',inplace=True)
        #print(g)
        
        ax = plt.gca()
        g.plot(kind='line',title=g.name[0],x='Fabricação',ax=ax)
        
        #print(g['Fabricação'],g['Alcool','Gasolina'])
        plt.show()
        
        
    return g


agmarcacat=dfCarse.groupby(['Marca','Categoria'])

agmarcacat['Fabricação','Alcool','Gasolina'].apply(consumoanos)

print(agmarcacat['Alcool','Gasolina'].agg(['mean','idxmax']))

print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("15) Crie e exiba uma tabela que relacione a Marca  x Peso, Categoria de Potência")
print("\n-------------------------------------------------------")
#
#   Categorize o peso em : 0 a 1000: Leve, 1000 a 1400: Padrao, acima de 1400, Pesado. 
#peso
#sDesemp

scatpeso=pd.cut(dfCarse['Peso'],bins=[0,1000,1400,dfCarse['Peso'].max()],labels=['Leve','Normal','Pesado'])
print(pd.crosstab(index=[dfCarse['Categoria'],scatpeso],columns=[sDesemp]))


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("16) Trabalhando com carros elétricos.") 
print("Crie a planilha dfcEl apenas com carros elétricos ou híbridos. Exiba-a") 
print("\n-------------------------------------------------------")

#leitura

dfAuton=pd.read_excel('DadosCarros2020.xlsx',header=0,index_col=0,sheet_name='Autonomia Eletricos')

###
#   Renomeie a coluna Gasolina para  Cons kwh/100km. Delete a coluna Alcool.
###

dfcEl=dfCarros.loc[(dfCarros['Combustivel']=='híbrido') | (dfCarros['Combustivel']=='eletricidade' )]
dfcEl.rename({'Gasolina':'Cons kwh/100km'},axis=1,inplace=True)
dfcEl.drop('Alcool',inplace=True,axis=1)

print(dfcEl)


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("17)Qual a média do peso, consumo e autonomia dos carros elétricos?"
      " Indique o peso medio, o consumo medio e autonomia media dos carros.Exiba-os") 
# Dica, use dfAuton
print("\n-------------------------------------------------------")


dfeltot=pd.concat([dfcEl,dfAuton],axis=1,join='inner')
dfeltot.rename({'Autonomia/ KM':'Autonomia'},inplace=True,axis=1)

dfeltot.drop('Marca',axis=1,inplace=True)
dfeltot['Marca']=dfcEl['Marca'].values


print(dfeltot[['Peso','Cons kwh/100km','Autonomia']].mean())


print("\n-------------------------------------------------------")
print("\n-------------------------------------------------------")
print("18) Exiba a tabela Marca, Modelo X Categoria ") 


print(pd.crosstab(index=[dfeltot['Marca'],dfeltot.index],columns=dfeltot['Categoria']))


print("\n-------------------------------------------------------")

print("\n-------------------------------------------------------")
print("19) Exiba uma tabela com a marca e a quantidade dos modelos que possuem a autonomia acima da média ")
def acimamedia(v,media):
    
    if v>media:
        
        return 'Acima'
    
    return 'Abaixo'


mediaaut=dfeltot['Autonomia'].mean()
#dfautaacima=dfeltot.loc[dfeltot['Autonomia']>mediaaut][['Marca']]

sacima=dfeltot['Autonomia'].apply(acimamedia,args=(mediaaut,))

ssacima=sacima.loc[sacima=='Acima']
lacima=list(ssacima.index.values)

print(pd.crosstab(index=ssacima,columns=dfeltot['Marca']))


print("\n-------------------------------------------------------")
print("20)Consigo observar através de uma tabela a marca e o modelos dos veículos que possuem autonomia abaixo da média?"
      " Exiba  marca, modelos e a categoria dos carros que possuem autonomia abaixo da media ")
print("\n-------------------------------------------------------")

sabaixo=sacima.loc[sacima=='Abaixo']
print(pd.crosstab(index=sabaixo,columns=[dfeltot['Marca'],dfeltot['Categoria']]))


print("\n-------------------------------------------------------")
print("21)Consigo observar através de uma tabela as informações de Ano por Categoria?"
      " Exiba a tabela  ANO X Categoria") 
print("\n-------------------------------------------------------")


print(pd.crosstab(index=dfeltot['Fabricação'],columns=dfeltot['Categoria']))

print("\n-------------------------------------------------------")
print("22) Exiba uma tabela com a informação  Peso, Categoria X  Autonomia, Marca") 
print("\n-------------------------------------------------------")
#
# Categorize o peso como Leve, Normal e Pesado.
# Categorize a autonomia como Ruim, Boa e Excelente.
#

scatpeso=pd.cut(dfeltot['Peso'],bins=[0,1400,2000,dfeltot['Peso'].max()],labels=['Leve','Normal','Pesado'])
scataut=pd.cut(dfeltot['Autonomia'],bins=3,labels=['Ruim','Boa','Excelente'])
print(pd.crosstab(index=[scatpeso,dfeltot['Categoria']],columns=[scataut,dfeltot['Marca']]))

print("\n-------------------------------------------------------")
