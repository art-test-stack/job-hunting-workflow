import { Button } from "@mantine/core";
import { useForm } from "@mantine/form";
import { useDisclosure } from "@mantine/hooks";
import AddJobModal from "./addJobModal";
import { JobStatus } from "@/pages/jobs";

interface AddJobProps {
    data: any,
    setData: any
}

export default function AddJob(props: AddJobProps) {
    const [opened, { open, close }] = useDisclosure(false); 
    const addJobForm = useForm({
        initialValues: {
            title: "",
            company: "",
            location: "",
            contract: "",
            type: "",
            business: [],
            url: "",
            status: "",
            application_date: new Date().toISOString().split('T')[0], // today's date in string format (YYYY-MM-DD)
        }
    })
    const onClose = () => {
        return close()
    }
    const onSubmit = () => {
        props.setData([...props.data, addJobForm.values])
        return close()
    }
    return (
        <>
            <AddJobModal opened={opened} onClose={onClose} onSubmit={onSubmit} content={addJobForm}/>
            <Button variant="default" onClick={open}>Add a New Job</Button>
        </>
    )
}