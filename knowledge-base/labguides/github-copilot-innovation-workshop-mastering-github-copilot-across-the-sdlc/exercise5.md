# Exercise 5 - Freeing Up Your Hands with Agentic Coding​

#### Duration: 45 Minutes

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Understand GitHub Copilot's Coding Agent and its autonomous capabilities
- Learn to create and assign GitHub issues to Copilot for autonomous implementation
- Experience the full autonomous development workflow from issue creation to pull request
- Monitor and interact with Copilot's development process through session logs
- Review and iterate on AI-generated code using pull request workflows
- Understand security, limitations, and best practices for coding agents

## 🍎 Scenario: Freeing Up Your Hands with Coding Agent

 The Daily Harvest is growing rapidly, but development bandwidth is becoming a bottleneck. Your manager has heard about GitHub Copilot's new Coding Agent—an autonomous AI developer that can work independently on GitHub issues, just like a human team member.

Today, you'll explore this revolutionary feature by:
- Creating GitHub issues for Daily Harvest's e-commerce improvements
- Assigning tasks directly to Copilot as you would to any team member
- Watching Copilot work autonomously in its own development environment
- Reviewing and iterating on Copilot's work through the standard pull request workflow

## ⌨️ Introduction to Coding Agent

Unlike the IDE modes of Ask and Agent, Coding Agent works within the GitHub.com user interface. Rather than engaging in a back-and-forth, iterative approach, utilizing Coding Agent involves delegating tasks to the agent, giving the agent time to work, then returning to see the results of GitHub Copilot's work.

Coding Agent can...
- Fix bugs
- Implement incremental new features
- Improve test coverage
- Update documentation
- Address technical debt

### GitHub Code Quality Review

![](../../media/gh-code-quality-review.png)

GitHub Code Quality turns every pull request into an opportunity to improve. With in-context findings, one-click Copilot fixes, and reliability and maintainability scores, you spend less time chasing nits and more time building. It’s there when you need it most, surfacing quality issues both in the pull request and the backlog so you can fix technical debt on your schedule.

- **One-click enablement:** Try GitHub Code Quality quickly and easily.
- **Actionable findings:** CodeQL-based quality rules detect maintainability and reliability issues in Java, C#, Python, JavaScript, Go, and Ruby.
- **Reviews in context:** See quality findings directly in the pull request with guidance you can immediately act on.
- **Track progress with quality scores:** Quality repository view groups findings by rule so you can prioritize fixes, while reliability and maintainability scores summarize their severity to help you target improvements.

### Custom Agents for GitHub Copilot

![](../../media/gh-custom-agents.png)

Custom agents for GitHub Copilot make it easy for users and organizations to specialize their Copilot coding agent (CCA) through simple, file-based configurations.

Anyone using GitHub Copilot can define and use custom agents, whether you’re an individual developer, part of a team, or managing an organization. Custom agents work across Copilot coding agent in GitHub.com, the Copilot CLI, and will be coming to a future release of Visual Studio Code.

- Define agent specializations that act like focused teammates, using prompts and tool selections unique to your workflow.
- Add organization-specific or team-specific agents by placing configuration files in a known location in your repository or organization settings.
- Refine agent behaviors beyond standard Copilot instructions, making it easier to enforce coding conventions, compliance, or custom automations.
- Enable agents to use custom tools and MCP servers, giving you fine-grained control over how tasks are completed.
- Get started quickly by adding a simple markdown file. There’s no need for a separate installation or complex setup.

## 📝 Step 1: Assign GitHub Copilot to an Issue

The first step in utilizing Coding Agent is to create a GitHub issue outlining a task you'd like completed.

### Instructions:

1. Navigate back to the **Microsoft Edge** tab where your GitHub repository is open, and click the **Issues** tab inside your repository.

   ![](../../media/new/c1.png)

2. Then, on the right-hand side of the screen, click **New Issue**.

   ![](../../media/new/c2.png)

