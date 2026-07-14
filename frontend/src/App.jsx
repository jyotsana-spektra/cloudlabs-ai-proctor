import { useEffect, useRef, useState } from "react";
import API from "./services/api";
import { SUPPORT_EMAIL, LIVE_CHAT_URL } from "./config";
import "./App.css";

// Fixed session id used for every request from this browser tab. Because
// it never changes, the backend keeps accumulating conversation history
// and a cached knowledge-base result under this same id -- both MUST be
// explicitly cleared (via clearBackendSession) whenever the learner clears
// the chat or switches to a different lab, otherwise Brainy keeps answering
// using the previous lab's history/context.
const SESSION_ID = "frontend-user-1";

// "Current Screen" / "Detected Page" choices shown in Screen Awareness,
// scoped per lab_id (matches the knowledge-base labguides/ folder names)
// so learners only see screens/pages that actually exist in the lab
// they're doing, instead of a fixed generic Fabric-flavored list no
// matter which workshop is selected. "current-lab" is the fallback used
// when no workshop has been picked yet (or for an unrecognized lab_id).
const SCREEN_OPTIONS_BY_LAB = {
  "current-lab": {
    screens: ["Azure Portal", "Microsoft Fabric", "CloudLabs VM", "Login Page", "Power Automate"],
    pages: ["Unknown", "Home Page", "Workspace Page", "Wrong Page", "Error Page"],
  },
  "fabric-iq": {
    screens: ["Microsoft Fabric", "Power BI Service", "Azure Portal", "Login Page"],
    pages: ["Unknown", "Home Page", "Workspace Page", "Lakehouse Page", "Eventhouse Page", "Data Agent Page", "Ontology Page", "Wrong Page", "Error Page"],
  },
  "virtual-machine-and-compute": {
    screens: ["CloudLabs VM", "Remote Desktop (RDP)", "Azure Portal", "Login Page"],
    pages: ["Unknown", "VM Connection Page", "Remote Desktop Session", "Azure Portal Home", "Resource Group Page", "Wrong Page", "Error Page"],
  },
  "microsoft-azure-ai-agents": {
    screens: ["Azure AI Studio", "Azure Portal", "Login Page"],
    pages: ["Unknown", "Agent Playground", "Model Deployment Page", "Azure Portal Home", "Wrong Page", "Error Page"],
  },
  "github-copilot-innovation-workshop-mastering-github-copilot-across-the-sdlc": {
    screens: ["VS Code", "GitHub", "Azure Portal", "Login Page"],
    pages: ["Unknown", "Repository Page", "Copilot Chat Panel", "Pull Request Page", "Actions Page", "Wrong Page", "Error Page"],
  },
};

const getScreenOptions = (labId) =>
  SCREEN_OPTIONS_BY_LAB[labId] || SCREEN_OPTIONS_BY_LAB["current-lab"];

