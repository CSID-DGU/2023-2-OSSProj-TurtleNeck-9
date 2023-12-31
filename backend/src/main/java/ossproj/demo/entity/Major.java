package ossproj.demo.entity;

import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
@Entity(name = "major")
public class Major {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "major_id", unique = true, nullable = false)
    private Long majorId;

    @Column(length = 20, nullable = false)
    private String department;

    @Builder
    public Major(String department) {
        this.department = department;
    }
}
