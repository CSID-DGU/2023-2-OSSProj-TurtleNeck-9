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
    private String alFirstLectureName;

    @Column(nullable = false)
    private String alSecondLectureName;

    @Column(nullable = false)
    private String alThirdLectureName;

    @Column(nullable = false)
    private String alFourthLectureName;

    @Column(nullable = false)
    private String alFifthLectureName;

    @Column(nullable = false)
    private String alSixthLectureName;


    @Builder
    public AlreadyLecture(Users user, String alFirstLectureName, String alSecondLectureName, String alThirdLectureName, String alFourthLectureName, String alFifthLectureName, String alSixthLectureName) {
        this.user = user;
        this.alFirstLectureName = alFirstLectureName;
        this.alSecondLectureName = alSecondLectureName;
        this.alThirdLectureName = alThirdLectureName;
        this.alFourthLectureName = alFourthLectureName;
        this.alFifthLectureName = alFifthLectureName;
        this.alSixthLectureName = alSixthLectureName;
    }
}