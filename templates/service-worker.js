var cacheName = "perris-v3";
var filesToCache = [
    "/",
    "/index.html",
    "/gallery.html",
    "/registro.html",
    "/js/app.js",
    "/js/region.js",
    "/js/validator.js",
    "/styles/mainMedio.css",
    "/styles/mainS5.css",
    "/styles/mainTablet.css",
    "/styles/menu.css",
    "/styles/Antaro.ttf",
    "/styles/AustieBostKittenKlub.ttf",
    "/styles/Cartoon.ttf",
    "/img/correo50.png",
    "/img/face50.png",
    "/img/galeria1.jpg",
    "/img/galeria2.jpg",
    "/img/galeria3.jpg",
    "/img/galeria4.jpeg",
    "/img/galeria5.jpg",
    "/img/galeria6.jpg",
    "/img/google50.png",
    "/img/insta50.png",
    "/img/logo.png",
    "/img/logo50.png",
    "/img/logo100.png",
    "/img/perro1.jpg",
    "/img/perro2.jpg",
    "/img/perro3.jpg",
    "/img/perro4.jpg",
    "/img/perro200-300.jpg",
    "/img/perro200.jpg",
    "/img/perro400-300.jpg",
    "/img/perro400.jpg"
];

self.addEventListener( 'install', function( e ) {
    console.log( '[ServiceWorker] Install' );
    e.waitUntil(
        caches.open( cacheName ).then( function( cache ) {
            console.log( '[ServiceWorker] Caching app shell' );
            return cache.addAll( filesToCache );
        } )
    );
} );

self.addEventListener( 'activate', function( e ) {
    console.log( '[ServiceWorker] Activate' );
    e.waitUntil(
        caches.keys( ).then( function( keyList ) {
            return Promise.all( keyList.map( function( key ) {
                if ( key != cacheName ) {
                    console.log('[ServiceWorker] Removing old cache', key);
                    return caches.delete( key );
                }
            }));
        })
    );
    return self.clients.claim();
});

self.addEventListener( 'fetch', function( e ) {
    console.log( '[ServiceWorker] Fetch', e.request.url );
    e.respondWith(
        caches.match( e.request ).then( function( response ) {
            return response || fetch( e.request );
        } )
    );
} );