package ossproj.demo.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ossproj.demo.dto.response.SuccessResponse;
import ossproj.demo.dto.response.TimetableResponse;
import ossproj.demo.exception.Success;
import ossproj.demo.service.TimetableService;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/timetables")
public class TimetableController {

    private final TimetableService timetableService;

    @GetMapping("/{userId}")
    public SuccessResponse<List<TimetableResponse>> getTimetables(@PathVariable Long userId) {
        List<TimetableResponse> timetables = timetableService.createTimetables(userId);
        return SuccessResponse.success(Success.GET_TIMETABLE_SUCCESS,timetables);
    }
}
