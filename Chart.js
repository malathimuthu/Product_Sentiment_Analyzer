import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

function Chart({ reviews }) {
  const positive = reviews.filter(
    (r) => r.sentiment === "Positive"
  ).length;

  const negative = reviews.filter(
    (r) => r.sentiment === "Negative"
  ).length;

  const neutral = reviews.filter(
    (r) => r.sentiment === "Neutral"
  ).length;

  const data = [
    { name: "Positive", value: positive },
    { name: "Negative", value: negative },
    { name: "Neutral", value: neutral },
  ];

  const COLORS = ["#28a745", "#dc3545", "#ffc107"];

  return (
    <div className="card p-3 mt-4">
      <h4 className="text-center">Sentiment Analysis Chart</h4>

      <ResponsiveContainer width="100%" height={300}>
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            outerRadius={100}
            label
          >
            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={COLORS[index % COLORS.length]}
              />
            ))}
          </Pie>

          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export default Chart;