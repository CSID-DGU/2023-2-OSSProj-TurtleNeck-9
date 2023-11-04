import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Lecture, Weekday } from '../types/lecture';
import { Box } from '@mui/material';
import { FC } from 'react';

const TIME_LIST = Array.from({ length: 14 }, (_, index) => index + 9);
const HEIGHT = '40px';
const WIDTH = '15%';
const WEEKDAY_ORDER = {
  [Weekday.Mon]: 0,
  [Weekday.Tue]: 1,
  [Weekday.Wed]: 2,
  [Weekday.Thu]: 3,
  [Weekday.Fri]: 4,
  [Weekday.Sat]: 5,
};

type Props = {
  lectureList: Lecture[];
};

const TimeTable: FC<Props> = ({ lectureList }) => {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead>
          <TableRow>
            <StyledTableCell align="center"></StyledTableCell>
            <StyledTableCell align="center">월</StyledTableCell>
            <StyledTableCell align="center">화</StyledTableCell>
            <StyledTableCell align="center">수</StyledTableCell>
            <StyledTableCell align="center">목</StyledTableCell>
            <StyledTableCell align="center">금</StyledTableCell>
            <StyledTableCell align="center">토</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody sx={{ position: 'relative' }}>
          {TIME_LIST.map((time) => (
            <StyledTableRow key={time}>
              <StyledTableCell width="10%" align="right" sx={{ paddingTop: 0 }}>
                {time}
              </StyledTableCell>
              <StyledTableCell width={WIDTH} align="center"></StyledTableCell>
              <StyledTableCell width={WIDTH} align="center"></StyledTableCell>
              <StyledTableCell width={WIDTH} align="center"></StyledTableCell>
              <StyledTableCell width={WIDTH} align="center"></StyledTableCell>
              <StyledTableCell width={WIDTH} align="center"></StyledTableCell>
              <StyledTableCell width={WIDTH} align="center"></StyledTableCell>
            </StyledTableRow>
          ))}
          {lectureList.map((lecture) => (
            <LectureBox lecture={lecture} key={lecture.lectureId} />
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default TimeTable;

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
    border: `1px solid ${theme.palette.divider}`,
    height: HEIGHT,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  '&:nth-of-type(odd)': {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  '&:last-child td, &:last-child th': {
    border: 0,
  },
}));

type LectureBoxProps = {
  lecture: Lecture;
};
const LectureBox: FC<LectureBoxProps> = ({ lecture }) => {
  return (
    <>
      {lecture.lectureTime.map((lectureTimeItem) => (
        <Box
          key={lectureTimeItem.weekday + lectureTimeItem.startTime}
          width={WIDTH}
          height={HEIGHT}
          bgcolor="yellow"
          top={0}
          left="10%"
          position="absolute"
        >
          asdf
        </Box>
      ))}
    </>
  );
};
