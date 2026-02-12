import { useEffect, useState } from "react";

type Health = {
  status: string;
};

function App() {
  const [health, setHealth] = useState<Health | null>(null);
  const [error, setError] = useState<string | null>(null);

  const baseUrl = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    fetch(`${baseUrl}/health`)
      .then((res) => res.json())
      .then(setHealth)
      .catch((err) => setError(err.message));
  }, [baseUrl]);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Faith Sobriety Tracker</h1>

      <h2>Backend Health Check</h2>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {health ? (
        <pre>{JSON.stringify(health, null, 2)}</pre>
      ) : (
        !error && <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
