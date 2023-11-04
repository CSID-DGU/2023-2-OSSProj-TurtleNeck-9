import jakarta.persistence.*;
import lombok.Getter;

@Getter
@Entity
public class Professor {
    @Id
    @GeneratedValue
    @Column(name = "professor_id")
    private Long id;

    private String name;

    @ManyToOne
    private Major major;

}
