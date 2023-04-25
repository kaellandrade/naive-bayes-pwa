const cacheName = "pet-indica";

const urlsToCache = [
  "/",
  "index.html",
  "styles.css",
  "python/main.py",
  "https://cdn.jsdelivr.net/pyodide/v0.23.1/full/pyodide.js",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(cacheName).then((cache) => {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      console.log(response);
      if (response) {
        return response;
      }

      return fetch(event.request).then((response) => {
        return caches.open(cacheName).then((cache) => {
          cache.put(event.request, response.clone());
          return response;
        });
      });
    })
  );
});
