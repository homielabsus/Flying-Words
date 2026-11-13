# ✨ Flying Words

A one-file website for kids. Type anything — a word, your name, `🦖🦖🦖`, `こんにちは`, `#1 BEST!` — press **Enter** (or tap the big yellow **GO!**) and the text performs a WordArt **style** plus a PowerPoint-style **move**, in front of a **scene** if you like. Every press is a fresh surprise, confetti included. Love one? Tap **📸** to keep it as a picture, a GIF or a video.

## Open it

Double-click `index.html`. That's it — no install, no build step, no server needed. It also works offline (the optional Fredoka web font is only fetched when the page is served from a website). Only the 3D scenes and the photo booth's **✂️ Just me** and **✨ Sharper still** need the internet (the browser usually keeps what it fetched, so after the first time they tend to work offline too).

Works on phones, tablets and desktops. Tap a letter to make it hop; double-tap the stage to replay the last trick; tap 🎲 (or the yellow sticker) for a surprise. On a phone, **GO!** tucks the keyboard away so the show gets the whole screen; tap the word box to type again.

## Put it on GitHub Pages

1. Push this folder to a GitHub repository.
2. In the repo go to **Settings → Pages**.
3. Under **Build and deployment** choose **Deploy from a branch**, pick your branch (e.g. `main`) and the **/ (root)** folder, then **Save**.
4. After a minute your site is live at `https://<your-user>.github.io/<repo-name>/`.

## How the page is laid out

- **The stage** shows your word. The yellow sticker says which style and move are playing; the ⭐ counter in the other corner is your score. Tap the counter and it takes you to a tile you haven't found yet. The **📸** button in the bottom corner keeps what is on stage (see below), and **⛶** in the other corner goes full screen.
- **⛶ Full screen** makes the stage fill the whole screen, which is good for a tablet, a TV or a projector. The word box tucks away the moment full screen starts, so nothing covers the show. Tap the stage or just start typing and it floats back over the stage with 🎲 and **GO!** A tap keeps it for three seconds; once you tap into it or type, it waits 30 seconds after your last letter before it goes again. A **▶️** button starts and stops Auto Play. After three quiet seconds the buttons fade too, and a tap, a mouse move or a key brings them back. **Esc** or **⛶** again leaves full screen. Where the browser isn't allowed to go full screen (an iPhone, or inside the claude.ai preview), the stage fills the page's window instead.
- **The word box** has 🎲 (a random style and move) and **GO!** Pressing GO! with the box empty plays the example the box is showing (🦖🦖🦖, pizza …).
- **The toy box** has tabs. On a phone it sits under the word box as a row of big tiles you can swipe (two rows on a tablet held upright); on a wide screen it is a side panel of grids.
  - 🎨 **Styles** — every style draws "Wow" in itself, so you can see it before you pick it. Tap one and your word wears it straight away; tap it again to replay the word. 🎲 **Mix** goes back to a new style every time.
  - 🎬 **Moves** — each tile's emoji acts out its move when you point at it. Tap one to see your word do it. 🎲 **Mix** goes back to a new move every time.
  - 🏞️ **Scenes** — a world behind your word: Sunny Sky, Outer Space, Under the Sea, Rainbow, Sunset, Snow Day, Flower Garden, Dino Land, Candyland, Party Time, Magic Castle, Pirate Cove, Safari, Spooky Night, Movie Night and Choo-Choo Train, plus eleven 3D scenes (see below). Each one moves smoothly, at 60 frames a second, and stays until you pick another. Everything in them is drawn by the page itself, not with emoji, so a scene looks the same on every phone, tablet and computer: a smiling sun with a hot-air balloon and birds; a planet, a UFO and a rocket; clownfish, a jellyfish and a crab among coral; hearts floating past the rainbow; palm trees and a sailboat at sunset; a snowman, a penguin and a cabin in the snow; tulips, daisies, a sunflower, butterflies and a bee; dinosaurs, a pterodactyl and a volcano; lollipops, cupcakes and candy canes; balloons, bunting and presents; a fairy flying round a pink castle under a sleepy moon; a pirate ship, a parrot, a shark's fin and a treasure chest; an elephant, a giraffe, a lion and a monkey swinging on a vine; friendly ghosts, bats, pumpkins and a black cat by a haunted house; a happy tub of popcorn and a clapperboard between red curtains and searchlights; a steam train with a teddy on board, puffing past a windmill. 🎲 **Mix** goes back to the colour-changing stage. **📷 Camera** and **🖼️ Add Photo** put *you* behind your word (see below).
  - 😀 **Emoji** — tap to add emoji to your word (handy on computers with no emoji keyboard), plus ⌫ to delete one and 🧹 to clear.
  - 🎛️ **Show** — Auto Play, Shuffle, the ⏱ timer, 🔊 Sound and 🐢 Calm. On a wide screen these are always in view at the bottom of the panel instead.

