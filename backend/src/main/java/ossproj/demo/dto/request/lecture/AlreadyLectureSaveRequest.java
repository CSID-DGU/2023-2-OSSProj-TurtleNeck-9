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
    private String alFirstLectureName;
    private String alSecondLectureName;
    private String alThirdLectureName;
    private String alFourthLectureName;
    private String alFifthLectureName;
    private String alSixthLectureName;
}
