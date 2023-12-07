from flask import Flask, jsonify, request
import json
import subprocess
import pandas as pd
from making_TrainedDL import class_recommendation#내가 making_TrainedDL.py를 if __name__ == '__main__' 아래에서 작성하지 않았기에, 해당 모듈(making_TrainedDL.py) 전체가 실행된다!
from extract_DBrow_by_id import fetch_row_by_id


app = Flask(__name__)
input_for_BeamSearch = [["산업시스템공학과","산업시스템공학의이해","산업시스템프로그래밍1","응용통계학","경영과학1","데이터분석입문"]]#연동 전 서버 제대로 작동하는지를 위한 예시일 뿐
#recommended_classes=[['디지털신호처리및설계', '마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '회로이론2'], ['고체전자소자', '마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '회로이론2'], ['고체전자소자', '디지털신호처리및설계', '물리전자공학2', '전자기학2', '회로이론2'], ['마이크로프로세서응용및실험', '물리전자공학2', '전자기학2', '전자회로1', '회로이론2'], ['고체전자소자', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2'], ['고체전자소자', '고체전자소자', '물리전자공학2', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '마이크로프로세서응용및실험', '물리전자공학1', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '랜덤신호이론', '물리전자공학2', '전자기학2', '회로이론2'], ['디지털신호처리및설계', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2'], ['디지털공학', '물리전자공학2', '신호및시스템', '전자기학2', '회로이론2']]

#csv파일로 과목 이름별 id 딕셔너리 생성
file_path = "/mnt/c/Users/USER/OneDrive/바탕 화면/융합 소프트웨어/오픈소스소프트웨어프로젝트/팀프로젝트/OSSProj.ver2.0/sibal.csv"
class_schedule_set = pd.read_csv(file_path)
name2id = dict(zip(class_schedule_set["lecture_name"],class_schedule_set["lecture_id"]))


# 첫 번째 엔드포인트: 데이터를 제공하는 엔드포인트
@app.route('/inference', methods=['POST'])
def get_data():
    #로그인시 로그인한 학생의 id 추출()
    

    id = 20180001#이 부분 본래 /users/login으로부터 id 받아와야됨.
    
    #DB연동해서 로그인된 학생 id로 해당 행 불러오기
    student_info = fetch_row_by_id(id)
    #input_for_BeamSearch = student_info[]#기수강과목들을 1차원 행렬로 만들기(어떤 student인지에 따라 major도 같이 뽑아야됨.)
    #input_for_BeamSearch = [[input_for_BeamSearch]]
    print(student_info)


    #DL 연동해서 실제 dl input값(class_recommendation.BeamSearch의 input) 받을 부분(input_for_BeamSearch)

    recommended_classes = class_recommendation.BeamSearch(input_for_BeamSearch, num_class=10, beam_size=2)

    # Flattening the list of lists
    recommended_classes = [item.upper() for sublist in recommended_classes for item in sublist]
    recommended_classes = [name2id[item] if item in name2id.keys() else 0 for item in recommended_classes]#과목명의 list를 각각 id로 변환된 list 

    data = {"lectures": recommended_classes}
    json_content = json.dumps(data, indent=2, ensure_ascii=False)
    return json_content

if __name__ == '__main__':
    app.run(port=8000,debug=False)#debug=True로 하면, 코드의 변경을 감지하고, 변경이 있을 때마다 자동으로 서버를 다시 시작하며, 보안에 취약하니, 실사용시에는 debug=False로 해야함.(+debug=True시, script 두 번씩 실행되어 시간 더 오래걸림.)