Every strip and grid slides: drag it with a finger or the mouse, or roll the wheel over it. A faded edge means there is more that way.

## The game: find all 70 tricks

Every style and every move you make happen counts once toward the ⭐ counter (26 styles + 44 moves = 70). Only your own finds count: the welcome "Hello!" and the Auto Play show don't. Tiles you haven't found yet wear a pink **NEW** sticker, the tabs show how many are left, and a new find gets a **NEW** tag on the yellow sticker. Stuck? Tap the ⭐ counter and it points at a tile you still need. Find all 70 and the counter turns into a 🏆. Your finds are remembered on this device.

## Styles (WordArt)

🌈 Rainbow · 🍬 Candy · 🧱 Chunky 3D · 🫧 Bubble Gum · ✏️ Outline · 🌃 Neon Sign · 🪙 Chrome · 🌉 Rainbow Arch · 〰️ Wavy · 🦄 Unicorn · 🍭 Lollipop · ✨ Glitter · 🔥 Fire · 🧊 Ice · 🌌 Galaxy · 💥 Comic POW · 🎈 Balloons · 🍩 Sprinkles · 🐯 Tiger · 🍉 Melon · 🫠 Slime · 🌋 Lava · 💎 Diamond · 🍫 Chocolate · 🦕 Dino Scales · 🎬 Movie Star

The Mix stage colours change on every press, now from 14 colour pairs (strawberry lemonade, mermaid, cotton candy, ocean mint, grape soda and lemon-lime among them).

## Moves (PowerPoint motions)

- **Entrances:** 🚀 Fly In · 🏀 Boing Bounce · 🔍 Big Zoom · 🌀 Spinny · 🪄 Magic Wipe · 🎈 Balloon Float · 🌱 Grow & Turn · 🪧 Swivel · ⌨️ Type-Type · 🌧️ Letter Rain · 🦘 Kangaroo Hop · 🌪️ Tornado · 🐍 Snake · 🧲 Magnet · 🪀 Yo-Yo · 🏎️ Race Car · 🎇 Fireworks · 🪂 Parachute · ☄️ Shooting Stars · 👣 Stomp
- **Emphasis:** 💓 Heartbeat · 🎢 Teeter · 🌊 The Wave · 🪩 Disco Colors · 🎡 Cartwheel · 🐘 Big & Tiny · 🍮 Jelly Wiggle · 🫨 Shake · 🕺 Dance Party · 👻 Peekaboo · 🤸 Backflip · 📺 Glitch · 🎠 Carousel · 🀄 Dominoes
- **Exit and return:** 🧨 Blast Off · 💥 Shatter · 🍂 Fall Apart
- **At the movies:** 🎬 Movie Title (out of focus, then sharp, with a glint of light) · 🛸 Space Crawl (the word rises from the bottom of the screen, lying back) · 🕶️ Slow-Mo (it rushes in, hangs in the air, then snaps into place) · 🦸 Hero Landing · 🎭 Curtain Up · 🎰 Jackpot
- **Everything at once:** 🎆 Party! It also turns up by itself on runs 10, 25 and 50, and for words like `party`, `🎉`, `🥳`, `🎂`, unless you have pinned a move. A tile you picked always wins.

