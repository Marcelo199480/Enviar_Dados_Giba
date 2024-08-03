```python
import boto3
import os

def lambda_handler(event, context):
    try:
        if os.path.isfile('/tmp/ca-bundle.crt'):
            print('arquivo existe')
            
        else:
            s3 = boto3.client('s3')
            payload = s3.get_object(Bucket='mrs-estudos',Key='testes.txt')
        
            arquivo = payload['Body'].read()
            print(f'captura: {arquivo}')
            
            with open('/tmp/ca-bundle.crt', 'wb') as f:
                f.write(arquivo)
                
        with open('/tmp/ca-bundle.crt','r') as f:
            print(f.read())
            
    except Exception as e:
        raise e
```
