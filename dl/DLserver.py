from flask import Flask, jsonify, request
import json
import subprocess
from making_TrainedDL import class_recommendation#내가 making_TrainedDL.py를 if __name__ == '__main__' 아래에서 작성하지 않았기에, 해당 모듈(making_TrainedDL.py) 전체가 실행된다! 그러니, 밑에서 app.run() 전에 이 script 또 실행할 필요 x!

app = Flask(__name__)
input_for_BeamSearch = [["전자전기공학","어드벤처디자인","c언어및자료구조","회로이론1","객체지향프로그래밍"]]#연동 전 서버 제대로 작동하는지를 위한 예시일 뿐
#recommended_classes=[['디지털신호처리및설계', '마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '회로이론2'], ['고체전자소자', '마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '회로이론2'], ['고체전자소자', '디지털신호처리및설계', '물리전자공학2', '전자기학2', '회로이론2'], ['마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '전자회로1', '회로이론2'], ['고체전자소자', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2'], ['고체전자소자', '고체전자소자', '물리전자공학2', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '마이크로프로세서응용및실험', '물리전자공학1', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '랜덤신호이론', '물리전자공학2', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2'], ['디지털공학', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2']]

# 첫 번째 엔드포인트: 데이터를 제공하는 엔드포인트
@app.route('/inference', methods=['POST'])
def get_data():
    
    #DL 연동해서 실제 dl input값(class_recommendation.BeamSearch의 input) 받을 부분(input_for_BeamSearch)

    recommended_classes = class_recommendation.BeamSearch(input_for_BeamSearch, num_class=5, beam_size=3)

    # Flattening the list of lists
    flattened_classes = sum(recommended_classes, [])
    data = {"lectures": flattened_classes}
    json_content = json.dumps(data, indent=2, ensure_ascii=False)
    return json_content

if __name__ == '__main__':
    app.run(port=8000,debug=True)