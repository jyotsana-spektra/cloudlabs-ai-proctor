# Exercise 3: 🧩 Create Ontology

## Overall Duration:

## Overview:

In this section, you will build an **Ontology** from the previously created **Lakehouse** and **Eventhouse** with bound attributes to map datasets into governed entities and relationships. This forms the foundation for **Data Agents** and enables context-aware analytics across the enterprise.

## Lab Scenario:

After onboarding retail data into the Lakehouse and Eventhouse, Contoso Analytics is ready to transform raw data into business-understandable intelligence using Ontology IQ. The organization needs a semantic layer that captures how business entities, processes, and relationships interact across sales, customers, inventory, logistics, and operations. By generating a Fabric IQ Ontology, Contoso Analytics can establish a unified business model that enables intuitive data discovery, contextual understanding, and natural language insights. This ontology will serve as the foundation for AI-powered analytics by connecting data to real-world business concepts and relationships.

## Lab Objectives:

- Task 1: Generate ontology from package
- Task 2: Ontology Validation

## Task 1: Generate ontology from package

#### Step 1: Import notebook

1. Navigate to your **Fabric workspace**.

2. On the workspace homepage, click on the **Import** option.

3. From the available options, select **Notebook**. 

4. Choose **From this computer** as the source.

    ![](../../media/L2T1S13.png) 

5. Click on **Upload** to import the notebook.

    ![](../../media/L2T1S14.png) 

6. To browse the notebooks from your virtual machine, open File Explorer. Click on the address bar, type the path `C:\LabFiles\Notebooks`, then select the **Create Ontology from Package** notebook file and click on the **Open** button.

    ![](../../media/L3T1S3.png)

7. After upload, the notebook will be listed in the workspace area.

    ![](../../media/l3t1s7.png)

#### Step 2: Execute notebook

1. Click the **Create Ontology from Package** notebook from the list.

    ![](../../media/l3i.png)

2. Notebook will open in a different tab without binding with any datastore(Lakehouse)

    ![](../../media/l3s2s2.png) 

    > **Note:** Before proceeding, remove any unused or outdated Lakehouses that are already attached to the notebook. To do this, click the ellipsis (...) next to the Lakehouse name on the right side, and then select Remove.

    ![](../../media/l2note.png)

3. On the left side , in Explorer pane under **Data Items (1)** click **Add data items (2)** and select **From OneLake catalog (3)** to open OneLake areas.

     ![](../../media/l3s2s3.png)

4. Select above created Lakehouse and click **Add** to include in the notebook execution.

    ![](../../media/l3ii.png)

5. Now, selected **Lakehouse** will be bound with Notebook.

    ![](../../media/l3s2s4.png)

    >Now, we are good to run this notebook.

6. For the notebook configuration, please move to 2nd cell(Out of two cells) and replace the value for 
    ![Configuration](../../media/Configuration.png) 

    - ontology_item_name: `Provide Ontology Name(Unique)`
    - binding_lakehouse_name: `Lakehouse name created in last exercise`
    - binding_eventhouse_name: `Eventhouse name created in last exercise`
    - binding_eventhouse_cluster_uri: `Query URI copied from last exercise`
    - binding_eventhouse_database_name: `Database name from Eventhouse`

7. After configuration, click **Run all** button at top banner and execute entire notebook cell by cell.
    - First cell will install .whl file to execute all referenced files.
    - Second cell will execute ontology package to create **Ontology**

8. Below is the response from successful run

    ![](../../media/l3iii.png) 

9. Navigate to the workspace area to see the new Ontology created.

    ![](../../media/l3iv.png) 

10. Click **Retail_Ontology**. It will redirect to a different page to see its details.

    ![](../../media/onto.png) 

1. Select an entity to see it's details. Below Order is selected
     
    - Left area will hold all the entities binded from Lakehouse and Eventhouse
    - Middle area will provide relational view of each selected entity.

        ![](../../media/l3onto.png) 
    

## Task 2: Ontology Validation

1. To validate the entities and review their associated details, select any entity from the list. In the example below, the Product entity has been selected.

    ![](../../media/l3new.png)

2. Product entity build relationship with "Forecast" , "Inventory" , "Return" , "Promotion" , "ProductCategory" , "Orderline" , "DemandSignal" 

    ![](../../media/l3newi.png) 

3. Click **View Entity Type details (1)** from top banner.

    ![](../../media/l3newii.png) 

1. Click **Overview** from top banner to see the graph views

    ![](../../media/l3newiii.png)

4. Review the **Properties** to see all attributes details binded from Lakehouse(Static) and Eventhouse(Timeseries)

    ![](../../media/l3newiv.png) 

5. Click **Manage Property Bindings** to validate or edit both static and timeseries data bindings.

    ![](../../media/l3newv.png)

    ![](../../media/l3newvi.png)

    ![](../../media/l3newvii.png) 


## Summary 

In this exercise, you generated a Fabric IQ Ontology from the previously created Lakehouse and Eventhouse by executing a notebook-based workflow. The ontology transformed raw data into a business-centric semantic model by defining entities, attributes, relationships, and data bindings across retail domains such as customers, products, inventory, logistics, and operations. You then validated the ontology structure, entity relationships, and bindings to ensure that both batch and real-time data sources were correctly mapped. This ontology now serves as the foundation for context-aware analytics, natural language interactions, and AI-powered Data Agents within Microsoft Fabric.