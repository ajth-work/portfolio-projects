import re
import nltk
import gensim
import gensim.corpora as corpora
import argparse
from collections import Counter
from nltk.corpus import stopwords, brown
from gensim.models import LdaModel
from gensim.utils import simple_preprocess
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('brown')

def read_documents(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return [line.strip() for line in text.split("\n") if line.strip()]

def preprocess(texts):
    stop_words = stopwords.words('english')
    return [
        [word for word in simple_preprocess(str(doc)) if word not in stop_words]
        for doc in texts
    ]

def build_lda_model(data, num_topics=5):
    id2word = corpora.Dictionary(data)
    corpus = [id2word.doc2bow(text) for text in data]
    lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=num_topics,
                         random_state=100, update_every=1, chunksize=10,
                         passes=10, alpha='auto', per_word_topics=True)
    return lda_model, corpus, id2word

def extract_keywords(lda_model, num_words=10):
    keywords = set()
    for idx, topic in lda_model.show_topics(formatted=False, num_words=num_words):
        for word, _ in topic:
            keywords.add(word)
    return sorted(list(keywords))

def filter_with_tfidf(texts, candidate_keywords, top_n=20):
    vectorizer = TfidfVectorizer()
    joined_texts = [' '.join(text) for text in texts]
    tfidf_matrix = vectorizer.fit_transform(joined_texts)
    tfidf_scores = dict(zip(vectorizer.get_feature_names_out(), tfidf_matrix.sum(axis=0).A1))
    filtered = sorted([(kw, tfidf_scores.get(kw, 0)) for kw in candidate_keywords], key=lambda x: x[1], reverse=True)
    return filtered[:top_n]

def filter_with_brown_comparison(candidate_keywords, top_n=20):
    brown_words = set(w.lower() for w in brown.words())
    filtered = [(kw, 'rare' if kw not in brown_words else 'common') for kw in candidate_keywords]
    rare_terms = [kw for kw, status in filtered if status == 'rare']
    return sorted(rare_terms)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LDA Term Extractor with optional filtering")
    parser.add_argument('--filter', choices=['tfidf', 'brown'], help="Apply TF-IDF or Brown corpus filtering")
    args = parser.parse_args()

    print("🧠 LDA Term Extractor (v2)")
    documents = read_documents("sample_corpus.txt")
    processed_data = preprocess(documents)
    lda_model, corpus, id2word = build_lda_model(processed_data)
    candidate_keywords = extract_keywords(lda_model)

    if args.filter == 'tfidf':
        print("\n🔍 Applying TF-IDF filtering...")
        filtered_keywords = filter_with_tfidf(processed_data, candidate_keywords)
        print("\n📌 TF-IDF filtered terms:")
        for word, score in filtered_keywords:
            print(f"- {word} (score: {score:.3f})")
    elif args.filter == 'brown':
        print("\n🔍 Filtering against Brown corpus vocabulary...")
        filtered_keywords = filter_with_brown_comparison(candidate_keywords)
        print("\n📌 Rare terms (not in Brown corpus):")
        for word in filtered_keywords:
            print(f"- {word}")
    else:
        print("\n📌 Raw LDA terms:")
        for kw in candidate_keywords:
            print("-", kw)
