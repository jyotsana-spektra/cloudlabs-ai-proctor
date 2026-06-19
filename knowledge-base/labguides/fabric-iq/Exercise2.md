# Exercise 2: Generate Ontology Data

## Overall Duration:

## Overview:

In this section, you will create a Fabric **Lakehouse** and a **Eventhouse** and integrates batch and real-time data into a unified platform. The Lakehouse scalable storage and the Eventhouse processes streaming data enables **Ontology IQ** to understand business entities, metrics, and relationships for intelligent AI-driven analytics.

## Lab Scenario:

After establishing the dedicated Fabric IQ workspace, Contoso Analytics begins onboarding enterprise data into the platform. Data from multiple business and operational systems is ingested and consolidated to create a unified foundation for analytics and AI-driven insights. The data sources include:

Store Inventory Systems
Online Sales Platforms
Campaign Management Systems
Historical Stock-out Data

All ingested data is centralized in Microsoft OneLake within the Fabric IQ environment, eliminating data silos and providing a trusted data foundation for downstream analytics, knowledge discovery, and intelligent decision-making.

## Lab Objectives

- Task 1: Building a Lakehouse   
- Task 2: Building an Eventhouse
- Task 3: Loading data into Lakehouse and Eventhouse

## Task 1: Building a Lakehouse
In this task of the workshop, you will be creating a Lakehouse.

1. From the left menu bar, select the workspace **FabricWorkspace<inject key="Deployment ID" enableCopy="false"/> (2)** from **Workspaces (1)**

    ![](../../media/L2T1S1.png)
   
2. Click on **+ New item (1)**, search for **Lakehouse (2)**, and select **Lakehouse (3)** from the results.

    ![](../../media/L2T1S2.png)

3. In the **New Lakehouse** pop-up, enter the following and click on **Create (4)**. 

      - Name: **Retail_Lakehouse (1)**

        ``` 
        Retail_Lakehouse
        ```
      - Location: **FabricWorkspace<inject key="Deployment ID" enableCopy="false"/> (2)** workspace
      - Lakehouse schemas: **checked (3)**

        ![](../../media/L2T1S3.png)
    
5. Wait for the Lakehouse to be successfully provisioned.

6. Once created, the Lakehouse will open automatically.

7. Verify the following components are available:

    - **Tables** section
    - **Files** section

        ![](../../media/L2T1S4.png)

        >**Note:** Both Tables and Files section is empty.

8. To upload files, click **ellipsis** in Files section. Mouseover the **Upload** option and click **Upload files** option. It will open a right pane at right side to upload files.

    ![](../../media/aa.png)

    ![](../../media/L2T1S5.png)

    >**Note:** If you don't see the ellipse ,hover in right side of Files

9. **Click** folder icon at right side to open and choose file path.

    ![](../../media/L2T1S6.png)

10. To browse the files from your virtual machine, open File Explorer. Click on the address bar, type the path `C:\Labfiles\Ontology`.

    ![](../../media/L2T1S7.png)

11. Select all files from this folder and click **Upload**

    - **retail_ontology_package.iq** 
    - **fabriciq_ontology_accelerator-0.1.0-py3-none-any.whl**
    - **Zava Black Friday Return Policy**

        ![](../../media/L2T1S8.png)

12. **Close (2)** the upload window once these files uploaded **(1)**.

    ![](../../media/l2t1i.png)

13. Now, the **Files** section of the Lakehouse has all three files. 

    ![](../../media/l2t1ii.png)

1. Hover over **retail_ontology_package.iq.zip** file and click on ellipse.

    ![](../../media/ren1.png)

1. Select the **Rename** option.

    ![](../../media/ren2.png)

1. Rename the file as given and click on **Rename (2)**

    ```
    retail_ontology_package.iq
    ```
    ![](../../media/ren3.png)

#### Understanding the Uploaded Files

> **Note:** 
> - `retail_ontology_package.iq` is a ZIP-based package. The `.iq` extension is added so the Fabric IQ workflow can recognize it as an ontology package. It contains structured definition of ontology to bind source static  data for the **Lakehouse**, and time-series operational data that will later be loaded into the **Eventhouse**.
> - `fabriciq_ontology_accelerator-0.1.0-py3-none-any.whl` is a Python helper library used within the notebook workflow to process the ontology package and generate data in the Lakehouse and Warehouse. It provides the necessary execution logic to read the package and load the data accordingly.