3. For the new issue, add an appropriate **Title** and **Description** to add a **Contact Us** page to the application. Feel free to add any specific requirements or acceptance criteria you wish. A sample issue is shown below:

   ```
   ## User Story

   A user should be able to click a "Contact Us" button, displaying a form where a user can input their name, email, and a request.

   Below the request, a user should be able to press "Submit".

   When the user clicks "Submit", a pop-up will display the words "Thank you for your message." alongside a "Continue" button, and the entries for the submission form will be removed.
   ```

   ![](../../media/new/c3.png)

4. Click the **Settings (1)** icon in the Assignees section, select **Copilot (GitHub) (2)** from the list, and click anywhere on the screen.

   ![](../../media/new/c4.png)

5. In the pop-up window, ensure the target repository and base branch are both accurate, then click **Assign**.

   ![](../../media/new/c5-n.png)

6. Once completed, click on **Create** to create the issue.

   ![](../../media/new/c6.png)

### 🚀 How Coding Agent Works:

**1. Assignment & Activation:**
- Assign a GitHub issue to `@copilot` like any team member
- Copilot adds a 👀 emoji reaction to show it's working
- Spins up a secure GitHub Actions environment

**2. Autonomous Development:**
- Analyzes the codebase using advanced RAG (Retrieval Augmented Generation)
- Plans implementation approach
- Creates a new branch (always prefixed with `copilot/`)
- Writes and commits code incrementally

**3. Quality Assurance:**
- Runs existing tests and linters
- Creates new tests when appropriate
- Validates changes against repository standards
- Documents reasoning in commit messages

**4. Pull Request & Review:**
- Opens a draft pull request with detailed description
- Provides session logs showing decision-making process
- Requests review from the original issue assignor
- Responds to feedback and iterates based on comments

## 👀 Step 2: Monitor GitHub Copilot Coding Agent

Now that Copilot has eyes on the issue, let's follow along with its progress:

1. Wait for GitHub Copilot to add a `👀` reaction to the issue, indicating it has started working. 

   ![](../../media/new/c7.png)

2. Copilot will create a new **Pull Request (1)** to track its progress. Browse to the PR by clicking the **Link (2)** in the **Development** section of the issue sidebar or in the issue timeline. If the PR link is not yet available, wait a few moments and refresh the page.

   ![](../../media/new/c8.png)

3. Notice how the PR is marked as a **Draft**, indicating that work is still in progress. Copilot will set the description of the PR based off the issue details you provided.

   ![](../../media/new/c9.png)

4. While Copilot is working, you can monitor its progress by viewing the session logs by clicking the **View Session** button in the Pull Request timeline.

   ![](../../media/new/c11.png)

5. Here you can see all the steps Copilot is taking to address the issue, including code changes, test runs, and any challenges it encounters. It will behave similarly to how it does in the IDE, but without the need for your direct input. Feel free to check back on this page periodically to see new updates as Copilot works through the issue.

   ![](../../media/new/view-session-1.png)

   ![](../../media/new/contact-us-session-2.png)

6. Back in the Pull Request, you can also watch as Copilot updated the **PR description** with it's planned approach to solving the issue. As it progresses, it will mark off tasks in the description to indicate what has been completed.

   ![](../../media/new/c12.png)

7. Once Copilot has completed its work, you can scroll to the bottom of the Pull Request and press the **Ready for review (1)** button, click on **Merge pull request (2)** and select **Confirm merge (3)**. 

   ![](../../media/new/c14a.png)

   ![](../../media/new/c15a.png)

   ![](../../media/new/c16.png)

**Note:** Depending on the complexity of the issue, this process may take some time. Be patient as Copilot works through the task autonomously. Remember, normally you would be free to work on other tasks while Copilot handles this issue in the background. In the meantime, feel free to explore the optional tasks below.

## 🎁 Optional Task: Become Your Own Tech Lead

While Copilot is working autonomously on your first issue, this is the perfect time to experience what it's like to be a tech lead delegating tasks to your AI team member. Just as a tech lead would distribute work across their team, you can now assign different types of tasks to Copilot based on complexity and priority.

