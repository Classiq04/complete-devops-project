from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#07111f">
    <title>DevOps Time Service</title>
    <style>
        :root {
            color-scheme: dark;
            --bg: #07111f;
            --panel: #0c1a2d;
            --border: #1b3452;
            --blue: #38bdf8;
            --text: #edf5ff;
            --muted: #91a9c6;
            --green: #4ade80;
        }

        * { box-sizing: border-box; }

        body {
            margin: 0;
            min-height: 100vh;
            background:
                radial-gradient(ellipse at 15% 0%, #102c4b 0%, transparent 40%),
                var(--bg);
            color: var(--text);
            font-family: system-ui, -apple-system, BlinkMacSystemFont,
                         "Segoe UI", sans-serif;
        }

        nav {
            min-height: 76px;
            padding: 18px 6%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            border-bottom: 1px solid var(--border);
        }

        .brand {
            font-size: clamp(1rem, 2.5vw, 1.4rem);
            font-weight: 750;
            letter-spacing: -.5px;
        }

        .brand span, .accent { color: var(--blue); }

        .online {
            color: var(--green);
            border: 1px solid #20573e;
            background: #0b2a22;
            border-radius: 30px;
            padding: 7px 13px;
            font-size: .82rem;
            white-space: nowrap;
        }

        main {
            width: min(1200px, 88%);
            margin: 55px auto 35px;
        }

        .hero {
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            gap: 32px;
            margin-bottom: 38px;
        }

        .eyebrow {
            color: var(--blue);
            text-transform: uppercase;
            letter-spacing: 3px;
            font-size: .78rem;
            font-weight: 750;
        }

        h1 {
            font-size: clamp(2.2rem, 5vw, 4.3rem);
            line-height: 1.05;
            letter-spacing: -2px;
            margin: 14px 0;
        }

        .gradient {
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .intro {
            max-width: 490px;
            color: var(--muted);
            line-height: 1.8;
            font-size: 1.02rem;
        }

        .tech {
            display: flex;
            flex-wrap: wrap;
            gap: 9px;
            margin-top: 25px;
        }

        .tech span {
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 8px 11px;
            color: #c9dcf4;
            font-size: .82rem;
        }

        .clock-card {
            position: relative;
            overflow: hidden;
            padding: 30px;
            border: 1px solid #23659a;
            border-radius: 18px;
            background: linear-gradient(145deg, #102b4b, #0a1629 75%);
        }

        .clock-card::after {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            right: -130px;
            bottom: -150px;
            border: 1px solid #2563a5;
            border-radius: 50%;
            box-shadow: 0 0 0 25px #12315a44,
                        0 0 0 50px #12315a22;
        }

        .clock-label {
            color: #bdd5f1;
            font-size: .92rem;
        }

        #utc {
            font-size: clamp(1.65rem, 3.4vw, 2.8rem);
            font-weight: 750;
            letter-spacing: -1px;
            margin: 24px 0 8px;
            font-variant-numeric: tabular-nums;
        }

        #date, #local-time {
            color: var(--muted);
            font-size: .9rem;
        }

        .local {
            margin-top: 12px;
            padding-top: 14px;
            border-top: 1px solid var(--border);
        }

        .section-title {
            font-size: 1.1rem;
            margin: 0 0 16px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }

        .panel {
            border: 1px solid var(--border);
            border-radius: 14px;
            background: linear-gradient(145deg, #0c1a2b, #091524);
            overflow: hidden;
        }

        .panel-head { padding: 20px 20px 12px; }

        .panel-head h3 { margin: 0 0 5px; font-size: 1rem; }
        .panel-head p { margin: 0; color: var(--muted); font-size: .85rem; }

        .panel-body { padding: 8px 20px 20px; }

        .item {
            display: flex;
            justify-content: space-between;
            gap: 12px;
            padding: 12px 0;
            border-bottom: 1px solid #182b41;
            font-size: .88rem;
        }

        .item:last-child { border-bottom: 0; }
        .muted { color: var(--muted); }
        .good { color: var(--green); }
        code { color: var(--blue); font-size: .86rem; }

        .banner {
            margin-top: 22px;
            padding: 20px 24px;
            border: 1px solid var(--border);
            border-radius: 12px;
            background: #0c1a2b;
            color: #cbdcf0;
            text-align: center;
        }

        footer {
            padding: 10px 20px 30px;
            text-align: center;
            color: #728aa6;
            font-size: .82rem;
        }

        @media (max-width: 850px) {
            main { width: 90%; margin-top: 35px; }
            .hero { grid-template-columns: 1fr; }
            .grid { grid-template-columns: 1fr; }
            .clock-card { padding: 24px; }
        }

        @media (prefers-reduced-motion: no-preference) {
            .panel, .clock-card { animation: appear .55s ease both; }
            @keyframes appear {
                from { opacity: 0; transform: translateY(8px); }
                to { opacity: 1; transform: translateY(0); }
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="brand"><span>◷</span> DevOps Time Service</div>
        <div class="online">● &nbsp; App running</div>
    </nav>

    <main>
        <section class="hero">
            <div>
                <div class="eyebrow">A little project, built to ship</div>
                <h1>Time, with a<br><span class="gradient">DevOps mindset.</span></h1>
                <p class="intro">
                    A lightweight Flask service with a live clock, a health
                    endpoint, and a JSON API — ready to be containerized
                    and deployed.
                </p>
                <div class="tech">
                    <span>Python</span>
                    <span>Flask</span>
                    <span>Docker</span>
                    <span>Kubernetes</span>
                    <span>Argo CD</span>
                    <span>Terraform</span>
                </div>
            </div>

            <div class="clock-card">
                <div class="clock-label">◷ &nbsp; CURRENT TIME · UTC</div>
                <div id="utc">Loading time...</div>
                <div id="date">Fetching current date</div>
                <div class="local">
                    <div class="clock-label">YOUR LOCAL TIME</div>
                    <div id="local-time" style="margin-top:8px">
                        Loading local time...
                    </div>
                </div>
            </div>
        </section>

        <h2 class="section-title">Service overview</h2>

        <section class="grid">
            <article class="panel">
                <div class="panel-head">
                    <h3>♡ &nbsp; Application health</h3>
                    <p>Basic service status</p>
                </div>
                <div class="panel-body">
                    <div class="item">
                        <span>Flask application</span>
                        <span class="good">● Running</span>
                    </div>
                    <div class="item">
                        <span>Database</span>
                        <span class="muted">Not required</span>
                    </div>
                    <div class="item">
                        <span>Health endpoint</span>
                        <code>/health</code>
                    </div>
                </div>
            </article>

            <article class="panel">
                <div class="panel-head">
                    <h3>⌘ &nbsp; API endpoints</h3>
                    <p>Available HTTP routes</p>
                </div>
                <div class="panel-body">
                    <div class="item">
                        <code>GET /</code>
                        <span class="muted">Web page</span>
                    </div>
                    <div class="item">
                        <code>GET /health</code>
                        <span class="muted">Health check</span>
                    </div>
                    <div class="item">
                        <code>GET /api/time</code>
                        <span class="muted">JSON time</span>
                    </div>
                </div>
            </article>

            <article class="panel">
                <div class="panel-head">
                    <h3>◈ &nbsp; Application details</h3>
                    <p>Runtime configuration</p>
                </div>
                <div class="panel-body">
                    <div class="item">
                        <span>Framework</span><span>Flask</span>
                    </div>
                    <div class="item">
                        <span>Language</span><span>Python</span>
                    </div>
                    <div class="item">
                        <span>Port</span><span>8080</span>
                    </div>
                </div>
            </article>
        </section>

        <div class="banner">
            Built for learning. Designed to improve. Ready for deployment.
        </div>
    </main>

    <footer>
        DEVOPS TIME SERVICE &nbsp; · &nbsp; Python · Flask · Docker ·
        Kubernetes · Argo CD · Terraform
    </footer>

    <script>
        const utc = document.getElementById("utc");
        const date = document.getElementById("date");
        const localTime = document.getElementById("local-time");

        function updateClock() {
            const now = new Date();

            utc.textContent = now.toISOString().slice(11, 19);
            date.textContent = now.toLocaleDateString("en-US", {
                timeZone: "UTC",
                weekday: "long",
                year: "numeric",
                month: "long",
                day: "numeric"
            });

            localTime.textContent = now.toLocaleString(undefined, {
                year: "numeric",
                month: "short",
                day: "numeric",
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit"
            });
        }

        updateClock();
        setInterval(updateClock, 1000);
    </script>
</body>
</html>
"""

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/api/time")
def api_time():
    now = datetime.now(timezone.utc)
    return jsonify(
        timestamp=now.isoformat(),
        timezone="UTC"
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
