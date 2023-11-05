import type { StoryObj } from '@storybook/react';
import { mockLectures } from '../../types/lecture';

import Header from './Header';

const meta = {
  title: 'Header',
  component: Header,
  tags: ['autodocs'],
  parameters: {
    layout: 'fullscreen',
  },
};

export default meta;

type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    lectureList: mockLectures,
  },
};
