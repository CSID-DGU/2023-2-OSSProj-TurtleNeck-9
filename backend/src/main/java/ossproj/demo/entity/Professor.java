package ossproj.demo.entity;

import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;


@Getter
@NoArgsConstructor
@Entity(name = "professors")
public class Professor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "professor_id", unique = true, nullable = false)
    private Long professorId;


    @Column(length = 20, nullable = false)
    private String name;

    @ManyToOne
    @JoinColumn(name = "major_id", nullable = false)
    private Major major;

    @Builder
    public Professor(String name, Major major) {
        this.name = name;
        this.major = major;
    }
}
