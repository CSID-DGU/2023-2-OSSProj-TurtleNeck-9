import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;

import org.springframework.data.annotation.Id;

@Getter
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column
    private Long studentId;

    @Column(nullable = false, unique = false)
    private String name;

    @Column(name="major_id")
    @OneToMany
    private Long majorId;

    @Column(length = 100)
    private String password;
}
