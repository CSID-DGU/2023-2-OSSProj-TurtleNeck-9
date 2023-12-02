package ossproj.demo.dto.response;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Getter
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class LectureTimeResponse {
    private String weekday;
    private String startTime;
    private String endTime;
}
