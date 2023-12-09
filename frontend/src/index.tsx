import { createRoot } from 'react-dom/client';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Home from './pages';
import TimeTableDetail from './pages/time-table';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { CssBaseline } from '@mui/material';
import Signup from './pages/signup';
import Signin from './pages/signin';
import axios from 'axios';
import { Global } from '@emotion/react';
import { reset } from './style';
import { getCookie } from './utils/cookie';

const container = document.getElementById('root') as HTMLElement;

const queryClient = new QueryClient();
axios.defaults.baseURL = 'http://ec2-43-203-18-207.ap-northeast-2.compute.amazonaws.com';
axios.defaults.headers.common['Authorization'] = 'Bearer ' + getCookie('access_token');

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
  },
  {
    path: '/time-table/:timeTableNumber',
    element: <TimeTableDetail />,
  },
  {
    path: '/signup',
    element: <Signup />,
  },
  {
    path: '/signin',
    element: <Signin />,
  },
]);

const root = createRoot(container);

root.render(
  <QueryClientProvider client={queryClient}>
    <Global styles={reset} />
    <CssBaseline />
    <RouterProvider router={router} />
  </QueryClientProvider>
);
