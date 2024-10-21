import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

const EmojiRain = ({ emojis, count = 50 }) => {
  const [raindrops, setRaindrops] = useState([]);

  useEffect(() => {
    const newRaindrops = Array.from({ length: count }, (_, i) => ({
      id: i,
      emoji: emojis[Math.floor(Math.random() * emojis.length)],
      style: {
        left: `${Math.random() * 100}%`,
        animationDuration: `${5 + Math.random() * 5}s`,
        animationDelay: `${Math.random() * -15}s`,
      },
    }));
    setRaindrops(newRaindrops);
  }, [emojis, count]);

  return (
    <div className="emoji-rain">
      {raindrops.map((raindrop) => (
        <span key={raindrop.id} className="raindrop" style={raindrop.style}>
          {raindrop.emoji}
        </span>
      ))}
    </div>
  );
};

EmojiRain.propTypes = {
  emojis: PropTypes.arrayOf(PropTypes.string).isRequired,
  count: PropTypes.number,
};

export default EmojiRain;
