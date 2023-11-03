
import jakarta.persistence.Entity;
import org.springframework.data.jpa.repository.JpaRepository;
import ossproj.demo.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
}
