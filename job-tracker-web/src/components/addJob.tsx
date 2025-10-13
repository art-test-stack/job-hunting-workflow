import { Button } from "@mantine/core";
import { useForm } from "@mantine/form";
import { useDisclosure } from "@mantine/hooks";
import AddJobModal from "./addJobModal";
import { addJobJobAddPost } from "@/client";
import { useUser } from "@auth0/nextjs-auth0";
import { useContext } from "react";
import { currentJobList } from "@/providers/jobs/jobListProvider";
import { useAuth } from "@/providers/auth/authProvider";


export default function AddJob() {
    const [data, setData, loading] = useContext(currentJobList)
    const { user } = useUser()
    const [opened, { open, close }] = useDisclosure(false); 
    const { token, isLoading: tokenLoading } = useAuth();
    const addJobForm = useForm({
        initialValues: {
            title: "",
            company: "",
            location: "",
            contract: "",
            place: "",
            business: [],
            url: "",
            status: "",
            applied_at: new Date().toISOString().split('T')[0], // today's date in string format (YYYY-MM-DD)
        }
    })
    const onClose = () => {
        return close()
    }
    const onSubmit = async () => {
        try {
                const response = await addJobJobAddPost({
                    query: {
                        user_id: user?.sub,
                        ...addJobForm.values}, 
                    headers: {
                        Authorization: `Bearer ${token}`,
                    }}
            );
            if (response.data) {
                setData([...data, response.data]);
            }
        } catch (error) {
            console.error("Failed to add job:", error);
        } finally {
            close();
        }
    }
    return (
        <>
            <AddJobModal opened={opened} onClose={onClose} onSubmit={onSubmit} content={addJobForm}/>
            <Button variant="default" onClick={open}>Add a New Job</Button>
        </>
    )
}