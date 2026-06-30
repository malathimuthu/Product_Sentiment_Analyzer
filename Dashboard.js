import { useState, useEffect } from "react";
import API from "../services/api";
import Navbar from "../components/Navbar";
import AddReview from "../components/AddReview";
import Search from "../components/Search";
import Chart from "../components/Chart";

function Dashboard() {
  const [reviews, setReviews] = useState([]);
  const [filteredReviews, setFilteredReviews] = useState([]);

  const loadReviews = async () => {
    try {
      const response = await API.get("/reviews");
      setReviews(response.data);
      setFilteredReviews(response.data);
    } catch (error) {
      console.log(error);
      alert("Backend is not running");
    }
  };

  useEffect(() => {
    loadReviews();
  }, []);

  return (
    <>
      <Navbar />

      <div className="container mt-4">

        <h2 className="text-center text-primary mb-4">
          Product Sentiment Analyzer
        </h2>

        <button
          className="btn btn-primary mb-4"
          onClick={loadReviews}
        >
          Refresh Reviews
        </button>

        <AddReview onReviewAdded={loadReviews} />

        <div className="mt-4">
          <Search
            reviews={reviews}
            setFilteredReviews={setFilteredReviews}
          />
        </div>

        <div className="mt-4">
          <Chart reviews={reviews} />
        </div>

        <div className="row mt-4">
          {filteredReviews.length > 0 ? (
            filteredReviews.map((item, index) => (
              <div className="col-md-4 mb-4" key={index}>
                <div className="card shadow h-100">
                  <div className="card-body">

                    <h4>{item.product}</h4>

                    <h6 className="text-warning">
                      ⭐ {item.rating}/5
                    </h6>

                    <p>{item.review}</p>

                    <h5
                      className={
                        item.sentiment === "Positive"
                          ? "text-success"
                          : item.sentiment === "Negative"
                          ? "text-danger"
                          : "text-warning"
                      }
                    >
                      {item.sentiment}
                    </h5>

                  </div>
                </div>
              </div>
            ))
          ) : (
            <div className="col-12 text-center">
              <h4 className="text-danger">
                No Reviews Found
              </h4>
            </div>
          )}
        </div>

      </div>
    </>
  );
}

export default Dashboard;