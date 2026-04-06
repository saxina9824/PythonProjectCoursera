import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the input JSON dictionary
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request to the service
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion scores from the specific path in the response
    # The response structure is: {'emotionPredictions': [{'emotion': {...}}]}
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract individual scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Logic to find the dominant emotion
    emotion_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    emotion_names = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    
    # Find the index of the highest score and use it to get the emotion name
    dominant_emotion_index = emotion_list.index(max(emotion_list))
    dominant_emotion = emotion_names[dominant_emotion_index]
    
    # Create the final output dictionary
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result