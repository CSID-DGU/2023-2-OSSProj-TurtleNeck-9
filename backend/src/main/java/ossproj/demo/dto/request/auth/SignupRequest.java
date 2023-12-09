package ossproj.demo.dto.request.auth;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import ossproj.demo.entity.Major;
import ossproj.demo.entity.Users;

import java.util.ArrayList;
import java.util.List;

@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SignupRequest {
    private String studentNumber;
    private String username;
    private Long major_id;
    private String password;
    private final List<String> roles = new ArrayList<>();

    public Users toEntity(String encodedPassword, Major major,List<String> roles) {
        return Users.builder()
                .studentNumber(studentNumber)
                .username(username)
                .password(encodedPassword)
                .major(major)
                .roles(roles)
                .build();
    }

}
