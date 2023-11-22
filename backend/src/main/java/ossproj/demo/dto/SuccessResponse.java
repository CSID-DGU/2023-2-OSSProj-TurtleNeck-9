package ossproj.demo.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import ossproj.demo.exception.Success;

import static lombok.AccessLevel.PRIVATE;

@Getter
@RequiredArgsConstructor(access = PRIVATE)
@AllArgsConstructor(access =  PRIVATE)
public class SuccessResponse<T> {
    private final int code;
    private final String message;
    private T data;

    public static SuccessResponse success(Success success) {
        return new SuccessResponse<>(success.getHttpStatusCode(), success.getMessage());
    }

    public static <T> SuccessResponse<T> success(Success success, T data) {
        return new SuccessResponse<T>(success.getHttpStatusCode(), success.getMessage(), data);
    }
}