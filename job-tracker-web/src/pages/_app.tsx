// Import styles of packages that you've installed.
// All packages except `@mantine/hooks` require styles imports
import '@mantine/core/styles.css';

import type { AppProps } from 'next/app';
import { createTheme, MantineProvider } from '@mantine/core';
import { HeaderMenu } from '@/components/headerMenu';
import { FooterLinks } from '@/components/footer';
import { HeroPage } from '@/components/heroPage';
import { useUser } from '@auth0/nextjs-auth0';
import LoadingLayout from '@/components/loadingLayout';


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