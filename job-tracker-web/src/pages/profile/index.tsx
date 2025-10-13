// 'use client';
import { profileLayout, ProfileLayoutProps } from "@/components/profileLayout";
import LoadingLayout from "@/components/loadingLayout";
import { useUser } from "@auth0/nextjs-auth0"
import { ThemeIcon, Title, useMantineTheme } from "@mantine/core";
import { Group, Avatar, Text, Accordion } from '@mantine/core';
import { useRouter } from "next/router";
import { useEffect, useState } from "react";


function AccordionLabel(item: ProfileLayoutProps) {
  const theme = useMantineTheme();
  return (
    <Group wrap="nowrap">
      <ThemeIcon radius="xl" size="lg" >
          <item.icon size={22} color={theme.colors.blue[6]} />
      </ThemeIcon>
      <div>
        <Text>{item.label}</Text>
        <Text size="sm" c="dimmed" fw={400}>
          {item.description}
        </Text>
      </div>
    </Group>
  );
}


function ProfileAccordion() {
  const router = useRouter();
  const [opened, setOpened] = useState<string | null>(null);

  // Sync the accordion with the URL (e.g., /profile/account)
  useEffect(() => {
    const path = router.asPath.split("/").pop(); // get last path segment
    const validItem = profileLayout.find((item) => item.href === path);
    if (validItem) {
      setOpened(validItem.href);
    } else {
      setOpened(null);
      // if not a valid section, redirect to /profile
      if (path && path !== "profile") {
        router.replace("/profile", undefined, { shallow: true });
      }
    }
  }, [router.asPath]);

  // Handle opening an accordion
  const handleAccordionChange = (value: string | null) => {
    setOpened(value);
    if (value) {
      // update the URL visually without leaving the page
      window.history.pushState(null, "", `/profile/${value}`);
    } else {
      window.history.pushState(null, "", `/profile`);
    }
  };

  return (
    <Accordion
      chevronPosition="right"
      variant="contained"
      radius="md"
      value={opened}
      onChange={handleAccordionChange}
    >
      {profileLayout.map((item) => (
        <Accordion.Item value={item.href} key={item.label}>
          <Accordion.Control aria-label={item.label}>
            <AccordionLabel {...item} />
          </Accordion.Control>
          <Accordion.Panel>
            <item.content />
          </Accordion.Panel>
        </Accordion.Item>
      ))}
    </Accordion>
  );
}

export default function Profile() {
  const { user, isLoading } = useUser();
  return (
    <>
      {isLoading && <LoadingLayout/>}
      { user && (
        <div>
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <img
              src={user.picture}
              alt="Profile"
              style={{ borderRadius: "50%", width: "80px", height: "80px" }}
            />
            <Title style={{ alignSelf: "flex-start" }}>Welcome {user.name}!</Title> 
          </div>
        Edit your profile
        <ProfileAccordion/>
        </div>
      )}
    </>
  );
}