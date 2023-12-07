package ossproj.demo.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;
import ossproj.demo.dto.request.lecture.AlreadyLectureSaveRequest;
import ossproj.demo.dto.response.AlreadyLectureSaveResponse;
import ossproj.demo.dto.response.SuccessResponse;
import ossproj.demo.exception.Success;
import ossproj.demo.service.AlreadyLectureService;

@RestController
@AllArgsConstructor
@RequestMapping("/already-lectures")
public class AlreadyLectureController {

    private final AlreadyLectureService alreadyLectureService;

    @PostMapping("/{userId}")
    public SuccessResponse saveUserAlreadyLectures(
            @PathVariable Long userId,
            @RequestBody AlreadyLectureSaveRequest saveRequest
            ) {
        AlreadyLectureSaveResponse alreadyLectureSaveResponse = alreadyLectureService.saveUserAlreadyLecture(userId, saveRequest);
        return SuccessResponse.success(Success.POST_ALREADYLECTURES_SUCCESS,"");
    }

}
