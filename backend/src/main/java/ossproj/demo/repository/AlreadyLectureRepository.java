package ossproj.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import ossproj.demo.entity.AlreadyLecture;

public interface AlreadyLectureRepository extends JpaRepository<AlreadyLecture, Long> {


}