## 🧊 3D scenes

Eleven scenes are little films in real 3D, with a moving camera and characters that walk, swim, fly and blink. Their tiles carry a **3D** badge:

- 🚀 **Space Ride 3D** flies through the stars past planets, with a rocket and a flying saucer for company.
- 🌆 **Neon Sunset 3D** is a night drive down a glowing road towards a huge striped sun.
- 🧱 **Block World 3D** circles an island made of cubes, where a pig, a cow, sheep and chickens hop about.
- 🤖 **Robot Disco 3D** has three robots dancing on a floor of lights under a glitter ball.
- 🐉 **Dragon Sky 3D** follows a friendly dragon round a castle on a floating island, above the clouds at sunset.
- 🦖 **Dino Valley 3D** has a T-rex on patrol (he roars now and then), a long-neck eating leaves, a triceratops, a pterodactyl overhead, a baby peeping out of its egg, and a smoking volcano.
- 🐠 **Coral Reef 3D** is under the sea: a school of clownfish, blue tangs, a puffer fish, a turtle, a waving octopus, jellyfish, a crab, a whale going by, and a yellow submarine.
- 🐧 **Penguin Party 3D** has penguins skating on a frozen pond and one sliding down the hill on his tummy, a polar bear waving, a seal bouncing a ball, a snowman and the northern lights.
- 👨‍🚀 **Moon Pals 3D** has an astronaut bounding about in low gravity, little green aliens popping out of a crater, one in a flying saucer, a rover with eyes, and the Earth in the sky.
- 🦄 **Unicorn Land 3D** has three unicorns galloping round a meadow under a rainbow, a winged one flying over, and hopping bunnies.
- 🐞 **Bug Garden 3D** is down in the grass among flowers as tall as trees: ladybirds, bumblebees, a caterpillar, butterflies and a snail in no hurry.

