import {
  Button,
  Container,
  FormControl,
  Grid,
  InputLabel,
  MenuItem,
  Select,
  SelectChangeEvent,
  TextField,
  Typography,
} from '@mui/material';
import { ChangeEventHandler, useState } from 'react';
import { Link } from 'react-router-dom';
import ResponsiveDrawer from '../../components/ResponsiveDrawer';
import { useSignupMutation } from '../../query/auth';

const Signup = () => {
  const [majorId, setMajorId] = useState<number>();
  const { mutate: signup } = useSignupMutation();
  const [username, setUsername] = useState('');
  const [studentId, setStudentId] = useState<number>();
  const handleMajorSelectChange = (e: SelectChangeEvent) => {
    const value = e.target.value;
    setMajorId(Number(value));
  };

  const handleUsernameChange: ChangeEventHandler<HTMLInputElement> = (e) => {
    const value = e.target.value;
    setUsername(value);
  };
  const handleStudentIdChange: ChangeEventHandler<HTMLInputElement> = (e) => {
    const value = e.target.value;
    setStudentId(Number(value));
  };
  return (
    <Container>
      <ResponsiveDrawer>
        <div>
          <Typography variant="h5">회원가입</Typography>
          <form noValidate>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  autoComplete="fname"
                  name="username"
                  variant="outlined"
                  required
                  fullWidth
                  id="username"
                  label="이름"
                  autoFocus
                  onChange={handleUsernameChange}
                  value={username}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  id="studentId"
                  label="학번"
                  name="studentId"
                  value={studentId}
                  onChange={handleStudentIdChange}
                  type="number"
                />
              </Grid>
              <Grid item xs={12}>
                <FormControl fullWidth>
                  <InputLabel id="demo-simple-select-label">전공</InputLabel>
                  <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={majorId}
                    label="Age"
                    onChange={handleMajorSelectChange}
                  >
                    <MenuItem value={1}>산업시스템공학과</MenuItem>
                    <MenuItem value={2}>정보통신공학과</MenuItem>
                    <MenuItem value={3}>전자전기공학과</MenuItem>
                  </Select>
                </FormControl>
              </Grid>
              <Grid item xs={12}>
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  name="password"
                  label="비밀번호"
                  type="password"
                  id="password"
                  autoComplete="current-password"
                />
              </Grid>
            </Grid>
            <Button type="submit" fullWidth variant="contained" color="warning" sx={{ marginY: '20px' }}>
              회원가입
            </Button>
            <Grid container>
              <Grid item>
                <Link to="/signin">이미 계정이 있으신가요? 로그인하기</Link>
              </Grid>
            </Grid>
          </form>
        </div>
      </ResponsiveDrawer>
    </Container>
  );
};

export default Signup;
