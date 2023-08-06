'use server';

import { prisma } from '@/db';

export const updateUserName = async (username: string, email: string) => {
  await prisma.user.update({
    where: {
      email: email,
    },
    data: {
      name: username,
    },
  });
};
