# 06-run-pytorch-data.py
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig
from azureml.core import Dataset

if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')
 
    experiment = Experiment(workspace=ws, name='day1-experiment-train-wine')

    config = ScriptRunConfig(
        source_directory='./src',
        script='wine-model.py',
        compute_target='cpu-cluster',
        
    )
    # set up pytorch environment
    env = Environment.from_conda_specification(
        name='sklearn-env-aml',
        file_path='./.azureml/sklearn-env-aml.yml'
    )
    config.run_config.environment = env

    run = experiment.submit(config)
    aml_url = run.get_portal_url()
    print("Submitted to compute cluster. Click link below")
    print("")
    print(aml_url)