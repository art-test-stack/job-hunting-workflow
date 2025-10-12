import React from "react";
import { Anchor, Button } from "@mantine/core";
import { useUser } from "@auth0/nextjs-auth0";
import Link from "next/link";
import LoadingLayout from "@/components/loadingLayout";
import { text } from "stream/consumers";
import { postUserUserAuthGet } from "@/client"

export interface LoginButtonProps {
  variant?: string;
  radius?: string | number;
  size?: string;
  className?: any;
}

export function AuthLoginButton(props: LoginButtonProps) {
  const { user, isLoading } = useUser();
  if (isLoading) {
    return <LoadingLayout/>
  }
  // const handleAuth = () => window.location.href = ;
  const textLayout = user ? "Log Out" : "Log In"
  const href =  user ? "/auth/logout" : "/auth/login"
  return (
    <Button
      component="a"
      href={href}
      variant={props.variant}
      size={props.size}
      className={props.className}
    >
      {textLayout}
    </Button>
  );
}
