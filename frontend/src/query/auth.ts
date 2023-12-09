import { useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { SigninPayload, SignupPayload } from '../types/auth';

const postSignup = async (payload: SignupPayload) => {
  const response = await axios.post('https://43.203.18.207:8080/users/signup', payload);

  return response.data;
};

export const useSignupMutation = () => {
  return useMutation({ mutationFn: postSignup });
};

const postSignin = async (payload: SigninPayload) => {
  const response = await axios.post('https://43.203.18.207:8080/users/login', payload);

  return response.data;
};

export const useSigninMutation = () => {
  return useMutation({ mutationFn: postSignin });
};
