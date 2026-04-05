import json             
import pandas as pd     
import boto3            
import io              
from datetime import datetime 

glue_client = boto3.client('glue')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key_name = event['Records'][0]['s3']['object']['key']

    print(f"Arquivo ok {key_name} no bucket: {bucket_name}")

    response = s3_client.get_object(Bucket=bucket_name, Key=key_name)

    content = response['Body'].read().decode('utf-8')

    data = json.loads(content)
    df = pd.json_normalize(data)

    parquet_buffer = io.BytesIO()
    df.to_parquet(parquet_buffer, index=False)

    target_key = f"orders_parquet_data_lake/order_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"

    s3_client.put_object(
        Bucket=bucket_name,
        Key=target_key,
        Body=parquet_buffer.getvalue()
    )

    print(f"Arquivo processado e salvo como Parquet em: {target_key}")

    return {
        'statusCode': 200,
        'body': json.dumps('ETL Finalizado com sucesso!')
    }

glue_client.start_crawler(Name='crawler-pedidos-diogo')
print("Crawler iniciado automaticamente!")
