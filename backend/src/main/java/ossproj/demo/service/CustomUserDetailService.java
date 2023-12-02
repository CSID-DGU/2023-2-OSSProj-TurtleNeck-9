package ossproj.demo.service;

import lombok.RequiredArgsConstructor;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import ossproj.demo.entity.Users;
import ossproj.demo.repository.UserRepository;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class CustomUserDetailService implements UserDetailsService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    @Override
    public UserDetails loadUserByUsername(String studentId) throws UsernameNotFoundException {
        Optional<Users> findOne = userRepository.findByStudentId(studentId);
        Users user =findOne.orElseThrow(() -> new UsernameNotFoundException("해당하는 회원을 찾을 수 없습니다."));
        return User.builder()
                .username(user.getStudentId())
                .password(user.getPassword())
                .roles(String.valueOf(user.getRoles()))
                .build();

    }
}
