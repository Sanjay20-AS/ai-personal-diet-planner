import React, { useEffect, useState } from "react";
import { api } from "./api";

const initialProfile = {
  age: 21,
  height_cm: 170,
  weight_kg: 65,
  activity_level: "moderate",
  diet_preference: "vegetarian",
  allergies: "",
  goal: "general wellness",
  meals_per_day: 4
};

function Card({ children }) {
  return <div className="card">{children}</div>;
}

function Login({ onLogin }) {
  const [register, setRegister] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function submit(e) {
    e.preventDefault();
    setError("");
    try {
      if (register) {
        await api.register({ email, password });
      }
      const data = await api.login({ email, password });
      localStorage.setItem("token", data.access_token);
      onLogin();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <main className="auth">
      <Card>
        <h1>🥗 AI Personal Diet Planner</h1>
        <p className="muted">Cloud Computing Project</p>
        <form onSubmit={submit}>
          <input type="email" placeholder="Demo email" value={email}
            onChange={e => setEmail(e.target.value)} required />
          <input type="password" placeholder="Password (8+ characters)" value={password}
            onChange={e => setPassword(e.target.value)} minLength="8" required />
          <button>{register ? "Create Demo Account" : "Login"}</button>
        </form>
        {error && <p className="error">{error}</p>}
        <button className="secondary" onClick={() => setRegister(!register)}>
          {register ? "Already registered? Login" : "New user? Register"}
        </button>
      </Card>
    </main>
  );
}

function Dashboard({ logout }) {
  const [profile, setProfile] = useState(initialProfile);
  const [plans, setPlans] = useState([]);
  const [files, setFiles] = useState([]);
  const [stats, setStats] = useState({});
  const [message, setMessage] = useState("");

  async function load() {
    try {
      const [p, pl, f, d] = await Promise.all([
        api.profile(), api.plans(), api.files(), api.dashboard()
      ]);
      if (p) setProfile(p);
      setPlans(pl);
      setFiles(f);
      setStats(d);
    } catch (e) {
      setMessage(e.message);
    }
  }

  useEffect(() => { load(); }, []);

  async function saveProfile(e) {
    e.preventDefault();
    try {
      await api.saveProfile({
        ...profile,
        age: Number(profile.age),
        height_cm: Number(profile.height_cm),
        weight_kg: Number(profile.weight_kg),
        meals_per_day: Number(profile.meals_per_day)
      });
      setMessage("Profile saved.");
    } catch (e) {
      setMessage(e.message);
    }
  }

  async function generate() {
    try {
      const plan = await api.generate();
      setPlans([plan, ...plans]);
      setMessage("Demo AI plan generated.");
      await load();
    } catch (e) {
      setMessage(e.message);
    }
  }

  async function upload(e) {
    const file = e.target.files?.[0];
    if (!file) return;
    const form = new FormData();
    form.append("file", file);
    try {
      await api.upload(form);
      setMessage("File uploaded.");
      await load();
    } catch (e) {
      setMessage(e.message);
    }
  }

  async function deleteFile(id) {
    await api.deleteFile(id);
    await load();
  }

  return (
    <div className="app">
      <header>
        <div>
          <h1>🥗 Diet Planner</h1>
          <span className="muted">Cloud-ready AI application</span>
        </div>
        <button className="secondary" onClick={logout}>Logout</button>
      </header>

      {message && <div className="notice">{message}</div>}

      <section className="stats">
        <Card><b>{stats.plan_count ?? 0}</b><span>Plans</span></Card>
        <Card><b>{stats.file_count ?? 0}</b><span>Files</span></Card>
        <Card><b>{stats.latest_provider ?? "—"}</b><span>AI Provider</span></Card>
      </section>

      <div className="grid">
        <Card>
          <h2>Demo Profile</h2>
          <form onSubmit={saveProfile}>
            <label>Age<input type="number" value={profile.age} onChange={e => setProfile({...profile, age:e.target.value})}/></label>
            <label>Height (cm)<input type="number" value={profile.height_cm} onChange={e => setProfile({...profile, height_cm:e.target.value})}/></label>
            <label>Weight (kg)<input type="number" value={profile.weight_kg} onChange={e => setProfile({...profile, weight_kg:e.target.value})}/></label>
            <label>Activity
              <select value={profile.activity_level} onChange={e => setProfile({...profile, activity_level:e.target.value})}>
                <option>low</option><option>moderate</option><option>high</option>
              </select>
            </label>
            <label>Diet
              <select value={profile.diet_preference} onChange={e => setProfile({...profile, diet_preference:e.target.value})}>
                <option>vegetarian</option><option>vegan</option><option>non-vegetarian</option>
              </select>
            </label>
            <label>Goal
              <select value={profile.goal} onChange={e => setProfile({...profile, goal:e.target.value})}>
                <option>general wellness</option><option>weight loss</option><option>weight gain</option><option>muscle gain</option>
              </select>
            </label>
            <label>Allergies<input value={profile.allergies} onChange={e => setProfile({...profile, allergies:e.target.value})} placeholder="Demo only"/></label>
            <button>Save Profile</button>
          </form>
        </Card>

        <Card>
          <h2>AI Plan Generator</h2>
          <p className="muted">Uses the configured AI provider. Local mode works without an API key.</p>
          <button onClick={generate}>Generate Meal Plan</button>
          <p className="disclaimer">Demo/educational content only. Not clinical nutrition advice.</p>
        </Card>
      </div>

      <Card>
        <h2>Plan History</h2>
        {plans.length === 0 ? <p className="muted">No plans yet.</p> : plans.map(p => (
          <div className="plan" key={p.id}>
            <div>
              <b>{p.title}</b>
              <span>{p.goal} · {p.daily_calories} kcal · {p.ai_provider}</span>
            </div>
            <div className="meals">
              {Object.entries(p.plan_data).filter(([k]) => k !== "notes").map(([name, item]) => (
                <div key={name}><b>{name}</b><p>{item.meal}</p><small>{item.calories} kcal</small></div>
              ))}
            </div>
          </div>
        ))}
      </Card>

      <Card>
        <h2>Cloud Storage Demo</h2>
        <p className="muted">Upload a demo PDF, image or text file. Local mode stores it under backend/storage.</p>
        <input type="file" accept=".pdf,.png,.jpg,.jpeg,.txt" onChange={upload}/>
        {files.map(f => (
          <div className="file" key={f.id}>
            <span>{f.original_filename} ({Math.round(f.file_size/1024)} KB)</span>
            <button className="danger" onClick={() => deleteFile(f.id)}>Delete</button>
          </div>
        ))}
      </Card>

      <footer>
        Built as a Cloud Computing project · React + FastAPI + SQL + Storage + AI
      </footer>
    </div>
  );
}

export default function App() {
  const [loggedIn, setLoggedIn] = useState(!!localStorage.getItem("token"));

  if (!loggedIn) return <Login onLogin={() => setLoggedIn(true)} />;

  return (
    <Dashboard
      logout={() => {
        localStorage.removeItem("token");
        setLoggedIn(false);
      }}
    />
  );
}
