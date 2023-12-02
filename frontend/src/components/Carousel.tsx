import { Box, Typography } from '@mui/material';
import MuiCarousel from 'react-material-ui-carousel';
const stepImage =
  'https://engineer.dongguk.edu/cmmn/fileView?path=/engineer/files/popup/1298/&physical=85B2BF5B5CCC4B8797616DE86E402FD4.jpg&contentType=image';
const stepFourCarousel = [
  {
    url: stepImage,
  },
  {
    url: 'https://www.dongguk.edu/cmmn/fileView?path=/files/banner/792/&physical=C781137AC5C847EB957F34210989AD30.jpg&contentType=image',
  },
];

const Carousel = () => {
  return (
    <MuiCarousel
      height="300px"
      sx={{ width: '100%', overflow: 'visible' }}
      cycleNavigation={true}
      navButtonsAlwaysVisible={true}
    >
      {stepFourCarousel.map((content) => (
        <Box key={content.url} width="100%" height="300px" display="flex" justifyContent="center">
          <img src={content.url} height="100%" />
        </Box>
      ))}
    </MuiCarousel>
  );
};

export default Carousel;
