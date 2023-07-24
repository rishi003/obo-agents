import AuthProvider from '@/context/AuthProvider';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import StyleProvider from '@/context/StyleProvider';
// import Font Awesome CSS
import '@fortawesome/fontawesome-svg-core/styles.css';

import { config } from '@fortawesome/fontawesome-svg-core';
import { Box } from '@chakra-ui/react';
// Tell Font Awesome to skip adding the CSS automatically
// since it's already imported above
config.autoAddCss = false;

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'OBO',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AuthProvider>
          <StyleProvider>{children}</StyleProvider>
        </AuthProvider>
      </body>
    </html>
  );
}
