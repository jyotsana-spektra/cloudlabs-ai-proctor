import axios from "axios";

// In local dev, requests go through the Vite "/api" proxy (see vite.config.js).
// In production (e.g. Render), set VITE_API_BASE_URL to the deployed backend's
// root URL (no trailing slash) so the built app calls it directly.
const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "/api",
  headers: {
    "Content-Type": "application/json",
  },
});

export default API;