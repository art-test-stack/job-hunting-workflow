import { Icon, IconBook, IconChartPie3, IconChevronDown, IconCoin, IconFingerprint, IconNotification, IconProps } from "@tabler/icons-react";
import { RefAttributes } from "react";

export interface ProfileLayoutProps {
  icon: React.ForwardRefExoticComponent<IconProps & RefAttributes<Icon>>, // React.ElementType,
  label: string,
  description: string,
  href: string,
  content: any
} 
export const profileLayout = [
  {
    icon: IconNotification,
    label: 'Summary',
    description: 'Provide a brief summary of your career goals and profile.',
    href: 'summary',
    content: () => <div>Summary Content</div>
  },
  {
    icon: IconBook,
    label: 'Headers',
    description: 'Customize the headers to organize your job applications.',
    href: 'headers',
    content: () => <div>Header Content</div>
  },
  {
    icon: IconBook,
    label: 'Education',
    description: 'Add and manage your educational background.',
    href: 'education',

    content: () => <div>Education Content</div>
  },
  {
    icon: IconCoin,
    label: 'Experiences',
    description: 'Document your professional experiences and achievements.',
    href: 'experiences',
    content: () => <div>Experiences Content</div>
  },
  {
    icon: IconFingerprint,
    label: 'Skills',
    description: 'Highlight your key skills and competencies.',
    href: 'skills',

    content: () => <div>Skills Content</div>
  },
  {
    icon: IconChartPie3,
    label: 'Activities',
    description: 'Track extracurricular activities and volunteer work.',
    href: 'activities',

    content: () => <div>Activities Content</div>
  },
  {
    icon: IconChevronDown,
    label: 'Languages',
    description: 'List the languages you speak and your proficiency levels.',
    href: 'languages',

    content: () => <div>Languages Content</div>
  },
];