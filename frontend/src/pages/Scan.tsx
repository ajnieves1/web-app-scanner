import axios from "axios";
import { useState } from "react";

export default function Scan() {
  const [url, setUrl] = useState("");
  const [results, setResults] = useState([]);

  const runScan = async () => {
    const res = await axios.post("http://localhost:8000/scans", null, {
      params: { target_url: url }
    });
    setResults(res.data.results);
  };

  return (
    <div className="p-6">
      <input
        className="border p-2"
        placeholder="https://example.com"
        onChange={e => setUrl(e.target.value)}
      />
      <button onClick={runScan} className="ml-2 bg-red-500 text-white px-4 py-2">
        Scan
      </button>

      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>
  );
}
