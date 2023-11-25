package ossproj.demo.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ossproj.demo.dto.JwtToken;
import ossproj.demo.dto.request.LoginRequest;
import ossproj.demo.dto.request.SignupRequest;
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
    public JwtToken login(@RequestBody LoginRequest loginRequest) {
        String studentId = loginRequest.getStudentId();
        String password = loginRequest.getPassword();
        JwtToken jwtToken = userService.login(studentId, password);
        log.info("requset studentId = {} , password = {}", studentId, password);
        log.info("jwtToken accessToken = {}, refreshToken = {}", jwtToken.getAccessToken(), jwtToken.getRefreshToken());
        return jwtToken;
    }

    @PostMapping("/test")
    public String test() {
        return "success";
    }
}
