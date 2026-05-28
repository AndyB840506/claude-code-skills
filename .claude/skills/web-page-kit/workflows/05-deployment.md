# Workflow 05 — Deployment: Publish Your Site

Get your site live. Primary method: **Netlify drag-and-drop** — no account required, free, live in under 2 minutes. Other options available for existing hosting.

---

## Local Preview Before Deploying

Test before publishing. Pick whichever option matches your setup:

**Option 1: VS Code Live Server** (simplest — no terminal needed)
1. Install the "Live Server" extension in VS Code
2. Right-click your HTML file → "Open with Live Server"
3. Opens at `http://127.0.0.1:5500/` — auto-refreshes on save

**Option 2: Node / npx** (recommended on Windows — Python often fails)
```bash
npx --yes serve -p 8080
```
Opens at `http://localhost:8080/` — installs `serve` automatically if not present.

**Option 3: Python** (works if Python is installed and not blocked)
```bash
python -m http.server 8000
```
Opens at `http://localhost:8000/` — on Windows, may fail with exit 255 due to antivirus or missing Python PATH. Use npx option as fallback.

**Option 3: Apache Alias on Windows (Laragon)** — for clean URLs without admin rights
Create `C:/laragon/etc/apache2/sites-enabled/alias.yourproject.conf`:
```apache
Alias /yourproject "C:/path/to/your/project"
<Directory "C:/path/to/your/project">
    Options Indexes FollowSymLinks MultiViews
    AllowOverride All
    Require all granted
</Directory>
```
Restart Laragon Apache. Access at `http://localhost/yourproject/`

This avoids needing admin rights to create symlinks on Windows — useful when VS Code or Python previews aren't enough (e.g., testing .htaccess rules or PHP includes).

---

## Primary Path: Netlify (Recommended)

The fastest way to go live. Works with a single HTML file or a full folder.

### Steps:

1. **Go to** [app.netlify.com/drop](https://app.netlify.com/drop) *(no account needed for a quick deploy)*
2. **Drag and drop** your HTML file (or the full project folder) onto the page
3. **Done** — Netlify gives you a live URL instantly (e.g., `https://amazing-name-123.netlify.app`)
4. **Share the URL** or continue to configure a custom domain

**That's it for a quick launch.** Under 2 minutes.

---

## Optional: Custom Domain on Netlify

After the initial deploy:

1. Create a free Netlify account to save your site
2. Go to: Site Settings → Domain Management → Add custom domain
3. Enter your domain (e.g., `mysite.com`)
4. Follow DNS instructions (point your domain's nameservers to Netlify)
5. SSL certificate is automatic — no extra steps

Domain cost: ~$10-15/year from Namecheap, Google Domains, or Porkbun.

---

## Alternative: Direct File Sharing

No hosting needed. Share the HTML file directly:

- **Email** — Attach the `.html` file
- **Google Drive / Dropbox** — Upload and share link
- **WhatsApp / Telegram** — Send file directly
- Recipient opens it in their browser — works offline

Good for: mockups, prototypes, client reviews, internal docs.

---

## Alternative: Traditional Web Hosting (FTP)

For users who already have a hosting provider (Bluehost, GoDaddy, Hostinger, etc.):

1. Download **FileZilla** (free FTP client)
2. Enter your host credentials: Host, Username, Password, Port 21
3. Navigate to `/public_html/` on the server
4. Drag and drop your HTML files + `sitemap.xml` + `robots.txt`
5. Visit your domain to verify

SSL: Request free Let's Encrypt from your host's control panel (most include it).

---

## Alternative: GitHub Pages (Free)

For users with a GitHub account:

1. Create a new repo named `[yourusername].github.io`
2. Upload your HTML files
3. Enable Pages: Settings → Pages → Source: main branch
4. Your site is live at `https://[yourusername].github.io`

---

## Alternative: Vercel

Similar to Netlify — preferred when the user already has a Vercel account (e.g., another site already deployed there).

**Via CLI (recommended for repeat deploys):**
```bash
npm install -g vercel   # one-time
vercel --prod           # from the website folder
```

Free tier: unlimited projects, custom domains, SSL included.

**Custom domain DNS:**
After adding the domain in Vercel Dashboard → Settings → Domains, use the **exact IP Vercel shows you** — it varies by project. Do NOT use a generic hardcoded IP like `76.76.21.21`. Common values are `76.76.21.21` or `216.198.79.1` but Vercel's dashboard is always the source of truth.

| Record | Name | Value |
|---|---|---|
| A | `@` | *(IP shown in Vercel dashboard)* |
| CNAME | `www` | `cname.vercel-dns.com` |

---

## Post-Launch Checklist

After deploying, verify:

```
✅ Site opens at the URL
✅ Homepage renders correctly
✅ All links work (navigation, CTAs)
✅ Images load
✅ Mobile layout looks good (check on phone)
✅ HTTPS lock icon visible in browser
✅ sitemap.xml accessible at [url]/sitemap.xml
```

---

## Submit to Google (Optional)

To get indexed faster:

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Add your site URL
3. Submit sitemap: `[your-url]/sitemap.xml`
4. Google starts crawling within 24-48 hours

---

## Summary

| Method | Time | Cost | Best For |
|---|---|---|---|
| Netlify drag-drop | ~2 min | Free | Quickest launch |
| Direct file share | ~1 min | Free | Mockups, reviews |
| Custom domain + Netlify | ~15 min | ~$12/year domain | Professional launch |
| FTP / Web host | ~20 min | Hosting cost | Existing hosting |
| GitHub Pages | ~10 min | Free | Developers |

---

**Your site is live!** Share the URL and start driving traffic.
