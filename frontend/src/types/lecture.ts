export interface Lecture {
  lectureId: number;
  place: string;
  lectureName: string;
  professorName: string;
  lectureTime: LectureTime[];
}

export enum Weekday {
  Mon = 'mon',
  Tue = 'tue',
  Wed = 'wed',
  Thu = 'thu',
  Fri = 'fri',
  Sat = 'sat',
  Sun = 'sun',
}

export interface LectureTime {
  weekday: Weekday;
  startTime: string;
  endTime: string;
}
