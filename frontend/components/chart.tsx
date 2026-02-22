"use client";

import { createChart } from "lightweight-charts";
import { useEffect, useRef } from "react";

export default function Chart() {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    const chart = createChart(ref.current, { height: 420, layout: { background: { color: "#09090b" }, textColor: "#d4d4d8" } });
    const series = chart.addCandlestickSeries();
    series.setData([
      { time: "2024-01-01", open: 100, high: 102, low: 98, close: 101 },
      { time: "2024-01-02", open: 101, high: 104, low: 100, close: 103 },
      { time: "2024-01-03", open: 103, high: 105, low: 102, close: 104 }
    ]);
    return () => chart.remove();
  }, []);

  return <div ref={ref} className="w-full rounded-xl border border-zinc-800" />;
}
