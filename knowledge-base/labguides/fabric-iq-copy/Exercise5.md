# Exercise 5: ⚡ Create Operations Agent

## Overall Duration:

## Overview:

In this section of the workshop, you will create an **Operations Agent** pointing to Eventhouse.

## Scenario: 

As Contoso Analytics expands its Fabric IQ implementation, business leaders require visibility into operational events as they happen. The organization wants to move beyond historical reporting and enable proactive decision-making based on real-time business activity. To achieve this, Contoso Analytics integrates streaming inventory and sales data into an Eventhouse and deploys an Operations Agent capable of continuously monitoring operational metrics. By combining real-time event data with intelligent monitoring, the organization can identify emerging risks, detect anomalies, and respond to inventory and demand fluctuations before they impact business performance.

## Lab Objectives: 
  
- Task 1: Create Operations Agent (Fabric IQ)
- Task 2: Observe agent behavior in real-time 
- Task 3: Ingest Data into Forecast Table

## Task 1: Create Operations Agent (Fabric IQ)
1. Select Fabric Workspace and click **New Item**.
2. In the search box type **Opertion** keyword to get Operation Agent. Click **Operation Agent**.

    ![](../../media/l5i.png)

3. New popup window will apear. Provide Operation Agent name and select workspace in the Location section. Click **Create**.

    ![](../../media/l5ii.png)

4. After create, Operation Agent will load its blank play area. 

    ![](../../media/l5iii.png)

5. Opertion Agent has sections like **Business goal**, **Agent instructions**, **Knowledge**, **Action**. Right side we have **Agent playbook** area.

6. Provide **Business goal** for RTI.

    ```
   Enable proactive, AI-driven sales intelligence to:
    - Detect low-confidence and unreliable forecasts
    - Identify sudden demand spikes or drops
    - Ensure timely and accurate forecast availability
    - Support proactive inventory and supply planning
   ```
    ![](../../media/l5iv.png)

7. Provide **Agent instuction** which agent will follow all the instructions and take action.

    ```
    Objective:
    Monitor the forecasts table in Eventhouse to evaluate forecast accuracy, detect anomalies in demand        predictions, and track forecast confidence.
    Provide structured alerts with recommended actions.
 
    Knowledge Data Source:
    Database: Retail_EventHouse
    Table: forecasts
    Columns: fcst_id, fcst_units, fcst_amt, fcst_conf_pct, ts
 
    Monitoring Logic:
       IF fcst_conf_pct < 0.15 THEN
           Classify the Risk Level as "Critical" and Generate immediate alert and Indicate "Low Confidence Forecast"
       IF fcst_conf_pct < 0.70 THEN
           Classify the Risk Level as "High Risk" and Generate immediate alert and Indicate "Average Confidence Forecast"
       IF none of the above conditions met  THEN
            Classify the Risk Level as "Normal" and do not generate any alert 
       CONTINUE Monitoring
     Alert Requirements:
     For each Critical, High Risk, or High Opportunity event, send alert including:
        fcst_id
        fcst_units
        fcst_amt
        fcst_conf_pct
        Risk Level    
        Alert Message (e.g., forecase low confidence / Sales Spike / No Activity)

    ```
    ![](../../media/l5v.png)

8. If instruction length is bigger then hold & drag bottom right corner to expand the window. So that, all instruction can be visible.

9. Add knowledge base in the **Knowledge** section. Click **Add data**.

    ![](../../media/l5vi.png)

10. Chose **Eventhouse** and click **Add** to add in the knowledge section

    ![](../../media/l5vii.png)

    After add we can see knowledge base.
    
    ![KQLDatabase](../../media/OA-KB-KQLDatabase.png)


## Task 2: Observe agent behavior in real-time

1. Creating **Custom Action** with clicking **Add action**

    ![](../../media/l5viii.png)