They are drawn with [three.js](https://threejs.org) (release 128), which the page fetches from the cdnjs network the first time the Scenes tab is opened or a 3D scene is used. Until it arrives, and on a device with no internet or no 3D graphics, each of these scenes shows a flat poster of itself instead and everything else works as before. Only the 3D scene on the stage is kept in memory, so a phone is not asked to hold them all. **📸 Keep it** saves a 3D scene in pictures, GIFs and videos like any other.

## 📷 Your own photo as the scene

- **🖼️ Add Photo** picks a picture from the device (on a computer you can also drop one onto the page). It fills the stage behind your word, whatever style or move is playing.
- **📷 Camera** puts the live camera on the stage, so you can see yourself with the word flying in front of you. Tap **📸 Snap!**: it counts 3, 2, 1, and the photo becomes the scene. **✕** closes the camera. With more than one camera (a laptop's own and a USB webcam, or a phone's front and back), **🔄** switches between them, says which one is on, and remembers it for next time. A selfie camera is shown like a mirror and the photo is saved the way you saw it.
- Each photo gets its own tile (newest first, up to 6). The photo in use shows a **✕** on its tile to remove it.
- Photos never leave the device. They are kept in the browser's own storage for this page, so they are still there next time, until you remove them.
- If the camera is not allowed (inside the claude.ai preview, for example, or if you said no), the page says so: a phone or tablet opens its own camera app instead, and on a computer you can use **🖼️ Add Photo**. The live camera needs the page opened directly (from the file or GitHub Pages) in a browser that can use the camera.
- **📸 Keep it** saves the photo scene with your word like any other scene.

## ✂️ Photo booth: stand in the scene

With the camera on, three buttons above **📸 Snap!** choose what the camera keeps:

- **🖼️ All** — the whole picture, as described above.
- **✂️ Just me** — the page finds the person in the picture and takes the room away, so you stand in the scene you picked: under the sea, on the moon, next to the dinosaurs. It is live: the scene keeps playing behind you, the word flies in front of you, and you can tap other scenes to try them on while the camera is on. It works anywhere, with no cloth. It keeps the person: hair, face, clothes and what they are wearing (a hat, glasses, a backpack). Something held in the hand, like a ball or a toy, is usually cut away; for that, use the green screen. Hair is kept as a whole, with a smooth outline; single strands that stick out from it are not.
- **🟩 Green screen** — hang a cloth or sheet of one colour behind you (green or blue work best) and everything that is *not* the cloth is kept: you, your hat, your toys, your dog. The page reads the cloth's colour from the top corners of the picture by itself; **🎯** reads it again if the light changes or the cloth moves. The cloth has to reach the top corners of the picture. Do not wear the cloth's colour, or that part of you goes see-through too. No cloth up there (a plain wall, wood and skin colours do not count)? It says so, and **📸 Snap!** waits until there is one.

**📸 Snap!** then saves the cut-out, like an instant photo from a party booth:

- The cut-out is a sticker of you, trimmed to your outline, and it lands on the stage exactly where you were standing in the camera picture. It is not a scene: it stands *in front of* whichever scene is on (your own photos included) and *behind* the word, so you can change the scene, the style and the move around yourself. It is enlarged (up to twice, to 1600 pixels at most) and sharpened as it is saved, so hair, faces, hands and clothes stay crisp when the stage shows you bigger than the camera took you. The outline of a **✂️ Just me** cut-out is cut only at that final size, after its pixel steps have been rounded off, so it comes out smooth instead of stepped, and a touch inside the edge, which keeps the room's colour off the rim.
- **✨ Sharper still:** that first sharpening is there at once. Behind it the page draws the cut-out again with [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN), an AI upscaler: clean lines, crisp eyes and hair, smoother skin. Its tile shows ✨ while this runs (from a few seconds to a minute or two, depending on the device and the size of the cut-out); then the sharper picture takes the place of the first one, on the stage and in the device's store, and the page says "✨ Sharper!". You can go on playing meanwhile. Only cut-outs up to 800 pixels are redrawn: a bigger one (a sharp camera, a kid close to it) has detail enough of its own and would take minutes. With no internet, with the browser's data saver on, or on a device that turned out too slow, the first picture simply stays.
- **Move it:** put a finger or the mouse on it and drag. Only the solid part counts, so the see-through corners do not get in the way of the stage.
- **Resize it:** pinch with two fingers. With a mouse, click it: a dashed frame appears with a round yellow grip at its corner; pull the grip away from the middle to grow it, towards the middle to shrink it. The grip works by touch too. The frame goes away by itself after three seconds.
- **Several at once:** every cut-out you snap joins the others on the stage (you and your friends, or you three times). The one you touch comes to the front. Each has its own tile, marked ✂️ on a checked background: tap the tile to take that one out of the picture, tap again to put it back where it was; while it is in, the **✕** on the tile removes it for good.
- **📸 Keep it** puts the scene, every cut-out and the word into the picture, GIF or video, each cut-out where you left it. In GIFs and videos the scene and the word move and the cut-outs hold their pose.
- Cut-outs share the six places with your photos, are saved on the device the same way (with where they stand), and never leave it. When a seventh picture arrives the oldest one goes: one that is not on the stage if there is one, and never the photo that is the scene. The page remembers which button you used last.

How it works: **✂️ Just me** uses Google's [MediaPipe](https://github.com/google-ai-edge/mediapipe) image segmenter (`@mediapipe/tasks-vision` 0.10.14, from the jsDelivr network) with its *selfie multiclass* model (from Google's model storage), about 26 MB together, fetched only when **✂️ Just me** is switched on (the button shows a dashed edge while it loads, and **📸 Snap!** waits). Each of the four files is checked against a hash written in the page before it is used, so a file that was changed on the way is not run. The camera picture is worked on inside the browser; nothing is uploaded. Without internet the page says so and the camera goes back to the whole picture. **🟩 Green screen** is done by the page itself and needs no internet.

