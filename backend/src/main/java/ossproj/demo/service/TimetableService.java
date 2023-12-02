package ossproj.demo.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import ossproj.demo.dto.response.LectureResponse;
import ossproj.demo.dto.response.LectureTimeResponse;
import ossproj.demo.dto.response.TimetableResponse;
import ossproj.demo.entity.Lecture;
import ossproj.demo.entity.Timetable;
import ossproj.demo.repository.LectureRepository;
import ossproj.demo.repository.TimetableRepository;

import java.time.LocalTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class TimetableService {

    private final LectureRepository lectureRepository;
    private final TimetableRepository timetableRepository;

    public List<TimetableResponse> createTimetables(Long userId) {
        Timetable userTimetable = timetableRepository.findByUserId(userId);
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
    private List<Long> extractLecturesIds(Timetable timetable) {

        List<Long> lecturesIds = new ArrayList<>();

        lecturesIds.add((long) timetable.getFirstLectureId());
        lecturesIds.add((long) timetable.getSecondLectureId());
        lecturesIds.add((long) timetable.getThirdLectureId());
        lecturesIds.add((long) timetable.getFourthLectureId());
        lecturesIds.add((long) timetable.getFifthLectureId());
        lecturesIds.add((long) timetable.getSixthLectureId());
        lecturesIds.add((long) timetable.getSeventhLectureId());
        lecturesIds.add((long) timetable.getEighthLectureId());
        lecturesIds.add((long) timetable.getNinthLectureId());
        lecturesIds.add((long) timetable.getTenthLectureId());

        return lecturesIds;
    }

    private List<List<Lecture>> generateTimetableCombinations(List<Lecture> lectures) {
        List<List<Lecture>> allCombinations = new ArrayList<>();
        for (int i = 0; i < lectures.size(); i++) {
            for (int j = i + 1; j < lectures.size(); j++) {
                for (int k = j + 1; k < lectures.size(); k++) {
                    List<Lecture> combination = Arrays.asList(lectures.get(i), lectures.get(j), lectures.get(k));
                    if (isValidCombination(combination)) {
                        allCombinations.add(combination);
                    }
                }
            }
        }
        return allCombinations;
    }

    private boolean isValidCombination(List<Lecture> combination) {
        for (int i = 0; i < combination.size(); i++) {
            for (int j = i + 1; j < combination.size(); j++) {
                if (isOverlapping(combination.get(i), combination.get(j))) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isOverlapping(Lecture lecture1, Lecture lecture2) {
        // 각 강의의 요일 및 시간을 비교하여 겹치는 경우가 있는지 확인
        // 예시: lecture1과 lecture2의 각 요일 및 시간대를 비교
        return isTimeOverlapping(lecture1.getFirstDay(), lecture1.getFirstDayStartTime(), lecture1.getFirstDayEndTime(), lecture2.getFirstDay(), lecture2.getFirstDayStartTime(), lecture2.getFirstDayEndTime())
                || isTimeOverlapping(lecture1.getFirstDay(), lecture1.getFirstDayStartTime(), lecture1.getFirstDayEndTime(), lecture2.getSecondDay(), lecture2.getSecondDayStartTime(), lecture2.getSecondDayEndTime())
                || isTimeOverlapping(lecture1.getSecondDay(), lecture1.getSecondDayStartTime(), lecture1.getSecondDayEndTime(), lecture2.getFirstDay(), lecture2.getFirstDayStartTime(), lecture2.getFirstDayEndTime())
                || isTimeOverlapping(lecture1.getSecondDay(), lecture1.getSecondDayStartTime(), lecture1.getSecondDayEndTime(), lecture2.getSecondDay(), lecture2.getSecondDayStartTime(), lecture2.getSecondDayEndTime());
    }

    private boolean isTimeOverlapping(String day1, String startTime1, String endTime1, String day2, String startTime2, String endTime2) {
        if (day1 == null || day2 == null) {
            return false;
        }

        if (!day1.equals(day2)) {
            return false;
        }

        LocalTime start1 = LocalTime.parse(startTime1);
        LocalTime end1 = LocalTime.parse(endTime1);
        LocalTime start2 = LocalTime.parse(startTime2);
        LocalTime end2 = LocalTime.parse(endTime2);

        return !(end1.isBefore(start2) || start1.isAfter(end2));
    }

    private List<TimetableResponse> convertToTimetableResponseDtos(List<List<Lecture>> timetableCombinations) {
        List<TimetableResponse> timetables = new ArrayList<>();

        for (List<Lecture> timetableCombination : timetableCombinations) {
            TimetableResponse timetableDto = new TimetableResponse();
            List<LectureResponse> lectureResponses = new ArrayList<>();

            for (Lecture lecture : timetableCombination) {
                LectureResponse lectureResponse = new LectureResponse();
                lectureResponse.setLectureId(lecture.getLectureId());
                lectureResponse.setLectureName(lecture.getLectureName());
                lectureResponse.setProfessorName(lecture.getProfessor().getName());

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
