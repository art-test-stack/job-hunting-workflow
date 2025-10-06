import { IconCheck } from '@tabler/icons-react';
import { Button, Container, Group, Image, List, Text, ThemeIcon, Title } from '@mantine/core';
import image from './../../public/image.9a65bd94.svg';
import classes from './../styles/HeroHeader.module.css';
import { AuthLoginButton } from '@/providers/auth/authButton';

export function HeroPage() {
    return (
        <Container size="md">
        <div className={classes.inner}>
            <div className={classes.content}>
            <Title className={classes.title}>
                Land <span className={classes.highlight}>your</span> dream <br /> job
                {/* Stay <span className={classes.highlight}>organized</span>, land your <br /> dream job */}
            </Title>
            <Text c="dimmed" mt="md">
                Track your job applications effortlessly – Job Tracker helps you stay organized and
                focused during your job hunting journey.
            </Text>

            <List
                mt={30}
                spacing="sm"
                size="sm"
                icon={
                <ThemeIcon size={20} radius="xl">
                    <IconCheck size={12} stroke={1.5} />
                </ThemeIcon>
                }
            >
                <List.Item>
                <b>Track your progress</b> – easily monitor the status of all your job applications in one place
                </List.Item>
                <List.Item>
                <b>Stay organized</b> – categorize and prioritize your applications for better focus
                </List.Item>
                <List.Item>
                <b>Accessible anywhere</b> – use the platform on any device, anytime
                </List.Item>
            </List>

            <Group mt={30}>
                <AuthLoginButton radius="xl" size="md" className={classes.control}/>
                {/* <Button radius="xl" size="md" className={classes.control} onClick={() => loginWithRedirect()}>
                Sign In
                </Button> */}
                {/* <Button variant="default" radius="xl" size="md" className={classes.control}>
                Log In
                </Button> */}
            </Group>
            </div>
            <Image src={image.src} className={classes.image} />
        </div>
        </Container>
    );
}