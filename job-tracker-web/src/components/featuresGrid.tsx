import { IconCookie, IconGauge, IconLock, IconMessage2, IconUser } from '@tabler/icons-react';
import { Container, SimpleGrid, Text, ThemeIcon, Title } from '@mantine/core';
import classes from './../styles/FeaturesGrid.module.css';

export const MOCKDATA = [
    {
        icon: IconGauge,
        title: 'Blazing Fast Performance',
        description:
            'Experience unparalleled speed and efficiency, ensuring your tasks are completed in record time without compromising quality.',
    },
    {
        icon: IconUser,
        title: 'User-Centric Design',
        description:
            'Our platform is built with your privacy in mind, giving you full control over your data and ensuring a seamless experience.',
    },
    {
        icon: IconCookie,
        title: 'No Data Sharing',
        description:
            'Rest assured that your information stays with you. We do not involve third parties in handling your data.',
    },
    {
        icon: IconLock,
        title: 'Robust Security',
        description:
            'With security as our top priority, we provide a safe environment to protect your data from any threats.',
    },
    {
        icon: IconMessage2,
        title: 'Round-the-Clock Support',
        description:
            'Our dedicated support team is available 24/7 to assist you with any issues or questions you may have.',
    },
];

interface FeatureProps {
  icon: React.FC<any>;
  title: React.ReactNode;
  description: React.ReactNode;
}

export function Feature({ icon: Icon, title, description }: FeatureProps) {
  return (
    <div>
      <ThemeIcon variant="light" size={40} radius={40}>
        <Icon size={18} stroke={1.5} />
      </ThemeIcon>
      <Text mt="sm" mb={7}>
        {title}
      </Text>
      <Text size="sm" c="dimmed" lh={1.6}>
        {description}
      </Text>
    </div>
  );
}

export function FeaturesGrid() {
  const features = MOCKDATA.map((feature, index) => <Feature {...feature} key={index} />);

  return (
    <Container className={classes.wrapper}>
    <Title className={classes.title}>Seamlessly integrate with your workflow</Title>

      <Container size={560} p={0}>
        <Text size="sm" className={classes.description}>
          Discover how our features can enhance your workflow, providing efficiency and reliability
          at every step of your journey.
        </Text>
      </Container>

      <SimpleGrid
        mt={60}
        cols={{ base: 1, sm: 2, md: 3 }}
        spacing={{ base: 'xl', md: 50 }}
        verticalSpacing={{ base: 'xl', md: 50 }}
      >
        {features}
      </SimpleGrid>
    </Container>
  );
}