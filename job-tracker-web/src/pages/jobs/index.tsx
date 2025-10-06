import { JobsTable } from "./../../components/jobsTable";
import AddJob from "@/components/addJob";
import { useState } from "react";


export enum JobStatus {
  NotSent = "Not Sent",
  Applied = 'Applied',
  Interview = 'Interviewing',
  Offer = 'Offer Received',
  Rejected = 'Rejected',
  Accepted = 'Accepted',
}

export interface RowData {
    id: string;
    title: string;
    company: string;
    location: string;
    contract: string;
    type: string;
    business: string;
    url: string;
    status: JobStatus;
    date: string
}


export const initialData: RowData[] = [
    {
        id: '1',
        title: 'Software Engineer',
        company: 'TechCorp',
        location: 'San Francisco, CA',
        contract: 'Full-time',
        type: 'Remote',
        business: 'Technology',
        url: 'https://techcorp.com/careers/1',
        status: JobStatus.Applied,
        date: '2023-10-01',
    },
    {
        id: '2',
        title: 'Product Manager',
        company: 'Innovate Inc.',
        location: 'New York, NY',
        contract: 'Full-time',
        type: 'On-site',
        business: 'Product Development',
        url: 'https://innovateinc.com/jobs/2',
        status: JobStatus.Interview,
        date: '2023-09-25',
    },
    {
        id: '3',
        title: 'UI/UX Designer',
        company: 'Designify',
        location: 'Austin, TX',
        contract: 'Contract',
        type: 'Hybrid',
        business: 'Design',
        url: 'https://designify.com/careers/3',
        status: JobStatus.Offer,
        date: '2023-09-20',
    },
    {
        id: '4',
        title: 'Data Scientist',
        company: 'DataWorks',
        location: 'Seattle, WA',
        contract: 'Full-time',
        type: 'Remote',
        business: 'Analytics',
        url: 'https://dataworks.com/jobs/4',
        status: JobStatus.Rejected,
        date: '2023-09-15',
    },
    {
        id: '5',
        title: 'DevOps Engineer',
        company: 'Cloudify',
        location: 'Boston, MA',
        contract: 'Full-time',
        type: 'On-site',
        business: 'Cloud Computing',
        url: 'https://cloudify.com/careers/5',
        status: JobStatus.Accepted,
        date: '2023-10-05',
    },
];

export default function Jobs(){
    // get data from curl
    const [data, setData] = useState(initialData)
    
    return (
        <>  
            <AddJob data={data} setData={setData}/> <br/>
            <JobsTable data={data} setData={setData}/>
        </>
    )
}