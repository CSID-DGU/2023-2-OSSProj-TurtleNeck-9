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

export const mockLectures = [
  {
    lectureId: 1,
    place: '원흥관 F540',
    lectureName: '산업시스템프로그래밍2',
    professorName: '이종태',
    lectureTime: [
      {
        weekday: 'fri',
        startTime: '11:00',
        endTime: '12:00',
      },
      {
        weekday: 'mon',
        startTime: '11:00',
        endTime: '12:00',
      },
    ],
  },
  {
    lectureId: 2,
    place: '원흥관 F340',
    lectureName: '경영과학1',
    professorName: '홍성조',
    lectureTime: [
      {
        weekday: 'thu',
        startTime: '09:00',
        endTime: '10:30',
      },
      {
        weekday: 'wed',
        startTime: '11:00',
        endTime: '12:00',
      },
    ],
  },
  {
    lectureId: 3,
    place: '원흥관 F450',
    lectureName: '데이터애널리틱스',
    professorName: '윤병운',
    lectureTime: [
      {
        weekday: 'wed',
        startTime: '13:00',
        endTime: '15:00',
      },
      {
        weekday: 'fri',
        startTime: '13:00',
        endTime: '15:00',
      },
    ],
  },
  {
    lectureId: 4,
    place: '정보문화관 443',
    lectureName: '기술경영',
    professorName: '서용윤',
    lectureTime: [
      {
        weekday: 'mon',
        startTime: '10:30',
        endTime: '12:00',
      },
      {
        weekday: 'wed',
        startTime: '10:30',
        endTime: '12:00',
      },
    ],
  },
  {
    lectureId: 6,
    place: '신공학관 340',
    lectureName: '품질공학',
    professorName: '서용윤',
    lectureTime: [
      {
        weekday: 'mon',
        startTime: '13:00',
        endTime: '15:00',
      },
      {
        weekday: 'wed',
        startTime: '13:00',
        endTime: '15:00',
      },
    ],
  },
] as Lecture[];
