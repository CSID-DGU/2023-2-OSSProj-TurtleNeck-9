package ossproj.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ossproj.demo.entity.Major;

import java.util.Optional;

@Repository
public interface MajorRepository extends JpaRepository<Major, Long> {
    Optional<Major> findByMajorId(Long majorId);

    @Override
    Optional<Major> findById(Long majorId);
}
