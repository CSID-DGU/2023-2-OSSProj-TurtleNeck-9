package ossproj.demo.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ossproj.demo.dto.request.lecture.AlreadyLectureSaveRequest;
import ossproj.demo.dto.response.AlreadyLectureSaveResponse;
import ossproj.demo.entity.AlreadyLecture;
import ossproj.demo.entity.Users;
import ossproj.demo.repository.AlreadyLectureRepository;
import ossproj.demo.repository.UserRepository;

@Service
@RequiredArgsConstructor
@Slf4j
@Transactional
public class AlreadyLectureService {

    private final UserRepository userRepository;
    private final AlreadyLectureRepository alreadyLectureRepository;

    public AlreadyLectureSaveResponse saveUserAlreadyLecture(Long userId, AlreadyLectureSaveRequest saveRequest) {
        Users user = userRepository.findById(userId).orElseThrow(() -> new RuntimeException("User not found"));

        AlreadyLecture generateAlreadyLecture = AlreadyLecture.builder()
                .user(user)
                .alFirstId(saveRequest.getAlFirstId())
                .alSecondId(saveRequest.getAlSecondId())
                .alThirdId(saveRequest.getAlThirdId())
                .alFourthId(saveRequest.getAlFourthId())
                .alFifthId(saveRequest.getAlFifthId())
                .alSixthId(saveRequest.getAlSixthId())
                .build();

        return alreadyLectureRepository.save(generateAlreadyLecture);
    }
}
