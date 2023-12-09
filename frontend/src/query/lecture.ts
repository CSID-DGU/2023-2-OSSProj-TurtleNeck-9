import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { Lecture } from '../types/lecture';
import { lectureKeys } from './queryKeys';

const getLectureList = async () => {
  const response = await axios.get<{ lectures: Lecture[] }[]>(`/timetables`);

  return response.data;
};

export const useLectureListQuery = (timeTableNumber: number) => {
  return useQuery({
    queryFn: getLectureList,
    queryKey: lectureKeys.list(),
    select: (lectureList) => lectureList[timeTableNumber - 1].lectures,
  });
};
