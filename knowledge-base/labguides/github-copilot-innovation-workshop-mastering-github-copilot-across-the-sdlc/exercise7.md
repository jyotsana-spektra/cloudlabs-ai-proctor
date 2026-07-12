# Exercise 7 - Leveraging Custom Instructions to Tailor Copilot’s Behavior​

#### Duration: 30 Minutes

## 🎯 Learning Objectives

By the end of this exercise, you will:

- Explain what custom instructions are and how they shape GitHub Copilot’s behavior.
- Enable custom instructions in this project.
- Use one custom instruction to plan a new feature.
- Use another to generate a GitHub Issue for that feature.
- Push the issue into the GitHub project using MCP.
- See how GitHub Copilot can be tailored to organizational workflows.

## 🍎 Scenario: Limiting Redundancy in The Daily Harvest's workflows

By now, things are running pretty smoothly at The Daily Harvest. Your team is utilizing GitHub Copilot to efficiently learn and develop new features and bug fixes, Coding Agent has been utilized for routine fixes and additions to free up developers' hands for more complex work, and MCPs have been integrated to ensure the information your team _and_ GitHub Copilot need is always available. However, amidst the productivity, you've noticed an issue that, while small at first, has become more noticeable with the most glaring improvements taken care of...

It began when you asked GitHub Copilot to spin up a new test suite for a customer support utility, and you received tests written using the Jest framework when your company uses Puppeteer. You later received functionality from GitHub Copilot that utilized the wrong version of an API for your payment processor.

You've begun to notice that every new context in which you utilize GitHub Copilot—new GitHub Copilot Chat threads, individual Issues assigned to Coding Agent, or using resources drawn from MCPs to create improved functionality—require you to regurgitate a copy-pasted list of do's and don'ts regarding style guides, package versions, and response formatting to ensure GitHub Copilot provides an answer that is not just functional but also correct for your organizational standards. There has to be a better way to ensure GitHub Copilot knows which rules to follow, and some diving into the internet leads you to a perfect solution: custom instructions files.

## 📄 Introduction to Custom Instructions

Custom Instructions Files are, unsurprisingly, files that can be created and stored at one of three levels:

1. Organization
2. Repository
3. Personal

While we are going to focus on repository-level custom instructions here, each has its own use case and they are all melded together when applicable for each individual prompt a user submits. When all three are utilized as context for a particular prompt, personal instructions take the highest priority, followed by repository instructions, with organization instructions prioritized last.

But what can these do? Using __natural language__, custom instruction files allow you to define information and rules that are prepended to every prompt within that context.  

<details>
  
  <summary>Repository Instructions support by environment</summary>
  
  <img width="731" height="503" alt="image" src="https://github.com/user-attachments/assets/43d8a28b-d9d7-4f79-97c4-2c905570bcfe" />

</details>

### A Rudimentary Example

Imagine that you have created a very simple `.github/copilot-instructions.md` file that reads,

```md
Begin every response with "Sure thing! Let me get on that."

End every response with "And that about does it."
```

What you will now see from GitHub Copilot, regardless of whether you are utilizing GitHub.com Copilot Chat, GitHub Copilot Chat in your IDE, or Coding Agent, is a response that looks like...

```md
Sure thing! Let me get on that.
...
---Answer to prompt---
...
And that about does it.
```

## ⚙️ Step 1: Enable custom instructions

Before we can begin utilizing custom instructions, we should first make sure they are enabled in our IDE.

__Instructions:__

1. In the **VS Code**, switch to the **Explorer** tab from the sidebar.

   ![](../../media/new/w1.png)

2. Open the Settings editor using:

   - **Linux/Windows** - Press the **`Ctrl`** key and the comma **`(,)`** key
   - **Mac** - Press the **`Cmd`** key and the comma **`(,)`** key

   ![](../../media/new/w3.png)

