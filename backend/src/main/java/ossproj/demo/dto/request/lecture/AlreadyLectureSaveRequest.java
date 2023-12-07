package ossproj.demo.dto.request.lecture;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@NoArgsConstructor
public class AlreadyLectureSaveRequest {
    private int alFirstId;
    private int alSecondId;
    private int alThirdId;
    private int alFourthId;
    private int alFifthId;
    private int alSixthId;
}
