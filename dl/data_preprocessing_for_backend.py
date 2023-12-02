import pandas as pd

def data_preprocessing_for_backend(excel_file_path,major,modified_excel_file_path):
    excel_file_path = excel_file_path
    raw_time_table = pd.read_excel(excel_file_path)
    # 데이터프레임 출력
    print("수정 전 시간표 : \n",raw_time_table)

    """#이 방식으로 새로운 데이터 만들 것
    empty_df = pd.DataFrame()
    # 빈 데이터프레임 출력
    print(empty_df)
    # 새로운 열 추가
    empty_df['새로운열'] = [1, 2, 3]
    # 업데이트된 데이터프레임 출력
    print(empty_df)
    """
    #여기에 열 추가 형식으로 넣기
    modified_time_table = pd.DataFrame()


    #print(raw_time_table["id"].tolist())#이렇게 하면, dataFrame의 "id" 열의 각 원소를 list로 변환 가능

    #1. modified_time_table에 "id" 열 추가
    modified_time_table["id"] = raw_time_table["번호"].tolist()
    print(modified_time_table["id"]==raw_time_table["번호"])#두 열 서로 맞는지 확인

    #2. modified_time_table에 "lecture_name" 열 추가
    modified_time_table["lecture_name"] = raw_time_table["교과목명"].tolist()
    print(modified_time_table["lecture_name"]==raw_time_table["교과목명"])#두 열 서로 맞는지 확인

    #3. modified_time_table에 "major" 열 추가
    major_list = [major for i in range(len(raw_time_table["번호"].tolist()))]#len(raw_time_table["id"].tolist()은 dataframe의 행의 개수와 동일하니 가능
    modified_time_table["major"] = major_list
    print(modified_time_table)

    #4. modified_time_table에 "professor_name" 열 추가
    modified_time_table["professor_name"] = raw_time_table["교원명"]
    print(modified_time_table["professor_name"]==raw_time_table["교원명"])

    #5. lecture_first_day,first_day_start_time, first_day_end_time | lecture_second_day, second_day_start_time, second_day_end_time 열 추가
    #슬라이싱으로 각각의 열에 들어갈 list로 만들고 각각을 열에 집어넣기
    raw_time_list = raw_time_table["요일/시간"].tolist()
    #print(raw_time_list)#잘 나왔는지 확인
    lecture_first_day_list=list();first_day_start_time_list=list();first_day_end_time_list=list()
    lecture_second_day_list=list();second_day_start_time_list=list();second_day_end_time_list=list()
    day_dict = {"월":"mon","화":"tue","수":"wed","목":"thu","금":"fri"}
    for i in range(len(raw_time_list)):
        print(raw_time_list[i])#list의 각 원소 확인
        daywise_time_list=raw_time_list[i].split(",")
        print(daywise_time_list)#요일 별로 시간이 split되어 list가 되었음을 확인
        #일주일에 3일 동안 수업하는 과목까지 넣으려면 45,46에서 third day까지 해야 됨!
        if len(daywise_time_list)==1:
            first_day_time_list=daywise_time_list[0]
            day_period , time = first_day_time_list.split("/")
            start,end=time.split("-")
            lecture_first_day_list.append(day_dict[day_period[0]]);first_day_start_time_list.append(start);first_day_end_time_list.append(end)#day_period[0]=요일
            lecture_second_day_list.append("NULL");second_day_start_time_list.append("NULL");second_day_end_time_list.append("NULL")
        elif len(daywise_time_list)==2:
            first_day_time_list=daywise_time_list[0]
            second_day_time_list=daywise_time_list[1]
            day_period , time = first_day_time_list.split("/")
            start,end=time.split("-")
            lecture_first_day_list.append(day_dict[day_period[0]]);first_day_start_time_list.append(start);first_day_end_time_list.append(end)
            day_period , time = second_day_time_list.split("/")
            start,end=time.split("-")
            lecture_second_day_list.append(day_dict[day_period[0]]);second_day_start_time_list.append(start);second_day_end_time_list.append(end)

    #5. lecture_first_day,first_day_start_time, first_day_end_time | lecture_second_day, second_day_start_time, second_day_end_time
    modified_time_table["lecture_first_day"]=lecture_first_day_list
    modified_time_table["first_day_start_time"]=first_day_start_time_list
    modified_time_table["first_day_end_time"]=first_day_end_time_list
    modified_time_table["lecture_second_day"]=lecture_second_day_list
    modified_time_table["second_day_start_time"]=second_day_start_time_list
    modified_time_table["second_day_end_time"]=second_day_end_time_list

    #6. 장소 입력
    modified_time_table["place"]=raw_time_table["강의실"]

    print(modified_time_table)

    # 데이터프레임을 엑셀 파일로 저장
#    excel_file_path = 'C:\\Users\\USER\\OneDrive\\바탕 화면\\융합 소프트웨어\\오픈소스소프트웨어프로젝트\\팀프로젝트\\산시시간표전처리연습.xlsx'
    modified_time_table.to_excel(modified_excel_file_path, index=False)
    return modified_time_table

#산시
data_preprocessing_for_backend('C:\\Users\\USER\\OneDrive\\바탕 화면\\융합 소프트웨어\\오픈소스소프트웨어프로젝트\\팀프로젝트\\23-2_ise_lecture.xlsx',"산업시스템공학과",'C:\\Users\\USER\\OneDrive\\바탕 화면\\융합 소프트웨어\\오픈소스소프트웨어프로젝트\\팀프로젝트\\산시시간표전처리.xlsx')
#정보통신
data_preprocessing_for_backend("C:\\Users\\USER\\OneDrive\\바탕 화면\\융합 소프트웨어\\오픈소스소프트웨어프로젝트\\팀프로젝트\\23-2_정보통신공학과.xlsx","정보통신공학과",'C:\\Users\\USER\\OneDrive\\바탕 화면\\융합 소프트웨어\\오픈소스소프트웨어프로젝트\\팀프로젝트\\정통시간표전처리.xlsx')
#전전
data_preprocessing_for_backend('C:\\Users\\USER\\OneDrive\\바탕 화면\\융합 소프트웨어\\오픈소스소프트웨어프로젝트\\팀프로젝트\\23-2_전자전기공학부.xlsx',"전자전기공학과",'C:\\Users\\USER\\OneDrive\\바탕 화면\\융합 소프트웨어\\오픈소스소프트웨어프로젝트\\팀프로젝트\\전전시간표전처리.xlsx')