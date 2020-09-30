import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# while thinking of threading think it as:
# in a factory there are bunch of workers and they are doing their own job
# here thread are workers and queue is job

# there is no variable type like constant in python so in order to make other
# programmer aware that the variable is a constant, make it all caps

# here we are just hard coding everything but if you want to make some 
# GUI kind of thing then, you can just ask the user to type the homepage

PROJECT_NAME = 'ulmedu'
HOMEPAGE = 'https://www.ulm.edu/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME+'/queue.txt'
CRAWLED_FILE = PROJECT_NAME+'/crawled.txt'
# this number is depended upon how much your OS can handle
# here I am going to put 8
NUMBER_OF_THREADS = 8

queue = Queue() # this is not the queue of the links but thread queue

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# here you just create jobs and worker
# you dont need to assign that this thread needs to do this job and that thread needs to do another job
# as long as the worker has the job, they start working automatically

# create worker threads (will die when main exits)
# here if we close the program then the threads will not still run in the background, it will be terminated
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True  #die when the main exits
        t.start()


# do next job in the queue
def work():
    while True:
        url=queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# each queue link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)    #sticking every queued link to the thread queue
    queue.join()   #dont bump around, be a nice worker :D
    crawl()  #??? is not it looping??


# check if there are items in the queue then get to work
def crawl():
    queue_links = file_to_set(QUEUE_FILE)   #returning the set and assigning to queue_links
    if(len(queue_links)>0):
        print(str(len(queue_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()