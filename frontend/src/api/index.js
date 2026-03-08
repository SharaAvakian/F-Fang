// API calls for FFAng frontend
import axios from 'axios';

const API_BASE_URL = '/api';  // Proxy to backend

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Add token to requests
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Products
export const getProducts = () => api.get('/products/');

// Users
export const registerUser = (data) => api.post('/users/register/', data);
export const loginUser = (data) => api.post('/users/login/', data);

// TODO: Add more API functions for orders, cart