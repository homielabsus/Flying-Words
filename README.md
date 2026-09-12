# ✨ Flying Words

A one-file website for kids. Type anything — a word, your name, `🦖🦖🦖`, `こんにちは`, `#1 BEST!` — press **Enter** (or tap the big yellow **GO!**) and the text performs a WordArt **look** plus a PowerPoint-style **move**. Every press is a fresh surprise, confetti included.

## Open it

Double-click `index.html`. That's it — no install, no build step, no server needed. It also works offline (the optional Fredoka web font is only fetched when the page is served from a website).

Works on phones and desktops. Tap a letter to make it hop; double-tap the stage to replay the last trick; tap the yellow sticker for a surprise.

## Put it on GitHub Pages

1. Push this folder to a GitHub repository.
2. In the repo go to **Settings → Pages**.
3. Under **Build and deployment** choose **Deploy from a branch**, pick your branch (e.g. `main`) and the **/ (root)** folder, then **Save**.
4. After a minute your site is live at `https://<your-user>.github.io/<repo-name>/`.

## Looks (WordArt styles)

🌈 Rainbow · 🍬 Candy · 🧱 Chunky 3D · 🫧 Bubble Gum · ✏️ Outline · 🌃 Neon Sign · 🪙 Chrome · 🌉 Rainbow Arch · 〰️ Wavy

The 🌈 button in the corner cycles through the looks (and pins the one you pick).

## Moves (PowerPoint motions)

- **Entrances:** 🚀 Fly In · 🏀 Boing Bounce · 🔍 Big Zoom · 🌀 Spinny · 🪄 Magic Wipe · 🎈 Balloon Float · 🌱 Grow & Turn · 🪧 Swivel · ⌨️ Type-Type · 🌧️ Letter Rain
- **Emphasis:** 💓 Heartbeat · 🎢 Teeter · 🌊 The Wave · 🪩 Disco Colors · 🎡 Cartwheel · 🐘 Big & Tiny · 🍮 Jelly Wiggle · 🫨 Shake
- **Exit and return:** 🧨 Blast Off · 💥 Shatter · 🍂 Fall Apart
- **Everything at once:** 🎆 EVERYTHING! (also appears on runs 10, 25 and 50, and for words like `party`, `🎉`, `🥳`, `🎂`)

The chip strip under the text box picks a move; 🎲 Surprise goes back to random.

## Style show (auto play)

Under the move chips there is a second row that runs the show for you:

- **▶️ Auto Play** — keeps replaying your word, moving to the next style each time. Press it again (it reads **⏸ Stop**) to stop. It always starts off, so nothing moves until you ask.
- **🔀 Shuffle / ➡️ In Order** — whether the next style is picked at random or taken straight down the list. This also decides how styles are chosen on an ordinary Enter press.
- **⏱ menu** — how long to wait between styles: 1s, 2s, 3s, 5s, 8s or 15s. The wait starts when the current show finishes, so a long animation is never cut short.

Type a new word while the show is running and it carries on with the new word. The 🌈 corner button jumps straight to the next style without stopping the show. Starting the show releases a pinned look, so the styles really do keep changing — the move you pinned on the chip strip is kept. Shuffle and the interval are remembered next time; auto play is not.

On a narrow phone the three controls stay on one line and the strip slides sideways, the same way the move chips do.

## Extras

- 🔊 sound toggle (three tiny synthesized sounds, off by default), 🐢 Calm mode for gentler motion (also follows your system's reduced-motion setting).
- Keyboard: **Enter** = go, **Esc** clears the box, **↑/↓** change the move — or step through the ⏱ menu while it has the focus.
- Any input works: emoji families, flags, accents, CJK, Arabic, long phrases, empty box (it replays the last word).
