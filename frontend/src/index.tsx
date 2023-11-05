import { createRoot } from 'react-dom/client';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Home from './pages';

const container = document.getElementById('root') as HTMLElement;

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
  },
]);

const root = createRoot(container);

root.render(<RouterProvider router={router} />);
