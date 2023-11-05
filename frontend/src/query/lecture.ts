import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { Lecture } from '../types/lecture';
import { lectureKeys } from './queryKeys';

const getLectureList = async () => {
  const response = await axios.get<Lecture[]>('https://6545b51afe036a2fa954b249.mockapi.io/api/v1/courses');

  return response.data;
};

export const useLectureListQuery = (index: number) => {
  return useQuery({
    queryFn: getLectureList,
    queryKey: lectureKeys.list(),
    select: (lectureList) => lectureList[index],
  });
};
