package ossproj.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ossproj.demo.entity.Lecture;

@Repository
public interface LectureRepository extends JpaRepository<Lecture, Long> {

}
