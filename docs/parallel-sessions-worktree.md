# Sesiones paralelas con git worktree

**Cuándo usar:** cuando corras **2+ sesiones de Claude sobre este repo al mismo tiempo**.
Evita que dos sesiones compartan el mismo working tree — esa es la causa raíz de los
"cables cruzados": el `git add` de una sesión barre los cambios sin commitear de la otra
(pasó el 2026-06-19: una edición de roadmap quedó absorbida en el commit del EP.018).

**Regla base:** cada sesión paralela = su **propia carpeta** (worktree) y su **propia rama**.
Git NO permite tener la misma rama checked-out en dos worktrees a la vez, por eso cada
worktree va en una rama de sesión.

> Si la 2da sesión solo va a **leer/consultar** (no editar ni commitear), no necesitas
> worktree — el riesgo solo existe cuando ambas escriben.

## 1. Crear el worktree (para la 2da sesión)

```powershell
# parado en C:\Users\andre\.claude\skills
git worktree add C:\Users\andre\.claude\skills-s2 -b session-<tema> main
```

Abre `C:\Users\andre\.claude\skills-s2` como la 2da sesión de Claude. Comparte el mismo
`.git` (historial común) pero tiene archivos y rama propios → cero cruce.

## 2. Trabajar

Commitea normal en cada worktree. Como el `.git` es compartido, los commits de uno son
visibles para el otro sin push/pull entre ellos.

## 3. Merge back al cerrar

```powershell
git -C C:\Users\andre\.claude\skills checkout main
git -C C:\Users\andre\.claude\skills pull --rebase origin main
git -C C:\Users\andre\.claude\skills merge session-<tema>
git -C C:\Users\andre\.claude\skills push origin main
```

## 4. Limpiar

```powershell
git worktree remove C:\Users\andre\.claude\skills-s2
git branch -d session-<tema>
git worktree prune
```

## Notas

- No pongas el path del worktree **dentro** del repo — usar una carpeta hermana (`skills-s2`).
- El otro checkout completo (`C:\Users\andre\repos\kit-skill-creator`) es un clon aparte,
  no un worktree: ese sí necesita `git pull` para sincronizar (ver gotcha recurrente).
- El harness de Claude Code también soporta worktrees para subagentes
  (`isolation: "worktree"`); esta rutina es para **tus sesiones interactivas paralelas**.
