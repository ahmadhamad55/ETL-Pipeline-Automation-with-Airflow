# ETL-Pipeline-Automation-with-Airflow
<img src="https://github.com/ahmadhamad55/ETL-Pipeline-Automation-with-Airflow/blob/main/Apacheflow.png" alt="Image Description" width="500">

### English version 
In this challenge, I successfully automated an ETL (Extract, Transform, Load) pipeline using Airflow. The objective was to read a CSV file, perform the necessary transformations, and save it as a JSON file. I implemented the pipeline within the Airflow framework, allowing for frequent and scheduled execution based on the cron format.
To accomplish this, I followed the following steps:

1. Copying the CSV Data: I copied the CSV data file to a desired location where the ETL pipeline could access it.

2. Writing the ETL Code: I created a new Python file and wrote the code for the ETL process. I defined a function that would read the CSV file, print the data along with some statistics, check for null values, and fill them as needed.

3. Saving Amended Data as JSON: Within the ETL function, I wrote the amended data as a JSON file in the desired location.

4. Reading and Printing the JSON Data: I implemented another function to read the saved JSON file and print the data for validation purposes.

5. Defining the DAG: Using Airflow, I defined a Directed Acyclic Graph (DAG) that consisted of two Python operators, one for each function: the ETL function and the data printing function.

6. Running the DAG and Observing Logs: I executed the DAG in Airflow and monitored the logs to ensure the successful execution of the ETL pipeline.

### French version 
Dans ce défi, j'ai automatisé avec succès un pipeline ETL (Extract, Transform, Load) en utilisant Airflow. L'objectif était de lire un fichier CSV, effectuer les transformations nécessaires et le sauvegarder au format JSON. J'ai mis en œuvre le pipeline dans le cadre d'Airflow, ce qui permet une exécution fréquente et planifiée basée sur le format cron.

Pour y parvenir, j'ai suivi les étapes suivantes :

1. Copie des données CSV : J'ai copié le fichier de données CSV dans l'emplacement souhaité où le pipeline ETL pouvait y accéder.

2. Écriture du code ETL : J'ai créé un nouveau fichier Python et écrit le code pour le processus ETL. J'ai défini une fonction qui lisait le fichier CSV, affichait les données ainsi que quelques statistiques, vérifiait les valeurs nulles et les remplissait si nécessaire.

3. Sauvegarde des données amendées au format JSON : Au sein de la fonction ETL, j'ai écrit les données modifiées au format JSON dans l'emplacement souhaité.

4. Lecture et affichage des données JSON : J'ai mis en place une autre fonction pour lire le fichier JSON sauvegardé et afficher les données à des fins de validation.

5. Définition du DAG : À l'aide d'Airflow, j'ai défini un graphe acyclique dirigé (DAG) qui se composait de deux opérateurs Python, un pour chaque fonction : la fonction ETL et la fonction d'affichage des données.

6. Exécution du DAG et observation des journaux : J'ai exécuté le DAG dans Airflow et surveillé les journaux pour m'assurer de l'exécution réussie du pipeline ETL.
