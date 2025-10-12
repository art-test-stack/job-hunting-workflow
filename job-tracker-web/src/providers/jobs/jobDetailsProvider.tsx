import { getUserJobByIdJobDetailGet, JobOutput } from "@/client"
import { Children, createContext, useEffect, useState } from "react"
import { useAuth } from "../auth/authProvider"
import { useUser } from "@auth0/nextjs-auth0"
import { useRouter } from "next/router";

export const JobDetailsContext = createContext<[JobOutput | undefined, React.Dispatch<React.SetStateAction<JobOutput | undefined>>, boolean]>([undefined, () => {}, true ]);
export const CurrentJobDetailsProvider = ( { children }: { children: any }) => {
    const { user } = useUser();
    const [ jobDetails, setJobDetails ] = useState<JobOutput>()
    const { token, isLoading: tokenLoading } = useAuth();
    const [loading, setLoading] = useState(true);
    const router = useRouter();
    const { job_id } = router.query;
    useEffect(() => {
        if (!user || !token || tokenLoading || !job_id) return;

        const fetchData = async () => {
        try {
            const response = await getUserJobByIdJobDetailGet({ query: { user_id: user.sub, job_id: job_id } });
            if (response.data) setJobDetails(response.data);
        } catch (err) {
            console.error('Error fetching jobs:', err);
        } finally {
            setLoading(false);
        }
        };

        fetchData();
    }, [user, token, tokenLoading, job_id]);

    return (
        <JobDetailsContext.Provider value={[jobDetails, setJobDetails, loading]}>
            {children}
        </JobDetailsContext.Provider>
    )
}
