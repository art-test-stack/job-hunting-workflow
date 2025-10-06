import '@mantine/core/styles.css';

import type { AppProps } from 'next/app';
import { createTheme, MantineProvider } from '@mantine/core';
import { HeaderMenu } from '@/components/headerMenu';
import { FooterLinks } from '@/components/footer';
import { HeroPage } from '@/components/heroPage';
import { useUser } from '@auth0/nextjs-auth0';
import LoadingLayout from '@/components/loadingLayout';
import { useEffect } from 'react';


const theme = createTheme({})

export default function App({ Component, pageProps }: AppProps) {
  const { user, isLoading } = useUser()
  useEffect(() => {
    if (user) {
    const fetchAccessToken = async () => {
      try {
        const response = await fetch('/auth/access-token');
        if (!response.ok) {
          throw new Error('Failed to fetch access token');
        }
        const data = await response.json();
        console.log('Access Token:', data.accessToken);
      } catch (error) {
        console.error('Error fetching access token:', error);
      }
    };
    fetchAccessToken();}
    
  }, []);
  if (isLoading) {
    return (
      <MantineProvider theme={theme}>
      <LoadingLayout/>
      </MantineProvider>
  )}
  if (user) {
    return (
      <MantineProvider theme={theme}>
        <HeaderMenu />
        <div style={{ margin: '15px 15%' }}>
          <Component {...pageProps} />
        </div>
        <FooterLinks />
      </MantineProvider>
  )}
  return (
    <MantineProvider theme={theme}>
      <HeroPage/>
      <FooterLinks/>
    </MantineProvider>
  );
}