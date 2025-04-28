import React, { useState, useEffect, useCallback } from 'react';
import { createRoot } from 'react-dom/client';

const initialCards = [
  { front: '你好', back: 'Hello' },
  { front: '谢谢', back: 'Thank you' },
  { front: '请', back: 'Please' },
  { front: '对不起', back: 'Sorry' },
  { front: '是', back: 'Yes' },
  { front: '不是', back: 'No' },
  { front: '早上好', back: 'Good morning' },
  { front: '晚安', back: 'Good night' },
  { front: '再见', back: 'Goodbye' },
  { front: '我爱你', back: 'I love you' },
];

function FlashcardApp() {
  const [cards, setCards] = useState(
    initialCards.map(card => ({ ...card, reviewed: false, correct: false }))
  );
  const [currentPage, setCurrentPage] = useState('review');
  const [searchTerm, setSearchTerm] = useState('');
  const [reviewIndex, setReviewIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [stats, setStats] = useState({ reviewedCount: 0, correctCount: 0 });
  const [newFront, setNewFront] = useState('');
  const [newBack, setNewBack] = useState('');

  const goNext = useCallback(() => {
    setFlipped(false);
    setReviewIndex(idx => (idx + 1) % cards.length);
  }, [cards.length]);

  const goPrev = useCallback(() => {
    setFlipped(false);
    setReviewIndex(idx => (idx - 1 + cards.length) % cards.length);
  }, [cards.length]);

  const handleReview = correct => {
    setStats(st => ({
      reviewedCount: st.reviewedCount + 1,
      correctCount: st.correctCount + (correct ? 1 : 0),
    }));
    goNext();
  };

  useEffect(() => {
    if (currentPage !== 'review') return;
    const handleKey = e => {
      switch (e.code) {
        case 'Space':
          e.preventDefault();
          setFlipped(prev => !prev);
          break;
        case 'ArrowRight':
          e.preventDefault();
          goNext();
          break;
        case 'ArrowLeft':
          e.preventDefault();
          goPrev();
          break;
        default:
          break;
      }
    };
    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, [currentPage, goNext, goPrev]);

  const addCard = () => {
    if (!newFront.trim() || !newBack.trim()) return;
    setCards(prev => [
      ...prev,
      { front: newFront.trim(), back: newBack.trim(), reviewed: false, correct: false },
    ]);
    setNewFront('');
    setNewBack('');
  };

  const filteredCards = cards.filter(
    card =>
      card.front.toLowerCase().includes(searchTerm.toLowerCase()) ||
      card.back.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const styles = {
    container: { display: 'flex', height: '100vh', fontFamily: 'sans-serif' },
    sidebar: { width: '200px', background: '#f0f0f0', padding: '10px' },
    main: { flex: 1, padding: '20px', overflowY: 'auto' },
    button: { display: 'block', width: '100%', padding: '10px', margin: '5px 0', cursor: 'pointer' },
    navButtons: { display: 'flex', justifyContent: 'space-between', marginTop: '10px' },
    cardContainer: { perspective: '1000px', margin: 'auto', width: '300px', height: '200px' },
    card: { width: '100%', height: '100%', position: 'relative', transformStyle: 'preserve-3d', transition: 'transform 0.6s' },
    cardFlipped: { transform: 'rotateY(180deg)' },
    cardFace: { position: 'absolute', width: '100%', height: '100%', backfaceVisibility: 'hidden', display: 'flex', justifyContent: 'center', alignItems: 'center', fontSize: '24px', border: '1px solid #ccc', borderRadius: '8px', background: '#fff' },
    cardBack: { transform: 'rotateY(180deg)' },
    input: { width: '100%', padding: '8px', margin: '5px 0' },
  };

  return (
    <div style={styles.container}>
      <div style={styles.sidebar}>
        <button style={styles.button} onClick={() => setCurrentPage('create')}>Create Cards</button>
        <button style={styles.button} onClick={() => setCurrentPage('search')}>Search Cards</button>
        <button style={styles.button} onClick={() => setCurrentPage('review')}>Review Cards</button>
        <button style={styles.button} onClick={() => setCurrentPage('stats')}>Statistics</button>
      </div>
      <div style={styles.main}>
        {currentPage === 'create' && (
          <div>
            <h2>Create a New Flashcard</h2>
            <input style={styles.input} placeholder="Front (Chinese)" value={newFront} onChange={e => setNewFront(e.target.value)} />
            <input style={styles.input} placeholder="Back (English)" value={newBack} onChange={e => setNewBack(e.target.value)} />
            <button style={styles.button} onClick={addCard}>Add Card</button>
          </div>
        )}
        {currentPage === 'search' && (
          <div>
            <h2>Search Flashcards</h2>
            <input style={styles.input} placeholder="Search..." value={searchTerm} onChange={e => setSearchTerm(e.target.value)} />
            <ul>
              {filteredCards.map((card, idx) => (
                <li key={idx}>{card.front} - {card.back}</li>
              ))}
            </ul>
          </div>
        )}
        {currentPage === 'review' && (
          <div>
            <h2>Review Flashcards</h2>
            <div style={styles.cardContainer} onClick={() => setFlipped(prev => !prev)}>
              <div style={{ ...styles.card, ...(flipped ? styles.cardFlipped : {}) }}>
                <div style={styles.cardFace}>{cards[reviewIndex]?.front}</div>
                <div style={{ ...styles.cardFace, ...styles.cardBack }}>{cards[reviewIndex]?.back}</div>
              </div>
            </div>
            {flipped && (
              <div style={styles.navButtons}>
                <button style={styles.button} onClick={() => handleReview(false)}>Missed it</button>
                <button style={styles.button} onClick={() => handleReview(true)}>Got it</button>
              </div>
            )}
          </div>
        )}
        {currentPage === 'stats' && (
          <div>
            <h2>Statistics</h2>
            <p>Cards reviewed: {stats.reviewedCount}</p>
            <p>Correct percentage: {stats.reviewedCount ? Math.round((stats.correctCount / stats.reviewedCount) * 100) : 0}%</p>
            <svg width={300} height={150}>
              <rect x={50} y={150 - stats.reviewedCount * 10} width={50} height={stats.reviewedCount * 10} />
              <rect x={150} y={150 - (stats.reviewedCount ? (stats.correctCount / stats.reviewedCount) * 100 : 0) * 1.5} width={50} height={(stats.reviewedCount ? (stats.correctCount / stats.reviewedCount) * 100 : 0) * 1.5} />
              <text x={50} y={145}>Reviewed</text>
              <text x={150} y={145}>Correct%</text>
            </svg>
          </div>
        )}
      </div>
    </div>
  );
}

const root = createRoot(document.getElementById('root'));
root.render(<FlashcardApp />);


export default FlashcardApp;