import { useEffect, useRef, useState } from "react";
import API from "./services/api";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hi Brainy 👋 I’m CloudLabs AI Proctor. Tell me what issue you are facing in your lab.",
      source: null,
      score: null,
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  const quickPrompts = [
    "VM is not loading",
    "I cannot login",
    "Azure portal is not opening",
    "Data agent is not visible",
    "Lab is stuck",
  ];

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const sendMessage = async (messageText = input) => {
    if (!messageText.trim()) return;

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
        lab_id: "fabric",
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
    } catch (error) {
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
    <div className="page">
      <div className="background-glow glow-one"></div>
      <div className="background-glow glow-two"></div>

      <div className="layout">
        <aside className="sidebar">
          <div className="brand">
            <div className="logo">AI</div>
            <div>
              <h1>CloudLabs</h1>
              <p>AI Proctor</p>
            </div>
          </div>

          <div className="status-card">
            <span className="pulse"></span>
            Backend Connected
          </div>

          <div className="quick-section">
            <h3>Quick Help</h3>
            {quickPrompts.map((prompt) => (
              <button key={prompt} onClick={() => sendMessage(prompt)}>
                {prompt}
              </button>
            ))}
          </div>

          <button className="clear-btn" onClick={clearChat}>
            Clear Chat
          </button>
        </aside>

        <main className="chat-panel">
          <header className="chat-header">
            <div>
              <h2>CloudLabs AI Proctor</h2>
              <p>Real-time lab support powered by Azure OpenAI</p>
            </div>
            <div className="badge">GPT Connected</div>
          </header>

          <section className="chat-body">
            {messages.map((message, index) => (
              <div key={index} className={`message-row ${message.role}`}>
                <div className={`avatar ${message.role}`}>
                  {message.role === "assistant" ? "🤖" : "🧑"}
                </div>

                <div className="message-content">
                  <div className={`bubble ${message.role}`}>
                    {message.text}
                  </div>

                  {message.role === "assistant" && message.source && (
                    <div className="meta">
                      Source: {message.source} | Confidence score:{" "}
                      {message.score}
                    </div>
                  )}
                </div>
              </div>
            ))}

            {loading && (
              <div className="message-row assistant">
                <div className="avatar assistant">🤖</div>
                <div className="typing">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            )}

            <div ref={chatEndRef}></div>
          </section>

          <footer className="chat-footer">
            <input
              value={input}
              placeholder="Describe your lab issue..."
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") sendMessage();
              }}
            />
            <button onClick={() => sendMessage()}>Send</button>
          </footer>
        </main>
      </div>
    </div>
  );
}

export default App;