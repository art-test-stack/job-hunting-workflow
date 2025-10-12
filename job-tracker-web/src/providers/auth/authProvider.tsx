import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { useUser } from '@auth0/nextjs-auth0';
import { client } from '@/client/client.gen';
import { postUserUserAuthGet } from '@/client';

interface AuthContextType {
  token?: string;
  isLoading: boolean;
}

const AuthContext = createContext<AuthContextType>({ isLoading: true });

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const { user } = useUser();
  const [token, setToken] = useState<string>();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!user) return;

    const fetchToken = async () => {
      try {
        const res = await fetch('/auth/access-token');
        if (!res.ok) throw new Error('Failed to fetch access token');

        const data = await res.json();
        if (!data?.token) throw new Error('Access token is undefined');

        setToken(data.token);

        client.setConfig({ auth: () => data.token });
        
        if (data.token) {
          try {
            client.setConfig({
              auth: () => data.token
            })
            await postUserUserAuthGet();
          } catch (error) {
            console.error('Error in postUserUserAuthGet:', error);
          }
        }
      } catch (err) {
        console.error('Error fetching access token:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchToken();
  }, [user]);

  return (
    <AuthContext.Provider value={{ token, isLoading: loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
