def create_empty_wordladder_file(wordladder_file_name):
    with open(wordladder_file_name,'w') as opened_file:
        pass
    


# In[3]:

def read_words_from_file(word_file_name):
    with open(word_file_name,'r') as readfile:
        return readfile.read()


# In[10]:

words_as_stringie = read_words_from_file('words.txt')


# In[10]:

# Input is a string of words separated by '\n'
# Output should be a list of valid words where a valid word
# contains no space, no -, no _ no numbers
def filter_words(words_as_string):
    initial = []
    final = []
    initial = words_as_string.split('\n')
    for i in range(len(initial)):
        werd = initial[i]
        werd = werd.strip()
        if '-' in werd:
            continue
        if '_' in werd:
            continue
        if '.' in werd:
            continue
        if ' ' in werd:
            continue
        final.append(werd)
    return final


def group_by_word_length(words):
    d = {}
    for i in range(len(words)):
        word = words[i]
        length = len(word)
        if length not in d:
            d[length] = []
        d[length].append(word)
    return d


# In[14]:

def create_file(wordladder_file_name, contents):
    with open(wordladder_file_name,'w') as opened_file:
        for i in range(len(contents)):
            opened_file.write(contents[i])
            if i != len(contents):
                opened_file.write('\n')
            else:
                continue
    return opened_file


# In[15]:

# create nodes for all the words into the words ladder file name
# input is the words ladder file name and the list of valid words
# the function should open the word_ladder_file_name for write 
# truncate the file contents (Use the truncate() function on the file handle)
# copy each of the words into the file in a loop using the write() function
# remember to put a new line after the first word
def create_nodes(word_ladder_file_name, contents):
    with open(word_ladder_file_name,'w') as opened_file:
        opened_file.truncate()
        for i in range(len(contents)):
            opened_file.write(contents[i])
            if i != len(contents):
                opened_file.write('\n')
            else:
                continue
    return opened_file
        


# In[17]:

# diff2words should find the difference between 2 words
# input is 2 words, both words are of the same length (100% guarenteed)
# output is a list that is of the same length as the word
# the output list can have only 2 possible values for each entry, 0 or 1
# entry should be 0 if the letters at that index are identical
# entry should be 1 if the latters at that index are not identical
# Some examples
# diff2words("HELO", "ALLO") should return [0,0,1,1]
# diff2words("RACE", "FELL") should return [0,0,0,0]
# diff2words("RACE", "RACE") should return [1,1,1,1]
def diff2words(word1, word2):
    diff = []
    for c in range(len(word1)):
        if word1[c] == word2[c]:
            diff.append(0)
        else:
            diff.append(1)
    return diff


# In[18]:

def build_nodes(word_ladder_file_name):
    with open(word_ladder_file_name,'r') as opened:
        return opened.read().split('\n')


# In[20]:

# create combinations of 2 words
# input is the list of words
# output is the list where each list is a tuple of 2 indexes which represents a combination
# ["abc", "def", "ghi"]
# returns
# [ (0,1), (0,2), (1,2) ]
def create_combinations(list_of_words):
    combos = []
    for i in range(len(list_of_words)-1):
        for j in range(1,len(list_of_words)):
            combo = []
            if i == j:
                continue
            combo = [i,j] 
            combos.append(combo)
    return combos


# In[22]:

# Create edges 
# input is the word ladder file name
# read in all the words into a list
# compare 2 words (combinations not permutations)
# run the words through the diff2words and get the results
# figure out if they are off by 1 and then
# if they are off by 1
# create an edge which is of the form
# from_node_idx,to_node_idx,diff_index
# from the second index
# write into the word_ladder_file_name
# first line indicates EDGES
def create_edges(word_ladder_file_name,nodes):
    edges = []
    combos = create_combinations(nodes)
    for i in range(len(combos)):
        diff = diff2words(nodes[combos[i][0]],nodes[combos[i][1]])
        if sum(diff) == 1:
            for cindex in range(len(diff)):
                if diff[cindex] == 1:
                    edge = [combos[i][0],combos[i][1],cindex]
                    edges.append(edge)
                    edge = [combos[i][1],combos[i][0],cindex]
                    edges.append(edge)
                    break
    with open(word_ladder_file_name,'a') as opened:
        opened.write('EDGES')
        opened.write('\n')
        for s in range(len(edges)):
            edges_str = reduce(lambda x,y: str(x) + ',' + str(y), edges[s])
            opened.write(edges_str)
            opened.write('\n')


# In[23]:

