import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { Lecture } from '../types/lecture';
import { getCookie } from '../utils/cookie';
import { lectureKeys } from './queryKeys';

const getLectureList = async (userId: number) => {
  const response = await axios.get<{ lectures: Lecture[] }[]>(`/timetables/${userId}`);

  return response.data;
};
const studentUserIdMapper: Record<string, number> = {
  20180001: 1,
  20190001: 2,
  20200001: 3,
};
export const useLectureListQuery = (timeTableNumber: number) => {
  const studentId = getCookie('studentId');
  const userId = studentUserIdMapper[studentId];
  return useQuery({
    queryFn: () => getLectureList(userId || 1),
    queryKey: lectureKeys.list(),
    select: (lectureList) => lectureList[timeTableNumber - 1].lectures,
  });
};
