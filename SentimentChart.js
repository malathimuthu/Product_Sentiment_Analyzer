import React, { useEffect, useState } from "react";
import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function SentimentChart() {
  const [stats, setStats] = useState({
    positive: 0,
    negative: 0,
    neutral: 0,
  });

  useEffect(() => {
    fetch("http://127.0.0.1:5000/statistics")
      .then((res) => res.json())
      .then((data) => setStats(data))
      .catch((err) => console.log(err));
  }, []);

  const data = {
    labels: ["Positive", "Negative", "Neutral"],
    datasets: [
      {
        data: [
          stats.positive,
          stats.negative,
          stats.neutral,
        ],
        backgroundColor: [
          "#4CAF50",
          "#F44336",
          "#FFC107",
        ],
        borderWidth: 1,
      },
    ],
  };

  return (
    <div style={{ width: "400px", margin: "30px auto" }}>
      <h3 style={{ textAlign: "center" }}>
        Sentiment Analysis Chart
      </h3>
      <Pie data={data} />
    </div>
  );
}

export default SentimentChart;