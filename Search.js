import { useState } from "react";

function Search({ reviews, setFilteredReviews }) {
  const [keyword, setKeyword] = useState("");

  const handleSearch = () => {
    if (keyword.trim() === "") {
      setFilteredReviews(reviews);
      return;
    }

    const filtered = reviews.filter(
      (item) =>
        item.product.toLowerCase().includes(keyword.toLowerCase()) ||
        item.review.toLowerCase().includes(keyword.toLowerCase()) ||
        item.sentiment.toLowerCase().includes(keyword.toLowerCase())
    );

    setFilteredReviews(filtered);
  };

  return (
    <div className="mb-4">
      <div className="input-group">
        <input
          type="text"
          className="form-control"
          placeholder="Search by Product, Review or Sentiment"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
        />

        <button className="btn btn-primary" onClick={handleSearch}>
          Search
        </button>
      </div>
    </div>
  );
}

export default Search;