Try creating and assigning Copilot some additional issues while it works on the first one. Here are some ideas for issues you can create and assign:
- Improve the shopping cart to make it easier for users to adjust quantities of items
- Add a search bar to the product listing page
- Add categories to the product page to make it easier to find specific types of products
- Anything you think would improve the Daily Harvest e-commerce experience!

### Pro Tips for Effective Delegation:
- Be specific in your issue descriptions - clear requirements lead to better outcomes
- Set clear acceptance criteria in your issues
- You can even use Copilot to help plan out the tasks before assigning them

- Start with smaller, well-defined tasks before moving to complex features

This parallel workflow mimics real-world team dynamics where a tech lead can keep multiple developers busy with different priorities while focusing on higher-level architecture and planning decisions.

## 🎁 Optional Task: More ways of working with the GitHub Copilot Coding Agent

Now that you've seen how to assign an issue to Copilot, here are additional ways you can interact with Coding Agent. Feel free to pick one or more of the methods below to create and assign new tasks to Copilot.

### Agent Panel

The Agent Panel is a dedicated interface within the GitHub UI that allows you to manage and monitor your interactions with Coding Agent: 

1. Navigate to the Agent Panel at https://github.com/copilot/agents or click the Copilot icon on the top right on any GitHub page.

   ![](../../media/new/d1.png)

2. Select the appropriate **repository (2)** from the **dropdown (1)** menu.

   ![](../../media/new/d2.png)

3. Describe a new task for **Copilot** to work on in the text box provided.

   ![](../../media/new/d3.png)

4. After describing a new task, click **Start Task** button to assign the task to Copilot without needing to create a formal GitHub issue.

   ![](../../media/new/d4.png)

