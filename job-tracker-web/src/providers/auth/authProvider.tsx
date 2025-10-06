// if you're on Next.js App Router (13+), otherwise not needed

// // import { Auth0Provider } from "@auth0/auth0-react";
// import { useRouter } from "next/router";
// import { ReactNode } from "react";

// interface WithAuth0Props {
//   children: ReactNode;
// }

// export const AuthProvider = ({ children }: WithAuth0Props) => {
//   const router = useRouter();

//   const onRedirectCallback = (appState?: any) => {
//     router.push(appState?.returnTo || "/");
//   };

//   return (
//     <Auth0Provider
//       domain="job-tracker.eu.auth0.com"
//       clientId="EFddAcCt44JHQZxauWNqelViOWTLel3X"
//       authorizationParams={{
//         redirect_uri: typeof window !== "undefined" ? window.location.origin : "",
//       }}
//       onRedirectCallback={onRedirectCallback}
//     >
//       {children}
//     </Auth0Provider>
//   );
// };
