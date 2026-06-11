#!/usr/bin/env python3
"""Rebuild the World Cup 2026 IPTV playlist from the live iptv-org API.

Fetches iptv-org channels + streams, matches the curated free-to-air World Cup
2026 broadcasters that have a public legal stream, and writes index.m3u (plus an
identical worldcup-2026.m3u). Run locally or via the daily GitHub Action.

    python3 scripts/build_playlist.py
"""
import json
import sys
import urllib.request
from collections import defaultdict

CHANNELS_URL = "https://iptv-org.github.io/api/channels.json"
STREAMS_URL = "https://iptv-org.github.io/api/streams.json"

# Curated: official WC2026 free-to-air broadcasters that ALSO have a public
# iptv-org stream. (country, display name, iptv-org channel id)
PICKS = [
    ("USA", "Fox Sports 1", "FoxSports1.us"),
    ("USA", "beIN SPORTS XTRA (free)", "beINSPORTSXTRA.us"),
    ("USA", "NBC Universo", "NBCUniverso.us"),
    ("USA", "Telemundo (KNSD 48.1)", "KNSD481.us"),
    ("Mexico", "Azteca Uno", "AztecaUno.mx"),
    ("Mexico", "Azteca 7", "Azteca7.mx"),
    ("Mexico", "Las Estrellas", "LasEstrellas.mx"),
    ("Brazil", "Rede Globo", "RedeGlobo.br"),
    ("Argentina", "TyC Sports", "TyCSports.ar"),
    ("Chile", "ChileVision", "ChileVision.cl"),
    ("Colombia", "RCN Mas", "RCNMas.co"),
    ("Germany", "Das Erste (ARD)", "DasErste.de"),
    ("Germany", "ZDF", "ZDF.de"),
    ("France", "M6", "M6.fr"),
    ("France", "TF1", "TF1.fr"),
    ("Spain", "La 1 (RTVE)", "La1.es"),
    ("Italy", "Rai 1", "Rai1.it"),
    ("Italy", "Rai 2", "Rai2.it"),
    ("Japan", "NHK BS", "NHKBS.jp"),
    ("South Africa", "SABC 1", "SABC1.za"),
    ("South Africa", "SABC 3", "SABC3.za"),
    ("China", "CCTV-5 (sports)", "CCTV5.cn"),
    ("China", "CCTV-5+ (sports)", "CCTV5Plus.cn"),
]

OUTPUTS = ["index.m3u", "worldcup-2026.m3u"]


def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def main():
    print(f"fetch {CHANNELS_URL}")
    channels = {c["id"]: c for c in fetch(CHANNELS_URL)}
    print(f"fetch {STREAMS_URL}")
    streams = fetch(STREAMS_URL)

    s_by_ch = defaultdict(list)
    for s in streams:
        s_by_ch[s["channel"]].append(s)

    lines = ["#EXTM3U"]
    added = 0
    missing = []
    for country, disp, cid in PICKS:
        chan_streams = s_by_ch.get(cid)
        if not chan_streams:
            missing.append(cid)
            continue
        s = chan_streams[0]
        cc = channels.get(cid, {}).get("country", "")
        name = f"{disp} ({cc})" if cc else disp
        lines.append(
            f'#EXTINF:-1 tvg-id="{cid}" tvg-country="{cc}" '
            f'group-title="World Cup 2026 - {country}",{name}'
        )
        if s.get("referrer"):
            lines.append(f'#EXTVLCOPT:http-referrer={s["referrer"]}')
        if s.get("user_agent"):
            lines.append(f'#EXTVLCOPT:http-user-agent={s["user_agent"]}')
        lines.append(s["url"])
        added += 1

    content = "\n".join(lines) + "\n"
    for path in OUTPUTS:
        with open(path, "w") as f:
            f.write(content)

    print(f"wrote {added} channels to {', '.join(OUTPUTS)}")
    if missing:
        print(f"dropped (no public stream right now): {', '.join(missing)}")
    if added == 0:
        print("ERROR: no channels matched — aborting", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
