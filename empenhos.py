#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


import numpy as np


# In[ ]:


def formatDate(x):
    print(x[6:10] + '-' + x[3:5] + '-' + x[0:2])
    return x[6:10] + '-' + x[3:5] + '-' + x[0:2]


# In[ ]:


def formatCurrency(x):
    # 1.298.300,00
    x = (x.replace('.', '')).replace(',', '.')      
    return (x)


# In[ ]:


def cutDate(x, start, end):    
    return x[start:end]


# In[ ]:


def replaceSpecificDate(oldDate, searchDate, newDate):
    format = '%Y/%m/%d'
    if (oldDate == searchDate): #np.datetime64(searchDate)):
        return newDate
    else:
        return oldDate


# In[ ]:


def splitDate(firstDate):    
    if (len(firstDate) >= 10):
        return firstDate[13:24]
    else:
        return '01/01/1900'


# In[ ]:





# In[ ]:


df = pd.read_csv('dados.csv', on_bad_lines='skip', encoding='ISO-8859-1', sep=';')


# In[ ]:


df.head(2)


# In[ ]:


# Using drop() function to delete last row
df.drop(index=df.index[-1],axis=0,inplace=True)


# In[ ]:


df.tail()


# In[ ]:


df.drop(["Cód. Forn.", "Reforço", "Local", "Funcional", "Função", "Nome da Função", "Subfunção"] ,axis=1, inplace=True)


# In[ ]:


df.drop(["N° Ficha","Nome da Subfunção", "Fonte", "Fonte de Recurso", "Cód. Fonte", "Código Fonte", "Fonte STN", "Nome Fonte STN"] ,axis=1, inplace=True)


# In[ ]:


df.head(2)


# In[ ]:


df.rename(columns={'Empenho': 'numero', 'Tipo': 'tipo', 'Data': 'data', 'Descrição' : 'descricao', 'Nome Natureza' : 'nome_natureza' }, inplace=True)


# In[ ]:


df.rename(columns={ 'Dotação' : 'dotacao', 'Alteração Dotação' : 'alteracao_dotacao', 'Natureza' : 'natureza' }, inplace=True)


# In[ ]:


df.rename(columns={'Dotação Atual' : 'dotacao_atual', 'Valor Anulado' : 'valor_anulado', 'Valor Empenhado' : 'valor_empenhado' }, inplace=True)


# In[ ]:


df.rename(columns={'Valor Liquidado' : 'valor_liquidado', 'Valor Pago' : 'valor_pago', 'Empenhado até Hoje' : 'empenhado_ate_hoje' },  inplace=True)


# In[ ]:


df.rename(columns={'Liquidado até Hoje' : 'liquidado_ate_hoje', 'Pago até Hoje' : 'pago_ate_hoje' },  inplace=True)


# In[ ]:


df.insert(loc=3, column='ano', value=2023)


# In[ ]:


df.head(2)


# In[ ]:


df['data']= df['data'].apply(lambda x: formatDate(x)) 


# In[ ]:


df['dotacao'] = df['dotacao'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['alteracao_dotacao'] = df['alteracao_dotacao'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['dotacao_atual'] = df['dotacao_atual'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['valor_anulado'] = df['valor_anulado'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['valor_empenhado'] = df['valor_empenhado'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['valor_liquidado'] = df['valor_liquidado'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['valor_pago'] = df['valor_pago'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['empenhado_ate_hoje'] = df['empenhado_ate_hoje'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['liquidado_ate_hoje'] = df['liquidado_ate_hoje'].apply(lambda x: formatCurrency(x))


# In[ ]:


df['pago_ate_hoje'] = df['pago_ate_hoje'].apply(lambda x: formatCurrency(x))


# In[ ]:





# In[ ]:


df.head(2)


# In[ ]:





# In[ ]:


df.head(1)


# In[ ]:





# In[ ]:





# In[ ]:


df.index = np.arange(1, len(df) + 1)


# In[ ]:





# In[ ]:


df.reset_index(drop=True, inplace=True)


# In[ ]:





# In[ ]:


df.head()


# In[ ]:


df.to_csv('dados_para_importar_junho2023.csv', header=False, index=False)


# In[ ]:


df


# In[ ]:




