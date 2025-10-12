import { getUserJobJobUserGet, JobOutput } from "@/client"
import { Children, createContext, useEffect, useState } from "react"
import { useAuth } from "../auth/authProvider"
import { useUser } from "@auth0/nextjs-auth0"

export const currentJobList = createContext<[JobOutput[] | undefined, React.Dispatch<React.SetStateAction<JobOutput[] | undefined>>, boolean]>([undefined, () => {}, true ]);

export const CurrentJobListProvider = ({ children }: { children: any }) => {
    const { user } = useUser();
    const [ jobList, setJobList ] = useState<JobOutput[]>()
    const { token, isLoading: tokenLoading } = useAuth();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (!user || !token || tokenLoading) return;

        const fetchData = async () => {
        try {
            const response = await getUserJobJobUserGet({ query: { user_id: user.sub } });
            if (response.data) setJobList(response.data);
        } catch (err) {
            console.error('Error fetching jobs:', err);
        } finally {
            setLoading(false);
        }
        };

        fetchData();
    }, [user, token, tokenLoading]);

    return (
        <currentJobList.Provider value={[jobList, setJobList, loading]}>
            {children}
        </currentJobList.Provider>
    )
}
