import '@mantine/core/styles.css';

import type { AppProps } from 'next/app';
import { createTheme, MantineProvider } from '@mantine/core';
import { HeaderMenu } from '@/components/headerMenu';
import { FooterLinks } from '@/components/footer';
import { HeroPage } from '@/components/heroPage';
import { Auth0Provider, useUser } from '@auth0/nextjs-auth0';
import LoadingLayout from '@/components/loadingLayout';
import { useEffect } from 'react';

import { client } from '@/client/client.gen';
import { postUserUserAuthGet } from '@/client';
import { AuthProvider } from '@/providers/auth/authProvider';

const theme = createTheme({})

export default function App({ Component, pageProps }: AppProps) {
  const { user, isLoading } = useUser()
  
  if (isLoading) {
    return (
      <MantineProvider theme={theme}>
      <LoadingLayout/>
      </MantineProvider>
  )}
  if (user) {
    return (
      <Auth0Provider>
        <AuthProvider>
          <MantineProvider theme={theme}>
            <HeaderMenu />
            <div style={{ margin: '15px 15%' }}>
              <Component {...pageProps} />
            </div>
            <FooterLinks />
          </MantineProvider>
        </AuthProvider>
      </Auth0Provider>
  )}
  return (
    <MantineProvider theme={theme}>
      <HeroPage/>
      <FooterLinks/>
    </MantineProvider>
  );
}