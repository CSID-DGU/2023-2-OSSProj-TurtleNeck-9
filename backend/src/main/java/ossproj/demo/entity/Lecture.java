import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter @Setter
public class Lecture {

    @Id
    @GeneratedValue
    @Column(name="lecture_id")
    private Long id;

    private String name;

    private String place;

    @ManyToOne
    @JoinColumn(name="professor_id")
    private Professor professor;

    @ManyToOne
    @JoinColumn(name = "major_id")
    private Major major;

    private String firstDay;
    private String secondDay;
    private String firstDayStartTime;
    private String firstDayEndTime;
    private String secondDayStartTime;
    private String secondDayEndTime;


}
