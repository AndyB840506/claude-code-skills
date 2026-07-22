# Pipeline Audit — BTQ EP.023

## Stage A — Roadmap y pre-producción

### Paso 1 — Confirmar episodio (con un giro de rumbo a mitad de camino)
- Arranque: EP.022 confirmado como fila `publicado` en `roadmap-btq.md` (estaba
  desactualizada en `guion listo` — corregida con la URL real de Spotify verificada en
  el handoff, no copiada por error de otro episodio). Roadmap no tenía fila para
  EP.023 ni tema confirmado.
- Primera ronda: siguiendo la regla de rotación vigente en ese momento (pilar SEO /
  pop-culture cada 3-4 episodios, EP.022 fue el pilar SEO), se presentaron 3
  candidatos pop-culture investigados y verificados (Metallica, Matrix, Star Wars) vía
  AskUserQuestion — Andy eligió Matrix. Guion completo escrito y aprobado sobre ese
  tema (ver Paso 2 más abajo, primera iteración).
- Giro de rumbo: a mitad de revisión del guion de Matrix, Andy cuestionó el desempeño
  de los episodios pop-culture recientes (Gladiator EP.019 y Los Simpson EP.021, ambos
  "no tan bien") frente al pilar SEO (EP.020, "muy bien") y pidió un giro completo a
  100% pilar SEO — no caso por caso, permanente. Confirmado vía AskUserQuestion
  (2 preguntas: qué hacer con el guion de Matrix ya escrito → descartarlo; alcance del
  giro → permanente).
- Guion de Matrix eliminado del disco (no archivado, por instrucción explícita).
  `roadmap-btq.md` reescrito: fila EP.022 corregida, fila EP.023 puesta en blanco,
  sección "Estrategia editorial" reestructurada con el giro documentado, las reglas de
  pop-cultura retiradas (no borradas) y marcadas como en pausa, candidatos Metallica/
  Star Wars parqueados como investigación reutilizable.
- Segunda ronda de tema: 4 candidatos de ley/teoría evergreen investigados y
  verificados (Efecto Hawthorne, Principio de Peter, Ley de Parkinson, Teoría de los
  Dos Factores de Herzberg) vía AskUserQuestion — Andy eligió el Efecto Hawthorne.
- Resultado: OK — roadmap consistente, tema confirmado en segunda vuelta.

### Paso 2 — Guion (dos iteraciones completas)
- **Iteración 1 (Matrix, descartada):** guion completo escrito siguiendo
  `guion-style-btq.md`, con investigación verificada (casting de Neo, bullet time,
  Baudrillard, Alan Mulally/Ford, United Airlines vuelo 173/CRM), calibrado a ~40.5 min
  (4.485 palabras), publicado como Artifact y aprobado por Andy — luego descartado
  por completo en el giro de Paso 1. Ningún archivo de esta iteración sobrevive en
  `launch-assets/`.
- **Iteración 2 (Efecto Hawthorne, la que queda):** investigación verificada:
  estudios de Hawthorne Works/Western Electric (Elton Mayo, fases de iluminación/
  relés/cableado de bancos), término acuñado por Henry Landsberger (1958), reanálisis
  de Levitt & List (2011, NBER), higiene de manos en hospitales (observación abierta
  vs. encubierta), Panóptico de Jeremy Bentham (1785), Volkswagen Dieselgate (2015) +
  estudio de mortalidad MIT/Harvard (2017), benchmark de industria de cobertura de
  auditoría de calidad en call center (1-5%), Amy Cuddy/power posing (TED 2012),
  The Truman Show (1998).