Additional details can be found in the [GitHub Docs](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr#asking-copilot-to-create-a-pull-request-from-the-agents-panel-or-page).

### Visual Studio Code

While you are working inside of Visual Studio Code, instead of writing TODOs comments in your codebase, you can hand off tasks to Copilot directly from your IDE:

1. Navigate back to **Visual Studio Code**.

1. Make sure you have the [GitHub Pull Request extension](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) installed in Visual Studio Code. 

1. If not, click on the **Extensions (1)** button from the left-hand pane, search for **GitHub Pull Request (2)** and **Install (3)** the extension.

   ![](../../media/new/d5.png)

1. Create a new terminal and run the commands below in the terminal. These Git commands configure your global Git identity:

   - `git config --global user.name` - Sets your Git username. This name appears in commit history.
   - `git config --global user.email` - Sets your Git email. This email is associated with your commits.

   These settings apply globally (to all Git repositories on your machine). They identify you as the author when you make commits.

   ```
   git config --global user.name "<inject key="GitHub User Name" enableCopy="true"/>"
   git config --global user.email "<inject key="AzureAdUserEmail"></inject>"
   ```

   ![](../../media/new/d9.png)

1. Use GitHub Copilot Chat to create a new task. Enter a clear and descriptive prompt in the chat panel to guide Copilot in generating or modifying code as needed. For example, you can prompt Copilot to **add a new feature to the application**.

1. Copilot will perform initial processing to gather context. Select the feature you want Copilot to implement, and it will begin working on the requested changes.
   

Additional details can be found in the [GitHub Docs](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr#asking-copilot-to-create-a-pull-request-from-copilot-chat-in-visual-studio-code).


### GitHub CLI

You can also use the GitHub CLI to manage development workflows such as creating issues, pull requests, and triggering workflows. However, Copilot-based code generation and task execution are currently performed through tools like Visual Studio Code and the GitHub web interface. Additional details can be found in the [GitHub Docs](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr#asking-copilot-to-create-a-pull-request-from-the-github-cli).

### Azure DevOps Work Items

If you are using Azure DevOps Boards to track work items, you can use GitHub Copilot to assist with implementing those tasks by generating and modifying code based on the work item requirements. Copilot is typically used within development environments such as Visual Studio Code. Additional details can be found in the [GitHub Blog](https://github.blog/changelog/2025-09-18-assign-azure-boards-work-items-to-copilot-coding-agent-in-public-preview/).

Even more ways to interact with Coding Agent can be found in the [GitHub Docs](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr).

## 🎁 Optional Task: Use GitHub Advanced Security + Copilot Autofix to fix a code vulnerability

So far, we've looked at utilizing Coding Agent to handle improved functionality. Now, we are going to see how it handles resolving security vulnerabilities.

### Turning on GitHub Advanced Security

Before having GitHub Copilot tackle some security flaws, we first need to enable GitHub Advanced Security.

**Instructions:**

1. At the top of your repository on GitHub, click the **Settings** tab (you may need to click the **More** dropdown option depending on your browser's width)

   ![](../../media/new/settings-1.png)

   ![](../../media/new/settings-2.png)

2. On the left navigation pane, scroll down to the *Security and quality* section, and then select **Advanced Security**.

   ![](../../media/gh-repo-settings-advanced-n.png)

3. Under Advanced Security, scroll to the bottom and **Enable** the **GitHub Advanced Security**.

   ![](../../media/new/d12.png)

4. In the pop-up confirming your desire to enable the feature, click **Enable GitHub Advanced Security for this repository**

   ![](../../media/new/d13.png)

5. Once the page refreshes, scroll down to the section labelled **Code Scanning**.

   ![](../../media/new/d15.png)

6. In the box titled **CodeQL Analysis**, click the **Set Up (1)** drop-down menu and choose **Default (2)**

   ![](../../media/new/d14.png)

7. At the bottom of the pop-up window that displays the scan details, click **Enable CodeQL**.

   ![](../../media/new/d16.png)

8. Verify that the confirmation message **Repository settings saved** is displayed, indicating that the configuration has been successfully applied.

   ![](../../media/new/d17.png)

### Combining the powers of GHAS and GitHub Copilot

With our repository scanned, we can now begin to utilize GitHub Copilot to resolve any unsavoury warnings we have received.

__Instructions:__

1. Click the **Security and quality (1)** tab from the top menu bar, under **Findings**, select **Code Scanning (2)**.

   ![](../../media/security-quality-code-scanning-n.png)

1. Click on the code scanning alert that has been generated by **GitHub Advanced Security** titled **DOM text reinterpreted as HTML**.

   ![](../../media/new/d21.png)

1. Take a moment to familiarize yourself with the Code scanning alert UI and to understand the current issue.

1. At the top of the page, below the title, notice the `Speed up the remediation of this alert with Copilot Autofix for CodeQL` text, and click **Generate Fix** button next to that text box.

   ![](../../media/new/d22.png)

1. Wait until **Copilot Autofix** finishes generating the fix suggestion for the detected security issue.

   ![](../../media/new/d23.png)

1. Once GitHub Copilot has generated a fix, scroll below the proposed change and click **Commit to a new branch**.

   ![](../../media/new/d25.png)

1. Select **Open a pull request (1)** and click **Commit change (2)** to commit the autofix to a new branch.

   ![](../../media/new/d24.png)

At this point, resolution of this vulnerability has moved into a similar workflow as with our other changes. It may be ready to submit as a Pull Request, where it will be reviewed and (hopefully) merged to keep your code base safe.

## 👀 Step 3: Review Copilot's Work

Once GitHub Copilot has completed work on your assigned issue, it's time to review the Pull Request it created. Just like with human developers, it's important to ensure that the code meets your team's standards and requirements.

**Instructions:**

1. Return to the **Pull Request** that Copilot created for the issue you assigned. From the top menu bar, click **Pull Requests (1)** and select your **PR (2)**.

   ![](../../media/new/e1.png)

2. Notice that Copilot has added a detailed **description** of the changes it made and likely has included screenshots of the implemented Contact Us page.

   ![](../../media/new/e2.png)

3. Review the code changes made by Copilot. Look for:

   - **Correctness:** Does the code function as intended?
   - **Quality:** Is the code clean, well-structured, and maintainable?
   - **Tests:** Are there sufficient tests covering the new functionality?

4. If you find any issues or areas for improvement, you can leave comments on the PR or specific lines of the code changes, just like you would in a regular code review. Make sure to tag `@copilot` in your comments so that Copilot is notified.

   ![](../../media/new/e3.png)

5. If you request changes, Copilot will re-open the session and work to address your feedback autonomously. You can monitor its progress through the session logs as before.

6. You can also even assign Copilot to review its own Pull Request (or any other PR in the repository) by adding `Copilot` as a reviewer on the PR. Copilot will analyze the code changes and provide feedback or suggest improvements. See the [GitHub Docs](https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review) for more details.

   ![](../../media/new/e4.png)

6. Once you are satisfied with the changes, approve the Pull Request and merge it into the main branch.

### Scaling Security with Copilot Autofix

Copilot Autofix isn't just for fixing individual vulnerabilities - it can help your organization pay down security debt at scale:

- **Security Campaigns**: Use [security campaigns](https://docs.github.com/enterprise-cloud@latest/code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns) to address vulnerabilities across multiple repositories in your organization, with Copilot Autofix helping to generate fixes automatically
- **Pull Request Integration**: Automatically [triage and fix vulnerabilities in pull requests](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/triaging-code-scanning-alerts-in-pull-requests#working-with-copilot-autofix-suggestions-for-alerts-on-a-pull-request) before they're merged, stopping new security issues before they enter your codebase

## 🏆 Exercise Wrap-up

Congratulations! You've successfully used GitHub Copilot Coding Agent to autonomously implement new functionality in a codebase. You've experienced the full workflow from issue creation to code review, gaining insight into how AI can augment your development process.

### Reflection Questions:
1. What types of tasks will you delegate to the Coding Agent in your projects?
2. When reviewing Copilot's work, what stood out as particularly well done? What areas could use improvement?
3. Should GitHub Copilot be the only reviewer on a Pull Request? If so, what are the trade-offs of foregoing human reviewers? If not, how might you supplement your current review process with Coding Agent?
4. Which method of assigning tasks to Copilot did you find most convenient or effective?
5. How does using Copilot autofix for security vulnerabilities compare to traditional methods of remediation?

## Key Takeaways:

### 🎯 Coding Agent as Your AI Team Member
- **Treat Copilot like a developer**: Assign issues with clear requirements, acceptance criteria, and context just as you would for any team member
- **Leverage autonomous work**: Copilot can work independently while you focus on other tasks, truly scaling your development capacity
- **Multiple assignment methods**: Use GitHub Issues, Agent Panel, VS Code, or CLI - choose what fits your workflow best

### 🔄 Quality Assurance & Review Process
- **Code review remains essential**: Even AI-generated code benefits from human oversight for correctness, maintainability, and alignment with project goals
- **Iterative improvement**: Copilot responds to feedback and can refine its work based on your comments, creating a collaborative development loop
- **Transparent decision-making**: Session logs provide visibility into Copilot's reasoning and approach, helping you understand and trust the process

### 🚀 Scaling Development Workflows  
- **Tech lead mindset**: Delegate multiple tasks across different complexity levels while maintaining oversight and architectural decisions
- **Security integration**: Copilot Autofix seamlessly integrates vulnerability remediation into your existing security workflows
- **Standard GitHub processes**: All work flows through familiar pull request workflows, maintaining your team's existing review and approval processes

### 💡 Best Practices for Success
- **Be specific in requirements**: Clear, detailed issue descriptions lead to better implementation outcomes
- **Start small and scale up**: Begin with well-defined tasks before moving to complex features
- **Combine human and AI review**: Use both Copilot's automated review capabilities and human oversight for comprehensive code quality
- **Monitor and guide**: While Copilot works autonomously, periodic check-ins help ensure alignment with your goals

## 🔮 Coming Up Next:

In Exercise 6, we'll take a look at bringing additional context to GitHub Copilot through the use of **MCP Servers** to provide new functionality and information to smooth out your workflows.

#### You have successfully completed the lab. Click on **Next >>** to continue to the next lab.

![](../../media/new/next.png)