2. In the search box, search for **Instruction file (1)** and ensure the **Checkbox (2)** under **Use Instruction Files** is marked.

   ![](../../media/new/w2.png)

Great! With that, we should be ready to go building our first set of custom instructions.

## 📝 Step 2: Create a custom instructions file

In order to begin utilizing a custom instructions file, we must first create one. Perhaps we could utilize GitHub Copilot to generate its own guardrails...? 

__Instructions:__

1. Open the **Set Agent (1)** menu, and then select **Agent (2)** mode.

   ![](../../media/E4S2S1-n.png)

2. Click the **Settings (1)** icon in the upper-right portion of the Chat window, from the left pane, select the **Instructions (2)**. Then click on **Generate Instructions (3)**. A `/create-instructions` prompt will pop-up in the Chat window, ask the Copilot Agent to generate custom instructions for the application.

   ![](../../media/new/intstruction-gen.png)
   
   ![](../../media/new/create-instructions.png)

3. Watch GitHub Copilot analyze your repository and return a custom instructions file specifically catered to your environment.

4. Review the changes in the `github/instructions` folder.

5. In the Explorer pane, expand the **.github** folder and open the newly created `instructions.md` file to review the updated instructions by clicking on **Keep**.

   ![](../../media/new/new-instructions-file.png)

7. Take a moment to assess the results returned from GitHub Copilot. Are there any results you think are out of place? Are there any guidelines that you might not have previously considered for this kind of project?

## 💭 Step 3: Using the instructions file for feature planning

Now that we have custom instruction files ready to guide GitHub Copilot to greatness, we are going to utilise them to plan and push a feature issue up to GitHub.

__Instructions:__

1. Switch GitHub Copilot to **Ask** Mode, and ask how it would plan to develop a new feature of your choice. Did GitHub Copilot's response match or break any of the rules from the instructions file?

   ![](../../media/E7S3S1.png)

2. Switch back to **Agent** Mode, and ask GitHub Copilot to utilize the `create_issue` tool in the GitHub MCP Server to push an issue detailing that plan to your GitHub repository.

   ![](../../media/E4S2S1-n.png)

   > **Note:** You can use the following prompt in agent mode to create an issue.

   ```
   Ensure the issue follows all rules defined in the custom instructions file.
   Use the create_issue tool to create a GitHub issue for the feature plan you just described.
   ```

<details>
  
  <summary>`create_issue` Documentation</summary>
  
  <img width="551" height="266" alt="image" src="https://github.com/user-attachments/assets/dd0f8940-8ae5-484a-b62a-1491f064e99b" />

</details>

3. After **GitHub Copilot** has finished, navigate to the __Issues (1)__ tab in your repository. Do you see your **issue? (2)** If so, did it follow the guidelines established in your instructions file?

   ![](../../media/new/w9.png)

## 💪 Extra Credit: Going further beyond with custom prompt files and chat modes

### Prompt Files

With custom instruction files, we have discussed the ability to set effective, automatic guardrails for GitHub Copilot: for every response, here are the things it should know and here is how it should respond.

But what if we wanted to take our automation a step further and ask the same __question__ every time? That is where custom prompt files come in. Stored either locally for a particular user or in the repository within the `.github/prompts` directory, these are files which can be formatted to ensure multiple parameters are identical across uses:

- What __mode__ are you using?
- What __model__ (e.g., GPT, Claude, or Gemini) do you want this particular prompt to target?
- Are there any __tools__ you want this prompt to use (such as those pulled from an MCP Server)?
- What __description__ would you provide for the goal of this prompt? 

<details>
  
  <summary>A note about tool priority</summary>

  While we will be discussing chat modes more in a moment, it is important to understand how the tools specified in your custom prompt file may be prioritized against tools selected by other means. In short, the list of available tools is determined in the following priority order...

  1. Tools specified in the prompt file (if any)
  2. Tools from the referenced chat mode in the prompt file (if any)
  3. Default tools for the selected chat mode
  
