import os

# Folder structure definition
structure = {
    "genai-infra": {
        "eks": {
            "modules": {
                "vpc": {},
                "eks-cluster": {},
                "cpu-nodegroup": {},
                "gpu-nodegroup": {},
                "iam": {}
            },
            "envs": {
                "dev": {
                    "main.tf": "",
                    "variables.tf": "",
                    "outputs.tf": ""
                },
                "prod": {}
            },
            "versions.tf": "",
            "providers.tf": "",
            "backend.tf": "",
            "README.md": ""
        }
    }
}


def create_structure(base_path, items):
    for name, content in items.items():
        path = os.path.join(base_path, name)

        # If content is a dict → folder
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # Otherwise create a file
            with open(path, "w") as f:
                f.write(content)


if __name__ == "__main__":
    create_structure(".", structure)
    print("📁 Folder structure generated successfully!")