function App() {
  const chatEndRef = useRef(null);

  const [isOpen, setIsOpen] = useState(true);

  const [availableLabs, setAvailableLabs] = useState([]);

  const [labContext, setLabContext] = useState({
    lab_id: "current-lab",
    lab_name: "Current CloudLabs Lab",
    exercise: "Exercise 1",
    task: "Task 1",
    step: "Step 1",
  });

  const [screenContext, setScreenContext] = useState({
    currentScreen: getScreenOptions("current-lab").screens[0],
    detectedPage: getScreenOptions("current-lab").pages[0],
  });

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Welcome! I'm Brainy, your Lab Copilot. Ask me anything, or use Screen Awareness so I can guide you based on your current lab step.",
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
    { icon: "⚠️", text: "I am stuck" },
  ];

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  // Load the list of lab-guide workshops from the knowledge base so the
  // learner can tell Brainy which workshop they're currently in. This is
  // what scopes/boosts knowledge-base search to the right lab guide.
  useEffect(() => {
    const loadLabs = async () => {
      try {
        const response = await API.get("/admin/labs");
        setAvailableLabs(response.data.labs || []);
      } catch {
        setAvailableLabs([]);
      }
    };

    loadLabs();
  }, []);

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

  // Pre-fills a mailto: draft with the learner's current lab context and
  // last-asked question so they can just hit send -- no need to manually
  // look up or copy the support email address.
  const openSupportEmail = () => {
    const subject = `CloudLabs Lab Support Request - ${labContext.lab_name}`;
    const body = [
      "Hi CloudLabs Support team,",
      "",
      "I need help with my lab.",
      "",
      `Workshop: ${labContext.lab_name}`,
      `Exercise: ${labContext.exercise}`,
      `Task: ${labContext.task}`,
      `Step: ${labContext.step}`,
      "",
      `Issue: ${lastTopic || "(please describe your issue here)"}`,
    ].join("\n");

    window.location.href = `mailto:${SUPPORT_EMAIL}?subject=${encodeURIComponent(
      subject
    )}&body=${encodeURIComponent(body)}`;
  };

  // Opens CloudLabs' live chat support in a new tab -- a one-click handoff
  // to a human instead of the learner having to go find the link themselves.
  const openLiveChat = () => {
    window.open(LIVE_CHAT_URL, "_blank", "noopener,noreferrer");
  };

  const analyzeCurrentScreen = () => {
    const message = `
I am currently on:
Screen: ${screenContext.currentScreen}
Detected Page: ${screenContext.detectedPage}

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
  const sendMessage = async (
    messageText = input,
    isFollowUp = false,
    viaQuickHelp = false
  ) => {
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
        session_id: SESSION_ID,
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
          questionType: response.data.question_type,
          userQuestion: outgoingText,
          feedbackSent: false,
          webSearchUsed: response.data.web_search_used,
          webSources: response.data.web_sources,
          quickHelp: viaQuickHelp,
          needsSupport: response.data.needs_support,
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
        session_id: SESSION_ID,
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

  // Deletes this tab's conversation history and cached KB result on the
  // backend. Without this, the backend keeps reusing the old history/cache
  // for SESSION_ID even after the UI chat is cleared or the lab is changed.
  const clearBackendSession = async () => {
    try {
      await API.delete(`/session/${SESSION_ID}`);
    } catch {
      // Non-fatal -- worst case the next message still carries old context,
      // which the backend will overwrite once a real answer comes back.
    }
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
    clearBackendSession();
  };

  // Switching the selected workshop/lab must not keep answering from the
  // previous lab's conversation history or cached search result, so this
  // resets the backend session in addition to updating the local context.
  // It also resets Screen Awareness to the new lab's own screens/pages --
  // otherwise a Fabric-only "Lakehouse Page" could stay selected while the
  // learner is now doing the VM lab.
  const handleWorkshopChange = (labId) => {
    updateContext("lab_id", labId);

    const options = getScreenOptions(labId);
    setScreenContext({
      currentScreen: options.screens[0],
      detectedPage: options.pages[0],
    });

    clearBackendSession();
    setMessages([
      {
        role: "assistant",
        text: "Switched lab context. How can I help you with this lab?",
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
          <img src="/brainy.png" alt="Brainy" />
          <strong>Brainy</strong>
        </button>
      )}

      {isOpen && (
        <div className="widget-shell">
          <aside className="sidebar">
            <div className="cloudlabs-badge">
              <img src="/cloudlabs-logo.png" alt="CloudLabs" />
            </div>

            <div className="brand">
              <div className="brand-icon">
                <img src="/brainy.png" alt="Brainy" />
              </div>
              <div>
                <h2 className="brand-subtitle">Session Controls</h2>
              </div>
            </div>

            <div className="panel-card">
              <h3>Current Lab Context</h3>

              <label title="Choose the workshop or lab guide you are currently working through">
                Workshop / Lab Guide
              </label>
              <select
                className="context-input"
                value={labContext.lab_id}
                onChange={(e) => handleWorkshopChange(e.target.value)}
                title="Choose the workshop or lab guide you are currently working through"
              >
                <option value="current-lab">Select a workshop...</option>
                {availableLabs.map((lab) => (
                  <option key={lab.id} value={lab.id}>
                    {lab.label}
                  </option>
                ))}
              </select>

              <label>Lab Name</label>
              <input
                className="context-input"
                value={labContext.lab_name}
                readOnly
                disabled
              />

              <label title="The exercise number or name you're currently working on, e.g. 'Exercise 2'">
                Exercise
              </label>
              <input
                className="context-input"
                value={labContext.exercise}
                onChange={(e) => updateContext("exercise", e.target.value)}
                title="The exercise number or name you're currently working on, e.g. 'Exercise 2'"
              />

              <label title="The task number or name within the current exercise, e.g. 'Task 3'">
                Task
              </label>
              <input
                className="context-input"
                value={labContext.task}
                onChange={(e) => updateContext("task", e.target.value)}
                title="The task number or name within the current exercise, e.g. 'Task 3'"
              />

              <label title="The specific step number you're on within the current task, e.g. 'Step 4'">
                Step
              </label>
              <input
                className="context-input"
                value={labContext.step}
                onChange={(e) => updateContext("step", e.target.value)}
                title="The specific step number you're on within the current task, e.g. 'Step 4'"
              />
            </div>

            <div className="panel-card">
              <details open>
                <summary>🖥️ Screen Awareness</summary>

                <div className="field-group">
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
                    {getScreenOptions(labContext.lab_id).screens.map((screen) => (
                      <option key={screen}>{screen}</option>
                    ))}
                  </select>
                </div>

                <div className="field-group">
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
                    {getScreenOptions(labContext.lab_id).pages.map((page) => (
                      <option key={page}>{page}</option>
                    ))}
                  </select>
                </div>

                <button className="analyze-btn" onClick={analyzeCurrentScreen}>
                  🧠 Analyze Current Screen
                </button>
              </details>
            </div>

            <div className="panel-card quick-help">
              <details open>
                <summary>💡 Quick Help</summary>
                {quickPrompts.map((item) => (
                  <button
                    key={item.text}
                    onClick={() => sendMessage(item.text, false, true)}
                  >
                    <span className="qh-icon">{item.icon}</span>
                    {item.text}
                  </button>
                ))}
              </details>
            </div>

            <button className="clear-chat" onClick={clearChat}>
              🗑 Clear Chat
            </button>
          </aside>

          <main className="main-panel">
            <header className="topbar">
              <div className="title-wrap">
                <div className="bot-logo">
                  <img src="/brainy.png" alt="Brainy" />
                </div>
                <div>
                  <h1>Brainy</h1>
                  <p>AI Lab Copilot</p>
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
                    {message.role === "assistant" ? (
                      <img src="/brainy.png" alt="Brainy" />
                    ) : (
                      "👤"
                    )}
                  </div>

                  <div className={`chat-bubble ${message.role}`}>
                    {message.role === "assistant" &&
                      index !== 0 &&
                      !message.quickHelp &&
                      message.questionType === "troubleshooting" &&
                      message.source && (
                        <div className="trouble-card-title">
                          ⚠️ AI Troubleshooting
                        </div>
                      )}

                    <p>{message.text}</p>

                    {message.role === "assistant" &&
                      !message.quickHelp &&
                      message.webSearchUsed &&
                      message.webSources?.length > 0 && (
                      <div className="trouble-card web-search-card">
                        <div className="card-metrics">
                          <div>
                            <h4>🌐 Source</h4>
                            <span>General web search (not the official lab guide)</span>
                          </div>
                        </div>

                        <ul className="web-source-list">
                          {message.webSources.map((item) => (
                            <li key={item.url}>
                              <a href={item.url} target="_blank" rel="noreferrer">
                                {item.title}
                              </a>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {message.role === "assistant" &&
                      index !== 0 &&
                      !message.quickHelp &&
                      message.needsSupport && (
                      <div className="trouble-card support-inline-card">
                        <h4 className="recommended">🆘 Connect with Support</h4>
                        <div className="support-actions">
                          <button
                            className="support-btn"
                            onClick={openSupportEmail}
                            title={`Email ${SUPPORT_EMAIL}`}
                          >
                            <span className="support-icon">📧</span>
                            Email
                          </button>

                          <button
                            className="support-btn"
                            onClick={openLiveChat}
                            title="Chat live with CloudLabs Support"
                          >
                            <span className="support-icon">💬</span>
                            Live Chat
                          </button>
                        </div>
                      </div>
                    )}

                    {message.role === "assistant" &&
                      !message.quickHelp &&
                      message.questionType === "troubleshooting" &&
                      message.source && (
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
                  <div className="chat-avatar assistant">
                    <img src="/brainy.png" alt="Brainy" />
                  </div>
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