- Publicado como Artifact — Andy detectó dos problemas que forzaron reescritura antes
  de aprobar:
  1. Un lapsus de tercera persona ("del tipo que Andy, personalmente, desconfía...")
     rompiendo la voz de primera persona del host — corregido a "yo, personalmente,
     desconfío...". Búsqueda exhaustiva confirmó que era el único caso en todo el
     guion (grep de "Andy", "Bermúdez", "el host", "el presentador"). Regla nueva
     agregada a `guion-style-btq.md`.
  2. Feedback estructural más grande: comparado explícitamente contra EP.020 (que a
     Andy le pareció "más profesional") — faltaban casos reales/nombrados con
     consecuencias severas y un dato duro propio de call center. Se fijó el "ADN
     estructural de pilar SEO" en `guion-style-btq.md` (2-3 casos reales escalando +
     dato duro de industria) y se reescribió el guion: los segmentos Cuerpo 1/Cuerpo 2
     originales (cuarto de relés + cuarto de cableado) se fusionaron en un solo
     segmento más ajustado, liberando espacio para un Cuerpo 2 nuevo — Volkswagen
     Dieselgate (11M autos, $30.000M en multas, 7 años de cárcel para un ejecutivo,
     ~1.260 muertes prematuras estimadas por MIT/Harvard) + el dato del 1-5% de
     llamadas auditadas manualmente en la industria de call center. El giro de
     Levitt & List (2011) se mantuvo como diferenciador respecto al patrón de EP.020.
  3. Cada vez que se editó el archivo fuente, la copia del Artifact quedó
     desactualizada una vez — Andy lo detectó ("si en el artifact sigue mal") y se
     corrigió regenerando y republicando en la misma URL. Anotado como hábito a
     mantener: republicar el Artifact después de cada edición al archivo fuente.
- Lint final: 4.542 palabras (p.line + remate + dato + sub) → ~41.0 min a 150 wpm +
  expansión 35.5%, dentro de 40-45 min. 2 REMATE (dentro de máx 3-4). Refrán central
  variado 3 veces (Puente/Cuerpo1, Re-enganche, firma de cierre). 1 "imagínense", 0
  "me vuela la cabeza". Sin disclaimer de cajón. Sin bloque "Mito o Realidad" aparte.
  Título con el nombre del creador (Elton Mayo) según la nueva regla. 0 recomendaciones
  o referencias cruzadas repetidas contra el catálogo (verificado por grep de
  `launch-assets/*.html`: Baudrillard/Cuddy/Truman Show/Volkswagen no aparecían antes).
- Archivos generados: `btq-production/launch-assets/EP023-hawthorne-guion.html`
- Resultado: OK — aprobado por Andy 2026-07-21 ("perfect")

### Paso 3 — Prompts de artwork
- Qué se hizo: tercer episodio sin referente pop en la dirección v3 (después de la
  diana de EP.020 y el checklist de EP.022) — se buscó, otra vez, un símbolo literal
  del propio contenido del episodio. Elegido: un solo agente de call center partido a
  la mitad por la luz (mitad dorada/observada, mitad en sombra/real — la misma persona,
  no dos personajes, siguiendo la regla de brand-constants de no forzar una segunda
  figura) + un patrón de fondo de forma de onda de audio (waveform de una llamada),
  literal al mundo de un pódcast sobre monitoreo de llamadas y sin tocar el círculo/
  anillo/diana vetado desde EP.021.
- Archivos generados: `btq-production/launch-assets/EP023-hawthorne-artwork-v3.md`
  (prompts 1:1 y 16:9 completos; 9:16 queda para derivar del 1:1 aprobado, mismo patrón
  de adaptación de episodios previos — no generado en este documento)
- Resultado: OK — prompts listos, pendiente generación real (no bloqueante para cerrar
  Stage A, mismo patrón que episodios anteriores)

### Paso 4 — Archivo de estado
- Qué se hizo: `pipeline-state-ep023.md` creado, `roadmap-btq.md` actualizado a
  `guion listo`.
- Resultado: OK — pausa natural, esperando grabación

### Extra — prueba de artwork local (ComfyUI, adelantada antes de la grabación)
- Qué se hizo: Andy notó que Stage A se cerró sin correr la validación local en ComfyUI
  que sí se hizo en EP.021/EP.022 antes de grabar — el workflow escrito
  (`episode-pipeline/workflows/00-roadmap.md` Paso 3) dice literalmente "no generes las
  imágenes todavía", pero la práctica real de los últimos 2 episodios fue adelantar un
  test de dirección visual en Stage A. Corregido en la misma sesión.
- Servidor ComfyUI (E:\AI, RTX 3080 Ti) no estaba arriba — lanzado headless con
  `--output-directory E:\AI\outputs`. Primer intento de lanzamiento vía Bash (Git Bash)
  perdió los backslashes del argumento (`E:\AI\outputs` → `E:AIoutputs`, argv corrupto) —
  relanzado vía PowerShell (`Start-Process`), confirmado con `/system_stats`
  (`argv` correcto, GPU `cuda:0 NVIDIA GeForce RTX 3080 Ti`).
