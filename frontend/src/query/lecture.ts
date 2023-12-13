import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { Lecture } from '../types/lecture';
import { getCookie } from '../utils/cookie';
import { lectureKeys } from './queryKeys';

let resolveFn: (value: unknown) => void;
const delay = new Promise((resolve) => {
  resolveFn = resolve;
});
const getLectureList = async (userId: number) => {
  const response = await axios.get<{ data: { lectures: Lecture[] }[] }>(`/timetables/${userId}`);
  setTimeout(() => {
    resolveFn(true);
  }, 2000);
  await delay;

  return response.data;
};

export const useLectureListQuery = (timeTableNumber: number) => {
  const majorId = getCookie('major_id');

  return useQuery({
    queryFn: () => getLectureList(Number(majorId)),
    queryKey: lectureKeys.list(Number(majorId)),
    select: (lectureList) => {
      return lectureList.data[timeTableNumber - 1].lectures;
    },
  });
};
