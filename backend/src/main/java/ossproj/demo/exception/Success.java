package ossproj.demo.exception;

import lombok.AllArgsConstructor;
import lombok.Getter;
import org.springframework.http.HttpStatus;

@Getter
@AllArgsConstructor
public enum Success {

    /**
     * STATUS CODE : 200 OK
     */
    GET_LECTURE_SUCCESS(HttpStatus.OK,"강의 조회 성공"),
    GET_TIMETABLE_SUCCESS(HttpStatus.OK,"시간표 조회 성공"),

    /**
     * STATUS CODE : 201 OK
     */
    POST_SIGNUP_SUCCESS(HttpStatus.CREATED,"유저 생성 성공");


    private final HttpStatus httpStatus;
    private final String message;

    public int getHttpStatusCode() {
        return httpStatus.value();
    }
}
