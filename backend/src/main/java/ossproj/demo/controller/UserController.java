package ossproj.demo.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ossproj.demo.dto.JwtToken;
import ossproj.demo.dto.request.auth.LoginRequest;
import ossproj.demo.dto.request.auth.SignupRequest;
import ossproj.demo.dto.response.LectureResponse;
import ossproj.demo.dto.response.LoginResponse;
import ossproj.demo.dto.response.SignupResponse;
import ossproj.demo.dto.response.SuccessResponse;
import ossproj.demo.exception.Success;
import ossproj.demo.service.UserService;

@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("users")
public class UserController {

    private final UserService userService;


    @PostMapping("/signup")
    public SuccessResponse<SignupResponse> signup(@RequestBody SignupRequest signupRequest) {
        SignupResponse savedUser = userService.signup(signupRequest);
        return SuccessResponse.success(Success.POST_SIGNUP_SUCCESS, savedUser);
    }


    @PostMapping("/login")
    public SuccessResponse<LoginResponse> login(@RequestBody LoginRequest loginRequest) {
        String studentId = loginRequest.getStudentNumber();
        String password = loginRequest.getPassword();
        LoginResponse login = userService.login(studentId, password);
        return SuccessResponse.success(Success.POST_LOGIN_SUCCESS, login);
    }

    @PostMapping("/test")
    public String test() {
        return "success";
    }
}
