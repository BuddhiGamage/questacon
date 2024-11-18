import csv

def get_tags_list():
    # Initialize an empty list to store the tags
    tags_list = []

    # Read the CSV file
    with open('pepper.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if present
        for row in reader:
            tags = row[0].strip()  # Get the tags from the first column
            tag_items = [tag.strip() for tag in tags.split(',')]  # Split and clean tags
            tags_list.append(tag_items)

    # Print the tags list
    # for tags in tags_list:
    #     print(tags)

    # Define the mapping dictionary
    tag_mapping = {
        "so": "self_and_others",
        "q": "question",
        "a": "affirmation",
        "st": "space_and_time",
        "ex": "exclamation",
        "en": "enumeration",
        "n": "negation",
        "green": "eyes_green",
        "fp": "facepalm",
        "red": "eyes_red",
        "con": "confused",
        "eyes":"eyes",
        "point":"point"
    }

    # Map the tags to their categories
    mapped_tags_list = [[tag_mapping[tag] for tag in tags] for tags in tags_list]

    # # Print the mapped list
    # for mapped_tags in mapped_tags_list:
    #     print(mapped_tags)

    return mapped_tags_list