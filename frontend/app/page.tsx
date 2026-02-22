import Chart from "@/components/chart";

async function getAnalysis() {
  const res = await fetch("http://localhost:8000/api/analysis/chart", { cache: "no-store" }).catch(() => null);
  if (!res || !res.ok) return null;
  return res.json();
}

export default async function Home() {
  const analysis = await getAnalysis();

  return (
    <div className="space-y-6">
      <header className="flex items-center justify-between">
        <h1 className="text-3xl font-semibold">Axium</h1>
        <span className="rounded bg-zinc-800 px-3 py-1 text-xs">Demo mode</span>
      </header>
      <Chart />
      <section className="grid grid-cols-1 gap-4 md:grid-cols-2">
        <div className="rounded-xl border border-zinc-800 p-4">
          <h2 className="mb-2 text-lg font-medium">AI Chart Analysis (1-2 weeks)</h2>
          <p className="text-sm text-zinc-300">{analysis?.thesis ?? "Backend not running yet."}</p>
        </div>
        <div className="rounded-xl border border-zinc-800 p-4">
          <h2 className="mb-2 text-lg font-medium">Risk Plan</h2>
          <p className="text-sm text-zinc-300">Stop: {analysis?.risk_plan?.stop ?? "n/a"}</p>
        </div>
      </section>
    </div>
  );
}
