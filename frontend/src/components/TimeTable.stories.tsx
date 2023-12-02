import type { StoryObj } from '@storybook/react';
import { mockLectures } from '../types/lecture';

import TimeTable from './TimeTable';

const meta = {
  title: 'TimeTable',
  component: TimeTable,
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
