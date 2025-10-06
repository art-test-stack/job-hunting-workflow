import fetch from 'node-fetch';
import dotenv from 'dotenv';
dotenv.config({ path: '.env.test' });

export async function getTestAccessToken() {
  const res = await fetch(`https://${process.env.AUTH0_DOMAIN}/oauth/token`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      grant_type: 'password',
      username: process.env.AUTH0_TEST_USERNAME,
      password: process.env.AUTH0_TEST_PASSWORD,
      audience: process.env.AUTH0_AUDIENCE,
      client_id: process.env.AUTH0_CLIENT_ID,
      client_secret: process.env.AUTH0_CLIENT_SECRET,
      scope: 'openid profile email'
    })
  });
  const data = await res.json();
  return data.access_token;
}
