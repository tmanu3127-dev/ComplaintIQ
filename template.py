import os
from pathlib import Path

project_name = "src"


list_of_files = [

    # --- package markers ------

    f"{project_name}/__init__.py",

    # --- pipeline components: one file per ML stage -----
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    # --- configuration plumbing ----
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    # --- reliability ----

    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",

    # ---- AI/LLM ----
    f"{project_name}/llm/__init__.py",
    f"{project_name}/llm/summarizer.py",

    # ---- pipelines ------
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    # --- helpers ------
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    # --- security --------
    f"{project_name}/security/__init__.py",
    f"{project_name}/security/auth.py",
    f"{project_name}/security/pii.py",
    f"{project_name}/security/guardrails.py",

    # ---- cloud and monitoring ------
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/gcp_storage.py",
    f"{project_name}/monitoring/__init__.py",
    f"{project_name}/monitoring/metrics.py",

    # --- config and deployment files in the project root ------
    "config/model.yaml",
    "config/schema.yaml",
    "monitoring/prometheus.yml",
    "docker-compose.yml",
    "notebook/exploration.ipynb",
    "app.py",
    "requirements.txt",
    "demo.py",
    "Dockerfile",
    ".dockerignore",
    ".env.example",
    "setup.py",
    "pyproject.toml",


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at:{filepath}")        