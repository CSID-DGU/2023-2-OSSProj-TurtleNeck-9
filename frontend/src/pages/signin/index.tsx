import { Button, Container, Grid, TextField, Typography } from '@mui/material';
import { ChangeEventHandler, MouseEventHandler, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import ResponsiveDrawer from '../../components/ResponsiveDrawer';
import { useSigninMutation } from '../../query/auth';

const Signin = () => {
  const { mutate: signin } = useSigninMutation();
  const [password, setPassword] = useState('');
  const [studentId, setStudentId] = useState('');

  const navigate = useNavigate();

  const handleStudentIdChange: ChangeEventHandler<HTMLInputElement> = (e) => {
    const value = e.target.value;
    setStudentId(value);
  };

  const handlePasswordChange: ChangeEventHandler<HTMLInputElement> = (e) => {
    const value = e.target.value;
    setPassword(value);
  };
  const handleSignupButtonClick: MouseEventHandler<HTMLButtonElement> = () => {
    signin(
      { student_id: Number(studentId), password: password },
      {
        onSuccess: () => {
          navigate('/');
        },
      }
    );
  };
  return (
    <Container>
      <ResponsiveDrawer>
        <div>
          <Typography variant="h5" marginBottom="40px">
            로그인
          </Typography>
          <form noValidate>
            <Grid container spacing={2}>
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
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  name="password"
                  label="비밀번호"
                  type="password"
                  id="password"
                  autoComplete="current-password"
                  value={password}
                  onChange={handlePasswordChange}
                />
              </Grid>
            </Grid>
            <Button
              type="button"
              fullWidth
              variant="contained"
              color="warning"
              sx={{ marginY: '20px' }}
              onClick={handleSignupButtonClick}
            >
              로그인
            </Button>
            <Grid container>
              <Grid item>
                <Link to="/signup" style={{ color: 'inherit' }}>
                  계정이 없으신가요? 회원가입하기
                </Link>
              </Grid>
            </Grid>
          </form>
        </div>
      </ResponsiveDrawer>
    </Container>
  );
};

export default Signin;
