# Handoff: CV ATS-compliant + guía LinkedIn

**Date:** 2026-07-12
**Status:** Complete — entregables listos; quedan verificaciones de datos que solo el usuario puede hacer

---

## What We Accomplished This Session

- CV reescrito ATS-compliant en dos idiomas, en `C:\Users\andre\repos\cv\` (carpeta nueva, NO es repo git):
  - Masters: `cv-andres-bermudez-en.md` / `cv-andres-bermudez-es.md`
  - `build_docx.py` genera `CV-Andres-Bermudez-EN.docx` / `-ES.docx` (Calibri 11, una columna, headers estándar; requiere `python-docx`, ya instalado en el desktop)
  - `NOTAS-verificacion.md` — fixes aplicados, checklist ATS, fuentes de la investigación
  - `linkedin-guia-latoneria.md` — textos paste-ready para arreglar el perfil de LinkedIn en 7 pasos
- Fixes al perfil original: duplicados Huawei y Sutherland fusionados, placeholder "X%" de Convergys eliminado, solapamientos 2006–2010 comprimidos en "Early Career", gap mar–sep 2023 como career break honesto (decisión del usuario: pausa personal), bullets reciclados y métricas "loyalty" no medibles eliminados, idioma unificado por versión.
- Decisiones del usuario (vía menú): CV híbrido (Director of Ops / Sr CSM / Sr Client Services), EN + ES, gap honesto, fusionar duplicados.
- DOCX verificados releyéndolos con python-docx: 71 párrafos, 36 bullets, 6 headers estándar, 8 marcadores [VERIFY] en rojo por versión.
- Memoria nueva: `project_cv_repo.md` (ubicación + flujo de regeneración + regla de marcadores [VERIFY] rojos en entregables).

## Where We Paused

**Last action:** guía de LinkedIn escrita; session-close en curso.
**Next action:** cuando el usuario traiga los datos reales de Hire Horatio, actualizar los masters .md y regenerar los .docx (`python build_docx.py`). NO editar los .docx directo.
**Blockers:** todos los [VERIFY] dependen del usuario (ver Questions).

## Files to Read First

- `C:\Users\andre\repos\cv\NOTAS-verificacion.md` — estado completo: qué se corrigió y qué falta
- `C:\Users\andre\repos\cv\cv-andres-bermudez-en.md` — master EN con los marcadores [VERIFY] en contexto
- Memoria `project_cv_repo.md` — flujo de regeneración

## Notes / Gotchas

- Los marcadores [VERIFY]/[VERIFICAR] se renderizan en ROJO en los .docx a propósito — no limpiarlos sin que el usuario confirme cada dato.
- El rol de Hire Horatio (oct 2023–ene 2026) estaba VACÍO en LinkedIn; sus bullets se redactaron desde las afirmaciones del extracto (15% retención, 20% revenue growth) y son hipótesis hasta que el usuario las confirme.
- El summary usa solo métricas trazables a bullets del CV; el extracto viejo de LinkedIn decía "8% downtime" pero el bullet real dice 15% — LinkedIn debe ajustarse (está en la guía, paso 3).
- `repos\cv` no es repo git — se le ofreció al usuario inicializarlo y subirlo a GitHub; no respondió (si trabaja desde el portátil, los archivos no estarán).

## Questions to Answer

- [VERIFY] Métricas y tamaño de portafolio de Hire Horatio (# cuentas, FTEs, valor).
- [VERIFY] Cifras de CCR BPO ($50M portafolio, +35% CLV, +25% retención) — ¿defendibles?
- [VERIFY] Nombres exactos de CRMs/herramientas usados (Salesforce, Zendesk, etc.) — los ATS matchean el nombre exacto.
- [VERIFY] Estado y fechas del MBA UNIMINUTO.
- [VERIFY] ¿Reclama portugués? (andyfreelancer.com dice trilingüe; LinkedIn solo ES/EN).
- ¿Inicializar `repos\cv` como repo git y subirlo a GitHub?
