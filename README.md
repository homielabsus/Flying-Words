# ✨ Flying Words

A one-file website for kids. Type anything — a word, your name, `🦖🦖🦖`, `こんにちは`, `#1 BEST!` — press **Enter** (or tap the big yellow **GO!**) and the text performs a WordArt **style** plus a PowerPoint-style **move**, in front of a **scene** if you like. Every press is a fresh surprise, confetti included. Love one? Tap **📸** to keep it as a picture, a GIF or a video.

## Open it

Double-click `index.html`. That's it — no install, no build step, no server needed. It also works offline (the optional Fredoka web font is only fetched when the page is served from a website).

Works on phones, tablets and desktops. Tap a letter to make it hop; double-tap the stage to replay the last trick; tap 🎲 (or the yellow sticker) for a surprise. On a phone, **GO!** tucks the keyboard away so the show gets the whole screen; tap the word box to type again.

## Put it on GitHub Pages

1. Push this folder to a GitHub repository.
2. In the repo go to **Settings → Pages**.
3. Under **Build and deployment** choose **Deploy from a branch**, pick your branch (e.g. `main`) and the **/ (root)** folder, then **Save**.
4. After a minute your site is live at `https://<your-user>.github.io/<repo-name>/`.

## How the page is laid out

- **The stage** shows your word. The yellow sticker says which style and move are playing; the ⭐ counter in the other corner is your score. Tap the counter and it takes you to a tile you haven't found yet. The **📸** button in the bottom corner keeps what is on stage (see below).
- **The word box** has 🎲 (a random style and move) and **GO!** Pressing GO! with the box empty plays the example the box is showing (🦖🦖🦖, pizza …).
- **The toy box** has tabs. On a phone it sits under the word box as a row of big tiles you can swipe (two rows on a tablet held upright); on a wide screen it is a side panel of grids.
  - 🎨 **Styles** — every style draws "Wow" in itself, so you can see it before you pick it. Tap one and your word wears it straight away; tap it again to replay the word. 🎲 **Mix** goes back to a new style every time.
  - 🎬 **Moves** — each tile's emoji acts out its move when you point at it. Tap one to see your word do it. 🎲 **Mix** goes back to a new move every time.
  - 🏞️ **Scenes** — a world behind your word: Sunny Sky, Outer Space, Under the Sea, Rainbow, Sunset, Snow Day, Flower Garden, Dino Land, Candyland, Party Time and Magic Castle. Each one moves (clouds drift, fish swim, stars twinkle) and stays until you pick another. 🎲 **Mix** goes back to the colour-changing stage.
  - 😀 **Emoji** — tap to add emoji to your word (handy on computers with no emoji keyboard), plus ⌫ to delete one and 🧹 to clear.
  - 🎛️ **Show** — Auto Play, Shuffle, the ⏱ timer, 🔊 Sound and 🐢 Calm. On a wide screen these are always in view at the bottom of the panel instead.

Every strip and grid slides: drag it with a finger or the mouse, or roll the wheel over it. A faded edge means there is more that way.

## The game: find all 50 tricks

Every style and every move you make happen counts once toward the ⭐ counter (18 styles + 32 moves = 50). Only your own finds count: the welcome "Hello!" and the Auto Play show don't. Tiles you haven't found yet wear a pink **NEW** sticker, the tabs show how many are left, and a new find gets a **NEW** tag on the yellow sticker. Stuck? Tap the ⭐ counter and it points at a tile you still need. Find all 50 and the counter turns into a 🏆. Your finds are remembered on this device.

## Styles (WordArt)

🌈 Rainbow · 🍬 Candy · 🧱 Chunky 3D · 🫧 Bubble Gum · ✏️ Outline · 🌃 Neon Sign · 🪙 Chrome · 🌉 Rainbow Arch · 〰️ Wavy · 🦄 Unicorn · 🍭 Lollipop · ✨ Glitter · 🔥 Fire · 🧊 Ice · 🌌 Galaxy · 💥 Comic POW · 🎈 Balloons · 🍩 Sprinkles

