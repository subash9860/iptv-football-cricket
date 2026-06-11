# FIFA World Cup 2026 — Streaming Channels, OTT Platforms & IPTV Playlist

Host nations: 🇺🇸 USA · 🇨🇦 Canada · 🇲🇽 Mexico · 11 Jun – 19 Jul 2026 · 104 matches · 48 teams.

This repo lists the **official World Cup 2026 broadcasters and OTT platforms** for every major
market, tags whether a **free, publicly-available IPTV stream** exists for that broadcaster in the
[iptv-org](https://github.com/iptv-org/iptv) project, and bundles the ones that do into an
[m3u playlist](worldcup-2026.m3u).

## ⚠️ Read this first (important)

- **Official World Cup feeds are paid, geo-locked and DRM-protected.** FOX, Peacock, DAZN, ZEE5,
  BBC iPlayer, ITVX, etc. **cannot** be put into an open `.m3u`. They are not in iptv-org and never
  will be.
- The `IPTV?` column below means: *does this broadcaster have a **free, legal, public** channel
  stream in iptv-org?* — **not** that the World Cup match itself will play through it. Most of those
  streams are **geo-restricted** to their home country, so you may need to be in-region.
- iptv-org (and this playlist) only reference **publicly available** streams. No piracy, no paid
  feeds. Streams break/rotate constantly — that's upstream, not this repo.

---

## Broadcaster list by country

`✅` = free public stream exists in iptv-org (added to playlist) · `❌` = paid / geo-locked / DRM only (not addable).

### Host & Americas
| Country | TV channel(s) | OTT / streaming | Type | IPTV? |
|---|---|---|---|---|
| 🇺🇸 USA | FOX, FS1 (EN); Telemundo, Universo (ES) | FOX One, Fubo, YouTube TV, Hulu Live, **Peacock** (ES, all 104) | FTA + Pay | ✅ FS1, Telemundo affil., Universo, beIN XTRA |
| 🇨🇦 Canada | CTV, TSN (EN); RDS (FR) | Bell / Crave, TSN+ | Pay | ❌ |
| 🇲🇽 Mexico | TelevisaUnivision (Las Estrellas, Canal 5), TV Azteca (Uno, 7) | **ViX** (free) | FTA | ✅ Azteca Uno/7, Las Estrellas |
| 🇧🇷 Brazil | Globo, SBT, N Sports | **CazéTV** (free, YouTube), Globoplay | FTA + Pay | ✅ Rede Globo |
| 🇦🇷 Argentina | Telefe, TV Pública, TyC Sports | Various | FTA + Pay | ✅ TyC Sports |
| 🇨🇱 Chile | Chilevisión | Various | FTA | ✅ |
| 🇨🇴 Colombia | Caracol, RCN, Win Sports | Various | Mixed | ✅ RCN Más (FAST) |
| 🇵🇪 Peru | América Televisión | Various | Mixed | ❌ |
| 🇺🇾 Uruguay | Canal 5, Antel TV | Antel | Mixed | ❌ |

### Europe
| Country | TV channel(s) | OTT / streaming | Type | IPTV? |
|---|---|---|---|---|
| 🇬🇧 UK | BBC, ITV, STV | BBC iPlayer, ITVX | FTA | ❌ (geo/DRM) |
| 🇩🇪 Germany | ARD (Das Erste), ZDF | Magenta Sport | FTA + Pay | ✅ Das Erste, ZDF |
| 🇫🇷 France | M6, TF1, beIN Sports | beIN Connect | FTA + Pay | ✅ M6, TF1 |
| 🇪🇸 Spain | RTVE (La 1) | DAZN, RTVE Play | FTA + Pay | ✅ La 1 |
| 🇮🇹 Italy | RAI (Rai 1/2) | DAZN, RaiPlay | FTA + Pay | ✅ Rai 1, Rai 2 |

### Asia · Africa · Oceania · MENA
| Country/Region | TV channel(s) | OTT / streaming | Type | IPTV? |
|---|---|---|---|---|
| 🇦🇺 Australia | SBS, SBS Viceland | SBS On Demand (free) | FTA | ❌ (geo/DRM) |
| 🇯🇵 Japan | NHK, Nippon TV, Fuji TV | DAZN, TVer | FTA + Pay | ✅ NHK BS |
| 🇨🇳 China | CCTV-5, Migu | Migu, Xiaohongshu | FTA + Pay | ✅ CCTV-5, CCTV-5+ |
| 🇮🇳 India | Unite8 Sports (Zee) | **ZEE5** | Pay | ❌ (OTT/DRM) |
| 🇿🇦 South Africa | SABC, SuperSport | DStv, SABC+ | Mixed | ✅ SABC 1/3 |
| 🌍 MENA (24 countries) | beIN Sports | beIN Connect | Pay | ✅ beIN SPORTS XTRA (free FAST feed) |

> Full official list (175+ territories): [FIFA Media Rights Licensees PDF](https://digitalhub.fifa.com/m/af2cdbbd380d70c/original/FWC26-Media-Rights-Licensees-Overview.pdf).

---

## The playlist

[`index.m3u`](index.m3u) — 23 free FTA broadcaster channels pulled from live iptv-org streams,
grouped by country (`group-title="World Cup 2026 - <country>"`).

### Copy this link
Just like iptv-org's `https://iptv-org.github.io/iptv/index.m3u`, this repo serves at:

```
https://subash9860.github.io/iptv-football-cricket/index.m3u
```

> ⚙️ That URL only goes live **after GitHub Pages is enabled** (one-time, see below). Until then,
> use the raw URL — works immediately, no setup:
>
> ```
> https://raw.githubusercontent.com/subash9860/iptv-football-cricket/main/index.m3u
> ```

Paste either into any IPTV player (VLC, Tivimate, IINA, Kodi…), or open the local file in VLC:
`Media → Open Network Stream → index.m3u`.

### Enable the `github.io` link (one-time)
1. Push this repo to GitHub (`git push`).
2. GitHub → repo **Settings** → **Pages**.
3. **Source** = `Deploy from a branch`, **Branch** = `main`, folder = `/ (root)` → **Save**.
4. Wait ~1 min. Link goes live: `https://subash9860.github.io/iptv-football-cricket/index.m3u`.

For the **full** iptv-org master list (all channels worldwide):
```
https://iptv-org.github.io/iptv/index.m3u
```

### Regenerate
The playlist is built from the iptv-org API:
```bash
curl -sL -o channels.json https://iptv-org.github.io/api/channels.json
curl -sL -o streams.json  https://iptv-org.github.io/api/streams.json
# then match broadcaster names -> stream URLs (see commit history for the script)
```

---

## Legal

Educational / informational. All streams are referenced from the public
[iptv-org](https://github.com/iptv-org/iptv) index — this repo hosts **no** video. Respect the
broadcasting rights in your region. To watch official World Cup matches, use the licensed
broadcaster/OTT for your country (FOX/Peacock in US, BBC/ITV in UK, ViX in Mexico, CazéTV in Brazil,
etc.).

## Sources
- [2026 FIFA World Cup broadcasting rights — Wikipedia](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_broadcasting_rights)
- [FWC Times — TV Channels & Broadcasting Rights](https://fwctimes.com/fifa-world-cup-broadcasting-rights/)
- [worldcuppass.com — Full channel list per country](https://worldcuppass.com/2026-fifa-world-cup-tv-coverage/)
- [NBC Sports — How to watch the 2026 World Cup](https://www.nbcsports.com/soccer/news/how-to-watch-the-2026-world-cup-live-stream-link-tv-channel-dates-full-details)
- [Al Jazeera — No deals signed in India, China (now resolved)](https://www.aljazeera.com/sports/2026/5/5/no-fifa-world-cup-2026-broadcast-deals-signed-in-india-china)
- [iptv-org/iptv](https://github.com/iptv-org/iptv) · [API](https://github.com/iptv-org/api)
