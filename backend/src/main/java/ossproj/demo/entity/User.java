package ossproj.demo.entity;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import lombok.*;
import java.util.List;
import java.lang.reflect.Member;

@Getter
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(nullable = false, unique = true)
    private String studentId;


    @Column(nullable = false, unique = false)
    private String name;

    @OneToMany(mappedBy = "user")
    private List<Member> members = new ArrayList<>();

    @Column(length = 100)
    private String password;

}
