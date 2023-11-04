import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Lecture, Weekday } from '../types/lecture';
import { Box, Typography } from '@mui/material';
import { FC } from 'react';

const TIME_LIST = Array.from({ length: 14 }, (_, index) => index + 9);
const HEIGHT = 60;
const WIDTH = '15%';

type Props = {
  lectureList: Lecture[];
};

const TimeTable: FC<Props> = ({ lectureList }) => {
  return (
    <TableContainer component={Paper} sx={{ position: 'relative', minWidth: 700 }}>
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
        <TableBody>
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
        </TableBody>
      </Table>
      {lectureList.map((lecture) => (
        <LectureBox lecture={lecture} key={lecture.lectureId} />
      ))}
    </TableContainer>
  );
};

export default TimeTable;

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
    height: `${HEIGHT}px`,
    padding: 0,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
    border: `1px solid ${theme.palette.divider}`,
    height: `${HEIGHT}px`,
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

const WEEKDAY_ORDER = {
  [Weekday.Mon]: 0,
  [Weekday.Tue]: 1,
  [Weekday.Wed]: 2,
  [Weekday.Thu]: 3,
  [Weekday.Fri]: 4,
  [Weekday.Sat]: 5,
} as Record<Weekday, number>;

const resolveTop = (startTime: string) => {
  const [hour, minute] = startTime.split(':').map(Number);
  return HEIGHT + (hour - 9 + minute / 60) * HEIGHT + 'px';
};

const resolveHeight = (startTime: string, endTime: string) => {
  const [startHour, startMinute] = startTime.split(':').map(Number);
  const [endHour, endMinute] = endTime.split(':').map(Number);
  return (endHour + endMinute / 60 - (startHour + startMinute / 60)) * HEIGHT;
};

const resolveLeft = (weekday: Weekday) => {
  return 10 + WEEKDAY_ORDER[weekday] * 15 + '%';
};

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
          height={resolveHeight(lectureTimeItem.startTime, lectureTimeItem.endTime)}
          bgcolor="yellow"
          top={resolveTop(lectureTimeItem.startTime)}
          left={resolveLeft(lectureTimeItem.weekday)}
          position="absolute"
          display="flex"
          flexDirection="column"
          alignItems="center"
        >
          <Typography fontSize="14px" variant="body1">
            {lecture.lectureName}
          </Typography>
          <Typography fontSize="10px" variant="body2">
            {lecture.professorName} ({lecture.place})
          </Typography>
        </Box>
      ))}
    </>
  );
};
