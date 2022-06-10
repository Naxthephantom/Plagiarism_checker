
import os
from numpy import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sample_file = [doc for doc in os.listdir() if doc.endswith(',txt')]
sample_contents = [open(file).read() for file in sample_file] 

vectorize = lambda text: TfidfVectorizer().fit_transform(text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(sample_contents)
s_vector = list(zip(sample_contents, vectors))

def check_plaigarism():
    result = set()
    global s_vector
    for sample_a, text_vector_a in s_vector:
        new_vectors = s_vector.copy()
        current_index = new_vectors.index((sample_a, text_vector_a))
        del new_vectors[current_index]
        for sample_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0] [1]
            sample_pair = sorted((sample_a, sample_b))
            score = sample_pair[0], sample_pair[1], sim_score
            result.add(score)
    return result

for data in check_plaigarism():\
    print(data)
