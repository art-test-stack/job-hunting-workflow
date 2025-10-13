import { JobStatus } from '@/pages/jobs';
import { currentJobList } from '@/providers/jobs/jobListProvider';
import { Center, MenuDropdown, Select, SemiCircleProgress } from '@mantine/core';
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

// export interface JobApplicationProgressProps {
//   jobId: string | string[] | undefined
// }

export default function JobApplicationProgress() {
  const [ data, setData, loading ] = useContext(JobDetailsContext)
  if (loading) { return <LoadingLayout/> }
  const jobStatus = data?.status
  const progressValue = jobStatusProgressMap[jobStatus];
  const filledSegmentColor = jobStatusProgressColor(jobStatus)
  const jobStatusDropDown = (
      <Select
          label="Status"
          placeholder="Pick a Status"
          data={Object.values(JobStatus)}
          defaultValue={jobStatus}
          onSelect={(value) => setData({...data, status: value})}
      />

  )
  return (
    <Center>
      <SemiCircleProgress
        fillDirection="left-to-right"
        orientation="up"
        filledSegmentColor={filledSegmentColor}
        size={200}
        thickness={12}
        value={progressValue}
        label={jobStatusDropDown}
        transitionDuration={200}
      />
    </Center>
  );
}