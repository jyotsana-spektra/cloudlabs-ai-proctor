# Exercise 1: Create a Workspace for Fabric IQ

### Estimated Duration: 

## Overview:

A dedicated **Microsoft Fabric** workspace is established to serve as the centralized foundation for all **Fabric IQ** capabilities, enabling seamless integration of data, analytics, and AI-driven insights. This workspace is configured with appropriate capacity, governance, and role-based access to support secure and scalable operations.

## Lab Scenario: 

Contoso Analytics wants to enable Fabric IQ to enhance knowledge discovery and AI-driven insights across its data estate. To support this initiative, the organization needs a dedicated Microsoft Fabric environment with the required tenant settings and governance controls in place. A centralized workspace will be created to securely host and manage Fabric IQ artifacts. This workspace will provide a scalable foundation for collaboration, data exploration, and intelligent analytics across the organization.

## Lab Objectives:

You will be able to complete the following tasks:

- Task 1: Configure Microsoft Fabric Tenant Settings for Fabric IQ
- Task 2: Create a Fabric Workspace 

## Task 1: Configure Microsoft Fabric Tenant Settings for Fabric IQ

Using a web browser of your choice, please navigate to this Microsoft Fabric link.

1. On the **Lab VM**, open **Microsoft Edge** from the desktop.

   ![](../../media/L1T1S1.png)
   
1. Open **Microsoft Fabric** by entering the link below in your browser.

      ```
      https://app.fabric.microsoft.com
      ```

1. On the **"Enter your email, we'll check if you need to create a new account."** screen, enter the below email and click **Submit (2)** to proceed with signing in. 

   * **Email/Username:** <inject key="AzureAdUserEmail"></inject> **(1)**

      ![](../../media/L1T2S2.png)

1. Enter the following temporary access pass and click on **Sign in (2)**.

   * **Temporary Access Pass:** <inject key="AzureAdUserPassword"></inject> **(1)**

      ![](../../media/L1T1S3.png)

1. On the **Stay signed in?** pop-up, click **No**.

   ![](../../media/L1T1S4.png)

1. On the **Welcome to the Fabric view** window, click on **Cancel**.

   ![](../../media/L1T1S5.png)

1. On the **Microsoft Fabric (Free) license assigned** pop-up, click **OK**.

   ![](../../media/L1T1S6.png)

1. Once signed in, click on **Power BI (1)** in the bottom-left corner and then select **Fabric (2)** from the menu.

   ![](../../media/L1T1S7.png)

   ![](../../media/L1T1S8.png)

1. In the Fabric window, click on Settings icon.

   ![](../../media/set1.png)

1. In the **Settings (1)** pane, go to **Admin Portal (2)**

   ![](../../media/set2.png)

1. Select **Tenant Settings (1)** and go to **Microsoft Fabric (2)**

   ![](../../media/set3.png)

1. In Microsoft Fabric, expand the **Users can create Ontology (preview) items (1)**, switch the option to **Enabled (2)**, and then select **Apply (3)** to save the changes.

   ![](../../media/set4.png)

1. Repeat Step 12 for :

   - **User can create Graph (preview)**
   - **Enable Operation agents (preview)** 

      ![](../../media/set5.png)

1. Scroll down and go to **Internal Settings (1)**, Select **Allow XMLA endpoints and Analyze in Excel with on premises semantic models (2)** and toggle on **Enabled (3)** then click on **Apply (4)**

   ![](../../media/set6.png)

## Task 2: Create a Fabric Workspace

1. You should be able to find a **New Workspace** tile near the top-left area of the screen. Select it to open the **Create a workspace** blade on the right side.
   
   ![](../../media/L1T1S14.png)

2. Create a new workspace named **Fabricworkspace-<inject key="Deployment ID" enableCopy="false"/> (1)**

   ![](../../media/L1T1S16.png)

3. Select **Advanced** and scroll down to see the License mode options and the selected capacity.
   
   ![](../../media/L1T1S17.png)

4. After you scroll down, make sure that License mode is set to **Fabric** and that Capacity is set to an available option and then click on **Apply**
   
   ![](../../media/L1T1S18.png)

6. On the **Introducing task flows (preview)** pop-up, click **Got it**.

   ![](../../media/L1T1S19.png)

## Summary

In this exercise, you configured the required Microsoft Fabric tenant settings to support Fabric IQ capabilities, including enabling Ontology items, Operation Agents, and XMLA endpoint access. You then created a dedicated Microsoft Fabric workspace with the appropriate license mode and capacity configuration. The workspace serves as a secure and governed environment for hosting and managing Fabric IQ artifacts, providing a scalable foundation for AI-driven insights, collaboration, and data exploration.
