import { useEffect, useRef, useState } from "react";
import API from "./services/api";
import "./App.css";

function App() {
  const chatEndRef = useRef(null);

  const [isOpen, setIsOpen] = useState(true);

  const [labContext, setLabContext] = useState({
    lab_id: "current-lab",
    lab_name: "Current CloudLabs Lab",
    exercise: "Exercise 1",
    task: "Task 1",
    step: "Step 1",
  });

  const [screenContext, setScreenContext] = useState({
    currentScreen: "Azure Portal",
    detectedPage: "Unknown",
    learnerState: "Needs Help",
  });

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hi 👋\n\nI'm CloudLabs AI Proctor. Tell me what issue you are facing, or use Screen Awareness to analyze where you are in the lab.",
      source: null,
      score: null,
      userQuestion: "",
      feedbackSent: false,
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  // Tracks the most recent substantive (non-canned-followup) question the
  // learner asked. Used so generic follow-ups like "Still stuck" can carry
  // the actual topic instead of sending a content-free sentence that the
  // backend has nothing real to search on.
  const [lastTopic, setLastTopic] = useState("");

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

  const updateContext = (field, value) => {
    setLabContext((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  const getConfidence = (score) => {
    if (score >= 4) return "High";
    if (score >= 3) return "Medium";
    return "Low";
  };

  const cleanSource = (source) => {
    if (!source) return "No source";
    return source.split("/").pop();
  };

  const analyzeCurrentScreen = () => {
    const message = `
I am currently on:
Screen: ${screenContext.currentScreen}
Detected Page: ${screenContext.detectedPage}
Learner State: ${screenContext.learnerState}

Lab Context:
Lab Name: ${labContext.lab_name}
Exercise: ${labContext.exercise}
Task: ${labContext.task}
Step: ${labContext.step}

Tell me:
1. Am I on the correct page?
2. What exact next click should I perform?
3. If I am on the wrong page, how should I recover?
`;

    setLastTopic(message);
    sendMessage(message);
  };

  // isFollowUp = true for canned "did that work?" style replies that carry
  // no topic of their own (e.g. "Still stuck"). These reuse lastTopic
  // instead of overwriting it, and get flagged to the backend.
  const sendMessage = async (messageText = input, isFollowUp = false) => {
    if (!messageText.trim() || loading) return;

    const outgoingText =
      isFollowUp && lastTopic
        ? `Follow-up on previous issue: "${lastTopic}". ${messageText}`
        : messageText;

    if (!isFollowUp) {
      setLastTopic(messageText);
    }

    setMessages((prev) => [
      ...prev,
      { role: "user", text: messageText, source: null, score: null },
    ]);

    setInput("");
    setLoading(true);

    try {
      const response = await API.post("/chat", {
        session_id: "frontend-user-1",
        user_message: outgoingText,
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
          userQuestion: outgoingText,
          feedbackSent: false,
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "I could not connect to the backend. Please confirm the FastAPI backend is running and the frontend proxy is configured.",
          source: null,
          score: null,
          userQuestion: outgoingText,
          feedbackSent: false,
        },
      ]);
    }

    setLoading(false);
  };

  const submitFeedback = async (index, rating) => {
    const message = messages[index];

    try {
      await API.post("/feedback/", {
        session_id: "frontend-user-1",
        user_message: message.userQuestion || "",
        answer: message.text,
        rating,
      });

      setMessages((prev) =>
        prev.map((msg, i) =>
          i === index ? { ...msg, feedbackSent: true } : msg
        )
      );
    } catch {
      alert("Feedback could not be saved.");
    }
  };

  const copyMessage = async (text) => {
    await navigator.clipboard.writeText(text);
    alert("Response copied.");
  };

  const clearChat = () => {
    setMessages([
      {
        role: "assistant",
        text: "Chat cleared. How can I help you with your lab now?",
        source: null,
        score: null,
        userQuestion: "",
        feedbackSent: false,
      },
    ]);
    setLastTopic("");
  };

  return (
    <>
      {!isOpen && (
        <button className="floating-launcher" onClick={() => setIsOpen(true)}>
          <span>🤖</span>
          <strong>AI Proctor</strong>
        </button>
      )}

      {isOpen && (
        <div className="widget-shell">
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
                <p>Lab Copilot active</p>
              </div>
              <div className="wave-icon">〽</div>
            </div>

            <div className="panel-card">
              <h3>Current Lab Context</h3>

              <label>Lab Name</label>
              <input
                className="context-input"
                value={labContext.lab_name}
                onChange={(e) => updateContext("lab_name", e.target.value)}
              />

              <label>Exercise</label>
              <input
                className="context-input"
                value={labContext.exercise}
                onChange={(e) => updateContext("exercise", e.target.value)}
              />

              <label>Task</label>
              <input
                className="context-input"
                value={labContext.task}
                onChange={(e) => updateContext("task", e.target.value)}
              />

              <label>Step</label>
              <input
                className="context-input"
                value={labContext.step}
                onChange={(e) => updateContext("step", e.target.value)}
              />
            </div>

            <div className="panel-card">
              <h3>Screen Awareness</h3>

              <label>Current Screen</label>
              <select
                className="context-input"
                value={screenContext.currentScreen}
                onChange={(e) =>
                  setScreenContext({
                    ...screenContext,
                    currentScreen: e.target.value,
                  })
                }
              >
                <option>Azure Portal</option>
                <option>Microsoft Fabric</option>
                <option>CloudLabs VM</option>
                <option>Login Page</option>
                <option>Power Automate</option>
              </select>

              <label>Detected Page</label>
              <select
                className="context-input"
                value={screenContext.detectedPage}
                onChange={(e) =>
                  setScreenContext({
                    ...screenContext,
                    detectedPage: e.target.value,
                  })
                }
              >
                <option>Unknown</option>
                <option>Home Page</option>
                <option>Workspace Page</option>
                <option>Lakehouse Page</option>
                <option>Eventhouse Page</option>
                <option>Data Agent Page</option>
                <option>Wrong Page</option>
                <option>Error Page</option>
              </select>

              <label>Learner State</label>
              <select
                className="context-input"
                value={screenContext.learnerState}
                onChange={(e) =>
                  setScreenContext({
                    ...screenContext,
                    learnerState: e.target.value,
                  })
                }
              >
                <option>Needs Help</option>
                <option>Wrong Page</option>
                <option>Stuck</option>
                <option>Error Visible</option>
                <option>Ready for Next Step</option>
              </select>

              <button className="analyze-btn" onClick={analyzeCurrentScreen}>
                🧠 Analyze Current Screen
              </button>
            </div>

            <div className="panel-card">
              <div className="progress-title">
                <span>Lab Progress</span>
                <strong>60%</strong>
              </div>
              <div className="progress-bar">
                <div className="progress-fill"></div>
              </div>
              <p className="small-text">Context-aware guidance enabled</p>
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
                  <h1>
                    <span>CloudLabs</span> AI Proctor
                  </h1>
                  <p>Floating lab copilot powered by Azure OpenAI</p>
                </div>
              </div>

              <div className="top-actions">
                <div className="gpt-badge">
                  <span></span>
                  GPT Connected
                </div>
                <button className="close-widget" onClick={() => setIsOpen(false)}>
                  ✕
                </button>
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
                      <div className="trouble-card-title">
                        ⚠️ AI Troubleshooting
                      </div>
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
                            <span className="confidence">
                              {getConfidence(message.score)}
                            </span>
                          </div>

                          <div>
                            <h4>🧠 Mode</h4>
                            <span className="issue">Lab Copilot</span>
                          </div>
                        </div>

                        <h4 className="recommended">💡 Recommended Actions</h4>

                        <div className="action-grid">
                          <button
                            onClick={() =>
                              sendMessage(
                                "I already waited 2-3 minutes but the issue is still happening.",
                                true
                              )
                            }
                          >
                            ⏳ Still stuck
                          </button>

                          <button
                            onClick={() =>
                              sendMessage(
                                "Guide me through this current exercise and task step by step."
                              )
                            }
                          >
                            🧭 Guide me
                          </button>

                          <button
                            onClick={() =>
                              sendMessage(
                                "What should I verify before continuing this lab step?"
                              )
                            }
                          >
                            ✅ Verify step
                          </button>

                          <button
                            onClick={() =>
                              sendMessage(
                                "Give me the next troubleshooting action based on my current lab context.",
                                true
                              )
                            }
                          >
                            🚀 Next action
                          </button>
                        </div>

                        <div className="feedback-row">
                          {message.feedbackSent ? (
                            <span className="feedback-thanks">
                              ✅ Thanks for your feedback!
                            </span>
                          ) : (
                            <>
                              <button onClick={() => submitFeedback(index, 1)}>
                                👍 Helpful
                              </button>
                              <button onClick={() => submitFeedback(index, -1)}>
                                👎 Not Helpful
                              </button>
                            </>
                          )}

                          <button
                            className="copy-btn"
                            onClick={() => copyMessage(message.text)}
                          >
                            📋
                          </button>
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
      )}
    </>
  );
}

export default App;
