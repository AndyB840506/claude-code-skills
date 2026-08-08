# Bitácora de auditoría — BTQ EP.025 «Ponerse la camiseta»

## Stage 0 — Intake
- Qué se hizo: episode brief construido a partir de contexto ya establecido en la sesión
  (no se repreguntó nada — guion, grabación y transcripción ya habían ocurrido en esta misma
  conversación).
- Episode brief:
  ```
  show:            BTQ
  ep_number:       EP.025
  title:           Ponerse la camiseta: la explotación laboral disfrazada de slogan
  cultural_ref:    ninguna — carril Oficio de Jefe #2, sin referente pop
  guest:           none (solo host)
  sources:         WeWork (comunicados oficiales SoftBank Group Corp., 2019 y 2021) ·
                   Susan Fowler, blog personal (2017) · Wells Fargo Consent Order CFPB
                   2016-CFPB-0015 · Los Angeles Times (2013) · audiencia de John Stumpf
                   ante el Senado (sept. 2016) · video de Travis Kalanick, Bloomberg (2017)
  closing_tm:      "Yo soy Andy. Y recuerden: la camiseta nunca fue gratis. Alguien
                   siempre paga la cuenta — la pregunta que le queda es si ha sido
                   usted, o si ha sido su gente."
  spotify_url:     pending
  audio_path:      E:\Podcast\BTQ\EP 25\BTQ EP 25.wav (confirmado por Andy, grabado
                   2026-08-07, ~40:53 medidos con ffprobe)
  language:        es
  speakers:        solo (host único — no multi, a diferencia del default del brief)
  ```
- Archivos generados/modificados: `pipeline-state-ep025.md` (normalizado a stage_a: complete,
  stage_b: in_progress), `launch-assets/EP025-camiseta-guion.artifact.html` (agregado el
  Closing TM que faltaba en el cierre — el guion original solo tenía firma genérica).
- Resultado: OK

## Stage 1 — Transcripción
- Qué se hizo: ya completada antes de invocar el pipeline (WhisperX large-v2 + diarización,
  español). No se repite.
- Archivos generados: `E:\Transcriptor\transcripciones\BTQ EP 25.srt` (48.516 bytes,
  2026-08-07 22:59). Verificado con `ffprobe` que el audio fuente mide 40:53 — consistente
  con el guion (40:00 medidos, diferencia normal por ritmo real de lectura).
- Validaciones:
  - Episodio dicho correctamente al aire ("episodio 25") → pass → confirmado leyendo el
    transcript, el bug de "episodio 26" detectado en la sesión anterior no se repitió.
- Resultado: OK
