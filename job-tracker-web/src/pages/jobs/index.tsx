import { JobsTable } from "./../../components/jobsTable";
import AddJob from "@/components/addJob";
import { CurrentJobListProvider } from "@/providers/jobs/jobListProvider";


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


export default function Jobs() {
    
    return (
        <CurrentJobListProvider>
            <AddJob/> <br />
            <JobsTable/>
        </CurrentJobListProvider>
    );
}