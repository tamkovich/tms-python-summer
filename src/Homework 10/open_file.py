def file_open(path: str, arg: str) -> list:
    """
    Open file
    :param path: path of file
    :param arg: type of file
    :return: list of text
    """
    with open(path, arg) as file:
        tmp = file.readlines()
    return tmp
