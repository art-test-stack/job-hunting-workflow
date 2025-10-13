import { useContext } from "react"
import LoadingLayout from "./loadingLayout"
import { JobDetailsContext } from "@/providers/jobs/jobDetailsProvider"
import { Textarea } from "@mantine/core"

export default function JobDescription(){
    const [ data, setData, loading ] = useContext(JobDetailsContext)
    if (loading) { return <LoadingLayout/> }
    console.log("data", data)
    if (data?.description) {
        return (
            <Textarea
            mt="md"
            label="Message"
            placeholder="Your message"
            maxRows={10}
            minRows={5}
            autosize
            name="message"
            variant="filled"
            onChange={(event) => setData({ ...data, description: event.currentTarget.value })}
            />
        )
    }
    return (
        <>
        <div style={{ display: "flex", justifyContent: "space-between", width: "100%" }}>
        <Textarea
            mt="md"
            label="Job Description"
            placeholder="Copy past the job description here"
            maxRows={10}
            minRows={5}
            autosize
            name="message"
            variant="filled"
            style={{ width: "100%" }}
            onChange={(event) => setData({ ...data, description: event.currentTarget.value })}
        />
        </div>
        </>
    )
}