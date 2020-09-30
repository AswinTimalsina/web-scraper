def reading_files_number(path):
    a = set()
    with open(path, 'rt') as file:
        for line in file:
            a.add(line)
    return len(a)

print('Crawled Pages: ' +str(reading_files_number('crawled.txt')))
print('Queued Pages: ' +str(reading_files_number('queue.txt'))+'\n')
print('Total: '+str(reading_files_number('crawled.txt') + reading_files_number('queue.txt')))
