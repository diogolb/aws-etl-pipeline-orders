# AWS Serverless ETL Pipeline

Este projeto demonstra a construção de um pipeline de dados baseado em eventosutilizando serviços da AWS. O objetivo é processar dados de vendas em formato JSON e transformá-los em tabelas otimizadas para analise SQL.

## Arquitetura
O fluxo de dados segue o modelo de Data Lake moderno:
1. **S3:** Upload de arquivos JSON brutos (princípio)
2. **AWS Lambda:** Gatilho automático que processa o JSON usando **Python & Pandas**.
3. **S3:** Armazenamento dos dados convertidos para **Apache Parquet**.
4. **AWS Glue Crawler:** Escaneamento automático dos metadados e criação do catálogo.
5. **Amazon Athena:** Consultas analíticas via SQL diretamente no S3.



## Tecnologias Utilizadas
* **Python 3.12** com biblioteca **Boto3**.
* **Pandas** (via AWS Lambda Layers) para manipulação de dados.
* **AWS S3** para armazenamento de objetos.
* **AWS Glue & Athena** para governança e análise de dados.

##Diferenciais Técnicos
* **Escalabilidade:** Arquitetura Serverless que escala conforme o volume de arquivos.
* **Performance:** Uso do formato Parquet, reduzindo custos de consulta no Athena em até 90%.
* **Automação:** Pipeline 100% reativo, sem necessidade de agendamento manual (Airflow).

## Como reproduzir
1. Crie um bucket no S3 com as pastas `orders_json_incoming/` e `orders_parquet_data_lake/`.
2. Configure uma Lambda com a Role de permissão correta (S3, CloudWatch, Glue).
3. Adicione a Layer `AWSSDKPandas` na Lambda.
4. Configure o gatilho (Trigger) do S3 para a pasta de entrada.
5. Execute o Glue Crawler e consulte via Athena.
