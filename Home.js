import { useState } from "react";
import API from "../services/api";

function Home() {
  const [reviews, setReviews] = useState([]);

  const loadReviews = async () => {
    try {
      const response = await API.get("/reviews");
      console.log(response.data); // Check browser console
      setReviews(response.data);
    } catch (error) {
      console.error(error);
      alert("Backend is not running");
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center text-primary">
        Product Sentiment Analyzer
      </h1>

      <button
        className="btn btn-primary mt-3"
        onClick={loadReviews}
      >
        Load Reviews
      </button>

      <div className="mt-4">
        {reviews.map((item, index) => (
          <div className="card p-3 mb-3" key={index}>
            <h3>{item.product}</h3>
            <p><b>Rating:</b> {item.rating}</p>
            <p><b>Review:</b> {item.review}</p>
            <p><b>Sentiment:</b> {item.sentiment}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;