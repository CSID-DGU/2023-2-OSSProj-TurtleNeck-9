import { useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { SignupPayload } from '../types/auth';

const postSignup = async (payload: SignupPayload) => {
  const response = await axios.post('https://43.203.18.207:8080/users/signup', payload);

  return response.data;
};

export const useSignupMutation = () => {
  return useMutation({ mutationFn: postSignup });
};
