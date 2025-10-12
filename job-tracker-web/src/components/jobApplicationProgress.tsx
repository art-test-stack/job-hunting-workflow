import { JobStatus } from '@/pages/jobs';
import { currentJobList } from '@/providers/jobs/jobListProvider';
import { Center, SemiCircleProgress } from '@mantine/core';
import { useContext } from 'react';
import LoadingLayout from './loadingLayout';
import { currentJobDetails, JobDetailsContext } from '@/providers/jobs/jobDetailsProvider';



const jobStatusProgressMap: Record<JobStatus, number> = {
  [JobStatus.NotSent]: 0,
  [JobStatus.Applied]: 20,
  [JobStatus.Interview]: 40,
  [JobStatus.Offer]: 60,
  [JobStatus.Rejected]: 100,
  [JobStatus.Accepted]: 100,
};

const jobStatusProgressColor = (jobStatus: string) => {
  if (jobStatus == JobStatus.Rejected){
    return "red"
  }
  if (jobStatus == JobStatus.Offer || jobStatus == JobStatus.Accepted){
    return "green"
  }
  return 'blue'
  // jobStatus == JobStatus.Rejected ? "red" : jobStatus == JobStatus.Offer ? "green" : "blue"
}

export interface JobApplicationProgressProps {
  jobId: string | string[] | undefined
}

export default function JobApplicationProgress( props: JobApplicationProgressProps ) {
  const [ data, useData, loading ] = useContext(JobDetailsContext)
  console.log("data", data)
  if (loading) { return <LoadingLayout/> }
  const jobStatus = data?.status
  console.log("jobStatus", jobStatus)
  const progressValue = jobStatusProgressMap[jobStatus];
  const filledSegmentColor = jobStatusProgressColor(jobStatus)
  return (
    <Center>
      <SemiCircleProgress
        fillDirection="left-to-right"
        orientation="up"
        filledSegmentColor={filledSegmentColor}
        size={200}
        thickness={12}
        value={progressValue}
        label={jobStatus}
        transitionDuration={200}
      />
    </Center>
  );
}