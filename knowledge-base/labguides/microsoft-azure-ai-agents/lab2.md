# Lab 2: Build a Simple AI Agent

### Estimated Duration: 30 Minutes

## 📘 Scenario

Contoso Health Services receives frequent requests from employees and customers to compare health insurance plans. Manually reviewing and comparing plan information is time-consuming and inefficient.

In this lab, you will act as an AI Engineer and build a simple AI Agent capable of analyzing health plan data and generating bar chart visualizations to compare healthcare benefits, coverage, and costs.

## 📖 Overview

In this lab, you will learn how to build a simple AI Agent that processes data and generates a bar chart comparing different health benefit plans. This AI Agent leverages Azure AI services to analyze and visualize data efficiently.

## 🎯 Objective

In this lab, you will complete the following tasks:

- Task 1: Create a Simple AI Agent

## Task 1: Create a Simple AI Agent

In this task, you will build a simple AI Agent that processes data and generates a bar chart comparing different health benefit plans using Azure AI services for analysis and visualization.

1. Open the **Lab 2 - Create A Simple AI Agent.ipynb** file. This **Lab 2 - Create A Simple AI Agent.ipynb** notebook guides you through how to build a simple AI Agent that processes data and generates a bar chart comparing different health benefit plans.

   ![](./media/new/f6.png)

1. In the notebook interface, click **Select kernel (1)** in the top-right corner and choose **venv (Python 3.X.X) (2)** from the available options.

   ![](./media/L2T1S2-2904.png)

1. Run the first cell to import necessary libraries and load environment variables for working with Azure AI Projects. This setup enables secure authentication and interaction with Azure AI services.

   ![](./media/new/f7.png)

1. Run the next cell to create an AIProjectClient instance that connects to your Microsoft Foundry project using the project endpoint from environment variables and Azure token-based authentication. This establishes a secure programmatic connection to your project resources without hardcoding credentials.

   ![](./media/new/f8.png)

1. Run the next cell to create a **simple AI Agent** that processes data and generates a bar chart comparing different health benefit plans using Microsoft Foundry. This script initializes the AI agent, sends a prompt containing health plan data, and requests a bar chart. The agent processes the request, generates the chart, saves the image file, and then cleans up by deleting the agent.

   ![](./media/new/f9.png)

1. Observe the resulting output chart by opening the **health-plan-comparison.png** file. This visualizes the comparison of health benefit plans based on the input data.

   ![](./media/new/f10.png)

   ![](./media/new/f11.png)

   > **Note:** The following image is an example of the expected output. The appearance, including the colours, may vary depending on your environment.

## 🧾 Summary

In this lab, you accomplished the following:

- Built a simple AI Agent using Microsoft Foundry
- Configured and initialized the AIProjectClient using environment-based authentication
- Processed health plan data using the AI agent
- Generated a bar chart visualization comparing different health benefit plans
- Saved and reviewed the output visualization as an image file
- Demonstrated basic AI agent execution and result generation using Microsoft Foundry

### You have successfully completed the lab. Click **Next >>** to continue to the next lab.

   ![Start Your Azure Journey](./media/3-next.jpg)
