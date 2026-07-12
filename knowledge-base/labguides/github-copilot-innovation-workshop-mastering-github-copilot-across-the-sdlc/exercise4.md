# Exercise 4 - GitHub Copilot Agent Mode: Goal-Oriented Development

#### Duration: 45 Minutes

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Understand what GitHub Copilot Agent mode is and when to use it
- Learn how Agent mode differs from Chat
- Experience how Agent mode autonomously makes changes across multiple files
- Use Agent mode to achieve a specific, measurable goal (80%+ code coverage)
- Observe and understand Agent mode's decision-making process
- Apply best practices for delegating complex tasks to AI agents

## 🤖 What is GitHub Copilot Agent Mode?

GitHub Copilot Agent mode represents a significant evolution in AI-assisted development. Unlike Chat mode (conversational), **Agent mode operates autonomously to achieve larger, goal-oriented tasks**.

### Key Features:
- 🎯 **Goal-Oriented**: Works toward specific, measurable objectives
- 🔄 **Autonomous Operation**: Makes decisions and changes without constant guidance  
- 📁 **Multi-File Awareness**: Understands and modifies multiple files simultaneously
- 🧠 **Advanced Models**: Leverages premium AI models for complex reasoning
- 📊 **Progress Tracking**: Monitors and reports progress toward goals
- 🔍 **Context Understanding**: Maintains awareness of project structure and dependencies

### When to Use Agent Mode:
- ✅ Large refactoring tasks across multiple files
- ✅ Implementing complete features end-to-end
- ✅ Achieving specific metrics (coverage, performance, security)
- ✅ Complex code migrations or upgrades
- ✅ Comprehensive documentation generation

### 💰 Billing Considerations

GitHub Copilot uses an AI Credits consumption model for premium AI experiences, advanced models, and agentic workflows.

AI Credit consumption varies depending on factors such as:

- The AI model selected for the request
- The size of the prompt and context provided
- The amount of generated output
- The complexity and duration of the task being performed

Different models may consume AI Credits at different rates. Some models and experiences included with your Copilot plan may have minimal or no additional AI Credit consumption, while premium models and advanced capabilities may consume credits based on usage.

When using Copilot Chat or Agent Mode, GitHub Copilot may perform multiple actions to complete a task, such as analyzing code, searching repositories, generating changes, updating files, or creating pull requests. These actions are handled automatically as part of the overall interaction.

Organizations can monitor AI Credit consumption, configure spending controls, and manage usage through GitHub's administrative and billing features.

### Agent HQ: Centralized Control for Every AI Agent:

![](../../media/agent-hq.png)

Agent HQ addresses the fragmentation in today’s AI tooling by bringing AI agents directly into the GitHub workflow developers already trust. With AI now an integral part of development and most new developers using Copilot from day one, GitHub is making agents native, secure, and seamless—not bolted on. Agent HQ transforms GitHub into an open, agent-powered platform, enabling developers to work with multiple specialized agents in parallel. All of this happens within the familiar GitHub experience, using existing tools and subscriptions.

- A single hub for AI agents built directly into GitHub
- An open ecosystem with agents from OpenAI, Anthropic, Google, Cognition, xAI, and more
- Works with familiar GitHub primitives such as Git, pull requests, issues, and Actions
- Enables parallel, agent-driven workflows for complex tasks
- Available through your existing GitHub Copilot subscription, with no workflow disruption

## 🍎 Scenario: Boosting The Daily Harvest's Test Coverage

After your excellent work in Exercise 3 writing unit tests, your team lead at The Daily Harvest has assigned you a critical pre-release task: **achieve 80% or higher code coverage across the entire project**.

The challenge? There are multiple components, utilities, and modules that need comprehensive testing. Manually identifying and writing tests for each uncovered area would take a lot of work. This is the perfect scenario for GitHub Copilot Agent mode!

