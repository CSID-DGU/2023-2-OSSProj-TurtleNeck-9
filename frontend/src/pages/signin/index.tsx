import { Button, Container, Grid, TextField, Typography } from '@mui/material';
import { ChangeEventHandler, MouseEventHandler, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import ResponsiveDrawer from '../../components/ResponsiveDrawer';
import { useSession } from '../../hooks/useSession';
import { useSigninMutation } from '../../query/auth';
import { setCookie } from '../../utils/cookie';

const Signin = () => {
  const { mutate: signin } = useSigninMutation();
  const [password, setPassword] = useState('');
  const [studentId, setStudentId] = useState('');
  const { signin: signinClient } = useSession();
  const navigate = useNavigate();

  const handleStudentIdChange: ChangeEventHandler<HTMLInputElement> = (e) => {
    const value = e.target.value;
    setStudentId(value);
  };

  const handlePasswordChange: ChangeEventHandler<HTMLInputElement> = (e) => {
    const value = e.target.value;
    setPassword(value);
  };
  const handleSigninButtonClick: MouseEventHandler<HTMLButtonElement> = () => {
    signin(
      { studentNumber: Number(studentId), password: password },
      {
        onSuccess: (data) => {
          signinClient(data.jwtToken.accessToken);
          // 백엔드 인증 구현 이슈로 임시 하드코딩
          setCookie('major_id', String(data.major_id), 10000000000);
          setCookie('user_id', String(data.user_id), 10000000000);
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
              onClick={handleSigninButtonClick}
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
