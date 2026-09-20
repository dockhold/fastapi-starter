# Python / FastAPI starter

A FastAPI app that deploys to [Dockhold](https://dockhold.eu) with a tiny,
reproducible Dockerfile — it pins exactly how the app installs and starts, so it
deploys the same way every time.

[![Deploy on Dockhold](https://dockhold.eu/button.svg)](https://app.dockhold.eu/new?repo=https://github.com/dockhold/fastapi-starter&name=fastapi-starter&ref=button)

## Deploy it

1. Click **Use this template** (or fork this repo) to get your own copy.
2. Click the **Deploy on Dockhold** button above, or open
   [app.dockhold.eu/new](https://app.dockhold.eu/new), connect GitHub, and pick
   your repo.
3. Dockhold builds from the [`Dockerfile`](Dockerfile) and runs it. The app goes
   live at `https://<your-app>.dockhold.app` with HTTPS handled.

`GET /` returns a JSON greeting; `GET /health` returns `{ "status": "ok" }`.
Every later push to your main branch redeploys.

## Deploy with your AI tool

Install the Dockhold plugin or MCP server in your AI coding tool
([setup guide](https://dockhold.eu/docs/recipes/deploy-from-your-ai-tool)), then
say "put this online" in a folder with this template. The tool signs you in
through the browser once and reports the URL when the app is live.

Or from a terminal: `npx dockhold login`, then `npx dockhold deploy`.

## How it runs

The [`Dockerfile`](Dockerfile) installs `requirements.txt` and starts uvicorn:

```dockerfile
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
```

Two things matter: bind `--host 0.0.0.0 --port $PORT` (never a fixed port), and
keep the `CMD` in **shell form** (no `[ ]` brackets) so `$PORT` expands at
runtime. `main:app` means the `app` object in `main.py` — rename to match your
project.

## Config and secrets

Set plain config in the dashboard, secrets in the Vault, then read them with
`os.environ`. See [`.env.example`](.env.example).

## Add a database

Enable the managed database add-on and read `os.environ["DATABASE_URL"]`. Apps
are stateless — the filesystem is wiped on every restart, so persist state in
the database, not on disk.

## Run it locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PORT=8000 uvicorn main:app --host 0.0.0.0 --port $PORT
# curl http://localhost:8000/health
```

## Full walkthrough

[Deploy a Python / FastAPI app](https://dockhold.eu/docs/recipes/deploy-a-python-fastapi-app)
— the step-by-step recipe, including the shell-form `CMD` and import-path fixes.
