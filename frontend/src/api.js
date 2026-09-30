const API = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

async function request(path, options = {}) {
  const token = localStorage.getItem("token");
  const headers = { ...(options.headers || {}) };

  if (token) headers.Authorization = `Bearer ${token}`;
  if (!(options.body instanceof FormData)) {
    headers["Content-Type"] = "application/json";
  }

  const response = await fetch(`${API}${path}`, { ...options, headers });
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(data.detail || "Request failed");
  }
  return data;
}

export const api = {
  register: (body) => request("/auth/register", { method: "POST", body: JSON.stringify(body) }),
  login: (body) => request("/auth/login", { method: "POST", body: JSON.stringify(body) }),
  profile: () => request("/profile"),
  saveProfile: (body) => request("/profile", { method: "PUT", body: JSON.stringify(body) }),
  dashboard: () => request("/dashboard"),
  plans: () => request("/plans"),
  generate: () => request("/plans/generate", { method: "POST" }),
  files: () => request("/files"),
  upload: (form) => request("/files/upload", { method: "POST", body: form }),
  deleteFile: (id) => request(`/files/${id}`, { method: "DELETE" })
};
