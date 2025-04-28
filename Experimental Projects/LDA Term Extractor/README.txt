# 🧠 LDA-Based Jargon Term Extractor (v2)

This version adds optional filtering to surface niche or rare terminology more effectively.

## 🚀 Usage

Install requirements:
    pip install gensim nltk scikit-learn

Download NLTK corpora (if needed):
    >>> import nltk
    >>> nltk.download('stopwords')
    >>> nltk.download('brown')

Run the script:
    python lda_term_extractor.py                # No filtering
    python lda_term_extractor.py --filter tfidf # Use TF-IDF filtering
    python lda_term_extractor.py --filter brown # Use Brown corpus comparison

## 💡 Teaching Idea

Ask students to run the script with each filtering method, compare the outputs, and evaluate:
- Which terms were surfaced that wouldn't normally stand out?
- Which filtering method better captures jargon or niche terminology?
- Which would be better suited for generating a terminology glossary?

## 📂 Files
- `lda_term_extractor.py` – main script with argument options
- `sample_corpus.txt` – sample corpus
