// // pages/api/auth/access-token.ts
// import { getAccessToken } from '@auth0/nextjs-auth0';

// export default async function handler(req, res) {
//   try {
//     const { accessToken } = await getAccessToken(req, res, {
//       audience: process.env.AUTH0_AUDIENCE,
//     });

//     if (!accessToken) {
//       return res.status(400).json({ error: 'No access token found' });
//     }

//     res.status(200).json({ accessToken });
//   } catch (error) {
//     console.error('Error fetching token:', error);
//     res.status(error.status || 500).json({ error: error.message });
//   }
// }
