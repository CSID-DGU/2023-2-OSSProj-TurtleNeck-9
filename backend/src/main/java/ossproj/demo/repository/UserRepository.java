package ossproj.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import ossproj.demo.entity.Major;
import ossproj.demo.entity.Users;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<Users, Long> {
    Optional<Users> findById(Long id);

    Optional<Users> findByUsername(String username);

    Optional<Users> findByStudentNumber(String studentNumber);

    @Query("SELECT u.id FROM Users u WHERE u.studentNumber = ?1")
    Long findIdByStudentNumber(String studentNumber);

    @Query("SELECT u.major FROM Users u WHERE u.studentNumber = ?1")
    Major findMajorByStudentNumber(String studentNumber);

    boolean existsByStudentNumber(String studentNumber);

}
