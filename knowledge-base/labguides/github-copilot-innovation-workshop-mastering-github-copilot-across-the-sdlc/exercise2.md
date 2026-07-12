# Exercise 2 - Exploring the Codebase with GitHub Copilot

#### Duration: 30 Minutes

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Use GitHub Copilot Chat in "Ask" mode to understand unfamiliar codebases
- Learn how to efficiently navigate and analyze project structure with AI assistance
- Understand how to identify build processes, testing frameworks, and dependencies
- Develop strategies for onboarding to new projects using GitHub Copilot

## 🍎 Scenario: Your First Day at The Daily Harvest

Welcome to your first day as a developer at The Daily Harvest! Your manager has just given you access to the e-commerce repository, but like any new team member, you need to understand:
- What does this application actually do?
- How is the code organized and structured?
- What technologies and frameworks are being used?
- How do I build, run, and test the application?

As a modern developer, you'll leverage GitHub Copilot Chat to accelerate your onboarding process and get productive quickly.

## 🤖 Introduction to GitHub Copilot Chat

GitHub Copilot Chat is an AI-powered conversational interface that helps you understand code, generate implementations, and solve development challenges. There are several modes to interact with GitHub Copilot:

| Mode | Purpose | Best For |
|------|---------|----------|
| **Ask** | Get explanations and answers about code | Understanding existing code, learning new concepts |
| **Agent** | Delegate complex tasks to AI | Multi-file changes, architectural decisions |
| **Plan** | Analyze requirements and create a step-by-step implementation plan | System design, task decomposition, aligning on approach before writing code |

For exploring an unfamiliar codebase, **Ask mode** is ideal because it allows you to:
- Query specific files or code patterns without making changes
- Get high-level explanations of project structure and purpose
- Understand dependencies, build processes, and testing strategies
- Ask follow-up questions to deepen your understanding

## 🧠 Choosing the Right AI Model

GitHub Copilot Chat provides access to multiple AI models, each optimized for different types of development tasks. Understanding when to use each model can help improve productivity, response quality, and overall development efficiency.

### Available Models

GitHub Copilot offers access to a growing selection of AI models from leading providers, including OpenAI, Anthropic, Google, and others. The available model catalog continues to evolve as new models are introduced and existing models are updated.

