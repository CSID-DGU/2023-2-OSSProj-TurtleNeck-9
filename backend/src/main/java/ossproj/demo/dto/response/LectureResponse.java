package ossproj.demo.dto.response;

import lombok.*;
import org.springframework.stereotype.Service;

import java.util.List;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class LectureResponse {
    private Long lectureId;
    private String place;
    private String lectureName;
    private String professorName;
    private List<LectureTimeResponse> lectureTime;
}
