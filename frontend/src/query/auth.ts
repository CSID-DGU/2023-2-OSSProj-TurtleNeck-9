import { useMutation, useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { SigninPayload, SignupPayload } from '../types/auth';
import { getCookie } from '../utils/cookie';
import { authKeys } from './queryKeys';

const postSignup = async (payload: SignupPayload) => {
  const response = await axios.post('/users/signup', payload);

  return response.data;
};

export const useSignupMutation = () => {
  return useMutation({ mutationFn: postSignup });
};

const postSignin = async (payload: SigninPayload) => {
  const response = await axios.post<{ data: { jwtToken: { accessToken: string }; major_id: number; user_id: number } }>(
    '/users/login',
    payload
  );

  return response.data.data;
};

export const useSigninMutation = () => {
  return useMutation({ mutationFn: postSignin });
};

const getAuth = () => {
  return getCookie('access_token');
};

export const useAuthQuery = () => {
  return useQuery({ queryFn: getAuth, queryKey: [authKeys.all], staleTime: Infinity });
};
