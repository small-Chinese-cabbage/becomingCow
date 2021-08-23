# breadth-first search
'''
from collections import deque

# graph
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
print(graph)


def person_is_seller(name):
    return name[-1] == 'm'

def breadthfirstsearch(name):
    search_queue = deque()  # create a queue
    search_queue += graph[name]  # add you neighbours to the search queue
    searched=[]

    while search_queue:
        person = search_queue.popleft()  # get the first element in the queue
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
breadthfirstsearch('you')

'''
first={}
first['getup']=['shower','brushteeth']
first['brushteeth']=['havebreakfest']
print(first)