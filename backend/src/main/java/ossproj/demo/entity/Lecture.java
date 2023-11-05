import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;

@Entity
@Getter @Setter
public class Lecture {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="lecture_id")
    private Long id;

    private String name;

    private String place;

    private Professor professor;
    private Major major;

    private String firstDay;
    private String secondDay;
    private String firstDayStartTime;
    private String firstDayEndTime;
    private String secondDayStartTime;
    private String secondDayEndTime;


}
