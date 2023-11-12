import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@NoArgsConstructor
public class Major {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "major_id", unique = true, nullable = false)
    private Long id;

    @Column(length = 20, nullable = false)
    private String professorName;

    @Column(length = 20, nullable = false)
    private String department;

    @Builder
    public Major(String professorName, String department) {
        this.professorName = professorName;
        this.department = department;
    }
}
