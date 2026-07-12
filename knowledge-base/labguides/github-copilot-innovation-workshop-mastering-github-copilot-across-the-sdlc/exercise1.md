# Exercise 1 - Lab Overview and Setup

#### Duration: 15 Minutes

## Overall Lab Objectives

This 4-hour hands-on lab is designed to give developers practical experience using **GitHub Copilot** as an AI-powered assistant throughout the Software Development Life Cycle (SDLC). You will explore how GitHub Copilot can improve developer productivity, code quality, and security—from feature planning and prototyping to implementation, code review, and remediation.

Through a series of guided, real-world exercises, you will learn how to:
- Understand GitHub Copilot’s role across all phases of the SDLC
- Plan new features and define success criteria with GitHub Copilot
- Use AI-powered code completions directly within the IDE
- Leverage GitHub Copilot Chat in Ask, Plan, and Agent modes
- Delegate tasks to the GitHub Copilot coding agent to multiply development impact
- Review code at scale using GitHub Copilot code reviews
- Detect and fix security vulnerabilities using GitHub Copilot Autofix
- Extend GitHub Copilot’s capabilities with Model Context Protocol (MCP) servers
- Optimize GitHub Copilot performance using Custom Instructions and Prompt Files

## Welcome to The Daily Harvest

🍎 **Your Mission: Develop your daily pick of fresh code!**

Congratulations! You've just been hired as a software developer at **The Daily Harvest**, an exciting new startup that's revolutionizing the way fresh fruit is sold. Your company specializes in creating websites that allow orchards to sell their products to those who will never drive to a store.

### Your Role

As a new developer on the team, you'll be working on extending the functionality of the website and ensuring that it is well-tested. The company has recently adopted **GitHub Copilot** as part of its development workflow, and you'll be learning how to leverage this AI-powered assistant to accelerate your productivity and code quality.

### The Challenge Ahead

Throughout this lab, you'll help The Daily Harvest tackle real development challenges:
- Understanding and navigating the existing codebase effectively
- Enhancing test coverage across critical application components
- Planning and implementing a robust shopping cart system for the e-commerce platform
- Maintaining high code quality standards across the development team
- Identifying and resolving security vulnerabilities

Your manager has emphasized that speed to market is crucial in the competitive fruit-selling space, but code quality and security cannot be compromised. This is where GitHub Copilot becomes your secret weapon—helping you write better code faster while maintaining the high standards that fruit lovers expect from The Daily Harvest.

Let's get started and grow some ripe code together! 🍊

## Logging into the Lab Environment

### Accessing Your Lab Environment
 
Once you're ready to dive in, your virtual machine and **Guide** will be right at your fingertips within your web browser.
   
![](../../media/lab-guide-updated.png)

### Virtual Machine & Lab Guide
 
Your virtual machine is your workhorse throughout the workshop. The lab guide is your roadmap to success.

### Exploring Your Lab Resources

To get a better understanding of your lab resources and credentials, navigate to the **Environment** tab.

![Manage Your Virtual Machine](../../media/gc1.png)

### Utilizing the Split Window Feature

For convenience, you can open the lab guide in a separate window by selecting the **Split Window** button from the top right corner.

![Use the Split Window Feature](../../media/new/split.png)

### Managing Your Virtual Machine

Feel free to **Start, Stop, or Restart (2)** your virtual machine as needed from the **Resources (1)** tab. Your experience is in your hands!

![Manage Your Virtual Machine](../../media/res-2801.png)

### Utilizing the Zoom In/Out Feature

To adjust the zoom level for the environment page, click the **A↕** icon located next to the timer in the lab environment.

![Use the Split Window Feature](../../media/new/zoom.png)

### Resize the Virtual Machine View

Use the **slider (three vertical dots)** located between the **Virtual Machine** and the **Lab Guide** panes to adjust the display size, allowing you to customize the layout based on your preference.

![](../../media/new/resize-vm-guide.png)

### Login to GitHub

1. In the **Lab VM**, open the **Microsoft Edge** browser from the desktop.

   ![](../../media/lab-vm-ms-edge.png)