**✨ Sharper still** uses Real-ESRGAN's small general model (`realesr-general-x4v3`, BSD 3-Clause, 5 MB), run by [ONNX Runtime Web](https://github.com/microsoft/onnxruntime) (MIT, about 11 MB from the jsDelivr network), in a worker so the page stays lively. The model file is in this repository (`models/`, with its licence and a note on where it comes from): the page takes it from beside itself when it is served as a website, and from the repository's copy on jsDelivr when it is opened as a file (or when it is not found beside the page). All four files are hash-checked before use. Nothing is fetched until the first cut-out is snapped; that first snap fetches about 16 MB, whichever way the cut-out was made, the green screen included. The picture is worked on inside the browser; nothing is uploaded.

## 📸 Keep it: save a picture, a GIF or a video

Saw one you love? Tap **📸** on the stage. You keep exactly what was playing: the same word, style, move, colours and scene, down to where each letter rained in from.

- Change the word if you like, then pick **🖼️ Picture** (PNG), **📷 Photo** (JPEG), **🎞️ GIF** (it moves and loops) or **🎬 Video** (MP4), and one of eight shapes. Each shape tile draws its own outline:

  | Shape | Ratio | Picture / Photo | GIF | Video |
  |---|---|---|---|---|
  | Square | 1:1 | 1080×1080 | 480×480 | 1080×1080 |
  | Wide | 16:9 | 1920×1080 | 640×360 | 1280×720 |
  | Tall | 9:16 | 1080×1920 | 360×640 | 720×1280 |
  | Tablet | 4:3 | 1440×1080 | 560×420 | 960×720 |
  | Portrait | 3:4 | 1080×1440 | 420×560 | 720×960 |
  | Poster | 4:5 | 1080×1350 | 384×480 | 864×1080 |
  | Postcard | 3:2 | 1620×1080 | 600×400 | 1080×720 |
  | Movie | 21:9 | 2520×1080 | 700×300 | 1680×720 |

- The preview shows what you will get. Tap **✨ Make**, watch it appear, then **⬇️ Save it!** The dialog remembers your last format and shape.
- On a phone or tablet, **📤 Share** can put it straight into Photos or a message.
- Videos play at 60 frames a second, as smooth as the stage (GIFs stay at 15, to keep them small). They are H.264 MP4 in Chrome, Edge and Safari. A browser without an H.264 encoder (some Linux builds) writes the MP4 with VP9 instead, and one with no video encoder at all records a WebM.
- Everything happens on your device: nothing is uploaded.

## Style show (auto play)

- **▶️ Auto Play** — keeps replaying your word, moving to the next style each time. Press it again (it reads **⏸ Stop**) to stop. It always starts off, so nothing moves until you ask.
- **🔀 Shuffle / ➡️ In Order** — 🔀 shuffles *everything*: every press gets a random style **and** a random move, and a pinned tile cannot hold it still (turning Shuffle on releases the pins). ➡️ In Order walks the styles down the list instead, carrying on from the last style you picked, and keeps whatever you pinned. Picking a style or a move while shuffling switches the toggle to In Order, so the two never disagree.
- **⏱ menu** — how long to wait between styles: 1s, 2s, 3s, 5s, 8s or 15s. The wait starts when the current show finishes, so a long animation is never cut short.

Type a new word while the show is running and it carries on with the new word. Tapping a style tile (or 🎲 Mix) during the show jumps straight to it, gives it a full turn, and the show carries on from there. Starting the show releases a pinned style, so the styles really do keep changing — the move you pinned is kept. Shuffle, the timer and your last tab are remembered next time; auto play is not.

## Extras

- 🔊 sound (a few tiny synthesized sounds, off by default), 🐢 Calm mode for gentler motion (also follows your system's reduced-motion setting); with Calm on, scenes stand still too.
- Keyboard: **Enter** = go, **Esc** clears the box (or closes the camera, or leaves full screen), **↑/↓** in the word box change the move, **←/→** move between the toy box tabs, and ↑/↓ step through the ⏱ menu while it has the focus.
- Any input works: emoji families, flags, accents, CJK, Arabic, long phrases. An empty box plays the example it shows, or replays your last word.
- A first-time hint points at the word box until the first word is typed.
