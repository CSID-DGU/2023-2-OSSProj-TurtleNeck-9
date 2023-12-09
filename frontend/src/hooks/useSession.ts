import { useQueryClient } from '@tanstack/react-query';
import axios from 'axios';
import { useEffect } from 'react';
import { useAuthQuery } from '../query/auth';
import { authKeys } from '../query/queryKeys';
import { setCookie } from '../utils/cookie';

export const useSession = () => {
  const queryClient = useQueryClient();
  const { data: token } = useAuthQuery();

  const signout = () => {
    setCookie('access_token', '');
    axios.defaults.headers.common['Authorization'] = null;
    queryClient.removeQueries({ queryKey: authKeys.auth() });
  };

  useEffect(() => {
    axios.defaults.headers.common['Authorization'] = token;
  }, [token]);

  return { signout, hasSession: !!token };
};