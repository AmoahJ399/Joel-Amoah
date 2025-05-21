import time
import random

class AIExperiment:
    def __init__(self, experiment_id, project_id, name, model_type, dataset_name, parameters):
        self.experiment_id = experiment_id
        self.project_id = project_id
        self.name = name
        self.model_type = model_type
        self.dataset_name = dataset_name
        self.parameters = parameters
        self.status = "Created"
        self.metrics = {}
        self.start_time = None
        self.end_time = None

    def run(self):
        self.status = "Running"
        self.start_time = datetime.datetime.now()
        print(f"--- Running Experiment '{self.name}' (ID: {self.experiment_id}) ---")
        print(f"Model Type: {self.model_type}, Dataset: {self.dataset_name}")
        print(f"Parameters: {self.parameters}")

        # Simulate AI training/processing
        time.sleep(random.uniform(2, 5)) # Simulate work

        # Simulate results
        if self.model_type == "classification":
            self.metrics["accuracy"] = random.uniform(0.75, 0.99)
            self.metrics["precision"] = random.uniform(0.70, 0.95)
        elif self.model_type == "regression":
            self.metrics["mae"] = random.uniform(0.1, 1.5)
            self.metrics["rmse"] = random.uniform(0.2, 2.0)
        else:
            self.metrics["dummy_score"] = random.uniform(0.5, 1.0)

        self.status = "Completed"
        self.end_time = datetime.datetime.now()
        print(f"Experiment '{self.name}' Completed. Results: {self.metrics}")
        print(f"Duration: {self.end_time - self.start_time}")

    def __str__(self):
        return (f"Experiment ID: {self.experiment_id}, Name: {self.name}, "
                f"Status: {self.status}, Model: {self.model_type}, "
                f"Metrics: {self.metrics if self.metrics else 'N/A'}")

class AIProject:
    def __init__(self, project_id, name, description):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.experiments = {} # experiment_id: AIExperiment object
        self.next_experiment_id = 1

    def create_experiment(self, name, model_type, dataset_name, parameters):
        experiment_id = f"E{self.next_experiment_id:04d}"
        experiment = AIExperiment(experiment_id, self.project_id, name, model_type, dataset_name, parameters)
        self.experiments[experiment_id] = experiment
        self.next_experiment_id += 1
        print(f"Experiment '{name}' created in project '{self.name}' with ID: {experiment_id}")
        return experiment_id

    def list_experiments(self):
        if not self.experiments:
            print(f"No experiments found for project '{self.name}'.")
            return
        print(f"\n--- Experiments in Project '{self.name}' (ID: {self.project_id}) ---")
        for exp_id, exp in self.experiments.items():
            print(exp)

    def __str__(self):
        return f"Project ID: {self.project_id}, Name: {self.name}, Description: {self.description}"

class AILabPlatform:
    def __init__(self):
        self.projects = {} # project_id: AIProject object
        self.next_project_id = 1

    def create_project(self, name, description):
        project_id = f"P{self.next_project_id:04d}"
        project = AIProject(project_id, name, description)
        self.projects[project_id] = project
        self.next_project_id += 1
        print(f"Project '{name}' created with ID: {project_id}")
        return project_id

    def get_project(self, project_id):
        return self.projects.get(project_id)

    def list_all_projects(self):
        print("\n--- All AI Projects ---")
        if not self.projects:
            print("No projects created yet.")
            return
        for proj_id, proj in self.projects.items():
            print(proj)

    def run_experiment(self, project_id, experiment_id):
        project = self.get_project(project_id)
        if not project:
            print(f"Error: Project with ID {project_id} not found.")
            return
        experiment = project.experiments.get(experiment_id)
        if not experiment:
            print(f"Error: Experiment with ID {experiment_id} not found in project {project_id}.")
            return
        experiment.run()

# --- How to use it (Basic CLI interaction) ---
if __name__ == "__main__":
    lab = AILabPlatform()

    while True:
        print("\n--- AI Lab Platform ---")
        print("1. Create Project")
        print("2. List All Projects")
        print("3. Select Project and Manage Experiments")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            lab.create_project(name, description)
        elif choice == '2':
            lab.list_all_projects()
        elif choice == '3':
            project_id = input("Enter Project ID to manage: ")
            current_project = lab.get_project(project_id)
            if not current_project:
                print("Project not found.")
                continue

            while True:
                print(f"\n--- Managing Project: '{current_project.name}' ---")
                print("1. Create New Experiment")
                print("2. List Experiments in this Project")
                print("3. Run an Experiment")
                print("4. Back to Main Menu")

                project_choice = input("Enter your choice: ")

                if project_choice == '1':
                    exp_name = input("Enter experiment name: ")
                    model_type = input("Enter model type (e.g., classification, regression): ")
                    dataset_name = input("Enter dataset name: ")
                    params_str = input("Enter parameters (e.g., learning_rate=0.01, epochs=10): ")
                    parameters = {}
                    for param_pair in params_str.split(','):
                        if '=' in param_pair:
                            key, value = param_pair.split('=', 1)
                            parameters[key.strip()] = value.strip()
                    current_project.create_experiment(exp_name, model_type, dataset_name, parameters)
                elif project_choice == '2':
                    current_project.list_experiments()
                elif project_choice == '3':
                    exp_id = input("Enter Experiment ID to run: ")
                    lab.run_experiment(current_project.project_id, exp_id)
                elif project_choice == '4':
                    print(f"Returning to main menu from project '{current_project.name}'.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '4':
            print("Exiting AI Lab Platform. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")