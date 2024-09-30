import re


def to_snake_case(text: str):
    # Replace all non-letter/number characters with a space
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    # Insert underscores between words and convert to lowercase
    snake_case = re.sub(r"(?<!^)(?=[A-Z])", "_", text).replace(" ", "_").lower()
    # Remove any leading/trailing underscores
    return snake_case.strip("_")
