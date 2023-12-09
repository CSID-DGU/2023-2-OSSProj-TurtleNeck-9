import { Box, CircularProgress, Container } from '@mui/material';
import { useParams } from 'react-router-dom';
import ResponsiveDrawer from '../../components/ResponsiveDrawer';
import TimeTable from '../../components/TimeTable';
import { useLectureListQuery } from '../../query/lecture';

const TimeTableDetail = () => {
  const { timeTableNumber } = useParams();
  const { data } = useLectureListQuery(Number(timeTableNumber));
  return (
    <Container>
      <ResponsiveDrawer>
        <Box display="flex" minHeight="400px" justifyContent="space-around" flexDirection="column" alignItems="center">
          {data ? <TimeTable lectureList={data} /> : <CircularProgress />}
        </Box>
      </ResponsiveDrawer>
    </Container>
  );
};

export default TimeTableDetail;
