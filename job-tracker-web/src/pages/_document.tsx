import { Head, Html, Main, NextScript } from 'next/document';
import { ColorSchemeScript, createTheme, mantineHtmlProps, MantineProvider } from '@mantine/core';
import { Auth0Provider } from '@auth0/nextjs-auth0';


export default function Document() {
  return (
    <Html lang="en" {...mantineHtmlProps}>
      <Head>
        <ColorSchemeScript defaultColorScheme="auto" />
      </Head>
      <body>
        <Auth0Provider>
        <Main />
        <NextScript/>
        </Auth0Provider>
      </body>
    </Html>
  );
}