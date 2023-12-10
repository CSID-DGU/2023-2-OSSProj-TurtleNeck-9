import mysql.connector

def fetch_row_by_id(row_id):#여기엔 user_id or student_id 등 행을 뽑을 때, 행을 찾을 행의 id를 입력
    # MySQL 연결 정보 설정
    db_config = {
        'host': '43.200.90.66',
        'user': 'admin',
        'password': '12341234',
        'database': 'dgu-timetable',
        'raise_on_warnings': True
    }
    try:
        # MySQL에 연결
        connection = mysql.connector.connect(**db_config)

        # 커서 생성 -> 데이터(원하는 행) 가져오기 -> cursor close
        cursor_lec = connection.cursor()
        query = "SELECT * FROM already_lectures WHERE user_id = %s"#from 다음의 table 이름(student_id는 해당 table에서 우리가 찾는 id열의 이름임.) | %s는 파라미터화된 SQL 쿼리를 나타내는데, 이는 SQL 쿼리에 동적으로 값을 전달할 때 사용
        cursor_lec.execute(query, (row_id,))#이 때, query의 %s에 row_id가 들어감.
        result = cursor_lec.fetchone()
        cursor_lec.close()


        cursor_major_id = connection.cursor()
        query = "SELECT * FROM users WHERE user_id = %s"
        cursor_major_id.execute(query,(row_id,))
        major_id = int(cursor_major_id.fetchone()[3])
        print("major_id = ",major_id)
        cursor_major_id.close()

        cursor_major_name = connection.cursor()
        query = "SELECT * FROM major WHERE major_id = %s"
        cursor_major_name.execute(query,(major_id,))
        major_name = cursor_major_name.fetchone()
        major_name = major_name[1]
        cursor_major_name.close()

        if result:
            print(f"1st_lec: {result[3]}, 2nd_lec: {result[6]}, 3rd_lec: {result[5]}, 4th_lec: {result[7]},5th_lec: {result[4]},6th_lec: {result[2]}")  # 예시에 따라 필드를 적절히 변경
            print(result)#튜플임
            print(type(result))
            already_taken = [result[3],result[6],result[5],result[7],result[4],result[2]]
            print(already_taken)
            print(major_name)
            return already_taken, major_name
        else:
            print(f"ID {row_id}에 해당하는 행이 없습니다.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # 연결 및 커서 닫기
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    row_id_to_fetch = 1  # 가져올 행의 ID를 적절히 변경(users table에서 user_id는 1~5까지이나, already_lectures에선 등록된 user_id가 1~3까지이니, id는 1~3중 하나!)
    fetch_row_by_id(row_id_to_fetch)