
def format_data_for_display(sample_people_data):
    new_list = []
    for i, data in enumerate(sample_people_data):
        print(i, data)
        new_list.append(data['given_name'] + " " + data['family_name'] + ": " + data['title'])
    # print(new_list)
    return new_list