2. Now action creation popup will appear to include **action name** and **copy the below description** (It's mandatory and any short description you can provide). Also, user can pass parameter for explicit specification while taking action. Click **Create** to create custom action.

    ![](../../media/l5ix.png)

    ```
    Inventory action is a custom action. While action required. Activator will trigger this action to send message/email to the authorized operation team.
    ```

4. Now, custom action will be created for operation agent.

    ![](../../media/l5x.png)

5. Scroll to the right of the newly created Action and select **Connect** to configure.

    ![](../../media/l5xi.png)

6. In the Worskpace dropdown, select **workspacename**.

7. Select the **Activator** dropdown, then **Create a new item**.

8. In the New item name field, enter `Forecast_Activator`, and then select **Create Activator** and then click on **Create a connection.**

    ![](../../media/l5xii.png)

9. Select **Copy** to the right of the connection string, and paste it in safe place

10. Select **Open flow builder**.

     ![](../../media/l5xiii.png)

     >[!Alert] If you see an error that the flow could not load, wait a few minutes and then attempt to reload the page.

11. On the box labeled When an activator rule is triggered, select **Invalid parameters**

    ![](../../media/l5xiv.png)

12. Enter the **connection string (1)** copied in previously and On the same flyout, select **Change Connection (2)**.

    ![](../../media/l5xv.png)

14. On the Change connection flyout, select **Add new**, and then select **Sign in**.

    ![](../../media/l5xvi.png)

    ![](../../media/l5xvii.png)

15. Select your user account **Username**

    ![](../../media/l5xviii.png)


16. Select the **+** plus sign under the existing box

	![](../../media/l5xix.png)


17. In the Add an action search bar enter `Teams`

18. Next to Microsoft Teams, select **See more** to display all available choices.

	![](../../media/l5xx.png)


19. Select **Post message in a chat or channel**.

	![](../../media/l5xxi.png)


20. On the Create connection flyout, select **Sign in**.

    ![OPAgent12.png](../../media/OPAgent12.png)

21. Select you user account **Username**

    ![OPAgent13.png](../../media/OPAgent13.png)

22. On the Post message in a chat or channel flyout, select the following options:

    | Object | Value |
    | -------- | -------- |
    | Post as | **Flow bot** |
    | Post in | **Chat with Flow bot** |
    | Recipient | `Username` |
    | Message | `Hi Mark, as per your advice, we have increased the stock count for the product.` |

23. On the upper-right side of the bar's menu, select **Save**.

     ![](../../media/l5a.png)

     >**Note:** If you face any error in saving the workflow click on **Sign up for 90 days free trial**

     ![](../../media/l5b.png)

     >Click on Start Trial

     ![](../../media/l5c.png)

24. Return to the **Fabric tab in your browser**.

25. Select **Apply**

     ![](../../media/l5e.png)

    >**Note:** If the apply button is not available to select, wait for the status to change to Connected.

26. Select **Generate playbook** to regenerate the playbook.

	![](../../media/l5f.png)

    ![](../../media/l5g.png)

27. Review the playbook, and then select **Save**.

    ![](../../media/l5h.png)

28. Start the Operation Agent.

    ![](../../media/l5i0.png)

29. Open Microsoft Teams by creating a new tab in your Edge browser and type +++**https://teams.microsoft.com/v2/?skipauthstrap=1**+++ and press **Enter** on your laptop keyboard to navigate to the Microsoft Teams application.

30. Activate the **Fabric Operations Agent** by going to **Apps** in the Microsoft Teams left pane, searching for **“Fabric Operations Agent”**.

    ![](../../media/l5j.png)

31. Click on **Add**.

    ![](../../media/l5k.png)

32. Click on **Open** to launch the Fabric Operation Agent card in your Teams environment..

    ![](../../media/l5l.png)

#### Steps to Process Streaming Data and Validate Anomalies

1. Nagivate back to the Fabric workspace **workspace**. and Open KQL database **Retail_Eventhouse** .

    ![](../../media/l5m.png)

2. Select your database **Retail_Eventhous** and click on **KQL Queryset**. 

    ![](../../media/l5n.png)

   > **Note:** If any pop-up window appears, please close it.

    ![](../../media/l5o.png)

3. **Remove** any pre-existing queries from the editor.

    ![](../../media/l5p.png)

## Task 3: Ingest Data into Forecast Table

1. **Copy (1)** the below code and **Run (2)** the following KQL command to ingest data into the **forecasts** table:

   ![](../../media/l5q.png)

     ```kql
     .ingest inline into table forecasts <|
     "FCST000627", 60, 75.25, 0.10, datetime(2025-12-30T10:50:00)
     "FCST000626", 55, 66.5, 0.00, datetime(2026-01-30T10:50:00)
     
     ```

2. In the same **KQL Queryset **editor, **Copy (1)** the below code and select only below code and **Run (2)** the query to validate the data (3):
    ```
    forecasts
    | where ingestion_time() > ago(5m)
    
    ```
    ![](../../media/l5r.png)

3. Navigate back to your **Microsoft Teams** tab.

4. **Open** the chats **Fabric Operation Agent**, you should see **alert messages** displaying forecast results, including **low confidence anomaly alerts** generated by the **Operation Agent**.

5. Click on **Yes** to proceed with the recommended action.

    ![](../../media/l5s.png)
6. The inventory action was **successfully** initiated using the provided parameters.

    ![](../../media/l5t.png)

We successfully ingested streaming **forecast** data into Eventhouse and verified that the data was being processed in real time. The **Operation Agent** continuously monitored this **streaming** data and **automatically** detected anomalies, including the test record with low confidence that was intentionally introduced for validation.  As part of this process, the agent generated real-time alerts directly in **Microsoft Teams**, enabling immediate visibility into issues without **manual monitoring**.
The solution also demonstrated how the **Operation Agent** provides recommended actions, such as triggering an inventory operation, allowing users to respond quickly and take corrective steps.  Overall, this end-to-end workflow—from streaming data ingestion to **anomaly** **detection**, **alerting**, and **action** execution—shows how Operation Agents enable real-time intelligence and automated decision-making within a business scenario.

### **Summary** 


This lab demonstrates how **Microsoft Fabric IQ acts as an end-to-end intelligence layer**, transforming fragmented enterprise data into **trusted, business-aware insights** using a unified platform.

Using the **Zava Retail scenario**, the lab highlights how organizations move from **siloed systems and inconsistent reporting** to a **centralized, governed intelligence foundation**. Zava faces common challenges such as disconnected data across systems, slow decision-making, and lack of consistent business metrics.

To address these issues, Fabric integrates:

- **Lakehouse** (batch data)
- **Eventhouse** (real-time data)
- **Ontology** (business model)

These components are unified within **OneLake**, enabling centralized data storage, governance, and analytics.

At the core of this transformation is **Fabric IQ**, which introduces a **shared business language** by modeling data into:

- Entities (e.g., Store, Product, Inventory)
- Relationships
- Real-time operational signals

This shifts analytics from technical structures (tables and SQL) to **meaningful business context**, understandable by both humans and AI.

The lab also showcases:

- **Real-Time Intelligence (RTI)**  
- **Operations Monitoring Agents**

These capabilities track live events, detect anomalies (such as inventory shortages), and enable **proactive decision-making**.

In the final stage, **Fabric Data Agents** connect to the ontology, allowing users to:

- Ask **natural language questions**
- Receive **accurate, explainable insights**

These insights are fully grounded in the business model.

## Key Outcome

The lab demonstrates how organizations evolve from:

**Raw Data → Unified Intelligence → Actionable Insights**

This enables **consistent, trusted decision-making** across all personas—from data engineers and analysts to executive leadership.