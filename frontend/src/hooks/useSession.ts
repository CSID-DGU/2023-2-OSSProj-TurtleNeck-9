import { useQueryClient } from '@tanstack/react-query';
import axios from 'axios';
import { useEffect } from 'react';
import { useAuthQuery } from '../query/auth';
import { authKeys } from '../query/queryKeys';
import { getCookie, setCookie } from '../utils/cookie';

export const useSession = () => {
  const queryClient = useQueryClient();
  const { data: token } = useAuthQuery();

  const signout = () => {
    setCookie('access_token', '');
    axios.defaults.headers.common['Authorization'] = null;
    queryClient.removeQueries({ queryKey: authKeys.auth() });
  };

  const signin = (token: string) => {
    setCookie('access_token', token, 10000000000);

    queryClient.setQueryData(authKeys.auth(), token);
  };

  useEffect(() => {
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
    }
  }, [token]);

  return { signout, hasSession: !!token || !!getCookie('access_token'), signin };
};
