from bs4 import BeautifulSoup
import csv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


def string_2_csv(input_path="input_strings.xml", output_path="output_strings.csv"):
    # Reading the data inside the xml
    # file to a variable under the name
    # data
    with open(input_path, 'r') as f:
        data = f.read()

    Bs_data = BeautifulSoup(data, "xml")

    print('======================\n\n')
    # Extract all string records
    b_name = Bs_data.find_all('string')

    if b_name:
        # Setup csv writer
        with open(output_path, mode='w') as csv_file:
            # init header
            field_names = ['key', 'value', 'translated']
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for resource in b_name:
                # print(resource.get('name') + " -- " + resource.text)
                translated = resource.get('translatable')
                if translated == 'false':
                    print('ignore key: {}'.format(resource.get('name')))
                    continue
                writer.writerow({
                    'key': resource.get('name'),
                    'value': resource.text,
                    'translated': ''
                })
            csv_file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    string_2_csv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
