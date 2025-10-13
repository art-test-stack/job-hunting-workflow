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

export default function Jobs() {
    
    return (
        <CurrentJobListProvider>
            <AddJob/>  <br />
            <JobsTable/>

        </CurrentJobListProvider>
    );
}