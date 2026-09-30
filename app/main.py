import os


def move_file(command: str) -> None:
    command_array = command.split()

    if len(command_array) != 3 or command_array[0] != "mv":
        return

    source_file = command_array[1]
    dest_full_file = command_array[2]

    if dest_full_file.endswith("/"):
        dest_full_file = dest_full_file + os.path.basename(source_file)

    directories = dest_full_file.split("/")
    file_name = directories.pop()

    current_directory = ""

    for directory in directories:
        if current_directory:
            current_directory += "/" + directory
        else:
            current_directory = directory

        if not os.path.exists(current_directory):
            os.mkdir(current_directory)

    if current_directory:
        dest_full_file = current_directory + "/" + file_name
    else:
        dest_full_file = file_name

    with open(source_file, "r") as source:
        text_content = source.read()

    with open(dest_full_file, "w") as destination_file:
        destination_file.write(text_content)

    os.remove(source_file)
