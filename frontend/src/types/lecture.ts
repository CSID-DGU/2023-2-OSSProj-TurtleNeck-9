export interface Lecture {
  lectureId: number;
  place: string;
  lectureName: string;
  professorName: string;
  lectureTime: LectureTime[];
}

export interface LectureTime {
  weekday: string;
  startTime: string;
  endTime: string;
}
