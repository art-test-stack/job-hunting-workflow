import {
  IconBook,
  IconChartPie3,
  IconChevronDown,
  IconCode,
  IconCoin,
  IconFingerprint,
  IconNotification,
} from '@tabler/icons-react';
import {
  Anchor,
  Box,
  Burger,
  Button,
  Center,
  Collapse,
  Divider,
  Drawer,
  Group,
  HoverCard,
  ScrollArea,
  SimpleGrid,
  Text,
  ThemeIcon,
  UnstyledButton,
  useMantineTheme,
} from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import classes from './../styles/HeaderMenu.module.css';
import { Logo } from './logo';
import { AuthLoginButton } from '@/providers/auth/authButton';
import { useUser } from '@auth0/nextjs-auth0';
import Link from 'next/link';

const mockdata = [
  {
    icon: IconNotification,
    title: 'Summary',
    description: 'Provide a brief summary of your career goals and profile.',
    href: '/summary',
  },
  {
    icon: IconBook,
    title: 'Headers',
    description: 'Customize the headers to organize your job applications.',
    href: '/headers',
  },
  {
    icon: IconBook,
    title: 'Education',
    description: 'Add and manage your educational background.',
    href: '/education',
  },
  {
    icon: IconCoin,
    title: 'Experiences',
    description: 'Document your professional experiences and achievements.',
    href: '/experiences',
  },
  {
    icon: IconFingerprint,
    title: 'Skills',
    description: 'Highlight your key skills and competencies.',
    href: '/skills',
  },
  {
    icon: IconChartPie3,
    title: 'Activities',
    description: 'Track extracurricular activities and volunteer work.',
    href: '/activities',
  },
  {
    icon: IconChevronDown,
    title: 'Languages',
    description: 'List the languages you speak and your proficiency levels.',
    href: '/languages',
  },
];

export function HeaderMenu() {
  const { user, isLoading } = useUser();
  const [drawerOpened, { toggle: toggleDrawer, close: closeDrawer }] = useDisclosure(false);
  const [linksOpened, { toggle: toggleLinks }] = useDisclosure(false);
  const theme = useMantineTheme();

  const links = mockdata.map((item) => (
    <Link href={"/profile"+item.href}>
      <UnstyledButton className={classes.subLink} key={item.title}>
        <Group wrap="nowrap" align="flex-start">
          <ThemeIcon size={34} variant="default" radius="md">
            <item.icon size={22} color={theme.colors.blue[6]} />
          </ThemeIcon>
          <div>
            <Text size="sm" fw={500}>
              {item.title}
            </Text>
            <Text size="xs" c="dimmed">
              {item.description}
            </Text>
          </div>
        </Group>
      </UnstyledButton>
    </Link>
  ));

  return (
    <Box pb={0}> 
      <header className={classes.header}>
        <Group justify="space-between" h="100%">
          <Logo size={50} />
          <Group h="100%" gap={0} visibleFrom="sm">
            <a href="/" className={classes.link}>
              Home
            </a>
            <a href="/jobs" className={classes.link}>
              Jobs
            </a>
            <a href="#" className={classes.link}>
              Todo
            </a>
            <HoverCard width={600} position="bottom" radius="md" shadow="md" withinPortal>
              <HoverCard.Target>
                <a href="/profile" className={classes.link}>
                  <Center inline>
                    <Box component="span" mr={5}>
                      Profile
                    </Box>
                    <IconChevronDown size={16} color={theme.colors.blue[6]} />
                  </Center>
                </a>
              </HoverCard.Target>

              <HoverCard.Dropdown style={{ overflow: 'hidden' }}>
                <Group justify="space-between" px="md">
                  <Text fw={500}>Edit Profile Sections</Text>
                  <Anchor href="/profile" fz="xs">
                    View all
                  </Anchor>
                </Group>

                <Divider my="sm" />

                <SimpleGrid cols={2} spacing={0}>
                  {links}
                </SimpleGrid>

                <div className={classes.dropdownFooter}>
                  <Group justify="space-between">
                    <div>
                      <Text fw={500} fz="sm">
                        Get started
                      </Text>
                      <Text size="xs" c="dimmed">
                        Their food sources have decreased, and their numbers
                      </Text>
                    </div>
                    <Button variant="default">Get started</Button>
                  </Group>
                </div>
              </HoverCard.Dropdown>
            </HoverCard>
          </Group>

          <Group visibleFrom="sm">
            <AuthLoginButton />
          </Group>

          <Burger opened={drawerOpened} onClick={toggleDrawer} hiddenFrom="sm" />
        </Group>
      </header>

      <Drawer
        opened={drawerOpened}
        onClose={closeDrawer}
        size="100%"
        padding="md"
        title="Navigation"
        hiddenFrom="sm"
        zIndex={1000000}
      >
        <ScrollArea h="calc(100vh - 80px" mx="-md">
          <Divider my="sm" />

          <a href="#" className={classes.link}>
            Home
          </a>
          <UnstyledButton className={classes.link} onClick={toggleLinks}>
            <Center inline>
              <Box component="span" mr={5}>
                Edit Profile Sections
              </Box>
              <IconChevronDown size={16} color={theme.colors.blue[6]} />
            </Center>
          </UnstyledButton>
          <Collapse in={linksOpened}>{links}</Collapse>
          <a href="#" className={classes.link}>
            Learn
          </a>
          {/* <a href="#" className={classes.link}>
            Academy
          </a> */}

          <Divider my="sm" />

          <Group justify="center" grow pb="xl" px="md">
            <Button variant="default">Log in</Button>
            <Button>Sign up</Button>
          </Group>
        </ScrollArea>
      </Drawer>
    </Box>
  );
}