import { useState } from "react";
import API from "../services/api";

function AddReview({ onReviewAdded }) {
  const [product, setProduct] = useState("");
  const [rating, setRating] = useState("");
  const [review, setReview] = useState("");

  const submitReview = async (e) => {
    e.preventDefault();

    if (
      product.trim() === "" ||
      rating === "" ||
      review.trim() === ""
    ) {
      alert("Please fill all fields");
      return;
    }

    try {
      const response = await API.post("/reviews", {
        product,
        rating: Number(rating),
        review,
      });

      alert(response.data.message);

      setProduct("");
      setRating("");
      setReview("");

      if (onReviewAdded) {
        onReviewAdded();
      }
    } catch (error) {
      console.error(error);
      alert("Failed to submit review");
    }
  };

  return (
    <div className="card shadow p-4 mt-4">
      <h3 className="mb-3">Add New Review</h3>

      <form onSubmit={submitReview}>
        <input
          type="text"
          className="form-control mb-3"
          placeholder="Product Name"
          value={product}
          onChange={(e) => setProduct(e.target.value)}
        />

        <input
          type="number"
          min="1"
          max="5"
          className="form-control mb-3"
          placeholder="Rating (1-5)"
          value={rating}
          onChange={(e) => setRating(e.target.value)}
        />

        <textarea
          className="form-control mb-3"
          rows="4"
          placeholder="Write your review..."
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />

        <button type="submit" className="btn btn-success w-100">
          Submit Review
        </button>
      </form>
    </div>
  );
}

export default AddReview;