For the most up-to-date information about supported models and their capabilities, see the official documentation: [GitHub Copilot Supported Models](https://docs.github.com/copilot/reference/ai-models/supported-models)

Different models are designed for different scenarios:

- Some models are optimized for code generation and code understanding.
- Others excel at complex reasoning, architecture discussions, and problem-solving.
- Some prioritize speed and responsiveness for everyday development tasks.
- Others provide deeper analysis and more comprehensive explanations.
- Agentic models can perform multi-step tasks, analyze repositories, and assist with larger development workflows.

### Auto Model Selection

GitHub Copilot includes Auto Model Selection, which automatically chooses the most appropriate model for your request based on the task, context, and model availability.

Benefits of Auto Model Selection include:

- Automatically selects the best model for the task.
- Balances performance, quality, and responsiveness.
- Reduces the need for manual model switching.
- Helps streamline developer workflows by routing requests to the most suitable model.

More information can be found here: [Auto Model Selection](https://docs.github.com/copilot/concepts/auto-model-selection).  

### 💰 AI Credits and Usage

GitHub Copilot uses an AI Credits consumption model for premium AI experiences and advanced workflows.

**Important:** Different models and features may consume AI Credits at different rates based on the complexity of the request and the model being used.

**Key Points:**
- Code completions and standard Copilot coding assistance remain included with eligible Copilot plans.
- Premium AI models and advanced agentic experiences consume AI Credits.
- Different models may have different consumption rates.
- Auto Model Selection can automatically choose from multiple models and may provide optimized credit usage for supported plans.
- Organizations can monitor and manage AI usage through administrative controls and reporting.

**Managing Usage:**

Organizations can:
- Track AI Credit consumption.
- Configure spending controls and budgets.
- Monitor usage trends across users and teams.
- Review model-specific consumption details.

For the latest pricing, billing, and AI Credit information, see: [GitHub Copilot Billing Documentation](https://docs.github.com/copilot/concepts/billing/copilot-requests)


### 🔄 Experimenting with Different Models

Try asking the same question to different models to compare their responses! Each model may provide unique insights or different perspectives on the same problem.

**How to Switch Models:**
1. In GitHub Copilot Chat, locate the **model selector**, typically displayed below the prompt input area.

2. Verify that the model selector is currently set to **Auto**, allowing GitHub Copilot to automatically choose the most appropriate model for your request.

   ![](../../media/model-picker.png)
   
3. Select a different model and ask your question. You may also choose from the latest models, such as **Claude Opus 4.7**, **Claude Sonnet 4.6** or **GPT-5.5**.

   ![](../../media/models-selector.png)

## 🔍 Step 1: Understanding the Project Purpose

Let's start by getting a high-level understanding of what this application does.

### Instructions:

1. Switch to **Ask** mode within GitHub Copilot Chat if you are not already in that mode.

   ![](../../media/E2S1S1.png)

2. Ask GitHub Copilot some questions to help you understand the application as it is currently working. First question you may ask:
`What is the main purpose of this application? What does it do?`.

   ![](../../media/E2S1S2.png)


3. **Try different models**: Start with the default model, then experiment with others to see how their explanations differ

If you get stuck, try using these sample prompts to explore the project. Click on Sample Prompts below to expand:

<details>
  <summary>Sample Prompts</summary>
  
  ```
  What is the main purpose of this application? What does it do?
  ```

  ```
  Can you give me a high-level overview of this project's features and functionality?
  ```

  ```
  What type of application is this? Is it a web app, API, desktop app, or something else?
  ```

</details>

### 💡 What to Expect from GitHub Copilot

When you ask these questions, GitHub Copilot will analyze your workspace and provide insights such as:
- **Application Type**: Whether it's an e-commerce site, API, web application, etc.
- **Core Features**: Key functionality like user authentication, product catalogs, payment processing
- **Technology Stack**: Programming languages, frameworks, and architectural patterns in use
- **Business Domain**: The industry or use case the application serves

GitHub Copilot's responses will be based on analyzing your codebase structure, configuration files, dependencies, and code patterns. The more specific your questions, the more targeted and useful the responses will be.

## 🏗️ Step 2: Analyzing Project Structure

Now let's understand how the code is organized and what the folder structure tells us.

### Instructions:

Ask GitHub Copilot some questions to help you understand the organization of the codebase. **Experiment**: Try asking the same structural question to different models - you might get varying levels of detail or different organizational perspectives! If you get stuck, try using these sample prompts to explore the project, click on Sample Prompts below to expand:

<details>
  <summary>Sample Prompts</summary>

  ```
  How is this project structured? Can you explain the main folders and their purposes?
  ```

  ```
  What are the most important files I should understand as a new developer on this project?
  ```

  ```
  Are there any configuration files I should be aware of? What do they control?
  ```

</details>

### 💡 What to Expect from GitHub Copilot

When you ask these questions, GitHub Copilot will analyze the files and folders in your workspace and provide a structural breakdown, including:
- **Folder Roles**: Explanations of what code lives in main directories like `src/`, `tests/`, `public/`, or `components/`.
- **Key Files**: Identification of critical files such as `package.json`, `README.md`, or main entry points (e.g., `index.js`, `main.py`).
- **Architectural Patterns**: Insights into how the project is organized (e.g., MVC, layered architecture, microservices).
- **Configuration Details**: Information about configuration files like environment variables (`.env`), build configuration (e.g., `webpack.config.js`), or database connection settings.

  ![](../../media/step-2-output.png)

GitHub Copilot's response helps new developers quickly orient themselves by providing a map of the codebase organization.

## 💻 Step 3: Identifying Technologies and Frameworks

Understanding the tech stack is crucial for knowing what skills you'll need and how to work effectively.

### Instructions:

Ask GitHub Copilot some questions to help you understand the technologies and frameworks used within the codebase. 

If you get stuck, click on Sample Prompts below to expand and try using these to explore the project. 

<details>
  <summary>Sample Prompts</summary>

  ```
  What programming languages are used in this project?
  ```

  ```
  What frameworks and libraries does this project depend on? Can you explain what each major one does?
  ```

  ```
  What's the package.json/requirements.txt/build.gradle telling me about the dependencies?
  ```

</details>

If GitHub Copilot mentions any technologies you're unfamiliar with, don't hesitate to ask follow-up questions! Remember, GitHub Copilot Chat isn't just for understanding your specific codebase—it's your **onboarding buddy**, **technical sounding board**, and **intelligent search engine** all rolled into one. Click on **Sample Follow-up Prompts** below to expand the sample prompts.  

<details>
  <summary>Sample Follow-up Prompts</summary>

  ```
  Can you explain what [framework name] is and why it might be used in this type of project?
  ``` 

  ```
  What are the key benefits of using [library name] over other similar libraries?
  ``` 

  ```
  How does [technology name] work at a high level?
  ```
</details>

### 🎁 Optional Model Experimentation Challenge

Technical framework questions are great for comparing models - try asking about a complex technology stack with different available models to see different explanation styles! 

**Try This**: Pick one technology or framework from the project and ask about it using different available models. Try each of these three prompts and compare the responses.

1. "What is [technology] and how does it work?"
2. "Explain [technology] and its role in this project"
3. "Analyze the architectural benefits of using [technology] in this context"

**Questions to Consider:**
- Which model gave the most comprehensive explanation?
- Did any model provide unique insights the others missed?
- Which explanation style did you prefer and why?
- How did the depth of technical detail vary between models?


## 🔨 Step 4: Understanding the Build Process

Now let's figure out how to actually build and run this application.

### Instructions:

Ask GitHub Copilot how to build your codebase. If you get stuck, you can use the sample prompts below. By clicking on Sample Prompts below, it will expand and show the prompts.

<details>
  <summary>Sample Prompts</summary>

  ```
  How do I build this project? What are the build commands?
  ```

  ```
  What do I need to install or set up before I can run this project locally?
  ```

  ```
  Are there any environment variables or configuration I need to set up?
  ```

  ```
  How do I start the development server or run the application?
  ```

</details>

### ⚙️ Try It Yourself:
1. Follow the build instructions GitHub Copilot provided
2. Try to start the development server
3. If you encounter errors, ask GitHub Copilot for help troubleshooting

   ![](../../media/E2S4S3.png)

You can expand the Hints by clicking on it below.

<details>
  <summary>Hints</summary>

  You can build the project by [opening a terminal](https://code.visualstudio.com/docs/terminal/getting-started) in Visual Studio Code and running the following commands:

  ```
  cd eCommApp
  npm install
  npm run dev
  ```

  To open a terminal, from the top menu, click **Terminal (1)**, and then select **New Terminal (2)** to open a new terminal window.

   ![](../../media/new/a7-n.png)

</details>

Once you have the application running locally, you can explore its functionality in your web browser at `http://localhost:3000`. See how the website compares to the high-level description GitHub Copilot provided earlier! You can test basic features like browsing products, adding items to the cart, and checking out.

![](../../media/new/a5.png)

## 🧪 Step 5: Understanding the Testing Strategy

Testing is crucial for maintaining code quality. Let's explore what testing frameworks and practices are in place.

### Instructions:

Ask GitHub Copilot how the codebase is being tested. If you get stuck, you can use the sample prompts below. Click on **Sample Prompts** button to expand it. 

![](../../media/E2S5S1.png)

<details>
  <summary>Sample Prompts</summary>

  ```
  How do I run the tests for this project? What testing frameworks are being used?
  ```

  ```
  What types of tests exist in this codebase? (unit, integration, e2e, etc.)
  ```

  ```
  Can you analyze the test coverage? Are there areas that might need more testing?
  ```

  ```
  How are tests organized? Where should I put new tests?
  ```

</details>

### 📈 Extension: Test Coverage Deep Dive

**Advanced Prompts:**

```
Can you identify which files or functions have low or missing test coverage?
```

```
What would be good candidates for adding more tests to improve coverage?
```

## 🎁 Optional Task: Building a Better README

Now that you understand the project structure and setup process, let's use GitHub Copilot to improve the project documentation for future developers.

### Instructions:

1. Use GitHub Copilot to analyze the current README (if it exists) and suggest improvements. See the below sample prompts if you get stuck.
2. Create or enhance documentation based on your exploration.
3. Expand the few Sample prompts by clicking on **Sample Prompts** below.
   
<details>
  <summary>Sample Prompts</summary>

  ```
  Does this project have a README? If so, what's missing that would help new developers?
  ```

  ```
  Based on our conversation about this project, can you help me create a comprehensive "Quick Start Guide" for new developers? Include setup steps, key commands, and important files to know about.
  ```

  ```
  Can you suggest a better project description and feature list for the README based on the actual codebase?
  ```

</details>

### 💡 Pro Tips for README Enhancement:
- Include actual setup commands you've tested
- Add troubleshooting sections for common issues
- Document environment requirements and dependencies
- Include links to important files and folders
- Add examples of common development tasks

### 🔄 Iterative Improvement:
After GitHub Copilot generates documentation, you can refine it:

```
Can you make this setup guide more beginner-friendly?
```

```
Add a troubleshooting section for common setup issues.
```

```
Include examples of how to run different types of tests.
```

## 💡 Tips and Tricks

### 🤝 GitHub Copilot as Your Learning Partner

Think of GitHub Copilot Chat as having a knowledgeable senior developer sitting next to you who's always available to answer questions. You can ask about:

**Technology Fundamentals:**

```
What is React and why is it popular for web development?
```

```
Explain the difference between REST APIs and GraphQL.
```

```
What are the pros and cons of using TypeScript vs JavaScript?
```

**Best Practices & Patterns:**

```
What's the MVC pattern and how does it apply to web development?
```

```
When should I use async/await vs Promises in JavaScript?
```

```
What are some common security considerations for web applications?
```

**Troubleshooting & Problem Solving:**

```
I'm getting this error: [paste error message]. What does it mean and how can I fix it?
```

```
What's the difference between 500 and 404 HTTP status codes?
```

```
Why might my tests be failing intermittently?
```

### 💡 Pro Tips for Effective Learning with GitHub Copilot

1. **Ask "Why" Questions**: Don't just ask what something does—ask why it's used

    ```
    Why would a team choose Redux over React's built-in state management?
    ```

2. **Request Comparisons**: Understanding alternatives helps you make better decisions

    ```
    Compare Docker vs virtual machines - when would I use each?
    ```

3. **Get Context**: Ask how technologies fit into the bigger picture

    ```
    How does JWT authentication work in a typical web application flow?
    ```

4. **Seek Examples**: Request practical demonstrations

    ```
    Can you show me a simple example of how middleware works in Express.js?
    ```

### 🔍 Making the Most of Your AI Learning Buddy

**Start Broad, Then Go Deep:**
- Begin with general concepts: "What is containerization?"
- Then get specific: "How do I write a good Dockerfile for a Node.js app?"

**Don't Be Afraid to Ask "Dumb" Questions:**
- "What's the difference between a library and a framework?"
- "Why do developers use version control?"
- "What does 'full-stack' actually mean?"

**Use It as a Sanity Check:**
- "Does this approach make sense for solving [problem]?"
- "Am I overthinking this, or is there a simpler way?"
- "What are the potential downsides of this solution?"

Remember: Every expert was once a beginner. GitHub Copilot Chat gives you a judgment-free space to ask questions, explore concepts, and build your understanding at your own pace!


## 🏆 Exercise Wrap-up

Congratulations! You've successfully used GitHub Copilot Chat in Ask mode to:
- ✅ Understand the purpose and functionality of an unfamiliar codebase
- ✅ Analyze project structure and organization
- ✅ Identify technologies, frameworks, and dependencies
- ✅ Learn how to build, run, and test the application

### Reflection Questions:
1. How did using GitHub Copilot Chat change your approach to exploring a new codebase compared to manual exploration?
2. What types of questions were most effective for getting useful information?
3. Were there any areas where GitHub Copilot's explanations needed clarification or weren't accurate?
4. **Model Comparison**: Which AI models did you try, and what differences did you notice in their responses?
5. **Model Preferences**: Did you develop preferences for certain models for specific types of questions? Why?

### Key Takeaways:
- GitHub Copilot Chat can dramatically accelerate codebase onboarding
- Starting with high-level questions and drilling down works well
- Always verify critical build/setup instructions by actually trying them
- Use follow-up questions to deepen understanding of unfamiliar technologies
- **Different AI models excel at different tasks** - experimenting with multiple models gives you a more complete picture
- **Model selection strategy** can improve both the quality and speed of your development workflow

## 🚀 Next Steps

In the next exercise, we'll use what we've learned about the codebase to start improving test coverage and implementing new features for The Daily Harvest's e-commerce platform!

#### You have successfully completed the lab. Click on **Next >>** to continue to the next lab.

![](../../media/new/next.png)
