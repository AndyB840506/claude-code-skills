# Puntos de pausa (los únicos donde el flujo se detiene)

1. **Stage A — confirmación del episodio + aprobación del guion**: inevitable, el
   roadmap y el guion son decisiones del usuario, no del pipeline
2. **Cierre de Stage A — "ve a grabar"**: pausa estructural más larga del ciclo —
   el episodio queda en `stage_a: complete` esperando que exista un audio grabado
3. **Stage B.0 — Intake**: inevitable, necesita los datos crudos del episodio recién
   grabado (a menos que ya vengan del checkpoint)
4. **Stage B.2 (ruta BTQ) — gate de `episode-launch`**: heredado del skill que
   invocamos, no es un bug del pipeline — déjalo aparecer con normalidad
5. **Cierre de Stage B — checkpoint de Spotify**: pausa estructural — no existe API de
   publicación; el usuario debe subir el episodio a Spotify for Podcasters y reportar
   la URL en vivo. Si el pipeline se invoca de nuevo antes de que esto se resuelva, el
   Paso 0 de `00-intake.md` lo detecta y se detiene aquí mismo (este es el punto que
   habría atrapado el caso de BTQ EP.16)
6. **Stage C.3 / C.3b — Pausa(s) de generación de imagen**: estructural, no existe API
   de generación automática; el usuario debe generar en Flow/Nani Banana y reportar
   rutas (cover-art en C.3, quote cards en C.3b)
7. **Stage C.5 — Gate final de aprobación**: el único gate explícitamente pedido por
   el usuario — muestra el resumen completo de lo que está por publicarse antes de
   `vercel --prod`

Fuera de estos puntos, el pipeline corre sin interrupciones — y entre macro-stages,
siempre puede cerrarse y retomarse en una sesión distinta gracias al archivo de estado.