1. Navigate to the **GitHub login** page by copying and pasting the following URL into the address bar:

   ```
   https://github.com/login
   ```

1. On the **Sign in to GitHub** tab, enter the provided **GitHub username** in the input field, and click on **Sign in with your identity provider** **(2)**.

    - Email/Username: <inject key="GitHub User Name" enableCopy="true"/> **(1)**

      ![](../../media/23-7-25-g1.png) 

1. Click on **Continue** on the **Single sign-on to CloudLabs Organizations** page to proceed.

   ![](../../media/23-7-25-g2.png)

1. You'll see the **Sign in** tab. Here, enter your Azure Entra credentials and click **Next (2)**.

   - **Email/Username:** <inject key="AzureAdUserEmail"></inject> **(1)**

     ![Enter Your Username](../../media/new/email.png)

1. Next, provide your Temporary Password and click on **Sign in (2)**

   - **Temporary Access Pass:** <inject key="AzureAdUserPassword"></inject> **(1)**

     ![Enter Your Password](../../media/new/pass.png)

1. On the **Stay Signed in?** pop-up, click on No.

   ![](../../media/new/stay.png)

1. You are now successfully logged in to **GitHub** and have been redirected to the **GitHub homepage**.

   ![](../../media/new/github-homepage.png)

### GitHub Copilot is moving to usage-based billing

Instead of counting premium requests, every Copilot plan will include a monthly allotment of **GitHub AI Credits**, with the option for paid plans to purchase additional usage. Usage will be calculated based on token consumption, including input, output, and cached tokens, using the listed API rates for each model.​

​**What's changing**

- Starting June 1, GitHub will replace Premium Request Units with GitHub AI Credits. ​
- Credits will be consumed based on actual AI token usage. ​
- Base pricing for all GitHub Copilot plans will remain unchanged. ​
- Code completions and Next Edit Suggestions will continue to be included at no extra cost. ​
- The fallback experience to lower-cost AI models will no longer be available after credits are exhausted. ​
- Copilot Code Review will also consume GitHub Actions minutes in addition to GitHub AI Credits.​

### GitHub Copilot Plan updates and AI Credit changes​

| Plan | Monthly Price | Included Monthly AI Credits | Key Update |
|:---|:---|:---|:---|
| **Copilot Pro** | $10/month | $10 AI Credits | Migrates to usage-based billing from June 1 |
| **Copilot Pro+** | $39/month | $39 AI Credits | Includes higher AI credit allocation |
| **Copilot Business** | $19/user/month | $19 AI Credits | Includes pooled organizational credits |
| **Copilot Enterprise** | $39/user/month | $39 AI Credits | Adds advanced budget and spending controls |

### Managing roles and governance via enterprise teams:

GitHub Enterprise Cloud has introduced new enterprise-level governance and management capabilities to help enterprises manage access, security, and policies at scale.

As of today, enterprise owners can use GitHub’s API or the enterprise settings UI to:

- Assign enterprise teams to organizations.
- Create and assign custom enterprise roles.
- Assign enterprise roles to both enterprise teams and users, including the new predefined Enterprise Security Manager role.
- Empower organization and repository owners to assign roles to enterprise teams within their scope.
- Assign enterprise teams and roles to ruleset bypass lists.

### Copilot Insights:

The Copilot usage metrics dashboard gives enterprise administrators and billing managers clear visibility into Copilot adoption and usage under the Insights tab.

These metrics help you understand:

- **Overall usage and adoption:** Review indicators like weekly usage provide a broad view of Copilot adoption across your enterprise.
- **Specific model, feature, and language usage:** See which AI models and programming languages are most utilized by your teams, highlighting areas for even greater value.
- **Agent adoption percentage:** Track how many developers are using Copilot for advanced tasks like refactoring, debugging, and complex problem solving. High agent adoption signals a shift toward truly transformative coding.

![](../../media/copilot-insights.png)

## Creating your Repository

1. Navigate to the **hol-copilot-lab** repository in a web browser.

   ```
   https://github.com/Coveros/hol-copilot-lab/tree/main
   ```

1. Click on the green **Use this template** button.

   ![](../../media/new/1.png)

