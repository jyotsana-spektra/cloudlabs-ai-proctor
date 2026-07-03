import { useEffect, useRef, useState } from "react";
import API from "./services/api";
import "./App.css";

function App() {
  const chatEndRef = useRef(null);

  const labContext = {
    lab_id: "fabric",
    lab_name: "Fabric IQ",
    exercise: "Exercise 2 of 5",
    task: "Task 3",
    step: "Step 5",
  };

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hi Brainy 👋\n\nI'm CloudLabs AI Proctor. Tell me what issue you are facing in your lab.",
      source: null,
      score: null,
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const quickPrompts = [
    { icon: "🖥️", text: "VM is not loading" },
    { icon: "👤", text: "I cannot login" },
    { icon: "🌐", text: "Azure portal is not opening" },
    { icon: "👁️", text: "Data agent is not visible" },
    { icon: "⚠️", text: "Lab is stuck" },
  ];

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const getConfidence = (score) => {
    if (score >= 4) return "High";
    if (score >= 3) return "Medium";
    return "Low";
  };

  const cleanSource = (source) => {
    if (!source) return "No source";
    return source.split("/").pop();
  };

  const sendMessage = async (messageText = input) => {
    if (!messageText.trim() || loading) return;

    setMessages((prev) => [
      ...prev,
      { role: "user", text: messageText, source: null, score: null },
    ]);

    setInput("");
    setLoading(true);

    try {
      const response = await API.post("/chat", {
        session_id: "frontend-user-1",
        user_message: messageText,
        lab_id: labContext.lab_id,
        lab_name: labContext.lab_name,
        exercise: labContext.exercise,
        task: labContext.task,
        step: labContext.step,
      });

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: response.data.answer,
          source: response.data.source,
          score: response.data.score,
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "I could not connect to the backend. Please check if the FastAPI server is running and port 8000 is public.",
          source: null,
          score: null,
        },
      ]);
    }

    setLoading(false);
  };

  const clearChat = () => {
    setMessages([
      {
        role: "assistant",
        text: "Chat cleared. How can I help you with your lab now?",
        source: null,
        score: null,
      },
    ]);
  };

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon">🤖</div>
          <div>
            <h1>CloudLabs</h1>
            <h2>AI Proctor</h2>
          </div>
        </div>

        <div className="status-card">
          <div>
            <span className="status-dot"></span>
            <strong>Backend Connected</strong>
            <p>All systems operational</p>
          </div>
          <div className="wave-icon">〽</div>
        </div>

        <div className="panel-card">
          <h3>Current Lab Context</h3>
          <div className="context-row">📘 <span>{labContext.lab_name}</span></div>
          <div className="context-row">🧩 <span>{labContext.exercise}</span></div>
          <div className="context-row">✅ <span>{labContext.task}</span></div>
          <div className="context-row">👉 <span>{labContext.step}</span></div>
        </div>

        <div className="panel-card">
          <div className="progress-title">
            <span>Lab Progress</span>
            <strong>60%</strong>
          </div>
          <div className="progress-bar">
            <div className="progress-fill"></div>
          </div>
          <p className="small-text">Exercise 2 of 5</p>
        </div>

        <div className="panel-card quick-help">
          <h3>Quick Help</h3>
          {quickPrompts.map((item) => (
            <button key={item.text} onClick={() => sendMessage(item.text)}>
              <span>{item.icon}</span>
              {item.text}
            </button>
          ))}
        </div>

        <button className="clear-chat" onClick={clearChat}>
          🗑 Clear Chat
        </button>
      </aside>

      <main className="main-panel">
        <header className="topbar">
          <div className="title-wrap">
            <div className="bot-logo">🤖</div>
            <div>
              <h1><span>CloudLabs</span> AI Proctor</h1>
              <p>Real-time lab support powered by Azure OpenAI</p>
            </div>
          </div>

          <div className="gpt-badge">
            <span></span>
            GPT Connected
            <small>🛰️</small>
          </div>
        </header>

        <section className="chat-area">
          {messages.map((message, index) => (
            <div key={index} className={`chat-row ${message.role}`}>
              <div className={`chat-avatar ${message.role}`}>
                {message.role === "assistant" ? "🤖" : "👤"}
              </div>

              <div className={`chat-bubble ${message.role}`}>
                {message.role === "assistant" && index !== 0 && (
                  <div className="trouble-card-title">⚠️ AI Troubleshooting</div>
                )}

                <p>{message.text}</p>

                {message.role === "assistant" && message.source && (
                  <div className="trouble-card">
                    <div className="card-metrics">
                      <div>
                        <h4>📘 Source</h4>
                        <span>{cleanSource(message.source)}</span>
                      </div>
                      <div>
                        <h4>⭐ Confidence</h4>
                        <span className="confidence">{getConfidence(message.score)}</span>
                      </div>
                      <div>
                        <h4>🧠 Issue Category</h4>
                        <span className="issue">VM Provisioning</span>
                      </div>
                    </div>

                    <h4 className="recommended">💡 Recommended Actions</h4>
                    <div className="action-grid">
                      <button>⏳ Wait 2–3 minutes</button>
                      <button>🔄 Refresh VM</button>
                      <button>🚀 Retry Launch</button>
                      <button>✅ Continue Lab</button>
                    </div>

                    <div className="feedback-row">
                      <button>👍 Helpful</button>
                      <button>👎 Not Helpful</button>
                      <button className="copy-btn">📋</button>
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}

          {loading && (
            <div className="chat-row assistant">
              <div className="chat-avatar assistant">🤖</div>
              <div className="typing">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          )}

          <div ref={chatEndRef}></div>
        </section>

        <footer className="input-area">
          <input
            value={input}
            placeholder="Describe your lab issue..."
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") sendMessage();
            }}
          />
          <button onClick={() => sendMessage()} disabled={loading}>
            ➤
          </button>
        </footer>
      </main>
    </div>
  );
}

export default App;