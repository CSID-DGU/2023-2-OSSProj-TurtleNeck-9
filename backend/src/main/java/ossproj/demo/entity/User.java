import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import lombok.Setter;
import org.springframework.data.annotation.Id;

@Entity
@Getter
@NoArgsConstructor
@Table(name = "user")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "user_id", unique = true, nullable = false)
    private Long id;

    @Column(length = 15, unique = true, nullable = false)
    private int studentNumber;

    @Column(nullable = false, unique = false)
    private String username;

    @OneToMany(mappedBy = "major", cascade = CascadeType.MERGE)
    private Major major;

    @Column(length = 100, nullable = false)
    private String password;

    @Builder
    public User(int studentNumber, String username, String password)
}
