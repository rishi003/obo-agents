import axios from 'axios';
import { headers } from 'next/dist/client/components/headers';

const BASE_URL = 'http://localhost:8000';

const client = axios.create({
  baseURL: BASE_URL,
  headers: {
    common: {
      'Content-Type': 'application/json',
    },
  },
});

export default client;
