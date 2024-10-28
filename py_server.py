from flask import Flask, request
import requests
import json 

app = Flask(__name__)

@app.route('/receive_json', methods=['POST'])
def receive_json():
    # Get the JSON data from the form-data
    json_data = request.form.get('alarmResult')
    
    # Log the received JSON data
    print(f"Received JSON Data: {json_data}")
    
    # Send the extracted JSON data to port 9090
    try:
       
        json_object = json.loads(json_data)
        
       
        print(f"Sending JSON Object: {json_object}")
        
        response = requests.post('http://localhost:9090/receive_extracted_json', json=json_object)
        return f"Data sent to port 9090: {response.text}"
    except json.JSONDecodeError as e:
        return f"Failed to decode JSON: {str(e)}"

if __name__ == '__main__':
    app.run(port=8080)
