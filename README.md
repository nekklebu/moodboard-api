# 🌈Moodboard API

A tiny, weird, aesthetic microservice for delivering randomized *vibes*.

This project started out with a simple idea in mind: vibes. It’s a quick API hit that returns a curated moment: a quote, a color, a song, a suggestion, and a name for the feeling you're chasing.

### Example Output
```json
{
  "mood": "Cloudcore Collapse",
  "quote": "Some things are too soft to survive, and they bloom anyway.",
  "song": "https://open.spotify.com/track/6JN4CM3Ue2qUQNMz1ydQFM",
  "color": "#E0F7FA",
  "suggestion": "Let the playlist play until the sky changes."
}
```

---

## [ What It Does ]

- Returns a randomized bundle of vibe content via a `/vibe` endpoint
- Each moodboard is a small curated package: one quote, one Spotify track, one hex color, one suggestion, and a “mood” name
- All bundles are defined in code (for now), with future OpenAI/GPT content planned

---

## [ Tech Stack ]

- Python 3.11+
- Flask (API framework)
- Pytest (for testing)
- Docker (coming soon)
- GitHub Actions (CI/CD coming soon)
- AWS or GCP deployment (TBD based on vibes)

---

## [ Roadmap ]

| Phase | Description |
|-------|-------------|
| [x] Phase 1 | Create static moodboard bundles and serve them via Flask |
| [ ] Phase 2 | Modularize vibe generation and introduce test coverage |
| [ ] Phase 3 | Add CI/CD with GitHub Actions |
| [ ] Phase 4 | Dockerize the app for portable deployment |
| [ ] Phase 5 | Deploy to AWS (likely EC2 or Lambda) or GCP |
| [ ] Phase 6 | Integrate OpenAI or GPT to generate moodboards on the fly |
| [ ] Phase 7 | Optional: build a cute frontend or Slackbot that consumes this API |

---

## [ Running Locally ]

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
flask run
```

Test the vibe engine:

```bash
pytest
```

