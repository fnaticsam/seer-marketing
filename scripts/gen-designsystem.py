#!/usr/bin/env python3
"""Generate /designsystem-{a..g} pages. Run from repo root: python3 scripts/gen-designsystem.py"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARK = (ROOT / "public/logos/seer-mark.svg").read_text()
MARK_INNER = MARK.split(">", 1)[1].rsplit("</svg>", 1)[0]

PAGES = [
    dict(slug="a", num="01", name="Sovereign", em="Mint",
         mood="Closest to the victory screen. Deep sea-green rooms, bone-white type, mint as the voice of the coach — red only when something is about to kill you. Calm, surgical, post-match clarity.",
         display="Anton", display_css="'Anton',sans-serif", display_ls=".015em", font_q="Anton",
         tokens=dict(bg="#0D1A19", surface="#132422", field="#0B1514", ink="#ECE8E1", muted="#9BA8A2",
                     line="rgba(236,232,225,.13)", line_strong="rgba(236,232,225,.3)",
                     primary="#9AE8CF", on_primary="#0C211D", secondary="#3FBF9F", alert="#FF4655"),
         card_icon="var(--primary)",
         swatches=[("#0D1A19","Abyss","bg"),("#132422","Room","surface"),("#ECE8E1","Bone","ink"),
                   ("#9AE8CF","Mint","primary"),("#FF4655","Riot Red","alert"),("#FF8A3D","Ember","warm support")]),
    dict(slug="b", num="02", name="Ember", em="Radiant",
         mood="Orange takes the wheel. Warm charcoal rooms, radiant-fire primary with tactical teal as the second voice — bridges League's gold and Valorant's heat without copying either. Loud, confident, esports-stage energy.",
         display="Chakra Petch", display_css="'Chakra Petch',sans-serif", display_ls=".01em", font_q="Chakra+Petch:wght@500;600;700",
         tokens=dict(bg="#14100D", surface="#1D1712", field="#100C09", ink="#F4EDE3", muted="#A99E8E",
                     line="rgba(244,237,227,.13)", line_strong="rgba(244,237,227,.3)",
                     primary="#FF6B2C", on_primary="#1A0E05", secondary="#2BC4A6", alert="#FF4655"),
         card_icon="var(--primary)",
         swatches=[("#14100D","Char","bg"),("#1D1712","Hearth","surface"),("#F4EDE3","Sand","ink"),
                   ("#FF6B2C","Radiant","primary"),("#2BC4A6","Tactical","secondary"),("#FF4655","Riot Red","alert")]),
    dict(slug="c", num="03", name="Bone", em="Protocol",
         mood="Valorant's signature off-white — used as the ink, not the paper. Bone type on neutral near-black charcoal, red leads, orange answers, pine green keeps score. The broadcast-package one: chunky, editorial, zero blue in the blacks.",
         display="Archivo Black", display_css="'Archivo Black',sans-serif", display_ls="0", font_q="Archivo+Black",
         tokens=dict(bg="#121416", surface="#1B1E21", field="#0D0F11", ink="#ECE8E1", muted="#9A968D",
                     line="rgba(236,232,225,.13)", line_strong="rgba(236,232,225,.3)",
                     primary="#FF4655", on_primary="#FFF6F0", secondary="#2E9C85", alert="#FF7A30"),
         card_icon="var(--secondary)",
         swatches=[("#121416","Studio Black","bg"),("#1B1E21","Slate","surface"),("#ECE8E1","Bone","ink"),
                   ("#FF4655","Riot Red","primary"),("#FF7A30","Ember","warm alert"),("#2E9C85","Pine","secondary")]),
    dict(slug="d", num="04", name="Spike", em="Navy",
         mood="The home colours. Valorant's deep navy with Riot red as the lead voice — bone type, steel-cyan data, orange held back for warnings. The most literal tribute of the set, tuned to read just as well over the Rift.",
         display="Oswald", display_css="'Oswald',sans-serif", display_ls=".03em", font_q="Oswald:wght@500;600",
         tokens=dict(bg="#0F1923", surface="#18242F", field="#0B121A", ink="#ECE8E1", muted="#93A1AC",
                     line="rgba(236,232,225,.13)", line_strong="rgba(236,232,225,.3)",
                     primary="#FF4655", on_primary="#FFF6F4", secondary="#53B9D1", alert="#FF7A30"),
         card_icon="var(--primary)",
         swatches=[("#0F1923","Navy","bg"),("#18242F","Locker","surface"),("#ECE8E1","Bone","ink"),
                   ("#FF4655","Riot Red","primary"),("#53B9D1","Steel","secondary"),("#FF7A30","Ember","alert")]),
    dict(slug="e", num="05", name="Hextech", em="Dusk",
         mood="League's side of the family. Hextech gold leads on deep dusk blue, magic teal answers, parchment type carries the body. Heritage colours with none of the skeuomorphism — still flat, still modern.",
         display="Saira Condensed", display_css="'Saira Condensed',sans-serif", display_ls=".02em", font_q="Saira+Condensed:wght@600;700",
         tokens=dict(bg="#0A1119", surface="#121B26", field="#080E14", ink="#F0E6D2", muted="#A09B8C",
                     line="rgba(240,230,210,.13)", line_strong="rgba(240,230,210,.3)",
                     primary="#C8AA6E", on_primary="#14100A", secondary="#0AC8B9", alert="#FF4655"),
         card_icon="var(--primary)",
         swatches=[("#0A1119","Dusk","bg"),("#121B26","Vault","surface"),("#F0E6D2","Parchment","ink"),
                   ("#C8AA6E","Hextech Gold","primary"),("#0AC8B9","Magic Teal","secondary"),("#FF4655","Riot Red","alert")]),
    dict(slug="f", num="06", name="Signal", em="Mono",
         mood="Strip everything. Ink, charcoal, warm grey — and one signal flare of orange. The quietest room in esports; confidence by subtraction. Reads as a precision tool, not a poster, and disappears behind any game it sits on.",
         display="Inter Tight", display_css="'Inter Tight',sans-serif", display_ls="-.01em", font_q="Inter+Tight:wght@700;800",
         tokens=dict(bg="#0C0C0D", surface="#161618", field="#0A0A0B", ink="#EDEAE4", muted="#8F8C86",
                     line="rgba(237,234,228,.13)", line_strong="rgba(237,234,228,.3)",
                     primary="#FF5A1F", on_primary="#160A04", secondary="#B9B5AD", alert="#FF4655"),
         card_icon="var(--primary)",
         swatches=[("#0C0C0D","Void","bg"),("#161618","Studio","surface"),("#EDEAE4","Chalk","ink"),
                   ("#FF5A1F","Signal","primary"),("#B9B5AD","Warm Grey","secondary"),("#FF4655","Riot Red","alert")]),
    dict(slug="g", num="07", name="Cobalt", em="Clutch",
         mood="Neither of them. Electric cobalt with mint and a flash of orange — the bet that Seer outgrows any single title. The coldest, most software-feeling of the set; built for dashboards first, hype second.",
         display="Sora", display_css="'Sora',sans-serif", display_ls="-.005em", font_q="Sora:wght@700;800",
         tokens=dict(bg="#0B1220", surface="#121C30", field="#080E1A", ink="#E9ECF4", muted="#8F9AB3",
                     line="rgba(233,236,244,.13)", line_strong="rgba(233,236,244,.3)",
                     primary="#4F6BFF", on_primary="#F4F7FF", secondary="#6FE3C2", alert="#FF4655"),
         card_icon="var(--primary)",
         swatches=[("#0B1220","Deep","bg"),("#121C30","Console","surface"),("#E9ECF4","Frost","ink"),
                   ("#4F6BFF","Cobalt","primary"),("#6FE3C2","Mint","secondary"),("#FF7A30","Ember","warm support")]),
]

def tabs_html(current):
    out = []
    for p in PAGES:
        cls = ' class="on"' if p["slug"] == current else ""
        out.append(f'<a href="/designsystem-{p["slug"]}"{cls}><b>{p["slug"].upper()}</b> {p["name"]} {p["em"]}</a>')
    return "\n    ".join(out)

def swatches_html(sw):
    return "\n        ".join(
        f'<div class="sw"><div class="chip" style="background:{hex}"></div><div class="info"><b>{name}</b>{hex} · {role}</div></div>'
        for hex, name, role in sw)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SEER — Design System @@NUM@@ · @@NAME@@ @@EM@@</title>
<meta name="robots" content="noindex" />
<link rel="icon" href="/logos/seer-mark-icon.svg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@700&family=JetBrains+Mono:wght@400;500&family=@@FONTQ@@&display=swap" rel="stylesheet" />
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:@@bg@@;--surface:@@surface@@;--field:@@field@@;
  --ink:@@ink@@;--muted:@@muted@@;
  --line:@@line@@;--line-strong:@@line_strong@@;
  --primary:@@primary@@;--on-primary:@@on_primary@@;
  --secondary:@@secondary@@;--alert:@@alert@@;
  --display:@@DISPLAYCSS@@;--display-ls:@@DISPLAYLS@@;
}
body{font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;background:var(--bg);color:var(--ink);line-height:1.5}
.wrap{width:min(1180px,92vw);margin:0 auto}
/* header + tabs */
.dshead{padding:26px 0 0;background:#0B0D0E;color:#ECE8E1;border-bottom:1px solid rgba(255,255,255,.1)}
.dshead .top{display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;padding-bottom:20px}
.dsbrand{display:flex;align-items:center;gap:14px}
.dsbrand svg{width:44px;height:auto}
.dsbrand .wm{font-family:'Orbitron',sans-serif;font-weight:700;font-size:19px;letter-spacing:.42em}
.dshead .meta{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.18em;color:#8d8a82;text-transform:uppercase;text-align:right;line-height:1.9}
.tabs{display:flex;gap:4px;overflow-x:auto;padding-bottom:0;scrollbar-width:none}
.tabs::-webkit-scrollbar{display:none}
.tabs a{display:inline-flex;align-items:center;gap:7px;white-space:nowrap;padding:11px 16px;font-size:12.5px;color:#8d8a82;border:1px solid transparent;border-bottom:0;border-radius:10px 10px 0 0;text-decoration:none;font-weight:500}
.tabs a b{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.1em;opacity:.7}
.tabs a:hover{color:#ECE8E1}
.tabs a.on{background:var(--bg);color:var(--ink);border-color:rgba(255,255,255,.12)}
/* band */
.opt{padding:64px 0 84px}
.tag{font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--primary);display:flex;align-items:center;gap:10px;margin-bottom:14px}
.tag::before{content:"";width:26px;height:2px;background:var(--primary)}
h1{font-family:var(--display);font-size:clamp(40px,6vw,76px);line-height:.98;text-transform:uppercase;letter-spacing:var(--display-ls);margin-bottom:10px}
h1 em{font-style:normal;color:var(--primary)}
.mood{color:var(--muted);font-weight:300;max-width:62ch;font-size:15.5px}
.fonts{margin-top:8px;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.08em;color:var(--muted)}
.row{display:grid;gap:16px;margin-top:38px}
.lab{font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.26em;text-transform:uppercase;color:var(--muted);margin-bottom:12px}
.logorow{display:flex;align-items:center;gap:clamp(24px,5vw,64px);flex-wrap:wrap;padding:26px 28px;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
.lock{display:flex;align-items:center;gap:18px}
.lock svg{width:64px;height:auto}
.lock .wm{font-family:'Orbitron',sans-serif;font-weight:700;font-size:26px;letter-spacing:.42em}
.lock.small svg{width:34px}
.lock.small .wm{font-size:15px}
.mk{width:64px;height:auto}
.swatches{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.sw{border-radius:10px;border:1px solid var(--line);overflow:hidden}
.sw .chip{height:84px}
.sw .info{padding:10px 12px;background:var(--surface);font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.06em;line-height:1.8;color:var(--muted)}
.sw .info b{display:block;color:var(--ink);font-weight:500;text-transform:uppercase;letter-spacing:.14em}
.spec{padding:30px;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
.spec .big{font-family:var(--display);text-transform:uppercase;font-size:clamp(30px,4.6vw,58px);line-height:1;letter-spacing:var(--display-ls)}
.spec .big em{font-style:normal;color:var(--primary)}
.spec p{margin-top:14px;color:var(--muted);max-width:60ch;font-weight:300;font-size:15px}
.spec .micro{margin-top:14px;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--primary)}
.comps{display:flex;align-items:center;gap:14px;flex-wrap:wrap;padding:26px 28px;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
.btn{font-weight:700;font-size:14px;letter-spacing:.04em;border:0;border-radius:8px;cursor:pointer;padding:13px 24px;text-transform:uppercase;font-family:'Inter',sans-serif}
.btn.primary{background:var(--primary);color:var(--on-primary)}
.btn.ghost{background:transparent;color:var(--ink);border:1.5px solid var(--line-strong)}
.btn.alert{background:var(--alert);color:#fff}
.field{display:flex;gap:8px;background:var(--field);border:1px solid var(--line-strong);border-radius:10px;padding:6px;min-width:280px}
.field input{flex:1;background:transparent;border:0;outline:0;color:var(--ink);font-size:14px;padding:8px 12px;font-family:'Inter',sans-serif}
.field input::placeholder{color:var(--muted)}
.field .btn{padding:9px 18px;font-size:12.5px}
.badges{display:flex;gap:8px;flex-wrap:wrap}
.bdg{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.12em;padding:5px 10px;border-radius:6px;border:1px solid}
.bdg.ok{color:var(--secondary);border-color:var(--secondary)}
.bdg.warn{color:var(--alert);border-color:var(--alert)}
.bdg.next{color:var(--primary);border-color:var(--primary)}
.samples{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.card{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:20px}
.card .who{display:flex;align-items:center;gap:9px;font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.22em;color:var(--primary);margin-bottom:10px}
.card .who svg{width:18px;height:auto}
.card p{font-size:14px;font-weight:300;line-height:1.6}
.card .data{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px}
.card .data span{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.06em;padding:4px 8px;border-radius:5px;border:1px solid var(--line);color:var(--muted)}
.card .game{margin-top:14px;font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.3em;color:var(--muted);text-transform:uppercase}
.statrow{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.stat{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:16px 14px;text-align:center}
.stat .v{font-family:var(--display);font-size:clamp(22px,2.6vw,34px);text-transform:uppercase;line-height:1;letter-spacing:var(--display-ls)}
.stat .v.win{color:var(--primary)}
.stat .v.alert{color:var(--alert)}
.stat .k{margin-top:7px;font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.24em;color:var(--muted)}
.vstrip{display:flex;align-items:center;justify-content:space-between;gap:14px;border:1px solid var(--line);border-radius:12px;padding:16px 24px;background:linear-gradient(90deg,var(--surface),transparent 60%,var(--surface))}
.vstrip .vic{font-family:var(--display);font-size:clamp(34px,5vw,54px);text-transform:uppercase;letter-spacing:.06em;color:var(--primary);line-height:1}
.vstrip .score{font-family:var(--display);font-size:clamp(24px,3.4vw,40px)}
.vstrip .score i{font-style:normal;color:var(--alert)}
.vstrip .mvp{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.26em;color:var(--muted)}
/* app patterns */
.status{display:flex;align-items:center;gap:14px;flex-wrap:wrap;border:1px solid var(--line);border-radius:12px;padding:14px 18px;background:color-mix(in srgb,var(--primary) 6%,var(--surface))}
.status .dot{width:9px;height:9px;border-radius:3px;background:var(--primary);animation:pulse 1.6s ease-in-out infinite}
@keyframes pulse{50%{opacity:.3}}
.status b{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.2em;color:var(--primary)}
.status span{color:var(--muted);font-size:13px;font-weight:300}
.status .btn{margin-left:auto}
.stepper{display:flex;align-items:center;gap:8px;flex-wrap:wrap;border:1px solid var(--line);border-radius:12px;padding:16px 18px;background:var(--surface)}
.step{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.14em;padding:7px 13px;border-radius:6px;border:1px solid var(--line);color:var(--muted)}
.step.done{color:var(--ink);border-color:var(--line-strong)}
.step.on{background:var(--primary);color:var(--on-primary);border-color:transparent}
.stepper .timer{margin-left:auto;display:flex;align-items:baseline;gap:8px}
.stepper .timer .t{font-family:var(--display);font-size:30px;line-height:1;color:var(--primary)}
.stepper .timer .u{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.26em;color:var(--muted)}
.msg{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:18px 20px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:16px}
.msg .typ{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.14em;padding:4px 9px;border-radius:5px;margin-right:10px}
.msg .typ.rec{color:var(--primary);background:color-mix(in srgb,var(--primary) 14%,transparent)}
.msg .typ.ana{color:var(--secondary);background:color-mix(in srgb,var(--secondary) 14%,transparent)}
.msg .typ.warn{color:var(--alert);background:color-mix(in srgb,var(--alert) 14%,transparent)}
.msg .ctx{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.08em;color:var(--muted)}
.msg p{margin-top:11px;font-size:14px;font-weight:300;line-height:1.6}
.msg p .caret{display:inline-block;width:8px;height:14px;background:var(--primary);vertical-align:-2px;margin-left:3px;animation:pulse 1s steps(1) infinite}
.msg .bullets{margin-top:11px;display:flex;flex-direction:column;gap:5px}
.msg .bullets span{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.04em;color:var(--muted)}
.msg .bullets span::before{content:"· ";color:var(--primary)}
.msg .ent{align-self:center;text-align:center;border:1px solid var(--line);border-radius:10px;padding:12px 14px;min-width:92px;background:var(--field)}
.msg .ent .eic{width:40px;height:40px;border-radius:8px;display:grid;place-items:center;margin:0 auto 8px;font-family:'JetBrains Mono',monospace;font-size:10px;background:color-mix(in srgb,var(--primary) 16%,transparent);color:var(--primary)}
.msg .ent .enm{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.08em;color:var(--muted)}
.msg .ent .est{margin-top:3px;font-family:'JetBrains Mono',monospace;font-size:10.5px;color:var(--primary)}
.intel{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.obj{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:18px 20px}
.obj .hd{display:flex;align-items:center;justify-content:space-between;gap:10px}
.obj .hd b{font-size:14px;font-weight:600}
.obj .hd span{font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.1em;color:var(--secondary)}
.obj .bar{height:6px;border-radius:3px;background:color-mix(in srgb,var(--ink) 8%,transparent);margin:12px 0 10px;overflow:hidden}
.obj .bar i{display:block;height:100%;border-radius:3px;background:var(--secondary)}
.obj .why{font-size:12.5px;color:var(--muted);font-weight:300}
.obj.miss .hd span{color:var(--alert)}
.obj.miss .bar i{background:var(--alert)}
.champ{display:flex;align-items:center;gap:13px;border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:13px 16px}
.champ .cic{width:42px;height:42px;border-radius:9px;display:grid;place-items:center;flex:0 0 auto;font-family:'JetBrains Mono',monospace;font-size:10.5px;background:color-mix(in srgb,var(--primary) 14%,transparent);color:var(--primary)}
.champ .cm{flex:1;min-width:0}
.champ .cm b{font-size:14.5px;font-weight:600;display:block}
.champ .cm span{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.14em;color:var(--muted)}
.champ .cr{text-align:right}
.champ .cr .wr{font-family:var(--display);font-size:22px;line-height:1;color:var(--primary)}
.champ .cr .kd{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.1em;color:var(--muted)}
.patterns{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.pat{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:15px 16px}
.pat .ph{font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.22em;color:var(--muted)}
.pat .pv{font-family:var(--display);font-size:26px;line-height:1.1;margin:6px 0 4px}
.pat.good .pv{color:var(--secondary)}
.pat.bad .pv{color:var(--alert)}
.pat .pn{font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.08em;color:var(--muted)}
.verdicts{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.ver{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:15px 16px}
.ver .vk{font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.22em;color:var(--muted)}
.ver .vg{font-family:var(--display);font-size:20px;text-transform:uppercase;margin:6px 0 4px}
.ver .vg.great{color:var(--secondary)}
.ver .vg.good{color:var(--primary)}
.ver .vg.avg{color:var(--muted)}
.ver .vm{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.06em;color:var(--muted)}
.phases{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}
.phs{border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:14px 16px}
.phs .pt{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:8.5px;letter-spacing:.14em;padding:3px 8px;border-radius:5px;margin-bottom:9px}
.phs .pt.early{color:var(--secondary);background:color-mix(in srgb,var(--secondary) 14%,transparent)}
.phs .pt.mid{color:var(--primary);background:color-mix(in srgb,var(--primary) 14%,transparent)}
.phs .pt.late{color:var(--ink);background:color-mix(in srgb,var(--ink) 10%,transparent)}
.phs .pt.watch{color:var(--alert);background:color-mix(in srgb,var(--alert) 14%,transparent)}
.phs p{font-size:12px;color:var(--muted);font-weight:300;line-height:1.55}
.buildrow{display:flex;align-items:center;gap:8px;flex-wrap:wrap;border:1px solid var(--line);border-radius:12px;background:var(--surface);padding:16px 18px}
.buildrow .bi{font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.08em;padding:7px 11px;border-radius:6px;border:1px solid var(--line);color:var(--ink);background:var(--field)}
.buildrow .arr{color:var(--muted);font-size:11px}
.buildrow .bi.next{border-color:var(--primary);color:var(--primary)}
@media(max-width:760px){.patterns,.verdicts{grid-template-columns:1fr 1fr}.msg{grid-template-columns:1fr}.msg .ent{justify-self:start}}
footer{padding:40px 0;border-top:1px solid var(--line)}
footer .wrap{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
.gate{position:fixed;inset:0;z-index:100;display:grid;place-items:center;background:#0B0D0E}
.gate.off{display:none}
.gate form{display:flex;gap:8px}
.gate input{background:#15181A;border:1px solid rgba(255,255,255,.2);border-radius:8px;color:#ECE8E1;padding:11px 14px;font-size:15px;outline:0}
.gate button{background:#ECE8E1;color:#0B0D0E;border:0;border-radius:8px;padding:11px 18px;font-weight:700;cursor:pointer}
@media(max-width:640px){.statrow{grid-template-columns:1fr 1fr}.vstrip{flex-wrap:wrap}}
</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><g id="mark">@@MARKPATHS@@</g></defs></svg>

<div class="gate" id="gate"><form><input type="password" placeholder="speak the word" aria-label="Password" /><button>Enter</button></form></div>

<header class="dshead"><div class="wrap">
  <div class="top">
    <a class="dsbrand" href="/" style="color:inherit;text-decoration:none">
      <svg viewBox="70 76 242 172" fill="#ECE8E1"><use href="#mark"/></svg>
      <span class="wm">SEER</span>
    </a>
    <div class="meta">Design system · v0.2<br>seven directions · league + valorant ready</div>
  </div>
  <nav class="tabs">
    @@TABS@@
  </nav>
</div></header>

<section class="opt"><div class="wrap">
  <div class="tag">Option @@NUM@@ · /designsystem-@@SLUG@@</div>
  <h1>@@NAME@@ <em>@@EM@@</em></h1>
  <p class="mood">@@MOOD@@</p>
  <p class="fonts">DISPLAY: @@DISPLAYUP@@ · UI/BODY: INTER · DATA: JETBRAINS MONO · WORDMARK: ORBITRON</p>

  <div class="row">
    <div><div class="lab">Logo</div>
      <div class="logorow">
        <div class="lock"><svg viewBox="70 76 242 172" fill="var(--ink)"><use href="#mark"/></svg><span class="wm">SEER</span></div>
        <svg class="mk" viewBox="70 76 242 172" fill="var(--primary)"><use href="#mark"/></svg>
        <svg class="mk" viewBox="70 76 242 172" fill="var(--secondary)"><use href="#mark"/></svg>
        <div class="lock small"><svg viewBox="70 76 242 172" fill="var(--muted)"><use href="#mark"/></svg><span class="wm" style="color:var(--muted)">SEER</span></div>
      </div>
    </div>

    <div><div class="lab">Colour</div>
      <div class="swatches">
        @@SWATCHES@@
      </div>
    </div>

    <div><div class="lab">Type</div>
      <div class="spec">
        <div class="big">It sees the game <em>before you do.</em></div>
        <p>Seer plugs into your account, learns your win rates, your matchup history, your cursed champion pool — then coaches you live through draft, the round, and the post-mortem.</p>
        <div class="micro">Ranked draft · 0:27 · locked in</div>
      </div>
    </div>

    <div><div class="lab">Components</div>
      <div class="comps">
        <button class="btn primary">Claim your spot</button>
        <button class="btn ghost">Watch the demo</button>
        <button class="btn alert">Ban Viego</button>
        <div class="field"><input placeholder="your@email.com" /><button class="btn primary">Enter</button></div>
        <div class="badges"><span class="bdg ok">✓ GG</span><span class="bdg warn">△ WARNING</span><span class="bdg next">→ NEXT FOCUS</span></div>
      </div>
    </div>

    <div><div class="lab">Game status — lobby detection</div>
      <div class="status">
        <span class="dot"></span><b>LOBBY DETECTED</b>
        <span>Champion Select found. Seer is ready to coach.</span>
        <button class="btn primary">Enter draft</button>
      </div>
    </div>

    <div><div class="lab">Draft flow — phase stepper</div>
      <div class="stepper">
        <span class="step done">PLANNING</span><span class="step done">BANS 1</span><span class="step done">PICKS 1</span><span class="step done">BANS 2</span><span class="step on">PICKS 2</span><span class="step">SUMMARY</span>
        <span class="timer"><span class="t">09</span><span class="u">SECONDS</span></span>
      </div>
    </div>

    <div><div class="lab">Coach messages — full anatomy</div>
      <div class="row" style="margin-top:0;gap:12px">
        <div class="msg">
          <div>
            <span class="typ rec">RECOMMENDATION</span><span class="ctx">Your build path · Enemy threats</span>
            <p>Build Zhonya's Hourglass second on Orianna. It counters both Karthus R and Nautilus engage — the Stopwatch component alone could save a key teamfight.</p>
            <div class="bullets"><span>ZHONYA'S HOURGLASS (2600G)</span><span>COUNTERS KARTHUS R + NAUTILUS ENGAGE</span><span>STOPWATCH COMPONENT: EARLY SAFETY</span></div>
          </div>
          <div class="ent"><div class="eic">ZH</div><div class="enm">ZHONYA'S</div><div class="est">2600G</div></div>
        </div>
        <div class="msg">
          <div>
            <span class="typ warn">WARNING</span><span class="ctx">Live vision tracking</span>
            <p>Save Updraft — Reyna has played your flank on B three rounds straight. Hold it until she peeks.<span class="caret"></span></p>
            <div class="bullets"><span>REYNA: 7/2 ON B SITE</span><span>HER ENTRY: 78% DRY</span></div>
          </div>
          <div class="ent"><div class="eic" style="background:color-mix(in srgb,var(--alert) 16%,transparent);color:var(--alert)">REY</div><div class="enm">REYNA</div><div class="est" style="color:var(--alert)">7/2</div></div>
        </div>
      </div>
    </div>

    <div><div class="lab">Player intel — objectives · mastery · patterns</div>
      <div class="intel">
        <div class="obj">
          <div class="hd"><b>Ward river by 3:00</b><span>3/4 GAMES HIT · 75%</span></div>
          <div class="bar"><i style="width:75%"></i></div>
          <p class="why">You died to early ganks in 3 of your last 5 losses.</p>
        </div>
        <div class="obj miss">
          <div class="hd"><b>Group after first tower falls</b><span>2/4 GAMES HIT · 50%</span></div>
          <div class="bar"><i style="width:50%"></i></div>
          <p class="why">You're farming 2+ extra waves top after tower. Rotate to dragon or herald.</p>
        </div>
        <div class="champ">
          <div class="cic">CAM</div>
          <div class="cm"><b>Camille</b><span>TOP · 47 GAMES · CONQUEROR</span></div>
          <div class="cr"><div class="wr">62%</div><div class="kd">3.8 KDA</div></div>
        </div>
        <div class="champ">
          <div class="cic">FIO</div>
          <div class="cm"><b>Fiora</b><span>TOP · 31 GAMES · GRASP</span></div>
          <div class="cr"><div class="wr">55%</div><div class="kd">2.9 KDA</div></div>
        </div>
      </div>
      <div class="patterns" style="margin-top:12px">
        <div class="pat good"><div class="ph">EARLY GAME</div><div class="pv">+12 CS</div><div class="pn">AVG LEAD AT 10 MIN</div></div>
        <div class="pat bad"><div class="ph">MID GAME</div><div class="pv">22:00</div><div class="pn">FIRST GROUP · RANK AVG 18:00</div></div>
        <div class="pat good"><div class="ph">LATE GAME</div><div class="pv">73%</div><div class="pn">DRAGON PARTICIPATION · RANK AVG 61%</div></div>
      </div>
    </div>

    <div><div class="lab">Post-game — verdicts · breakdown · build</div>
      <div class="verdicts">
        <div class="ver"><div class="vk">⚔ KILLS</div><div class="vg great">GREAT</div><div class="vm">8/2/12 · KP 71%</div></div>
        <div class="ver"><div class="vk">💰 GOLD &amp; CS</div><div class="vg good">GOOD</div><div class="vm">198 CS · 7.0/MIN</div></div>
        <div class="ver"><div class="vk">👁 VISION</div><div class="vg avg">AVG</div><div class="vm">SCORE 24 · 3 CONTROL WARDS</div></div>
      </div>
      <div class="phases" style="margin-top:12px">
        <div class="phs"><span class="pt early">1–6 · EARLY</span><p>Dominant lane — +18 CS at 10 with a solo kill at level 6.</p></div>
        <div class="phs"><span class="pt mid">10–20 · MID</span><p>Good roam timing, but you grouped 2 minutes late after first tower.</p></div>
        <div class="phs"><span class="pt late">25+ · LATE</span><p>Clean close — you led Baron with a 3-man Hookshot.</p></div>
        <div class="phs"><span class="pt watch">! WATCH OUT</span><p>Both deaths were Hookshot before Thresh's Flay. Wait for the chain.</p></div>
      </div>
      <div class="buildrow" style="margin-top:12px">
        <span class="bi">DORAN'S BLADE</span><span class="arr">→</span><span class="bi">SHEEN</span><span class="arr">→</span><span class="bi">TRINITY FORCE</span><span class="arr">→</span><span class="bi">STERAK'S GAGE</span><span class="arr">→</span><span class="bi next">HEXDRINKER — NEXT</span>
      </div>
    </div>

    <div><div class="lab">Match result</div>
      <div class="samples">
        <div class="statrow" style="grid-column:1/-1">
          <div class="stat"><div class="v win">13–11</div><div class="k">VICTORY · SPLIT</div></div>
          <div class="stat"><div class="v">18/6/8</div><div class="k">KDA · JETT</div></div>
          <div class="stat"><div class="v alert">364</div><div class="k">COMBAT SCORE · MVP</div></div>
        </div>
        <div class="vstrip" style="grid-column:1/-1">
          <span class="vic">Victory</span><span class="score">13 <i>–</i> 11</span><span class="mvp">MVP · BOASTER · 364 ACS</span>
        </div>
      </div>
    </div>
  </div>
</div></section>

<footer><div class="wrap">
  <span>seer.coach · design system v0.2 · option @@NUM@@ of 07</span>
  <span>new mark · monochrome-first · pick a lane</span>
</div></footer>

<script>
(function(){
  const gate=document.getElementById('gate');
  const KEY='seer-gate', HASH='076a89c23179cedfc61171fe400ecf01fb76b9a48a68fb82dd0cd688d684d900';
  if(localStorage.getItem(KEY)==='ok'){gate.classList.add('off');return;}
  const form=gate.querySelector('form'),input=gate.querySelector('input');
  async function sha(s){const b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s));return [...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('');}
  form.addEventListener('submit',async e=>{
    e.preventDefault();
    if(await sha(input.value.trim().toLowerCase())===HASH){localStorage.setItem(KEY,'ok');gate.classList.add('off');}
    else input.select();
  });
  input.focus();
})();
</script>
</body>
</html>
"""

for p in PAGES:
    html = TEMPLATE
    repl = {
        "@@NUM@@": p["num"], "@@SLUG@@": p["slug"], "@@NAME@@": p["name"], "@@EM@@": p["em"],
        "@@MOOD@@": p["mood"], "@@DISPLAYUP@@": p["display"].upper(),
        "@@DISPLAYCSS@@": p["display_css"], "@@DISPLAYLS@@": p["display_ls"],
        "@@FONTQ@@": p["font_q"], "@@TABS@@": tabs_html(p["slug"]),
        "@@SWATCHES@@": swatches_html(p["swatches"]), "@@CARDICON@@": p["card_icon"],
        "@@MARKPATHS@@": MARK_INNER,
    }
    for k, v in p["tokens"].items():
        repl[f"@@{k}@@"] = v
    for k, v in repl.items():
        html = html.replace(k, v)
    out = ROOT / f"public/designsystem-{p['slug']}.html"
    out.write_text(html)
    print("wrote", out.name, len(html))
