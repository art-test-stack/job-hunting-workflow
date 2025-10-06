// File: app/components/Logo.jsx
import React from 'react';
import { Image, Center, Box } from '@mantine/core';
import Link from 'next/link';

export interface LogoProps {
    size?: string | number;
    href?: string;
}

export function Logo ( props: LogoProps) {
  return (
    <Center>
      <Link href={props.href ? props.href : "/"} style={{ textDecoration: "none" }}>
      <Box
        style={{
          width: props.size,
          height: props.size,
          borderRadius: 8,
          overflow: 'hidden',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Image
          src="/logo.png"
          alt="App Logo"
          fit="contain"
          width="100%"
          height="100%"
        />
      </Box>
      </Link>
    </Center>
  );
}