def creator(file_name,output_file_name):
    read_string = read_words_from_file(file_name)
    filtered_werdz = filter_words(read_string)
    create_empty_wordladder_file(output_file_name)
    grouped_words = group_by_word_length(filtered_werdz)
    create_nodes(output_file_name,grouped_words[4])
    create_edges(output_file_name,grouped_words[4])
    


# In[24]:

# In[25]:

# In[129]:

# create empty list called solver_nodes
# open the word_ladder_file_name
# read the entire contents as string
# split the string on new line '\n' and store into a list
# read each of the entries in the list one by one
# if the entry is not EDGES in upper case, then add to the solver_nodes
# if its EDGES then stop reading
# return the solver_nodes
def create_solver_nodes_and_edges(word_ladder_file_name):
    solver_nodes = []
    solver_edges = []
    with open(word_ladder_file_name) as file_name:
        contents = file_name.read()
        lined_contents = contents.strip('\n')
        filtered_contents = filter_words(lined_contents)
        adding_nodes = True
        for i in range(len(filtered_contents)):
            if filtered_contents[i] == 'EDGES':
                adding_nodes = False
            else:
                if adding_nodes:
                    solver_nodes.append(filtered_contents[i])
                else:
                    edge = []
                    line = filtered_contents[i].split(',')
                    for entry in line:
                        edge.append(int(entry))
                    tuple_edge = tuple(edge)
                    solver_edges.append(tuple_edge)
        return  (solver_nodes, solver_edges)


# In[131]:

# solver is a recursive function
# each time its invoked
# start_index, end_index, solver_nodes, edges, max_moves dont change
# current_move is increased by 1
# the steps:
# compare current_move with max_moves
# if current_move >= max_moves
#   stop
# else
#   look at the path list
#   last entry in the path list is the next word index that needs to be processed
#   check the last entry in the path list
#     if last_entry_index == end_index
#        append path to the answers list
#     else
#        get the tuples for that last_entry_index from edges
#        for each entry in the tuple:
#          get the end_index create a new path thats initialized from the old path
#          append the end_index to the new path
#          invoke solve again but using the new path, with current_move incremented by 1
#        
def solve(start_index, end_index, solver_nodes, edges, max_moves, current_move, path, answers):
    if current_move>= max_moves:
        return
    last_entry_index = path[-1]
    if last_entry_index == end_index:
        answers.append(path)
        return
    tuples = edges[last_entry_index]
    for t in tuples:
        edge_end_index = t[0]
        new_path = path[:]
        new_path.append(edge_end_index)
        solve(start_index, end_index, solver_nodes, edges, max_moves, current_move+1,new_path, answers)


# In[132]:

def simplify_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] == array[j]:
                pass
            else:
                del array[i]


# In[139]:

# read in the file
# create an array nodes of all the words. 
# The order of the words in the nodes should match the order in the file
# create a dictionary edges of the edges
# the key for the dictionary is the index of the 1st node
# the value for each key is a list of ALL nodes that can be reached from this node
# each entry in the list will be a tuple of the form (other_node_idx, index_of_diff)
def solver(word_ladder_file_name,start_word, end_word, max_moves):
    # read all the words into a nodes file from the word_ladder_file_name
    solver_nodes, solver_edges = create_solver_nodes_and_edges(word_ladder_file_name)
    solver_edges = set(solver_edges)
    edges = {}
    for solver_edge in solver_edges:
        edge_start_word_idx = solver_edge[0]
        edge_end_word_idx = solver_edge[1]
        edge_diff_idx = solver_edge[2]
        if edge_start_word_idx in edges:
            tuples = edges[edge_start_word_idx]
        else:
            tuples = []
            edges[edge_start_word_idx] = tuples
        tuples.append((edge_end_word_idx, edge_diff_idx))
    index = 0
    start_index = solver_nodes.index(start_word)
    end_index = solver_nodes.index(end_word)
    answers = []
    current_move = 0
    path= [ start_index ]
    solve(start_index, end_index, solver_nodes, edges, max_moves, current_move, path, answers)
    for answer in answers:
        print 'Answer:'
        for word_idx in answer:
            print solver_nodes[word_idx]
            


# In[144]:

import sys

def main():
    print "Usage: python word_ladder.py <start_word> <end_word> <max_moves>"
    args = sys.argv[1:]
    start_word = 'cool'
    end_word = 'warm'
    max_moves = 6
    if len(args) >= 2:
        start_word = args[0]
        end_word = args[1]
    if len(args) > 2:
        max_moves = int(args[2])
    print 'Inputs:'
    print 'start word', start_word
    print 'end word', end_word
    print 'max moves', max_moves

    creator('words.txt', 'word_ladder.txt')
    solver('word_ladder.txt',start_word, end_word, max_moves)

if __name__ == '__main__':
    main()