**What is inside `retail_ontology_package.iq`?**

The package is organized into four folders: `instance_data`, `events_data`, `definition`, and `binding`.

- **`instance_data`:** Holds data files which contains the batch and transactional retail data that are loaded into the **Lakehouse**. For our lab, we have considered below entities:
  
  - `carriers.csv`: Stores logistics provider details; used to track shipping partners, delivery performance, and transportation assignments.
  - `customers.csv`: Contains customer profiles; supports segmentation, behavior analysis, personalization, and customer-centric reporting.
  - `demand_signals.csv`: Captures batch data on demand indicators; used for trend detection, demand spikes, and responsive supply chain decisions.
  - `forecasts.csv`: Stores predicted demand values; enables planning, budgeting, and comparison against actual sales performance.
  - `inventories.csv`: Tracks stock levels across locations; supports replenishment, stock optimization, and inventory availability analysis.
  - `orders.csv`: Stores customer transaction records; enables revenue tracking, order lifecycle monitoring, and sales analytics.
  - `order_lines.csv`: Contains individual items within orders; used for detailed sales, pricing, and product-level analysis.
  - `product_categories.csv`: Defines product groupings; supports hierarchical classification, category-level reporting, and assortment analysis.
  - `products.csv`: Holds product details; enables performance tracking, pricing analysis, and inventory-product relationships.
  - `promotions.csv`: Stores campaign and discount data; supports effectiveness analysis, uplift measurement, and marketing optimization.
  - `regions.csv`: Defines geographic hierarchies; enables regional performance analysis and location-based business insights.
  - `returns.csv`: Tracks returned items; supports return rate analysis, quality issues identification, and reverse logistics.
  - `shipments.csv`: Stores shipment records; enables delivery tracking, fulfillment analysis, and logistics performance monitoring.
  - `stores.csv`: Contains retail store details; supports store-level performance, operations analysis, and location-based insights.
  - `warehouses.csv`: Stores warehouse information; supports storage management, inventory distribution, and supply chain optimization.

- **`events_data/`** : Holds data files which contains the real-time (Timeseries) data that are loaded into the **Eventhouse**. For our lab, we have considered below entities:
  - `carriers.csv`: Captures real-time logistics provider updates; monitors delivery status, transit delays, and carrier performance across active shipments.
  - `customers.csv`: Streams customer interactions and activities; supports real-time personalization, behavioral tracking, and dynamic engagement insights.
  - `demand_signals.csv`: Captures live demand events; enables immediate detection of demand spikes, trends, and rapid supply chain adjustments.
  - `forecasts.csv`: Continuously updated demand predictions; integrates real-time signals to refine forecasting accuracy and support dynamic planning decisions.
  - `inventories.csv`: Tracks real-time stock levels; enables instant visibility into availability, replenishment needs, and inventory movement across locations.
  - `products.csv`: Maintains product activity data; supports real-time tracking of performance, availability, and demand-driven product insights.
  - `regions.csv`: Represents geographic performance streams; enables real-time regional analysis, trend monitoring, and location-based decision-making insights.
  - `shipments.csv`: Tracks live shipment movements; provides real-time visibility into delivery progress, delays, and fulfillment execution.
  - `stores.csv`: Captures real-time store operations; monitors sales activity, inventory changes, and in-store performance continuously.

- **`definition/`**: Holds entity definition and its relationship details.
  - `entity_types.csv`: Capture both batch and real-time entities and its attributes along with identity and time series column
  - `relationship_types.csv`: Defines the logical relationships between entity types. 

- **`binding/`**: Holds entity binding and its relationship which is required to build Ontology.
  - `binding_entity_types.csv`: Maps ontology properties to the physical source tables and columns in the Lakehouse or Eventhouse, including time-series binding details. 
  - `binding_relationship_types.csv`: Maps ontology relationships to the source tables and join keys used to connect entities. 

> In summary, the `.iq` file provides the **business model and packaged sample data**, while the `.whl` file provides the parametrized **execution logic** that processes that package and loads data into Fabric services. 

## Task 2: Building an Eventhouse  

1. Follow the above steps to navigate and choose the appropriate Fabric Workspace.
2. Click **New Item** to create Eventhouse.

    ![](../../media/L2T1S1.png)