1. You should see a repository creation form. Make the following selections :

   - **Include all branches:** Turn it **On (1)**

   - **Owner:** Select **Cloudlabs-Enterprises (2)**

   - **Repository name:** Enter the name **<inject key="GitHub User Name"  enableCopy="true"/> (3)**

   - **Visibility:** Choose **Internal (4)**.
   
   - Scroll down and then click **Create repository (5)**.
  
     ![](../../media/new/2.png)

     ![](../../media/new/3.png)

1. After a few moments, you should be taken to the home page of your newly-created repository and then click on **Code (1)** and copy the repository **URL (2)** and paste it into a notepad.

   ![](../../media/new/4-n.png)

## Setting up IDE

1. Open the **Visual Studio Code** shortcut from the desktop of your **Lab VM**.

   ![](../../media/new/vs.png)

1. Once the IDE opens, you will see a prompt to sign in to GitHub. Click **Continue without signing in** (you will sign in during the upcoming steps).

   ![](../../media/vsc-new-continue-without-signing-in.png)

1. When the color theme pop-up appears, select your preferred theme and click **Continue**.

   ![](../../media/vsc-new-colour-theme-continue.png)

1. When the Build with AI Agents pop-up appears, explore the available Copilot agents and features, then click **Get Started**.

   ![](../../media/build-ai-agents.png)

1. Under **Start**, click on the **Clone Git Repository...**.

   ![](../../media/new/Image_6.png)

1. **Paste (1)** the **URL** that you had copied earlier in the search bar at the top of the **Visual Studio Code** and select **Clone from URL (2)** option.

   ![](../../media/new/8-n.png)

1. Click on **New Folder** (1) to create a folder with name **odl-user-lab** (2) and then choose that folder and click on **Select as Repository Destination** (3). 

   ![](../../media/new/10.png)

1. If prompted with **Connect to GitHub** pop-up, click on **Sign in with your browser** under GitHub Sign in.
 
   ![](../../media/new/11.png)

1. Now, in the browser, click on **Authorize git-ecosystem**.

   ![](../../media/new/12.png)

1. Once you are logged in, you will get **Authentication Succeeded** message. You can now switch to IDE VS Code. 

   ![](../../media/new/13.png)

1. On VS Code, you will find a pop-up for confirmation **Would you like to open the repository?**, click on **Open**.

   ![](../../media/new/14.png)

1. If prompted a screen, **Do you trust the authors of the files in this folder?**. click on **Trust Folder & Continue**.

     ![](../../media/trust-folders.png)

1. To sign in to **GitHub Copilot**, follow the steps below:

   - In Visual Studio Code, click on the **Icon (1)** in the GitHub Copilot Chat panel located at the bottom-right corner of the window, and select **Use AI Features (2)**.

     ![](../../media/ghc-sign-in-new-1.png)

   - On the *Sign in to use GitHub Copilot* screen, select **Continue with GitHub** to sign in.
  
     ![](../../media/ghc-sign-in-to-use-ai-features-n.png)

   - Now, in the browser, click on **Continue** to Authorize Visual Studio Code. 

     ![](../../media/new/21.png)

   - On the next window, click on **Authrize Visual-Studio-Code**.

     ![](../../media/new/22a.png)

   - You will see a pop-up asking **This site is trying to open Visual Studio Code**. Enable the **CheckBox** (1) and then click on **Open** (2). It will take you to VS Code. 

     ![](../../media/auth-vs-code-open-n.png)

## Summary

In this lab, you successfully set up your development environment, logged into GitHub, created a new repository, and configured Visual Studio Code with GitHub Copilot. 

## Support Contact

The CloudLabs support team is available 24/7, 365 days a year, via email and live chat to ensure seamless assistance at any time. We offer dedicated support channels tailored specifically for both learners and instructors, ensuring that all your needs are promptly and efficiently addressed.

Learner Support Contacts:

- Email Support: cloudlabs-support@spektrasystems.com
- Live Chat Support: https://cloudlabs.ai/labs-support

#### You have successfully completed the lab. Click on **Next >>** to continue to the next lab.

![](../../media/new/next.png)
