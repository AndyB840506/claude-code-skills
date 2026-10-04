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
teórico. Ninguna cifra que el audio no sostenga para los dos hosts.

## Descripción (§A)
Se mantiene: 250-400 palabras contadas con script, usted, sin rayas ni angulares,
pregunta personal, "Escúchalo ahora en Spotify.", contacto, HTML + texto. No aplica:
abrir con referencia cultural. Cada afirmación anotada con su timestamp del SRT.

## Piezas (compuestas con PIL, nunca generadas)
Portada: comfyui/templates/btq-portada-t3.py · Redes: comfyui/templates/btq-social-t3.py
(citas TEXTUALES del SRT, zonas seguras de stories/reels ya incluidas).

## Plan social (§B)
Sin artículo, así que el primer comentario lleva siempre Spotify. LinkedIn en primera
persona: la @-mención del co-host se hace a mano. Si un post usa una anécdota personal
del host, avisarle antes.

## Clip (§E)
Sin quote cards: elegirlo del SRT con el gancho al inicio.

## Web
El embed del show muestra el último episodio publicado: commitear la web antes y
desplegar (`vercel --prod`) solo cuando el episodio ya esté en línea.
