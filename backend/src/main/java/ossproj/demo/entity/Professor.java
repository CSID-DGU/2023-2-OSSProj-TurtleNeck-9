import jakarta.persistence.*;
import lombok.Getter;

import static jakarta.persistence.FetchType.LAZY;

@Getter
@Entity
public class Professor {
    @Id
    @GeneratedValue
    @Column(name = "professor_id")
    private Long id;

    private String name;

    @ManyToOne(fetch = LAZY)
    @JoinColumn(name = "major_id")
    private Major major;
}
