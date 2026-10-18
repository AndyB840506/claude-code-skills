# T3 (conversacional, dos hosts): qué cambia en el launch
Vigente desde el EP.01 de T3 (2026-10-03). El resto de la skill es de T2 (solo, con guion).
Ejemplo completo: btq-production/launch-assets/T3-EP01-escampadero-launch.md

## Antes de escribir nada
- No hay guion: la fuente es el SRT, leído entero.
- Mapear hablantes por una línea que se nombre ("Yo soy Andy") y medir el reparto de voz.
- Escribir en el launch file la lista "fuera de todo texto escrito" ANTES de redactar:
  acusaciones a empresas identificables, personas con nombre en tono negativo,
  ilegalidades. Las nombradas en tono positivo tampoco van sin su permiso.

## Título
`EP.NN — <frase dicha en el episodio>: <gancho con keyword call center/BPO>`. Sin
teórico. Ninguna cifra que el audio no sostenga para los dos hosts. Todas las opciones
que se propongan cumplen el formato (chequeo: cada una matchea `(?i)call center|bpo`); si
el host elige una sin keyword, avisarlo una vez.

## Descripción (§A)
Se mantiene: 250-400 palabras contadas con script, usted, sin rayas ni angulares,
pregunta personal, "Escúchalo ahora en Spotify.", contacto, HTML + texto. No aplica:
abrir con referencia cultural. Cada afirmación anotada con su timestamp del SRT.
Términos de industria en inglés quedan en inglés, también en citas (atrición →
attrition, decisión de Andy en EP.02).

## Piezas (compuestas con PIL, nunca generadas)
Portada: comfyui/templates/btq-portada-t3.py · Redes: comfyui/templates/btq-social-t3.py
(citas TEXTUALES del SRT, zonas seguras de stories/reels ya incluidas). El texto de cada
episodio va en `EPS` (`btq-social-t3.py <out> EP.NN`). Al editar el generador, correr el
EP.01 con la versión anterior (`git show <sha>:<ruta>`) y con la nueva y diffear: 0 px salvo
lo buscado (no contra lo publicado: sus 3 piezas con cita difieren a propósito desde 5ab4690).
PIL `Errno 22` al guardar = archivo abierto en un visor (no aislado): generar en temporal.
Portada/teaser = oración completa: al recortar el título no se quita el sujeto (EP.02).

## Plan social (§B)
Sin artículo, así que el primer comentario lleva siempre Spotify. LinkedIn en primera
persona: la @-mención del co-host se hace a mano. Si un post usa una anécdota personal
del host, avisarle antes.

## Clip (§E)
No sale de una quote card (en T2 sí): se elige del SRT con el gancho al inicio y la lámina
del reel lleva una cita de ese clip (`reel_quote`). Bordes y MP4: step2-generate-assets.md
§E (re-transcribir el clip solo; `-t`, no `-shortest`).

## Web
El embed del show muestra el último episodio publicado: commitear la web antes y
desplegar (`vercel --prod`) solo cuando el episodio ya esté en línea. Excepción si Andy
pide teaser antes (EP.02): tarjeta con fecha y botón al show; al salir, botón al link del
episodio y redeploy; antes, el oEmbed del link debe devolver el título del episodio, y
después `curl -L` del sitio + diff contra el local. El preview tiene Vercel Auth: `curl` da 200 con el login (mirar el
`<title>`), así que la revisión del preview la hace Andy.
