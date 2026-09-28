# ✨ Flying Words

A one-file website for kids. Type anything — a word, your name, `🦖🦖🦖`, `こんにちは`, `#1 BEST!` — press **Enter** (or tap the big yellow **GO!**) and the text performs a WordArt **style** plus a PowerPoint-style **move**. Every press is a fresh surprise, confetti included.

## Open it

Double-click `index.html`. That's it — no install, no build step, no server needed. It also works offline (the optional Fredoka web font is only fetched when the page is served from a website).

Works on phones, tablets and desktops. Tap a letter to make it hop; double-tap the stage to replay the last trick; tap 🎲 (or the yellow sticker) for a surprise. On a phone, **GO!** tucks the keyboard away so the show gets the whole screen; tap the word box to type again.

## Put it on GitHub Pages

1. Push this folder to a GitHub repository.
2. In the repo go to **Settings → Pages**.
3. Under **Build and deployment** choose **Deploy from a branch**, pick your branch (e.g. `main`) and the **/ (root)** folder, then **Save**.
4. After a minute your site is live at `https://<your-user>.github.io/<repo-name>/`.

## How the page is laid out

- **The stage** shows your word. The yellow sticker says which style and move are playing; the ⭐ counter in the other corner is your score. Tap the counter and it takes you to a tile you haven't found yet.
- **The word box** has 🎲 (a random style and move) and **GO!** Pressing GO! with the box empty plays the example the box is showing (🦖🦖🦖, pizza …).
- **The toy box** has tabs. On a phone it sits under the word box as a row of big tiles you can swipe (two rows on a tablet held upright); on a wide screen it is a side panel of grids.
  - 🎨 **Styles** — every style draws "Wow" in itself, so you can see it before you pick it. Tap one and your word wears it straight away; tap it again to replay the word. 🎲 **Mix** goes back to a new style every time.
  - 🎬 **Moves** — each tile's emoji acts out its move when you point at it. Tap one to see your word do it. 🎲 **Mix** goes back to a new move every time.
  - 😀 **Emoji** — tap to add emoji to your word (handy on computers with no emoji keyboard), plus ⌫ to delete one and 🧹 to clear.
  - 🎛️ **Show** — Auto Play, Shuffle, the ⏱ timer, 🔊 Sound and 🐢 Calm. On a wide screen these are always in view at the bottom of the panel instead.

Every strip and grid slides: drag it with a finger or the mouse, or roll the wheel over it. A faded edge means there is more that way.

## The game: find all 31 tricks

Every style and every move you make happen counts once toward the ⭐ counter (9 styles + 22 moves = 31). Only your own finds count: the welcome "Hello!" and the Auto Play show don't. Tiles you haven't found yet wear a pink **NEW** sticker, the tabs show how many are left, and a new find gets a **NEW** tag on the yellow sticker. Stuck? Tap the ⭐ counter and it points at a tile you still need. Find all 31 and the counter turns into a 🏆. Your finds are remembered on this device.

## Styles (WordArt)

🌈 Rainbow · 🍬 Candy · 🧱 Chunky 3D · 🫧 Bubble Gum · ✏️ Outline · 🌃 Neon Sign · 🪙 Chrome · 🌉 Rainbow Arch · 〰️ Wavy

## Moves (PowerPoint motions)

- **Entrances:** 🚀 Fly In · 🏀 Boing Bounce · 🔍 Big Zoom · 🌀 Spinny · 🪄 Magic Wipe · 🎈 Balloon Float · 🌱 Grow & Turn · 🪧 Swivel · ⌨️ Type-Type · 🌧️ Letter Rain
- **Emphasis:** 💓 Heartbeat · 🎢 Teeter · 🌊 The Wave · 🪩 Disco Colors · 🎡 Cartwheel · 🐘 Big & Tiny · 🍮 Jelly Wiggle · 🫨 Shake
- **Exit and return:** 🧨 Blast Off · 💥 Shatter · 🍂 Fall Apart
- **Everything at once:** 🎆 Party! It also turns up by itself on runs 10, 25 and 50, and for words like `party`, `🎉`, `🥳`, `🎂`, unless you have pinned a move. A tile you picked always wins.

## Style show (auto play)

- **▶️ Auto Play** — keeps replaying your word, moving to the next style each time. Press it again (it reads **⏸ Stop**) to stop. It always starts off, so nothing moves until you ask.
- **🔀 Shuffle / ➡️ In Order** — 🔀 shuffles *everything*: every press gets a random style **and** a random move, and a pinned tile cannot hold it still (turning Shuffle on releases the pins). ➡️ In Order walks the styles down the list instead, carrying on from the last style you picked, and keeps whatever you pinned. Picking a style or a move while shuffling switches the toggle to In Order, so the two never disagree.
- **⏱ menu** — how long to wait between styles: 1s, 2s, 3s, 5s, 8s or 15s. The wait starts when the current show finishes, so a long animation is never cut short.

Type a new word while the show is running and it carries on with the new word. Tapping a style tile (or 🎲 Mix) during the show jumps straight to it, gives it a full turn, and the show carries on from there. Starting the show releases a pinned style, so the styles really do keep changing — the move you pinned is kept. Shuffle, the timer and your last tab are remembered next time; auto play is not.

## Extras

- 🔊 sound (a few tiny synthesized sounds, off by default), 🐢 Calm mode for gentler motion (also follows your system's reduced-motion setting).
- Keyboard: **Enter** = go, **Esc** clears the box, **↑/↓** in the word box change the move, **←/→** move between the toy box tabs, and ↑/↓ step through the ⏱ menu while it has the focus.
- Any input works: emoji families, flags, accents, CJK, Arabic, long phrases. An empty box plays the example it shows, or replays your last word.
- A first-time hint points at the word box until the first word is typed.
