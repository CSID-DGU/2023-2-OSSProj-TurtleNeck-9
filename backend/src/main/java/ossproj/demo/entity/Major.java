import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
public class Major {

    @Id
    @GeneratedValue
    @Column(name = "major_id")
    private Long id;

    private String name;
    private String department;

}
