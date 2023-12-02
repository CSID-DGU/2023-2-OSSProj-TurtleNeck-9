package ossproj.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ossproj.demo.entity.Timetable;

@Repository
public interface TimetableRepository extends JpaRepository<Timetable, Long> {

    Timetable findByUserId(Long userId);

}
