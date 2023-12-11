package ossproj.demo.dto.response;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import ossproj.demo.dto.JwtToken;
import ossproj.demo.entity.Major;

@RequiredArgsConstructor
@AllArgsConstructor
@Getter
public class LoginResponse {
    private JwtToken jwtToken;
    private Long user_id;
    private Long major_id;

}
