package ossproj.demo.dto.response;

import lombok.*;

import java.util.List;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class TimetableResponse {
    private List<LectureResponse> lectures;
}
