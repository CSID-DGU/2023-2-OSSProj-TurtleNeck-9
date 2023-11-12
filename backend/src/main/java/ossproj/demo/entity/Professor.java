package entity;

import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import static jakarta.persistence.FetchType.LAZY;

@Entity
@Getter
@NoArgsConstructor
public class Professor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "professor_id", unique = true, nullable = false)
    private Long id;


    @Column(length = 20, nullable = false)
    private String name;

    @ManyToOne(fetch = LAZY)
    @JoinColumn(name = "major_id", nullable = false)
    private Major major;

    @Builder
    public Professor(String name, Major major) {
        this.name = name;
        this.major = major;
    }
}
