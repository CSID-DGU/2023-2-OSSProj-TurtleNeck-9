package ossproj.demo.service;

import ossproj.demo.dto.JwtToken;
import ossproj.demo.dto.request.auth.SignupRequest;
import ossproj.demo.dto.response.SignupResponse;

public interface UserService {
    JwtToken login(String studentId, String password);

    SignupResponse signup(SignupRequest signupRequest);
}
