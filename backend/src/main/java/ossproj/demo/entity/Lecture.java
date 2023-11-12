import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@NoArgsConstructor
public class Lecture {

    @Id
    @GeneratedValue
    @Column(name="lecture_id", nullable = false)
    private Long id;

    @ManyToOne
    @JoinColumn(name="professor_id", nullable = false)
    private Professor professor;

    @ManyToOne
    @JoinColumn(name = "major_id", nullable = false)
    private Major major;

    @Column(length = 30, nullable = false)
    private String lectureName;

    @Column(length = 30, nullable = false)
    private String lecturePlace;

    @Column(length = 5, nullable = false)
    private String firstDay;

    @Column(length = 5)
    private String secondDay;

    @Column(length = 50)
    private String firstDayStartTime;

    @Column(length = 50)
    private String firstDayEndTime;

    @Column(length = 50)
    private String secondDayStartTime;

    @Column(length = 50)
    private String secondDayEndTime;
}
