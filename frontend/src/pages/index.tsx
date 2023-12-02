import { Box, Button, Container, Typography } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import ResponsiveDrawer from '../components/ResponsiveDrawer';

const Home = () => {
  const navigate = useNavigate();
  const handleButtonClick = (timeTableNumber: number) => () => {
    navigate(`/time-table/${timeTableNumber}`);
  };
  return (
    <Container>
      <ResponsiveDrawer>
        <Box display="flex" height="400px" justifyContent="space-around" flexDirection="column" alignItems="center">
          <Typography variant="h5">추천시간표 조회</Typography>
          <Box display="flex" justifyContent="space-around" width="100%">
            <Button size="medium" variant="contained" color="warning" onClick={handleButtonClick(1)}>
              시간표 1
            </Button>
            <Button size="medium" variant="contained" color="warning" onClick={handleButtonClick(2)}>
              시간표 2
            </Button>
            <Button size="medium" variant="contained" color="warning" onClick={handleButtonClick(3)}>
              시간표 3
            </Button>
          </Box>
        </Box>
      </ResponsiveDrawer>
    </Container>
  );
};

export default Home;
