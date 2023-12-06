import mysql.connector

def fetch_row_by_id(row_id):
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

        # 커서 생성
        cursor = connection.cursor()

        # SQL 쿼리 작성 및 실행
        query = "SELECT * FROM users WHERE student_id = %s"#from 다음의 table 이름(student_id는 해당 table에서 우리가 찾는 id열의 이름임.)
        cursor.execute(query, (row_id,))

        # 결과 가져오기
        result = cursor.fetchone()

        if result:
            print(f"ID: {result[0]}, password: {result[1]}, student_id: {result[2]}, student_name: {result[3]},major_id: {result[4]}")  # 예시에 따라 필드를 적절히 변경
            print(result)#튜플임
            print(type(result))
            return result
        else:
            print(f"ID {row_id}에 해당하는 행이 없습니다.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # 연결 및 커서 닫기
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    row_id_to_fetch = 20180001  # 가져올 행의 ID를 적절히 변경
    fetch_row_by_id(row_id_to_fetch)