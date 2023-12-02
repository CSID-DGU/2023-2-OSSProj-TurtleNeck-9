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

const container = document.getElementById('root') as HTMLElement;

const queryClient = new QueryClient();

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
  },
  {
    path: '/time-table/:timeTableNumber',
    element: <TimeTableDetail />,
  },
]);

const root = createRoot(container);

root.render(
  <QueryClientProvider client={queryClient}>
    <CssBaseline />
    <RouterProvider router={router} />
  </QueryClientProvider>
);