</details>

With these optional values established, you can now define any prompt you would like. In addition to using natural language, we can include various parameters as a part of the prompt using a special `${variableName}` syntax:

- Workspace variables: `${workspaceFolder}`, `${workspaceFolderBasename}`
- Selection variables: `${selection}`, `${selectedText}`
- File context variables: `${file}`, `${fileBasename}`, `${fileDirname}`, `${fileBasenameNoExtension}`
- Input variables: `${input:variableName}`, `${input:variableName:placeholder} (pass values to the prompt from the chat input field)`

Finally, the format for our custom prompt files is:

```md
---
{header values, if applicable. For example...}
description: 'This is a test prompt'
---
{body, including any variables and the prompt itself} 
Workspace to target: ${workspaceFolder}
How to start each response: ${input:greeting}

Please begin your response with your assigned greeting.

Create a file named `test.txt` and write "Hello, world!" to that file
```

With this, we now have the building blocks to build a simple reusable prompt file of our own! 

__Instructions:__

1. In the **VS Code**, switch to the **Explorer** tab from the sidebar.

   ![](../../media/new/w1.png)

2. Open the Settings editor using **`Cmd`+`,` (Mac)** or **`Ctrl`+`,` (Linux/Windows)**.

   ![](../../media/new/w3.png)

3. In the search box, search for **Prompt files (1)** and ensure the **Value** is **true (2)**.

   ![](../../media/new/r2.png)

4. Click the **Settings (1)** icon in the upper-right portion of the Chat window, from the drop-down, select the **Prompts (2)**. Then click on **Generate Prompt (3)**. A `/create-prompt` prompt will pop-up in the Chat window, ask the Copilot Agent to generate a clear code explanation with examples.

   ![](../../media/new/prompt-instr.png)

   ![](../../media/new/create-prompt.png)

5. Watch GitHub Copilot analyze your repository and return a custom prompt file specifically catered to your environment.

6. Review the changes in the `github/prompts` folder.

5. In the Explorer pane, expand the **.github** folder and open the newly created `prompt.md` file to review the updated instructions by clicking on **Keep**.

   ![](../../media/new/new-prompt-file.png)

6. Take some time to create a custom prompt file that offers an explanation to the user about a code snippet that the user has input as part of the prompt. Consider the many components we have discussed above, although a sample has been provided below to give you some ideas if you are stuck

   <details>

   <summary>Example Prompt File</summary>

  
   ```md
   ---
   mode: 'agent'
   description: 'Generate a clear code explanation with examples'
   ---
    
   Explain the following code in a clear, beginner-friendly way:
    
   Code to explain: ${input:code:Paste your code here}
   Target audience: ${input:audience:Who is this explanation for? (e.g., beginners, intermediate developers, etc.)}
    
   Please provide:
    
   * A brief overview of what the code does
   * A step-by-step breakdown of the main parts
   * Explanation of any key concepts or terminology
   * A simple example showing how it works
   * Common use cases or when you might use this approach
    
   Use clear, simple language and avoid unnecessary jargon.
   ```
  
   </details>

7. To use the prompt, add the newly created prompt file as a context in the GitHub Copilot Chat window and
 ask the Copilot to implement it.

8. If applicable to your particular prompt file, you will see GitHub Copilot change its chat mode to whichever is specified and will, if necessary, ask you for inputs relative to the ones denoted in your reusable prompt. Provide those inputs, and see how GitHub Copilot continues responding to what you have requested in your file! 

### 🤖 Custom Agents

Custom agents enable you to configure the AI to adopt different personas tailored to specific development roles and tasks. For example, you might create agents for a security reviewer, planner, solution architect, or other specialized roles. Each persona can have its own behavior, available tools, and instructions.

You can also use handoffs to create guided workflows between agents, allowing you to transition seamlessly from one specialized agent to another with a single click. For example, you could move from planning agent directly into implementation agent, or hand off to a code reviewer with the relevant context.

