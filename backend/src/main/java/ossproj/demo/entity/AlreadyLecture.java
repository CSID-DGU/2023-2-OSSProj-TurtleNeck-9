package ossproj.demo.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
@Entity(name="already_lectures")

public class AlreadyLecture {

    @Id
    @GeneratedValue
    @Column(name = "already_lecture_id", nullable = false)
    private Long id;

    @OneToOne
    @JoinColumn(name = "user_id", nullable = false)
    private Users user;

    @Column(nullable = false)
    private String alFirstId;

    @Column(nullable = false)
    private String alSecondId;

    @Column(nullable = false)
    private String alThirdId;

    @Column(nullable = false)
    private String alFourthId;

    @Column(nullable = false)
    private String alFifthId;

    @Column(nullable = false)
    private String alSixthId;

}