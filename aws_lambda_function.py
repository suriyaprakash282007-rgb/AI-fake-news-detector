import json
import boto3
import os

# usage: This file demonstrates how the backend logic would look in AWS Lambda
# It connects to a SageMaker endpoint to get predictions

# Initialize SageMaker runtime client
runtime = boto3.client('runtime.sagemaker')

# Environment variable for the endpoint name
ENDPOINT_NAME = os.environ.get('ENDPOINT_NAME', 'fake-news-detector-endpoint')

def lambda_handler(event, context):
    """
    AWS Lambda Handler function
    Triggered by API Gateway
    """
    print("Received event:", json.dumps(event))
    
    try:
        # 1. Parse Input
        # API Gateway passes data in the 'body' field
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event
            
        news_text = body.get('text', '')
        
        if not news_text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No text provided'})
            }

        # 2. Call SageMaker Endpoint
        # We send the text payload to the deployed model
        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType='application/json',
            Body=json.dumps([news_text])  # Wrap in list as scikit-learn expects
        )
        
        # 3. Process Response
        result = json.loads(response['Body'].read().decode())
        
        # Assuming the model returns [prediction_label] (0 or 1)
        prediction = result[0]
        
        is_real = True if prediction == 1 else False
        label = "Likely Real" if is_real else "Likely Fake"
        
        # 4. Construct Response
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({
                'prediction': label,
                'confidence': 85, # In a real scenario, ask model for proba
                'message': f"Analysis complete. Result: {label}"
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error', 'details': str(e)})
        }
