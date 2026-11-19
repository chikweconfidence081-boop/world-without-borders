// Offline cache for World Without Borders 3D. Bump VERSION with every release.
const VERSION = "wwb3d-v1.0.1";
const FILES = ["./", "index.html", "manifest.json", "js/engine.js", "js/world.js", "js/characters.js", "js/game.js",
  "assets/logo.jpg", "assets/icon-192.png", "assets/icon-512.png"];
self.addEventListener("install", (e) => { e.waitUntil(caches.open(VERSION).then((c) => c.addAll(FILES))); self.skipWaiting(); });
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  e.respondWith(fetch(e.request).then((r) => { const copy = r.clone(); caches.open(VERSION).then((c) => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request)));
});
