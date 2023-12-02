import type { Preview } from '@storybook/react';
import CssBaseline from '@mui/material/CssBaseline';


const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: '^on[A-Z].*' },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
  },
  decorators: [
    (Story) => (
    <>
      <CssBaseline />
      <Story/>
    </>)
    ]
};

export default preview;
