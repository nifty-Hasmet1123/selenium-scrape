def get_store_as_a_list(file_path = r"D:\Comparison_scrape\utils\list_of_store.txt"):
    with open(file_path, "r") as file:
        list_of_store = file.readlines()
    
    store_objects = [store.strip() for store in list_of_store]

    return store_objects

STORES = get_store_as_a_list()


# with open("sample.txt", "a") as file:
#     for elements in my_data:
#         for element in elements:
#             file.write(element + "\n")


# def string_modification(string):
#     modification = (string.strip().
#                     replace("Pending Approval", "Pending-Approval").
#                     replace("United States", "United-States").
#                     replace("New Caledonia", "New-Caledonia").
#                     replace("South Africa", "South-Africa").
#                     replace("Saudi Arabia", "Saudi-Arabia").
#                     replace("New Zealand", "New-Zealand").
#                     replace("United Arab Emirates", "United-Arab-Emirates").
#                     replace("United Kingdom", "United-Kingdom").
#                     replace(" am ", "-am").
#                     replace(" pm ", "-pm").
#                     replace("  ", " none")
#                     )
    
#     modification = re.sub(r'\s+(\d+\/\d+\/\d+\s\d+:\d+:\d+)\s+', r'-\1-', modification)

#     modification = re.sub(r'(\d+\/\d+\/\d+)\s(\d+:\d+:\d+)', r'\1-\2', modification)
    
#     return modification

# result = []
# for elements in my_data:
#     x = map(string_modification, elements)
    # result.extend(list(x))

    # with open("validator_numbers.txt", "w") as file:
#     for item in next_labels:
#         file.write(item + "\n")