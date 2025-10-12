import JobApplicationProgress from '@/components/jobApplicationProgress';
import { CurrentJobDetailsProvider } from '@/providers/jobs/jobDetailsProvider';
import Link from 'next/link';
import { useRouter } from 'next/router';

export default function JobId() {
    const router = useRouter();
    const { job_id } = router.query;

    return (
        <>
            <Link 
                href='/jobs'
            >Go Back to Job List</Link>
            <CurrentJobDetailsProvider>
                <JobApplicationProgress />
            </CurrentJobDetailsProvider>
            <div>Hello world {job_id}</div>
        </>
    )
}