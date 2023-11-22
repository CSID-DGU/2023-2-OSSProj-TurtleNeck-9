package ossproj.demo.entity;

import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;


@Entity
@Getter
@NoArgsConstructor
@Table(name = "users")
public class Users {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "user_id", unique = true, nullable = false)
    private Long userId;

    @Column(length = 15, unique = true, nullable = false)
    private int studentNumber;

    @Column(nullable = false, unique = false)
    private String username;

    @ManyToOne
    @JoinColumn(name = "major_id", nullable = false)
    private Major major;

    @Column(length = 100, nullable = false)
    private String password;

    @Builder
    public Users(int studentNumber, Major major, String username, String password) {
        this.studentNumber = studentNumber;
        this.major = major;
        this.username = username;
        this.password = password;
    }
}
