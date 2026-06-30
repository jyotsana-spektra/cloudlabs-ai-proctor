import axios from "axios";

const API = axios.create({
  baseURL: "https://probable-space-adventure-69qp9p49wpvxf5rrr-8000.app.github.dev",
  headers: {
    "Content-Type": "application/json",
  },
});

export default API;