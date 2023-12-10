export const lectureKeys = {
  all: 'lecture',
  list: (userId: number) => [lectureKeys.all, 'list', userId],
};

export const authKeys = {
  all: 'auth',
  auth: () => ['auth'],
};