The Mix stage colours change on every press, now from 14 colour pairs (strawberry lemonade, mermaid, cotton candy, ocean mint, grape soda and lemon-lime among them).

## Moves (PowerPoint motions)

- **Entrances:** 🚀 Fly In · 🏀 Boing Bounce · 🔍 Big Zoom · 🌀 Spinny · 🪄 Magic Wipe · 🎈 Balloon Float · 🌱 Grow & Turn · 🪧 Swivel · ⌨️ Type-Type · 🌧️ Letter Rain · 🦘 Kangaroo Hop · 🌪️ Tornado · 🐍 Snake · 🧲 Magnet · 🪀 Yo-Yo · 🏎️ Race Car · 🎇 Fireworks
- **Emphasis:** 💓 Heartbeat · 🎢 Teeter · 🌊 The Wave · 🪩 Disco Colors · 🎡 Cartwheel · 🐘 Big & Tiny · 🍮 Jelly Wiggle · 🫨 Shake · 🕺 Dance Party · 👻 Peekaboo · 🤸 Backflip
- **Exit and return:** 🧨 Blast Off · 💥 Shatter · 🍂 Fall Apart
- **Everything at once:** 🎆 Party! It also turns up by itself on runs 10, 25 and 50, and for words like `party`, `🎉`, `🥳`, `🎂`, unless you have pinned a move. A tile you picked always wins.

## 📸 Keep it: save a picture, a GIF or a video

Saw one you love? Tap **📸** on the stage. You keep exactly what was playing: the same word, style, move, colours and scene, down to where each letter rained in from.

- Change the word if you like, then pick **🖼️ Picture** (PNG), **📷 Photo** (JPEG), **🎞️ GIF** (it moves and loops) or **🎬 Video** (MP4), and a shape: **Square**, **Wide** or **Tall**.
- The preview shows what you will get. Tap **✨ Make**, watch it appear, then **⬇️ Save it!**
- Pictures are 1080 pixels on the short side (1920×1080 when wide), GIFs 480 pixels, videos 1080×1080 or 720p.
- On a phone or tablet, **📤 Share** can put it straight into Photos or a message.
- Videos are H.264 MP4 in Chrome, Edge and Safari. A browser without an H.264 encoder (some Linux builds) writes the MP4 with VP9 instead, and one with no video encoder at all records a WebM.
- Everything happens on your device: nothing is uploaded.

## Style show (auto play)

- **▶️ Auto Play** — keeps replaying your word, moving to the next style each time. Press it again (it reads **⏸ Stop**) to stop. It always starts off, so nothing moves until you ask.
- **🔀 Shuffle / ➡️ In Order** — 🔀 shuffles *everything*: every press gets a random style **and** a random move, and a pinned tile cannot hold it still (turning Shuffle on releases the pins). ➡️ In Order walks the styles down the list instead, carrying on from the last style you picked, and keeps whatever you pinned. Picking a style or a move while shuffling switches the toggle to In Order, so the two never disagree.
- **⏱ menu** — how long to wait between styles: 1s, 2s, 3s, 5s, 8s or 15s. The wait starts when the current show finishes, so a long animation is never cut short.

Type a new word while the show is running and it carries on with the new word. Tapping a style tile (or 🎲 Mix) during the show jumps straight to it, gives it a full turn, and the show carries on from there. Starting the show releases a pinned style, so the styles really do keep changing — the move you pinned is kept. Shuffle, the timer and your last tab are remembered next time; auto play is not.

## Extras

- 🔊 sound (a few tiny synthesized sounds, off by default), 🐢 Calm mode for gentler motion (also follows your system's reduced-motion setting); with Calm on, scenes stand still too.
- Keyboard: **Enter** = go, **Esc** clears the box, **↑/↓** in the word box change the move, **←/→** move between the toy box tabs, and ↑/↓ step through the ⏱ menu while it has the focus.
- Any input works: emoji families, flags, accents, CJK, Arabic, long phrases. An empty box plays the example it shows, or replays your last word.
- A first-time hint points at the word box until the first word is typed.