### Your Mission:
Use Agent mode to automatically:
- 🔍 Analyze the current codebase and identify coverage gaps
- 📝 Generate comprehensive test suites for uncovered code
- 🎯 Achieve the 80% coverage target efficiently
- 📊 Ensure all new tests follow project conventions and pass

## 🚀 Step 1: Assessing Current Coverage

Before we delegate to the Agent, let's understand our starting point.

### Instructions:

1. **Run the existing test suite** to see current coverage (make sure you're in the **eCommApp** directory first):
   ```bash
   npm run test:coverage
   ```

2. **Review the coverage report** that displays in the terminal. Note:
   - Overall coverage percentage
   - Which files have low coverage
   - Which lines are uncovered

3. **Note** the current coverage percentage - you'll compare this to the final result!

## 🤖 Step 2: Activating Agent Mode

Now let's put the Agent to work on our coverage goal.

### Instructions:

1. Switch to **Agent (2)** mode in **GitHub Copilot Chat** by selecting **Set Agent (1)** from the dropdown underneath the prompt text area.

   ![](../../media/E4S2S1-n.png)

2. **Provide your goal-oriented prompt** (example below):

   ![](../../media/E4S2S2.png)
   
<details>
<summary>Sample Agent Prompt</summary>

```
I need you to help me achieve 80% code coverage for The Daily Harvest project. Please:

1. Analyze the current test coverage across all files
2. Identify components, functions, and modules that lack adequate testing
3. Generate comprehensive unit tests for uncovered code paths
4. Ensure all new tests follow the existing testing patterns and conventions
5. Make sure all tests pass and actually improve coverage
6. Continue working until we reach at least 80% overall coverage

Please work autonomously and let me know your progress as you go. Focus on business logic, utility functions, and React components first.
```

</details>

3. **Submit the prompt** and let the Agent begin working.

## 👀 Step 3: Observing Agent Mode in Action

This is where Agent mode truly shines! Watch as it works autonomously, **behaving like a real developer** working toward your goal.

### What You'll Observe:

**🔍 Analysis Phase:**

- Agent examines your project structure like a developer would
- Identifies files with low/no test coverage by analyzing existing tests
- Plans its testing strategy and prioritizes high-impact areas
- Reviews existing code patterns to maintain consistency

**⚡ Execution Phase:**

- Creates new test files or enhances existing ones across multiple components
- **Runs tests automatically** to verify its work (you may see permission prompts)
- Writes tests for multiple components simultaneously with awareness of dependencies
- Makes real-time adjustments based on test results and builds feedback

**🔧 Self-Healing Capabilities:**

- **Automatically fixes build failures** it encounters during development
- **Resolves test failures** by analyzing error messages and adjusting code
- **Handles dependency issues** by installing missing packages or adjusting imports
- **Iterates on solutions** when initial attempts don't work, just like a human developer would

**📊 Progress Reporting:**

- Updates you on coverage improvements with specific metrics
- Reports any issues or blockers it encounters and how it's addressing them
- Suggests additional areas that need attention based on its analysis
- Shows you its decision-making process and next steps

### Instructions:

1. **Monitor the Agent's work** - don't interrupt unless there's an error
   - If GitHub Copilot times out, simply restart the analysis

   - Click **Allow** when prompted - the Agent will ask permission before running tests or terminal commands for safety

     ![](../../media/new/b3.png)

     ![](../../media/new/b4.png)

   - You might need to press `Ctrl+C` to stop the test execution process before the Agent continues working

2. **Watch the file explorer** - you'll see new test files being created in real-time

   ![](../../media/new/b34.png)

3. **Check the Agent's status updates** - it will report progress toward the 80% goal with detailed feedback

4. **Note the multi-file coordination** - observe how it handles dependencies between tests and maintains project consistency

5. **Observe the self-healing** - watch how it responds to and fixes any build or test failures it encounters

6. **You're always in control** - remember that you can:
   - **Review all changes** before accepting them
   - **Keep or discard individual files** the Agent creates
   - **Easily undo the work** using Git if the Agent misses the mark or goes in the wrong direction
   - **Guide the Agent** with additional instructions if needed

Additional information can be found in the [GitHub Copilot Agent Mode blog post](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/) and the [Visual Studio Code Documentation](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode).


## 🔧 Step 4: Reviewing and Refining Agent Results

The Agent will work toward the 80% goal, but you should review its work.

### Instructions:

1. **Run coverage again** to verify the improvement:
   ```bash
   npm test -- --coverage
   ```

2. **Compare before/after results:**
   - Starting coverage: ____%
   - Final coverage: ____%
   - Goal achieved? ✅/❌

3. **Review the generated tests:**
   - Open a few of the new test files
   - Check if they follow your project's testing patterns
   - Verify test quality and comprehensiveness

4. **If coverage is still below 80%**, ask the Agent to continue:
    <details>
    <summary>Sample Agent Prompt</summary>

    ```
    Current coverage is at X%. Please continue working to reach our 80% goal. Focus on the remaining uncovered areas.
    ```

    </details>

## 🎯 Step 5: Understanding Agent Decision-Making

Let's gain insight into how the Agent approached this complex task.

### Instructions:

**Ask the Agent to explain its strategy:**
<details>
<summary>Sample Agent Prompt</summary>

```
Can you explain your approach to achieving the code coverage goal? What was your strategy for:
- Prioritizing which files to test first
- Deciding what types of tests to write
- Handling dependencies between different components
- Ensuring tests followed our project conventions
```

</details>

**Follow up with specific questions about its decisions:**
<details>
<summary>Sample Agent Prompt</summary>

```
What were the biggest challenges you encountered while working toward the 80% coverage goal? How did you handle edge cases or complex components?
```

</details>


## 🎓 Best Practices for Agent Mode

Based on this exercise, here are the key practices for effective Agent usage:

### ✅ Do:

- **Set clear, measurable goals** (like "80% coverage")
- **Provide context** about project conventions and requirements
- **Let the Agent work autonomously** - avoid micro-managing
- **Review results** before considering the task complete
- **Ask for explanations** to understand the Agent's reasoning

### ❌ Don't:

- **Interrupt frequently** - let the Agent complete its work cycles  
- **Give vague instructions** - be specific about desired outcomes
- **Skip verification** - always test that the Agent's work achieves your goal
- **Ignore errors** - address any issues the Agent reports

## 🚀 Real-World Applications

Consider how you might use Agent mode in your actual development work:

**🏢 Enterprise Scenarios:**
- Legacy code modernization across hundreds of files
- Implementing comprehensive security scanning and fixes
- Migrating entire codebases to new frameworks or standards
- Achieving compliance requirements (accessibility, security, performance)

**🚀 Startup Scenarios:**  
- Rapidly implementing MVPs with proper test coverage
- Scaling applications while maintaining code quality
- Adding comprehensive error handling and monitoring
- Preparing codebases for production deployment

## 🏆 Exercise Wrap-up

Congratulations! You've successfully used GitHub Copilot Chat in Agent mode to achieve a complex, goal-oriented development task.

### Reflection Questions:

1. What surprised you most about Agent mode's capabilities?
2. How would Agent mode change your approach to large refactoring tasks?
3. What types of development goals would you delegate to Agent mode in real projects?
4. How did the Agent's autonomous approach compare to your manual development process?
5. Which mode of GitHub Copilot (Autocomplete, Chat, Agent) do you find most useful for different scenarios?

### Key Takeaways:

- Agent mode is particularly effective for complex, multi-file tasks that require a high level of coordination and autonomy.
- Setting clear goals and providing context are crucial for maximizing the effectiveness of Agent mode.
- Reviewing and validating the output of Agent mode is essential to ensure quality and adherence to project standards.

## 🔮 What's Next?

In Exercise 5, we'll take things further by exploring how GitHub Copilot Coding Agent can work autonomously in the background to assist with your coding tasks directly from a GitHub Issue. 

#### You have successfully completed the lab. Click on **Next >>** to continue to the next lab.

![](../../media/new/next.png)
