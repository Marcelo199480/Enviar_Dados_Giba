import awswrangler as wr
import pandas as pd

# le arquivo considerando o filtro de partições (só funciona o filtro se o dataset for passado como True)
parquet_existente = wr.s3.read_parquet('s3://mrs-estudos/tabela_exposicao_ativo',
                         partition_filter=lambda x: True if x["ano"] == "2024" and x["mes"] == "6" and x['dia'] == "10" else False,
                         dataset=True)

# le arquivo da máquina, mas nesse caso vai fazer o esquema de ler do bucket e descompactar, como já é feito hoje 
csv_capturado_no_evento = pd.read_csv("C:\\Users\marce\Downloads\Exposicao_Ativo_2.csv", delimiter=';')

a = parquet_existente.set_index('fundo')
b = csv_capturado_no_evento.set_index('fundo')

c = b.combine_first(a)
c = c.reset_index()
df_final = c.reindex(columns=parquet_existente.columns)

df_final['ano'] = '2024'
df_final['mes'] = '6'
df_final['dia'] = '10'

# envia arquivo para o bucket como parquet considerando as partições
# overwrite sobrescreve o arquivo existente nessa partição, mantendo apenas um arquivo
wr.s3.to_parquet(df_final,'s3://mrs-estudos/tabela_exposicao_ativo',dataset=True,mode='overwrite',partition_cols=['ano','mes','dia'])