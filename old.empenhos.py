#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd


# In[37]:


import numpy as np


# In[38]:


def formatDate(x):
    print(x[6:10] + '-' + x[3:5] + '-' + x[0:2])
    return x[6:10] + '-' + x[3:5] + '-' + x[0:2]


# In[39]:


def formatCurrency(x):
    # 1.298.300,00
    x = (x.replace('.', '')).replace(',', '.')      
    return (x)


# In[40]:


def cutDate(x, start, end):    
    return x[start:end]


# In[41]:


def replaceSpecificDate(oldDate, searchDate, newDate):
    format = '%Y/%m/%d'
    if (oldDate == searchDate): #np.datetime64(searchDate)):
        return newDate
    else:
        return oldDate


# In[42]:


def splitDate(firstDate):    
    if (len(firstDate) >= 10):
        return firstDate[13:24]
    else:
        return '01/01/1900'


# In[ ]:





# In[43]:


df = pd.read_csv('dados.csv',  error_bad_lines=False, encoding='ISO-8859-1', sep=';')


# In[44]:


df.head(2)


# In[45]:


df.drop(["Cód. Forn.", "Reforço", "Local", "Funcional", "Função", "Nome da Função", "Subfunção"] ,axis=1, inplace=True)


# In[46]:


df.drop(["Nome da Subfunção", "Fonte", "Fonte de Recurso", "Cód. Fonte", "Código Fonte", "Fonte STN", "Nome Fonte STN"] ,axis=1, inplace=True)


# In[47]:


df.head(2)


# In[48]:


df.rename(columns={'Empenho': 'numero', 'Tipo': 'tipo', 'Data': 'data', 'Descrição' : 'descricao', 'Nome Natureza' : 'nome_natureza' }, inplace=True)


# In[49]:


df.rename(columns={ 'Dotação' : 'dotacao', 'Alteração Dotação' : 'alteracao_dotacao', 'Natureza' : 'natureza' }, inplace=True)


# In[50]:


df.rename(columns={'Dotação Atual' : 'dotacao_atual', 'Valor Anulado' : 'valor_anulado', 'Valor Empenhado' : 'valor_empenhado' }, inplace=True)


# In[51]:


df.rename(columns={'Valor Liquidado' : 'valor_liquidado', 'Valor Pago' : 'valor_pago', 'Empenhado até Hoje' : 'empenhado_ate_hoje' },  inplace=True)


# In[52]:


df.rename(columns={'Liquidado até Hoje' : 'liquidado_ate_hoje', 'Pago até Hoje' : 'pago_ate_hoje' },  inplace=True)


# In[53]:


df.insert(loc=3, column='ano', value=2022)


# In[54]:


df.head(2)


# In[55]:


df['data']= df['data'].apply(lambda x: formatDate(x)) 


# In[56]:


df['dotacao'] = df['dotacao'].apply(lambda x: formatCurrency(x))


# In[57]:


df['alteracao_dotacao'] = df['alteracao_dotacao'].apply(lambda x: formatCurrency(x))


# In[58]:


df['dotacao_atual'] = df['dotacao_atual'].apply(lambda x: formatCurrency(x))


# In[59]:


df['valor_anulado'] = df['valor_anulado'].apply(lambda x: formatCurrency(x))


# In[60]:


df['valor_empenhado'] = df['valor_empenhado'].apply(lambda x: formatCurrency(x))


# In[61]:


df['valor_liquidado'] = df['valor_liquidado'].apply(lambda x: formatCurrency(x))


# In[62]:


df['valor_pago'] = df['valor_pago'].apply(lambda x: formatCurrency(x))


# In[63]:


df['empenhado_ate_hoje'] = df['empenhado_ate_hoje'].apply(lambda x: formatCurrency(x))


# In[64]:


df['liquidado_ate_hoje'] = df['liquidado_ate_hoje'].apply(lambda x: formatCurrency(x))


# In[65]:


df['pago_ate_hoje'] = df['pago_ate_hoje'].apply(lambda x: formatCurrency(x))


# In[ ]:





# In[66]:


df.head(2)


# In[ ]:





# In[67]:


df.head(1)


# In[ ]:





# In[ ]:





# In[68]:


df.index = np.arange(1, len(df) + 1)


# In[69]:


df.to_csv('dados_para_importar.csv', header=False, index=False )


# In[ ]:





# In[ ]:




