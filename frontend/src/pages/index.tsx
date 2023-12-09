import { Box, Button, Container, Typography } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import Carousel from '../components/Carousel';
import MediaCard from '../components/MediaCard';
import ResponsiveDrawer from '../components/ResponsiveDrawer';

const Home = () => {
  const navigate = useNavigate();
  const handleButtonClick = (timeTableNumber: number) => () => {
    navigate(`/time-table/${timeTableNumber}`);
  };
  return (
    <ResponsiveDrawer>
      <Box
        display="flex"
        height="400px"
        justifyContent="space-around"
        flexDirection="column"
        alignItems="center"
        paddingTop="300px"
      >
        <Carousel />
        <Box display="flex" justifyContent="space-around" width="100%" gap="5px" mt="30px">
          <MediaCard title="추천 시간표 1️⃣" description="📌 공강있는 시간표">
            <Button size="medium" variant="contained" color="warning" onClick={handleButtonClick(1)}>
              시간표 확인하기
            </Button>
          </MediaCard>
          <MediaCard title="추천 시간표 2️⃣" description="📌 A+ 맞는 시간표">
            <Button size="medium" variant="contained" color="warning" onClick={handleButtonClick(2)}>
              시간표 확인하기
            </Button>
          </MediaCard>
          <MediaCard title="추천 시간표 3️⃣" description="📌 갓생사는 시간표">
            <Button size="medium" variant="contained" color="warning" onClick={handleButtonClick(3)}>
              시간표 확인하기
            </Button>
          </MediaCard>
        </Box>
      </Box>
    </ResponsiveDrawer>
  );
};

export default Home;
