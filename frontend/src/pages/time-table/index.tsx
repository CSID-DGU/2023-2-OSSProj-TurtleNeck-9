import { Box, CircularProgress, Container, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';
import ResponsiveDrawer from '../../components/ResponsiveDrawer';
import TimeTable from '../../components/TimeTable';
import { useLectureListQuery } from '../../query/lecture';

const TimeTableDetail = () => {
  const { timeTableNumber } = useParams();
  const { data, isError } = useLectureListQuery(Number(timeTableNumber));

  return (
    <Container>
      <ResponsiveDrawer>
        <Box display="flex" minHeight="400px" justifyContent="space-around" flexDirection="column" alignItems="center">
          {data ? <TimeTable lectureList={data} /> : <CircularProgress />}
          {isError && <Typography>시간표 조회 중 에러가 발생했습니다. 새로고침 후 다시 시도해주세요.</Typography>}
        </Box>
      </ResponsiveDrawer>
    </Container>
  );
};

export default TimeTableDetail;
