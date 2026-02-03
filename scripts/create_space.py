import shutil
import sys
import os

def create_space(destination):
    template_path = 'templates/space-template'

    if not os.path.exists(template_path):
        print(f"Error: Template path '{template_path}' does not exist.")
        sys.exit(1)

    if os.path.exists(destination):
        print(f"Error: Destination '{destination}' already exists.")
        sys.exit(1)

    try:
        shutil.copytree(template_path, destination)
        print(f"Successfully created space at '{destination}'")
    except Exception as e:
        print(f"Error creating space: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 create_space.py <destination_path>")
        sys.exit(1)

    destination = sys.argv[1]
    create_space(destination)
