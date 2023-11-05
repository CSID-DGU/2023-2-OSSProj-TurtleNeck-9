import { Box, CircularProgress, Container, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';
import Header from '../../components/layout/Header';
import TimeTable from '../../components/TimeTable';
import { useLectureListQuery } from '../../query/lecture';

const TimeTableDetail = () => {
  const { timeTableNumber } = useParams();
  const { data } = useLectureListQuery(Number(timeTableNumber));
  return (
    <Container>
      <Header />
      <Typography variant="h5">추천시간표 {timeTableNumber}</Typography>
      <Box display="flex" minHeight="400px" justifyContent="space-around" flexDirection="column" alignItems="center">
        {data ? <TimeTable lectureList={data} /> : <CircularProgress />}
      </Box>
    </Container>
  );
};

export default TimeTableDetail;