- Test 1 (Z-Image Turbo, 1024×1024, ángulo 3/4): el fondo de waveform dorado salió
  perfecto (sin ningún rastro de círculo/anillo/diana pese al veto vigente desde
  EP.021) y el headset boom-mic quedó correcto, pero el concepto central del artwork —
  el mismo agente partido a la mitad por la luz — NO se leyó: en ángulo 3/4 solo un
  lado del rostro es visible a cámara, así que no hay línea de luz que dividir.
- Test 2 (mismo prompt, ajustado a retrato frontal + línea de luz vertical dura y
  explícita "sharp and straight, not a soft gradient" en vez de "rim light"): PASS —
  la división de luz se lee con claridad en rostro y camisa, headset/boom-mic
  correctos, dos manos de cinco dedos, waveform de fondo intacto sin círculos.
- Bug propio detectado y corregido antes de poder encolar el primer render: el JSON
  del workflow API quedó con una llave de cierre faltante en el nodo de texto positivo
  (typo al escribirlo a mano) — el server devolvía 500 genérico sin detalle útil hasta
  revisar `E:\AI\comfyui-stderr.log`, que sí trae el traceback exacto
  (`JSONDecodeError`). Corregido, validado con `json.load()` antes de reintentar.
- Archivo aprobado como dirección validada: `E:\AI\outputs\BTQ-EP023-scene-v2_00001_.png`
  (1024×1024, seed 230231, prompt en el historial de esta sesión).
- Resultado (parcial, revisado abajo): dirección validada técnicamente, pero descartada
  por preferencia de Andy — ver siguiente entrada.

### Extra — segundo giro de concepto: sin persona (feedback de Andy)
- Andy vio el render v2 (headset + rostro partido por la luz) y dio dos piezas de
  feedback en broma-pero-en-serio: (1) el modelo generó por defecto un hombre de rasgos
  asiáticos sin que el prompt pidiera ninguna etnia — Andy no lo quería así; (2) más
  allá del render puntual, prefiere que el artwork de este episodio no lleve una persona
  en absoluto, sino algo anclado directamente al contenido del capítulo (mismo criterio
  que la diana de EP.020 y el checklist de EP.022, que tampoco llevan personas).
- Presentadas 3 opciones sin persona vía AskUserQuestion (foco vintage + headset /
  headset solo partido por luz / panel de cableado con un hilo dorado) — Andy eligió
  "Foco + headset" (recomendado).
- Nuevo prompt: foco incandescente estilo 1920s de filamento visible (el objeto real del
  experimento de iluminación de la fábrica Hawthorne, 1924) colgando sobre un headset
  moderno de call center con boom-mic, apoyado en un escritorio de madera oscura, waveform
  dorado de fondo. Negativo reforzado con "people, person, human, face, hands" para
  garantizar que no se colara ninguna figura.
- Test (Z-Image Turbo, 1024×1024, seed 550101): PASS al primer intento — foco con
  filamento realista como única fuente de luz, headset reconocible con boom-mic, madera
  con veta real, waveform limpio sin ningún rastro de círculo/anillo. Aprobado por Andy
  ("si esta bn").
- Archivo aprobado: `E:\AI\outputs\BTQ-EP023-bulb-v1_00001_.png`.
- Regla nueva agregada a `comfyui/docs/prompting.md` (sección Z-Image): cualquier escena
  CON persona sin referente conocido debe declarar rasgos étnicos explícitos en el
  positivo — sin esa descripción, Z-Image Turbo cae por defecto en un hombre de rasgos
  asiáticos independientemente del contexto de la escena. Confirmado en 2 renders
  consecutivos de esta sesión (agente de call center genérico, sin ninguna pista étnica
  en el prompt, ambos salieron con el mismo sesgo).
- `EP023-hawthorne-artwork-v3.md` reescrito: concepto, prompt 1:1, prompt 16:9 y nota
  final actualizados al foco+headset; concepto de la persona partida por luz queda
  documentado como descartado (no técnicamente fallido) en el propio archivo.
- Pendiente (mismo patrón que EP022 "Extra 2", se hace más cerca del cierre): escalar
  la escena del foco+headset a 1536×1536 nativo → upscale RealESRGAN_x4plus → 3000×3000
  exacto, generar 16:9 y 9:16, componer tipografía/footer con `portada-compose.py`, y
  las quote cards del Stage 3b — no bloqueante para la pausa de Stage A (ir a grabar).
- Resultado: OK — concepto final de artwork validado y aprobado por Andy