#### What are custom agents?

The built-in agents provide general-purpose configurations for chat in VS Code. For a more tailored chat experience, you can create your own custom agents.

Custom agents consist of a set of instructions and tools that are applied when you switch to that agent. For example, a "Plan" agent could include instructions for generating an implementation plan and only use read-only tools. By creating a custom agent, you can quickly switch to that specific configuration without having to manually select relevant tools and instructions each time.

Custom agents are defined in a `.agent.md` Markdown file, and can be stored in your workspace for others to use, or in your user profile, where you can reuse them across different workspaces.

__Instructions:__

1. In your VS Code instance, ensure GitHub Copilot Chat is open

1. Click the **Settings (1)** icon in the upper-right portion of the Chat window, from the drop-down, select the **Agents (2)**. Then click on **Generate Agent (3)**. A `/create-agent` prompt will pop-up in the Chat window, ask the Copilot Agent to generate an implementation plan for new features or refactor the existing code.

   ![](../../media/new/agents-custom.png)

   ![](../../media/new/create-agent.png)

1. Watch GitHub Copilot analyze your repository and return a custom agent file specifically catered to your environment.

1. Review the changes in the `github/agents` folder.

1. In the Explorer pane, expand the **.github** folder and open the newly created `agent.md` file to review the updated instructions by clicking on **Keep**.

   ![](../../media/new/new-agent-file.png)

1. From this template, take a few minutes to build a custom agent that will plan out how to tackle new code changes

   <details>

   <summary>Example Chat Mode File</summary>

   ```md
   ---
   description: Generate an implementation plan for new features or refactoring existing code.
   name: Custom-Planning
   tools: ['fetch', 'githubRepo', 'search', 'usages']
   model: Claude Sonnet 4
   handoffs:
     - label: Implement Plan
       agent: agent
       prompt: Implement the plan outlined above.
       send: false
   ---
   
   # Planning mode instructions
   You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.
   Don't make any code edits, just generate a plan.
  
   The plan consists of a Markdown document that describes the implementation plan, including the following sections:
  
   * Overview: A brief description of the feature or refactoring task.
   * Requirements: A list of requirements for the feature or refactoring task.
   * Implementation Steps: A detailed list of steps to implement the feature or refactoring task.
   * Testing: A list of tests that need to be implemented to verify the feature or refactoring task.
   ```

   </details>

8. To use this custom agent, return to your **GitHub Copilot Chat** window. At the bottom, where your prompt is entered, click your currently selected **mode (1)** and in the drop-down list provided, choose **newly the created custom agent (2)**.

   ![](../../media/new/implementation-planner.png)

   >**Note**: The custom agent name generated in this step may differ based on the agent's response.

9. Now, write a prompt to GitHub Copilot using this new mode about a new feature you would like to implement, and see how your answer reflects the goals provided by the custom agent file you created

## 🏆 Exercise Wrap-up

In this exercise, we explored how to customize GitHub Copilot's behavior using custom agents and custom instruction files. By creating a specific custom agent for planning, we were able to guide Copilot's responses to better align with our needs for implementing new features or refactoring existing code.

### Reflection Questions

- A more limited feature utilizing custom instructions is the [path-specific custom instructions file](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions#creating-path-specific-custom-instructions-1). How might these be beneficial over more general repository instruction sets?
- What are some prompts you might be using in your daily workflow that can be consolidated into an instructions file?

### Key Takeaways

- Custom instruction files can be used to limit repetition in your prompts
- Custom instruction can both reinforce context and define response formats
- These files can be stored at different levels to enforce rules with different scopes

## 🎉 Conclusion

Congratulations! You have now completed all seven exercises in the GitHub Copilot Labs series. You should now have a solid understanding of how to leverage GitHub Copilot's various modes, tools, and customization options to enhance your development workflow. Keep experimenting with these features to discover new ways they can assist you in your coding journey!
