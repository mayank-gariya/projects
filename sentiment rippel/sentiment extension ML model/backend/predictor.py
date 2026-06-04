import joblib

# Load the pipeline once when the module imports
pipe = joblib.load('logistic_regression_pipeline.pkl')

class SentimentPredictor: # Cleaned up name
    def __init__(self):        
        print('Model pipeline loaded successfully.')
        
    async def predict(self, text: str):
        sentiment = pipe.predict([text])[0]
        
        if sentiment == 1:
            return {
                'sentiment': 'positive sentiment',
                'description': 'Your text has positive sentiment',
                'status code':200
            }
        else:
            return {
                'sentiment': 'negative sentiment',
                'description': 'Your text has negative sentiment',
                'status code':200
            }
