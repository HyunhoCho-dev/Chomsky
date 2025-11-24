from flask import Flask, request, jsonify, send_from_directory, Response, stream_with_context
from flask_cors import CORS
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

GLM_API_KEY = os.getenv('GLM_API_KEY')
GLM_API_URL = 'https://api.z.ai/api/paas/v4/chat/completions'

# 프론트엔드 서빙
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

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

        def generate():
            try:
                headers = {
                    'Authorization': f'Bearer {GLM_API_KEY}',
                    'Content-Type': 'application/json'
                }

                payload = {
                    'model': 'glm-4.5-flash',
                    'messages': messages,
                    'stream': True,
                    'max_tokens': 4000,
                    'temperature': 0.8
                }

                response = requests.post(GLM_API_URL, headers=headers, json=payload, stream=True, timeout=60)
                response.raise_for_status()

                for line in response.iter_lines():
                    if line:
                        line_str = line.decode('utf-8')
                        if line_str.startswith('data: '):
                            data_str = line_str[6:]
                            if data_str.strip() == '[DONE]':
                                break
                            try:
                                chunk_data = json.loads(data_str)
                                if 'choices' in chunk_data and len(chunk_data['choices']) > 0:
                                    delta = chunk_data['choices'][0].get('delta', {})
                                    content = delta.get('content', '')
                                    if content:
                                        yield f"data: {json.dumps({'content': content})}\n\n"
                            except json.JSONDecodeError:
                                continue

                yield f"data: {json.dumps({'done': True})}\n\n"

            except Exception as e:
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return Response(stream_with_context(generate()), mimetype='text/event-stream')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)