3. Provide Eventhouse name and click the **Create** button to create the Eventhouse

    ```
    Retail_Eventhouse
    ```

    ![](../../media/L2T1S10.png)

4. Wait for a few moments for the Eventhouse to be created. Once created, you will be redirect to the dashboard. KQL database will be created by default.

    ![](../../media/L2T1S11.png)

    >**Note:** Currently we have empty database

5. Please Navigate to the right side to locate **Eventhouse Details**, copy the **Query URI**, and note down the **Eventhouse Name** and **Database Name** and paste them in Notepad, keeping all three details safe for use in the next exercises.

    ![](../../media/L2T1S12.png)

    > **Note:** The Eventhouse Name is the name you provided while creating the Eventhouse, and the Database Name is the same as the Eventhouse name by default.

## Task 3: Loading data into Lakehouse and Eventhouse

#### Step 1: Import notebook 
1. Navigate to your **Fabric workspace**.

2. On the workspace homepage, click on the **Import** option.

3. From the available options, select **Notebook**. 

4. Choose **From this computer** as the source.

    ![](../../media/L2T1S13.png)


5. Click on **Upload** to import the notebook.

    ![](../../media/L2T1S14.png)

6. To browse the notebooks from your virtual machine, open File Explorer. Click on the address bar, type the path `C:\Labfiles\Notebooks` **(1)**, then select the **Generate Ontology Data (2)** notebook file and click on the **Open (3)** button.

     ![](../../media/L2T1S15.png) 


7. After upload, notebook will be listed in the workspace area.

    ![](../../media/L2T1S16.png) 

#### Step 2: Execute notebook

1. Click **Generate Ontology Data** notebook from the list.
  
    ![](../../media/L2T1S17.png)
  

2. Notebook will open in a different tab without binding with any datastore(Lakehouse)

    ![](../../media/L2T1S18I.png)

    > **Note:** Before proceeding, remove any unused or outdated Lakehouses that are already attached to the notebook. To do this, click the ellipsis (...) next to the Lakehouse name on the right side, and then select Remove.

    ![](../../media/l2note.png)

3. Click **Add data items** and select **From OneLake catalog** to open OneLake areas.

    ![](../../media/L2T1S18.png)

4. Select above created Lakehouse and click **Add** to include in the notebook execution.

    ![](../../media/L2T1S19.png)

5. Now, selected **Lakehouse** will be bound with Notebook.

    ![BindLakehouse](../../media/BindLakehouse.png) 

    >Now, we are good to run this notebook.

6. For the notebook configuration, please move to last cell(Create kusto tables) and replace the value for **eventhouse_cluster_uri** and **eventhouse_database** copied earlier in Notepad in Task 2.

    ![](../../media/L2T1S21.png) 

7. After configuration, click **Run all** button at top banner and execute entire notebook cell by cell.
    - First cell will install .whl file to execute all referenced files.
    - Second cell will execute ontology package and load data in the Lakehouse

        ![](../../media/L2T1S22.png)

    - Third and last cell will load data in the Eventhouse.

        ![](../../media/L2T1S23.png) 

8. Wait for the execution to complete successfully.

9. Let's validate both Lakehouse and Eventhouse whether data is loaded or not.

10. Navigate to the Lakehouse that was created earlier by going to the Fabric workspace you created under Workspaces in the left pane and verify that the data is successfully loaded. 

    ![](../../media/L2T1S24.png)

11. Go to the **Tables** section
   and Click on the three dots (⋯) menu and select **Refresh** to load all table under **dbo** schema.

    ![](../../media/L2T1S25.png) 

12. Verify that Tables are created automatically
    
    ![](../../media/L2T1S26.png)

13. Navigate to the Eventhouse that was created earlier and verify that the data is successfully loaded. 

    ![](../../media/L2T1S27.png)

14. Refresh Eventhouse database to see all **real time tables**.

    ![](../../media/L2T1S28.png)

## Summary

In this exercise, you created a Lakehouse and an Eventhouse within the Microsoft Fabric workspace to establish the foundation for Fabric IQ data processing. You uploaded the ontology package and supporting accelerator library, which provide the business model, sample data, and execution logic required for ontology generation. Using a notebook, you loaded both batch and real-time retail data into the Lakehouse and Eventhouse, respectively. Finally, you validated that the data was successfully populated, ensuring that the environment is ready for ontology creation, knowledge discovery, and AI-driven analytics in subsequent exercises.