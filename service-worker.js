const cacheName = "pet-indica";

// const urlsToCache = [
//   "/",
//   "styles.css",
//   "https://cdn.jsdelivr.net/pyodide/v0.23.1/full/pyodide.js",
//   "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css",
// ];

// self.addEventListener("install", (event) => {
//   event.waitUntil(
//     caches.open(cacheName).then((cache) => {
//       return cache.addAll(urlsToCache);
//     })
//   );
// });

// self.addEventListener("fetch", (event) => {
//   // Evita que o arquivo python  seja carregado em cache e nao altere os seus dados
//   if (event.request.url.includes("main.py")) {
//     console.log("URL NAO CHAMADA: ", event.request.url);
//     return; // Ignora a solicitação fecth do arquivo python
//   }
//   event.respondWith(
//     caches.match(event.request).then((response) => {
//       if (response) {
//         return response;
//       }

//       return fetch(event.request).then((response) => {
//         return caches.open(cacheName).then((cache) => {
//           cache.put(event.request, response.clone());
//           return response;
//         });
//       });
//     })
//   );
// });
