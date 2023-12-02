package ossproj.demo.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ossproj.demo.dto.response.LectureResponse;
import ossproj.demo.dto.response.LectureTimeResponse;
import ossproj.demo.dto.response.TimetableResponse;
import ossproj.demo.entity.Lecture;
import ossproj.demo.entity.Timetable;
import ossproj.demo.entity.Users;
import ossproj.demo.repository.LectureRepository;
import ossproj.demo.repository.TimetableRepository;
import ossproj.demo.repository.UserRepository;

import java.time.LocalTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Slf4j
public class TimetableService {

    private final LectureRepository lectureRepository;
    private final TimetableRepository timetableRepository;
    private final UserRepository userRepository;

    @Transactional
    public List<TimetableResponse> createTimetables(Long userId) {
        Optional<Timetable> userTimetable = timetableRepository.findByUser_Id(userId);
        List<Long> lectureIds = extractLecturesIds(userTimetable);
        List<Lecture> lectures = lectureRepository.findAllById(lectureIds);

        // 시간표 조합
        List<List<Lecture>> timetableCombinations = generateTimetableCombinations(lectures);

        return convertToTimetableResponseDtos(timetableCombinations);
    }

    /**
     * 시간표 엔티티에서 강의 Id들을 가져오는 함수
     * @param timetable
     * @return List<lecture>
     */
    private List<Long> extractLecturesIds(Optional<Timetable> timetable) {

        System.out.println("timetable = " + timetable);
        List<Long> lecturesIds = new ArrayList<>();

        lecturesIds.add((long) timetable.get().getFirstLectureId());
        lecturesIds.add((long) timetable.get().getSecondLectureId());
        lecturesIds.add((long) timetable.get().getThirdLectureId());
        lecturesIds.add((long) timetable.get().getFourthLectureId());
        lecturesIds.add((long) timetable.get().getFifthLectureId());
        lecturesIds.add((long) timetable.get().getSixthLectureId());
        lecturesIds.add((long) timetable.get().getSeventhLectureId());
        lecturesIds.add((long) timetable.get().getEighthLectureId());
        lecturesIds.add((long) timetable.get().getNinthLectureId());
        lecturesIds.add((long) timetable.get().getTenthLectureId());

        return lecturesIds;
    }

    private List<List<Lecture>> generateTimetableCombinations(List<Lecture> lectures) {
        List<List<Lecture>> validCombinations = new ArrayList<>();

        // 강의를 6개씩 묶어서 조합을 생성하고, 겹치지 않는 조합만 선택합니다.
        for (int i = 0; i < lectures.size(); i++) {
            for (int j = i + 1; j < lectures.size(); j++) {
                for (int k = j + 1; k < lectures.size(); k++) {
                    for (int l = k + 1; l < lectures.size(); l++) {
                        for (int m = l + 1; m < lectures.size(); m++) {
                            for (int n = m + 1; n < lectures.size(); n++) {
                                List<Lecture> combination = Arrays.asList(
                                        lectures.get(i), lectures.get(j), lectures.get(k),
                                        lectures.get(l), lectures.get(m), lectures.get(n)
                                );
                                if (isValidCombination(combination)) {
                                    validCombinations.add(combination);
                                }
                            }
                        }
                    }
                }
            }
        }

        int limit = 3;
        List<List<Lecture>> selectedCombinations = new ArrayList<>();
        for (int i = 0; i < validCombinations.size() && i < limit; i += 3) {
            if (i + 2 < validCombinations.size()) {
                selectedCombinations.add(validCombinations.get(i));
                selectedCombinations.add(validCombinations.get(i + 1));
                selectedCombinations.add(validCombinations.get(i + 2));
            }
        }

        return selectedCombinations;
    }

    private boolean isValidCombination(List<Lecture> combination) {
        // 각 강의끼리의 모든 시간을 비교하여 겹치지 않는지 확인합니다.
        for (int i = 0; i < combination.size(); i++) {
            for (int j = i + 1; j < combination.size(); j++) {
                System.out.println("combination 21321321= " + combination.get(j));
                if (isOverlapping(combination.get(i), combination.get(j))) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isOverlapping(Lecture lecture1, Lecture lecture2) {
        // 강의의 요일을 비교하여 겹치는 경우가 있는지 확인합니다.
        return isDayOverlapping(lecture1, lecture2) && isTimeOverlapping(lecture1, lecture2);
    }

    private boolean isDayOverlapping(Lecture lecture1, Lecture lecture2) {
        // 강의의 요일을 비교하여 겹치는 경우가 있는지 확인합니다.
        if (lecture1.getSecondDay() == null || lecture2.getSecondDay() == null) {
            // 두 번째 날 중 하나가 null인 경우 겹치지 않음으로 처리
            return false;
        }

        return lecture1.getFirstDay().equals(lecture2.getFirstDay()) ||
                lecture1.getFirstDay().equals(lecture2.getSecondDay()) ||
                lecture1.getSecondDay().equals(lecture2.getFirstDay()) ||
                lecture1.getSecondDay().equals(lecture2.getSecondDay());
    }

    private boolean isTimeOverlapping(Lecture lecture1, Lecture lecture2) {
        // 강의의 시간을 비교하여 겹치는 경우가 있는지 확인합니다.
        LocalTime start1 = LocalTime.parse(lecture1.getFirstDayStartTime());
        LocalTime end1 = LocalTime.parse(lecture1.getFirstDayEndTime());
        LocalTime start2 = LocalTime.parse(lecture2.getFirstDayStartTime());
        LocalTime end2 = LocalTime.parse(lecture2.getFirstDayEndTime());

        return !(end1.isBefore(start2) || start1.isAfter(end2));
    }

    private List<TimetableResponse> convertToTimetableResponseDtos(List<List<Lecture>> timetableCombinations) {
        List<TimetableResponse> timetables = new ArrayList<>();

        for (List<Lecture> timetableCombination : timetableCombinations) {
            TimetableResponse timetableDto = new TimetableResponse();
            List<LectureResponse> lectureResponses = new ArrayList<>();

            for (Lecture lecture : timetableCombination) {
                LectureResponse lectureResponse = new LectureResponse();
                lectureResponse.setPlace(lecture.getPlace());
                lectureResponse.setLectureId(lecture.getLectureId());
                lectureResponse.setLectureName(lecture.getLectureName());
                lectureResponse.setProfessorName(lecture.getProfessorName());

                // 강의 시간 정보 변환
                List<LectureTimeResponse> lectureTimes = new ArrayList<>();
                if (lecture.getFirstDay() != null && lecture.getFirstDayStartTime() != null && lecture.getFirstDayEndTime() != null) {
                    lectureTimes.add(new LectureTimeResponse(lecture.getFirstDay(), lecture.getFirstDayStartTime(), lecture.getFirstDayEndTime()));
                }
                if (lecture.getSecondDay() != null && lecture.getSecondDayStartTime() != null && lecture.getSecondDayEndTime() != null) {
                    lectureTimes.add(new LectureTimeResponse(lecture.getSecondDay(), lecture.getSecondDayStartTime(), lecture.getSecondDayEndTime()));
                }

                lectureResponse.setLectureTime(lectureTimes);
                lectureResponses.add(lectureResponse);
            }

            timetableDto.setLectures(lectureResponses);
            timetables.add(timetableDto);
        }

        return timetables;
    }

}
