from flask import Flask, jsonify, request
import json

app = Flask(__name__)
recommended_classes=[['디지털신호처리및설계', '마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '회로이론2'], ['고체전자소자', '마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '회로이론2'], ['고체전자소자', '디지털신호처리및설계', '물리전자공학2', '전자기학2', '회로이론2'], ['마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '전자회로1', '회로이론2'], ['고체전자소자', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2'], ['고체전자소자', '고체전자소자', '물리전자공학2', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '마이크로프로세서응용및실험', '물리전자공학1', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '랜덤신호이론', '물리전자공학2', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2'], ['디지털공학', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2']]

# 첫 번째 엔드포인트: 데이터를 제공하는 엔드포인트
@app.route('/inference', methods=['GET'])
def get_data():
    

    # Flattening the list of lists
    flattened_classes = sum(recommended_classes, [])
    data = {"lecture": flattened_classes}
    json_content = json.dumps(data, indent=2, ensure_ascii=False)
    return json_content

if __name__ == '__main__':
    app.run(debug=True)