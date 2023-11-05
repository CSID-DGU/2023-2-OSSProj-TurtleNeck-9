import { Box, Container, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';
import Header from '../../components/layout/Header';
import TimeTable from '../../components/TimeTable';
import { useLectureListQuery } from '../../query/lecture';

const TimeTableDetail = () => {
  const { timeTableNumber } = useParams();
  const { data, isSuccess } = useLectureListQuery(Number(timeTableNumber));
  return (
    <Container>
      <Header />
      <Box display="flex" minHeight="400px" justifyContent="space-around" flexDirection="column" alignItems="center">
        <Typography variant="h5">추천시간표 1</Typography>
        {isSuccess && <TimeTable lectureList={data} />}
      </Box>
    </Container>
  );
};

export default TimeTableDetail;
