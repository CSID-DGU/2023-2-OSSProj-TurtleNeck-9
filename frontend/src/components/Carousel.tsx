import { Typography } from '@mui/material';
import MuiCarousel from 'react-material-ui-carousel';
const stepFourCarousel = [
  {
    title: '2004',
    url: step2Image8,
    desc: [
      '안전한 화장품을 위한 아로마티카의 시작',
      'No, 미네랄오일 & 실리콘 - 아로마테라피롤온, 마사지 오일 출시',
      'Free 파라벤 & 실리콘 - 로즈 스킨케어 라인 출시',
    ],
  },
  {
    title: '2005',
    url: step2Image9,
    desc: [
      '기업 부설 연구소 설립',
      '천연 방부제 특허 취득',
      'Free 실리콘 & 설페이트 - 샴푸 출시',
      'Free 합성향 - 페이셜 미스트 출시',
    ],
  },
  {
    title: '2010',
    url: step2Image10,
    desc: ['Free PEG & 페녹시에탄올 - 알로에 베라 젤 출시', 'EWG Skindeep 전성분 등재'],
  },
  {
    title: '2020',
    url: step2Image7,
    desc: ['100% PCR 용기 제품 출시', '국내 뷰티 브랜드 최초 리필 스테이션 오픈'],
  },
];

const Carousel = () => {
  const description = '123';
  return (
    <MuiCarousel cycleNavigation={true} navButtonsAlwaysVisible={true}>
      {stepFourCarousel.map((content) => (
        <>
          <Typography variant="h3" color="#112b23">
            {content.title}
          </Typography>
          <img src={content.url} />
          {content.desc.map((description) => (
            <li>{description}</li>
          ))}
        </>
      ))}
    </MuiCarousel>
  );
};

export default Carousel;
