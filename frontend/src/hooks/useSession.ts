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
    queryClient.removeQueries({ queryKey: authKeys.auth() });
    setCookie('access_token', '');
    axios.defaults.headers.common['Authorization'] = null;
  };

  useEffect(() => {
    axios.defaults.headers.common['Authorization'] = token;
  }, [token]);

  return { signout };
};
