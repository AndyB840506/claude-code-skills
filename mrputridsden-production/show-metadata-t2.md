# Metadata del SHOW — Mr. Putrid's Den (Temporada 2)

> Metadata a nivel de **show**, no de episodio. Los `episodios/ep00X-metadata.md` siguen siendo
> por episodio. Este archivo es lo que se pega en el panel de Spotify for Creators (y en Apple,
> Amazon, etc.) para reposicionar el show completo tras el pivote a misterios y leyendas.
>
> Creado 2026-07-22, junto con el overhaul de la web y el kit de redes.

---

## Nombre

```
Mr. Putrid's Den
```

**No cambia.** El nombre público sigue siendo el mismo — dominio, handles y suscriptores intactos.
"The Crossroads" es codename interno y nunca sale a plataformas.

## Tagline / subtítulo

```
Donde la música se encuentra con el mito
```

> Nota: el specimen (`rebrand/identidad-la-guarida.html`) asigna *"Donde los riffs encuentran el
> whisky"* a "PERFIL". Se usa la principal acá porque el show pivotó 100% a misterios: liderar con
> riffs y whisky vende el show viejo a quien llega nuevo. La de whisky sigue viva dentro del cuerpo
> del texto, como sabor.

---

## Descripción del show

> **Límite: 600 caracteres.** Aplica al texto tal como se pega, así que la versión HTML se mide
> **con las etiquetas incluidas** (~7 caracteres por párrafo). La primera versión de este archivo
> se pasó por mucho — 949 la plana y 1102 la HTML — porque no se midió. Medir, no estimar:
> `python -c "print(len(open('x.txt',encoding='utf-8').read()))"`.

Texto plano — para el campo de descripción de Spotify/Apple/Amazon. **543 caracteres.**

```
Mr. Putrid's Den es el podcast donde la música se encuentra con el mito.

Cada episodio abre un expediente: la muerte que nadie explicó, el disco maldito, el genio que se apagó demasiado pronto. Primero va la leyenda completa, tal como se cuenta a medianoche. Después la abrimos y separamos qué es mito y qué es dato. Casi siempre pasa lo mismo: cuando se le quita la maldición, lo que queda debajo asusta más.

Sin ouija ni sustos baratos. Conducido por Andrés desde Bogotá.

Temporada 1 (EP.001-005) queda como archivo: rock, metal y raíces.
```

## Descripción del show — HTML

Spotify acepta HTML limitado. `<p>` por párrafo garantiza el espaciado y evita que se peguen
palabras al pegar (mismo criterio que en los `ep00X-metadata.md`). **565 caracteres con etiquetas.**

```html
<p>Mr. Putrid's Den es el podcast donde la música se encuentra con el mito.</p>
<p>Cada episodio abre un expediente: la muerte que nadie explicó, el disco maldito, el genio que se apagó demasiado pronto. Primero va la leyenda completa, tal como se cuenta a medianoche. Después la abrimos y separamos qué es mito y qué es dato: cuando se le quita la maldición, lo que queda debajo asusta más.</p>
<p>Sin ouija ni sustos baratos. Conducido por Andrés desde Bogotá.</p>
<p>Temporada 1 queda como archivo. <a href="https://www.mrputridsden.com">mrputridsden.com</a></p>
```

**Qué se perdió al recortar**, por si algún campo largo lo admite después: el párrafo de método
completo ("con todos sus detalles escalofriantes… le miramos las tripas"), la línea de "acá no
vendemos humo", los nombres de bandas del archivo (Black Sabbath, Kraken, Aterciopelados) y el
email en el cuerpo. La web sí conserva todo eso.

## Descripción corta

Para donde el campo sea de una o dos líneas.

```
Misterios y leyendas del rock. Primero la leyenda completa; después los datos. Desde Bogotá.
```

---

## Categoría

| | Valor | Nota |
|---|---|---|
| Primaria | **Music › Music History** | El ancla sigue siendo musical; el género es el misterio |
| Secundaria | **Society & Culture › Documentary** | Refuerza el método: investigar, no asustar |

> ⚠️ La taxonomía de Spotify hereda la de Apple Podcasts. Confirmá los rótulos exactos en el panel
> antes de guardar — no los tomé de la documentación oficial, así que puede que el nombre visible
> difiera un poco. La categoría actual del perfil (`Entretenimiento / Música`) es de la T1.

## Palabras clave

```
misterios del rock, leyendas del rock, club de los 27, archivos secretos del rock,
muertes del rock, mitos musicales, historia del rock, podcast en español,
podcast colombiano, Bogotá, música y misterio, discos malditos
```

## Otros campos

| Campo | Valor |
|---|---|
| Idioma | Español (Colombia) |
| Tipo de show | Episódico |
| Autor / host | Andrés |
| Copyright | © 2026 Mr. Putrid's Den |
| Web | https://www.mrputridsden.com |
| Email | hello@mrputridsden.com |
| Temporada actual | 2 (campos nativos Season/Episode) |

## Portada a subir

```
E:\Podcast\MPD\Temporada 2\artwork\MPD-T2-PORTADA-CONTEXTO-3000.jpg
```

3000×3000, acento brasa `#D9BF7A`. Sube a Spotify, Apple y Amazon — hasta que se suba, esas
plataformas siguen mostrando la portada con el ámbar viejo `#CE8B3A`, que ya no es del sistema.

---

## Decisión pendiente: marcado de contenido explícito

El show pasa a tratar **muertes, sobredosis y suicidios** de forma recurrente (T2·E1 es
exactamente eso). No hay groserías ni contenido sexual, así que "explícito" en el sentido
estricto de la plataforma seguiría siendo **No**.

Lo que sí vale la pena decidir aparte: si los episodios abren con una **nota de contenido** hablada
o escrita en las show notes. No lo agregué por mi cuenta — es una decisión editorial tuya, y el
guion de T2·E1 ya trata el tema con cuidado ("cada nombre de la lista fue una persona real, con
una madre real que enterró a un hijo de veintisiete años").

---

## Checklist de actualización

- [ ] Descripción del show (Spotify for Creators)
- [ ] Descripción del show (Apple Podcasts Connect)
- [ ] Descripción del show (Amazon Music)
- [ ] Categoría primaria y secundaria
- [ ] Portada nueva en las tres plataformas
- [ ] Confirmar que EP.006 sale con Season=2 / Episode=1 en los campos nativos
