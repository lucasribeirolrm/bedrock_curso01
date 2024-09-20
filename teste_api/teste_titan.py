import boto3
import json

client = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")
titan_model_id = 'amazon.titan-text-express-v1'

titan_config = json.dumps({
   "inputText": "Opções de sandália para uma caminhada na praia.",
                "textGenerationConfig":{
                    "maxTokenCount": 200,
                    "stopSequences": [],
                    "temperature": 0.5,
                    "topP": 0.2
            } 
})


response = client.invoke_model(
    body=titan_config,
    modelId=titan_model_id,
    accept="application/json",
    contentType="application/json" 
)

resposta = json.loads(response['body'].read().decode('utf-8'))
print(resposta.get('results')[0].get('outputText'))
#completion = resposta.get('completion','Resposta não encontrada')
#resposta_formatada = f"Resposta:\n{completion}\n"
#print(resposta_formatada)