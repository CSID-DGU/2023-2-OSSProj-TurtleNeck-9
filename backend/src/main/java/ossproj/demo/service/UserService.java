package ossproj.demo.service;

import org.springframework.stereotype.Service;
import ossproj.demo.entity.Users;
import ossproj.demo.repository.UserRepository;

import java.util.Optional;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public Optional<Users> findByUserId(Long id) {
        return userRepository.findById(id);
    }

    public Optional<Users> findByUsername(String username) {
        return userRepository.findByUsername(username);
    }
}
