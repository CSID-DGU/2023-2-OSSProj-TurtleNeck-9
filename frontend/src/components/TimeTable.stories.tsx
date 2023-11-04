import type { Meta, StoryObj } from '@storybook/react';

import TimeTable from './TimeTable';

const meta = {
  title: 'TimeTable',
  component: TimeTable,
  tags: ['autodocs'],
  parameters: {
    layout: 'fullscreen',
  },
}

export default meta;

type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
  },
};


