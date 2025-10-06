import request from 'supertest';
import { getTestAccessToken } from './auth0Token';

const BACKEND_URL = 'http://localhost:8000';

describe('Auth0 → FastAPI integration', () => {
  it('should authenticate user and get profile', async () => {
    const token = await getTestAccessToken();
    const res = await request(BACKEND_URL)
      .get('/profile')
      .set('Authorization', `Bearer ${token}`);
    
    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('user_id');
    console.log('Authenticated user:', res.body);
  });
});
