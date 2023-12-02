package ossproj.demo.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.core.Authentication;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ossproj.demo.dto.JwtToken;
import ossproj.demo.dto.request.auth.SignupRequest;
import ossproj.demo.dto.response.SignupResponse;
import ossproj.demo.entity.Major;
import ossproj.demo.entity.Users;
import ossproj.demo.repository.MajorRepository;
import ossproj.demo.repository.UserRepository;
import ossproj.demo.util.JwtTokenProvider;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Slf4j
public class UserServiceImpl implements UserService {
    private final UserRepository userRepository;
    private final MajorRepository majorRepository;
    private final AuthenticationManagerBuilder authenticationManagerBuilder;
    private final JwtTokenProvider jwtTokenProvider;
    private final PasswordEncoder passwordEncoder;


    @Transactional
    public JwtToken login(String studentId, String password) {

        UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(studentId, password);
        Authentication authentication = authenticationManagerBuilder.getObject().authenticate(authenticationToken);

        return jwtTokenProvider.generateToken(authentication);
    }

    @Transactional
    @Override
    public SignupResponse signup(SignupRequest signupRequest) {
        if (userRepository.existsByStudentId(signupRequest.getStudentId())) {
            throw new IllegalArgumentException("이미 사용중인 학번입니다.");
        }
        System.out.println("회원 가입시 " + signupRequest.getMajor_id());
        Major major = majorRepository.findById(signupRequest.getMajor_id())
                .orElseThrow(() -> new RuntimeException("Major not found with id: " + signupRequest.getMajor_id()));
        String encodedPassword = passwordEncoder.encode(signupRequest.getPassword());
        List<String> roles = new ArrayList<>();
        roles.add("USER");
        return SignupResponse.toUser(userRepository.save(signupRequest.toEntity(encodedPassword, major, roles)));
    }

    public Optional<Users> findByStudentId(String studentId) {
        return userRepository.findByStudentId(studentId);
    }

    public Optional<Users> findByUserId(Long id) {
        return userRepository.findById(id);
    }

    public Optional<Users> findByUsername(String username) {
        return userRepository.findByUsername(username);
    }
}
