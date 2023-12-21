import requests

def lambda_handler(event, context):
    # Extrai informações da requisição recebida    
    http_method = event['httpMethod'] 
    request_url = 'https://sua-url-de-destino.com'
    # Substitua pela URL desejada    
    headers = event['headers']
    query_string_parameters = event.get('queryStringParameters', {})
    body = event.get('body', '')
    try: 
        # Desativa a validação SSL para a requisição        
        
        response = requests.request(http_method, request_url, headers=headers, params=query_string_parameters, data=body, verify=False)
        # Prepara a resposta para retornar ao chamador original        
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.text
        }
    except Exception as e: 
        # Se ocorrer um erro, retorna uma resposta de erro        
        return { 
            'statusCode': 500, 
            'body': str(e)
        }