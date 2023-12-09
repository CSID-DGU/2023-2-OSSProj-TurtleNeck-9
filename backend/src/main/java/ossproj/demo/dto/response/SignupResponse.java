package ossproj.demo.dto.response;

import lombok.*;
import ossproj.demo.entity.Major;
import ossproj.demo.entity.Users;

@Getter
@ToString
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class SignupResponse {

    private Long userId;
    private String username;
    private String studentNumber;
    private Long majorId;

    static public SignupResponse toUser(Users user) {
        return SignupResponse.builder()
                .userId(user.getId())
                .studentNumber(user.getStudentNumber())
                .majorId(user.getMajor().getMajorId())
                .username(user.getUsername())
                .build();
    }
}
