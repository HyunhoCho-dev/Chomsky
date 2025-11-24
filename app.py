from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

GLM_API_KEY = os.getenv('GLM_API_KEY')
GLM_API_URL = 'https://api.z.ai/api/paas/v4/chat/completions'

# 프론트엔드 서빙
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'Chomsky AI by CTTechnologies'})

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        messages = data.get('messages', [])
        
        if not messages:
            return jsonify({'error': 'Messages are required'}), 400
        
        # GLM API 호출
        headers = {
            'Authorization': f'Bearer {GLM_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': 'glm-4.5-flash',
            'messages': messages,
            'stream': False,
            'max_tokens': 2000,
            'temperature': 0.7
        }
        
        response = requests.post(GLM_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        return jsonify({
            'success': True,
            'message': result['choices'][0]['message']['content']
        })
        
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API request failed: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
