import JobApplicationProgress from '@/components/jobApplicationProgress';
import { Button } from '@mantine/core';
import Link from 'next/link';
import { useRouter } from 'next/router';
import { initialData } from '.';

export default function JobId() {
    const router = useRouter();
    const { job_id } = router.query;
    const data = initialData.find(job => job.id === job_id);
    console.log("job id", job_id);
    return (
        <>
        <Link 
            href='/jobs'
        // onClick={() => router.push('/jobs')}
        >Go Back to Job List</Link>
        <div>Hello world {job_id}</div>
        <JobApplicationProgress jobStatus={data?.status}/>
        </>
    );
}