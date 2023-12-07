package ossproj.demo.entity;

import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import ossproj.demo.dto.response.AlreadyLectureSaveResponse;

@Getter
@NoArgsConstructor
@Entity(name="already_lectures")
public class AlreadyLecture extends AlreadyLectureSaveResponse {

    @Id
    @GeneratedValue
    @Column(name = "already_lecture_id", nullable = false)
    private Long id;

    @OneToOne
    @JoinColumn(name = "user_id", nullable = false)
    private Users user;

    @Column(nullable = false)
    private int alFirstId;

    @Column(nullable = false)
    private int alSecondId;

    @Column(nullable = false)
    private int alThirdId;

    @Column(nullable = false)
    private int alFourthId;

    @Column(nullable = false)
    private int alFifthId;

    @Column(nullable = false)
    private int alSixthId;


    @Builder
    public AlreadyLecture(Users user, int alFirstId, int alSecondId, int alThirdId, int alFourthId, int alFifthId, int alSixthId) {
        this.user = user;
        this.alFirstId = alFirstId;
        this.alSecondId = alSecondId;
        this.alThirdId = alThirdId;
        this.alFourthId = alFourthId;
        this.alFifthId = alFifthId;
        this.alSixthId = alSixthId;
    }
}