#chunk_counter
from collections import Counter

'''function that pulls chunks out of chunked sentence
and finds the most common chunks '''
def chunk_counter(chunked_sentences, phrasetype): 

    if isinstance(phrasetype, str):
        pass
    else: 
        phrasetype = str(phrasetype)
    
    #create a list to hold chunks 
    chunks=list()

    '''Loop through each chunked sentence 
    to extract phrase chunks
    '''
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == phrasetype): chunks.append(tuple(subtree))

    #Create a Counter object
    chunk_counter = Counter()
    # loop through list of chunks
    for chunk in chunks:
        # increase chunk counter by 1
        chunk_counter[chunk] += 1
    #Return the 30 most frequent chunks
    return chunk_counter.most_common(5)
