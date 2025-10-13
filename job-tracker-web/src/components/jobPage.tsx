import { JobDetailsContext } from "@/providers/jobs/jobDetailsProvider"
import { useContext } from "react"
import LoadingLayout from "./loadingLayout"
import { Title } from "@mantine/core"



export default function JobPage(){
    const [ data, setData, loading ] = useContext(JobDetailsContext)
    if (loading) { return <LoadingLayout/> }

    return (
        <>
        <div style={{ display: "flex", justifyContent: "space-between" }}>
            <Title style={{ alignSelf: "flex-start" }}>{data?.title}</Title>
            <Title style={{ alignSelf: "flex-start" }}>{data?.company}</Title>
        </div>
        </>
    )
}