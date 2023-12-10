import { Box, Button, CircularProgress, Typography } from '@mui/material';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Carousel from '../components/Carousel';
import MediaCard from '../components/MediaCard';
import ResponsiveDrawer from '../components/ResponsiveDrawer';
import { useSession } from '../hooks/useSession';

const Home = () => {
  const { hasSession } = useSession();
  const [isLoading, setIsLoading] = useState(true);

  const navigate = useNavigate();
  const handleButtonClick = (timeTableNumber: number) => () => {
    navigate(`/time-table/${timeTableNumber}`);
  };

  useEffect(() => {
    if (!hasSession) {
      navigate('/signin');
    }
  }, []);
  useEffect(() => {
    setTimeout(() => {
      setIsLoading(false);
    }, 3000);
  }, []);
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
        <Box display="flex" justifyContent="center" alignItems="center" gap="5px" mt="30px" minHeight="30px">
          {isLoading ? (
            <>
              <CircularProgress size="30px" />
              <Typography variant="body2">기존 수강과목 동기화 중...</Typography>
            </>
          ) : (
            <Typography variant="body2">기존 수강과목 동기화 완료 ✅</Typography>
          )}
        </Box>
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
