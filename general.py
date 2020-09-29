import os 

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project '+ directory)
        os.makedirs(directory)

def create_project_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')


# in this function had a small question about
# f = open(path, 'w')
# with open(path, 'w') as file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#append data to the file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#delete contents of the file
def delete_file_content(path):
    with open(path, 'w'):
        pass

# read file and convert each line to set items
def file_to_set(path):
    result = set()
    with open(path, 'rt') as file:
        for lines in file:
            result.add(lines.replace('\n', ''))
    return result

def set_to_file(links, path):
    delete_file_content(path)
    for link in sorted(links):
        append_to_file(path, link)
