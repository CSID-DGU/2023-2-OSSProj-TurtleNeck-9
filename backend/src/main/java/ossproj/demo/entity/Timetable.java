package ossproj.demo.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
@Entity(name = "timetables")
public class Timetable {

    @Id
    @GeneratedValue
    @Column(name = "timetable_id", nullable = false)
    private Long id;


    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private Users user;

    @Column
    private int firstLectureId;

    @Column
    private int secondLectureId;

    @Column
    private int thirdLectureId;

    @Column
    private int fourthLectureId;

    @Column
    private int fifthLectureId;

    @Column
    private int sixthLectureId;

    @Column
    private int seventhLectureId;


}
