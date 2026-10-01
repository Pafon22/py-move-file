import os


def move_file(command: str) -> None:
    try:
        command_array = command.split()
        if len(command_array) != 3:
            raise ValueError()
        move_cmd, source_path, dest_path = command_array
    except ValueError:
        print("Command must have exactly 3 arguments.")

    try:
        with open(source_path, "r") as source_file:
            content = source_file.read()
    except FileNotFoundError:
        print(f"Check the origin file name, {source_path}")

    if not os._exists(dest_path):
        os.makedirs(dest_path)

    try:
        with open(dest_path, "w") as dest_file:
            dest_file.write(content)
    except FileExistsError:
        print(f"Already exists a file with this name, {dest_path}")

    os.remove(source_path)