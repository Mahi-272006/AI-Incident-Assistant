import { useState } from "react";
import "./style.css";

function App() {

  const [ticket, setTicket] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const [listening, setListening] = useState(false);
  const highCount = history.filter(i => i.priority === "HIGH").length;
  const mediumCount = history.filter(i => i.priority === "MEDIUM").length;
  const lowCount = history.filter(i => i.priority === "LOW").length;


  const analyzeTicket = async () => {

    setLoading(true);

    const response = await fetch("http://127.0.0.1:5000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ticket }),
    });

    const data = await response.json();

    setResult(data);
    setHistory([data, ...history]);
    setLoading(false);
  };
  const startVoiceInput = () => {

    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.start();

    setListening(true);

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setTicket(transcript);
      setListening(false);
    };

    recognition.onerror = () => {
      setListening(false);
    };
  };
  const getPriorityClass = (priority) => {
    if (priority === "HIGH") return "high";
    if (priority === "MEDIUM") return "medium";
    return "low";
  };

  return (
    <div className="container">

      <h1>AI Incident Assistant</h1>
      <div className="stats">

        <div className="card">
          <h3>Total Incidents</h3>
          <p>{history.length}</p>
        </div>

        <div className="card high-card">
          <h3>High Priority</h3>
          <p>{highCount}</p>
        </div>

        <div className="card medium-card">
          <h3>Medium Priority</h3>
          <p>{mediumCount}</p>
        </div>

        <div className="card low-card">
          <h3>Low Priority</h3>
          <p>{lowCount}</p>
        </div>

      </div>

      <textarea
        placeholder="Describe your IT issue..."
        value={ticket}
        onChange={(e) => setTicket(e.target.value)}
      />

      <button onClick={analyzeTicket}>
        Analyze Ticket
      </button>

      <button className="voice" onClick={startVoiceInput}>
        🎤 Speak Incident
      </button>

      {listening && <p className="listening">Listening...</p>}

      {loading && <p className="loading">AI is analyzing the incident...</p>}

      {result && (
        <div className="result">

          <h2>Incident Analysis</h2>

          <p><strong>Ticket:</strong> {result.ticket}</p>

          <p>
            <strong>Category:</strong> {result.category}
          </p>

          <p>
            <strong>Priority:</strong>
            <span className={`badge ${getPriorityClass(result.priority)}`}>
              {result.priority}
            </span>
          </p>

          <h3>AI Solution</h3>
          <pre>{result.ai_solution}</pre>
          <h3>Similar Past Incidents</h3>

          <ul>
            {result.similar_tickets &&
              result.similar_tickets.map((ticket, index) => (
                <li key={index}>{ticket}</li>
              ))}
          </ul>

        </div>
      )}

      {history.length > 0 && (
        <div className="history">

          <h2>Incident History</h2>

          <table>
            <thead>
              <tr>
                <th>Ticket</th>
                <th>Category</th>
                <th>Priority</th>
              </tr>
            </thead>

            <tbody>
              {history.map((item, index) => (
                <tr key={index}>
                  <td>{item.ticket}</td>
                  <td>{item.category}</td>
                  <td>
                    <span className={`badge ${getPriorityClass(item.priority)}`}>
                      {item.priority}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>

          </table>

        </div>
      )}

    </div>
  );
}

export default App;