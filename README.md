# World Without Borders 3D, v1.0.1

A friendly 3D life simulator. Create your character, look after their needs, work jobs, buy a home, invest in businesses, make friends and become a legend of New Horizon.

## Play on Windows
| Option | How |
|---|---|
| **Quickest** | Double-click `game\index.html`. It opens in Chrome or Edge. |
| **Game window** | Double-click `Play_World_Without_Borders.bat`. It opens the game in its own window (needs Python). |
| **Standalone .exe** | Double-click `build_exe.bat`, which produces `dist\WorldWithoutBorders3D.exe`. You can share that file; players don't need Python. |

The .exe opens the game in its own window using Microsoft Edge, which is built into Windows, so nothing extra needs installing.
Your save stays on your computer.

**Requirements:** a graphics card or chip with WebGL2. Any PC, phone or tablet from about 2017 onwards works.

## Get the Android APK (free, built in the cloud by GitHub)
You don't need to install anything on your PC.
1. Sign in at **github.com** and click **New repository**. Name it `world-without-borders`, choose **Private**, and click **Create repository**.
2. Click **uploading an existing file**. In File Explorer turn on *View > Show > Hidden items*, then drag in **everything inside this folder**, including the hidden `.github` folder. Click **Commit changes**.
3. Open the **Actions** tab. If asked, click **I understand my workflows, go ahead and enable them**.
4. Click **Build Android APK**, then **Run workflow**, then the green **Run workflow** button.
5. After about 6-10 minutes the run shows a green tick. Open it, scroll to **Artifacts** and download **WorldWithoutBorders3D-android**. It's a zip with `WorldWithoutBorders3D.apk` inside.
6. Copy the APK to your phone and open it. Android asks you to allow installing apps from this source; allow it, then tap **Install**.

**Updating:** upload the changed files, then run the workflow again. Every build is signed with the same key in `android-signing/`, so new versions install over the old one and **keep your save**. Keep the repository private, and don't lose that key.
**Release page:** to get a permanent download link, create a tag such as `v1.0.1` (*Releases > Draft a new release > Choose a tag*). The APK is attached automatically.
**Website (optional):** *Settings > Pages > Source: GitHub Actions*, then run **Publish website**. The game goes online and installs to a phone home screen from the browser menu.

## How to play
- **Click or tap** the ground to walk. Click a **building** or **person** to go there automatically.
- **WASD / arrow keys** to walk, **Shift** to run, **E** to interact.
- **Drag** to turn the camera, **scroll or pinch** to zoom.
- **⏸ ▶ ⏩ ⏭** by the clock control the speed of time.
- **Goal card** (bottom left): press **Go** and your character walks to the next objective.

### Needs
⚡ Energy, 🍔 Food, 🎉 Fun and 💬 Social go down over time. A happy character earns up to **15% more** at work. A miserable one earns 20% less.

| Need | Where to fix it |
|---|---|
| ⚡ Energy | Sleep at your home (free) or the Skyline Hotel; energy drink at Unity Market |
| 🍔 Food | Snack box at Unity Market, cook at home, fine dining at the hotel |
| 🎉 Fun | Fountain at Orbit Plaza, Arena challenges, video games at home |
| 💬 Social | Talk to residents, community event at Orbit Plaza |

### The city
| Place | What you can do |
|---|---|
| 🏛️ Orbit Plaza | Daily bonus, fountain, community event, notice board |
| 🏦 Nova Bank | Savings earn 2% interest every day |
| 🏨 Skyline Hotel | Dinner, rooms, and a penthouse (level 6) |
| 🛒 Unity Market | Food and energy drinks; invest 350 (+40/day) |
| 🏡 Your Future Home | Buy for 500: free sleep, cooking and games |
| 🎬 Creator Hub | Film content; invest 900 (level 2, +95/day) |
| 🏟️ Global Arena | Timing challenge for coins, XP and gems |
| ⚓ Port Authority | Dock shifts: steady pay |
| 💻 Tech District | Code sprints (level 3); invest 2,000 (level 4, +210/day) |

Businesses pay out at midnight. Lifestyles give perks: Explorer, Entrepreneur, Creator, Athlete or Engineer.
There are 10 life goals, from your first steps up to **City Legend** (level 8).

## Technical notes
- 100% offline, no internet needed. A small custom WebGL2 engine (`game/js/engine.js`) with real-time shadows, day/night lighting and glowing street lights.
- Files: `engine.js` (3D renderer), `world.js` (city, collisions, pathfinding), `characters.js` (3D characters and cars), `game.js` (life-sim rules and interface).
- Saves use browser storage under a fixed local address, so the .exe always finds your save.
- Android: Capacitor app shell (`package.json`, `capacitor.config.json`), icons in `resources/`, cloud build in `.github/workflows/android.yml`. The hardware back button closes menus.
- Google Play: needs a signed App Bundle (.aab) and a Play Console account. The signing key here can be your upload key.
