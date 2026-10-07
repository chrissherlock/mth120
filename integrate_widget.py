#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

def execute_git(args: list[str]) -> None:
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Git execution error: {' '.join(args)}\n{res.stderr.strip()}", file=sys.stderr)
        sys.exit(res.returncode)

def main() -> None:
    target = Path("week1-lecture3.html")
    if not target.exists():
        print(f"Error: {target.name} not found.", file=sys.stderr)
        sys.exit(1)

    content = target.read_text(encoding="utf-8")

    start_marker = "<!-- VISUAL CANCELLATION DIAGRAM -->"
    end_marker = "<h3 style=\"color: #0f172a; font-size: 1.15rem; margin-top: 1.75rem;\">2. Computing Famous Sums with Telescoping Magic</h3>"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("Error: Could not locate the replacement boundaries.", file=sys.stderr)
        sys.exit(1)

    WIDGET_HTML = """            <!-- INTERACTIVE WIDGET: THE COLLAPSING POCKET TELESCOPE -->
            <style>
            /* ===== Widget styles (scoped under .ct) ===== */
            .ct{--ink:#0f172a;--mut:#64748b;--line:#e2e8f0;--pos:#1d4ed8;--neg:#b91c1c;--ok:#15803d;--acc:#b45309;
              width:100%;margin:2.5rem 0;background:#ffffff;border:1px solid var(--border);border-radius:8px;padding:clamp(14px,3vw,24px);color:var(--ink);box-sizing:border-box;box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);}
            .ct *{box-sizing:border-box}
            .ct h4{margin:0 0 4px;font-size:1.15rem;color:#0f172a;display:flex;align-items:center;gap:0.5rem;}
            .ct .sub{margin:0 0 16px;color:var(--mut);font-size:.9rem}
            .ct .tele{display:flex;align-items:center;justify-content:center;height:44px;margin-bottom:10px;padding-right:12px}
            .ct .tube{height:var(--h);width:84px;margin-left:-4px;border-radius:6px;border:1px solid #92400e;
              background:linear-gradient(#fde68a,#d97706 45%,#92400e);transition:margin-left .8s cubic-bezier(.4,0,.2,1);box-shadow:0 1px 2px rgba(0,0,0,.2)}
            .ct .tube:first-child{margin-left:0}
            .ct .tele[data-s="3"] .tube:not(:first-child){margin-left:-34px}
            .ct .tele[data-s="4"] .tube:not(:first-child){margin-left:-60px}
            .ct .tele .lens{width:10px;height:30px;border-radius:0 8px 8px 0;background:linear-gradient(#bae6fd,#38bdf8);border:1px solid #0369a1;margin-left:-2px}
            .ct .stage{background:#f8fafc;border:1px solid var(--line);border-radius:8px;padding:clamp(14px,3vw,26px);min-height:150px;display:flex;align-items:center}
            .ct .row{position:relative;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:.25em .45em;width:100%;
              font:italic clamp(1.15rem,3.6vw,1.7rem)/1.9 "STIX Two Text","Latin Modern Math","Cambria Math",Georgia,serif;border:2px solid transparent;border-radius:8px;padding:6px 10px;transition:background .6s,border-color .6s}
            .ct .row.final{background:#f0fdf4;border-color:var(--ok)}
            .ct .row i{font-style:italic}.ct .row sub{font-size:.62em;line-height:0}
            .ct .lhs{display:inline-flex;align-items:center;gap:.3em;font-style:normal}
            .ct .sum{display:inline-flex;flex-direction:column;align-items:center;line-height:1;font-size:.7em;font-style:normal}
            .ct .sum .sig{font-size:2em;line-height:1}
            .ct .tok{display:inline-block;white-space:nowrap;will-change:transform;position:relative}
            .ct .tok.gone{display:none}
            .ct .tok.p{color:var(--pos)}.ct .tok.m{color:var(--neg)}.ct .tok.op{color:var(--mut);font-style:normal}
            .ct .tok.enter{animation:ct-in .6s .25s both}
            .ct .ghost{position:absolute;pointer-events:none;animation:ct-out .45s forwards;white-space:nowrap}
            .ct .tok.cx{color:var(--ok);opacity:.45;text-decoration:line-through;text-decoration-thickness:2px;transform:scale(.9)}
            .ct .tok.chk::after{content:"= 0 ✓";font:600 .5em system-ui,sans-serif;font-style:normal;color:var(--ok);background:#dcfce7;border-radius:99px;padding:1px 7px;margin-left:.5em;vertical-align:middle;text-decoration:none;display:inline-block}
            .ct .tok.keep{font-weight:700;text-shadow:0 0 14px rgba(180,83,9,.35)}
            .ct .tok{transition:opacity .5s,color .5s,scale .5s}
            @keyframes ct-in{from{opacity:0;scale:.7}to{opacity:1;scale:1}}
            @keyframes ct-out{to{opacity:0;scale:.6}}
            .ct .cap{margin-top:12px;background:#f8fafc;border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:8px;padding:12px 16px;min-height:96px}
            .ct .cap b{display:block;margin-bottom:4px;color:#0f172a;}
            .ct .cap p{margin:0;font-size:.95rem;line-height:1.55;color:#334155;}
            .ct .cap i{font-family:Georgia,serif}.ct .cap sub{font-size:.7em}
            .ct .bar{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px;margin-top:14px}
            .ct button{font:600 .9rem system-ui,sans-serif;padding:8px 14px;border-radius:8px;border:1px solid #cbd5e1;background:#ffffff;color:var(--ink);cursor:pointer;min-height:40px}
            .ct button:hover:not(:disabled){background:#f1f5f9}.ct button:disabled{opacity:.4;cursor:default}
            .ct button.main{background:#0f172a;color:#fff;border-color:#0f172a;min-width:92px}
            .ct button:focus-visible{outline:3px solid #93c5fd;outline-offset:2px}
            .ct .prog{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:12px;color:var(--mut);font-size:.85rem}
            .ct .dots{display:flex;gap:6px}
            .ct .dots button{min-height:0;width:26px;height:8px;padding:0;border-radius:99px;border:0;background:#cbd5e1}
            .ct .dots button.on{background:var(--acc)}
            @media (prefers-reduced-motion:reduce){.ct .tube{transition:none}.ct .tok.enter,.ct .ghost{animation-duration:.01s}}
            </style>

            <div class="ct" id="ct">
              <h4><span>🔭</span> Interactive: The Collapsing Pocket Telescope</h4>
              <p class="sub">Why a sum of differences leaves only its boundary terms.</p>

              <div class="tele" data-s="1" aria-hidden="true">
                <span class="tube" style="--h:40px"></span>
                <span class="tube" style="--h:34px"></span>
                <span class="tube" style="--h:28px"></span>
                <span class="tube" style="--h:22px"></span>
                <span class="lens"></span>
              </div>

              <div class="stage">
                <div class="row" id="ct-row" aria-live="off"></div>
              </div>

              <div class="cap" aria-live="polite">
                <b id="ct-t"></b>
                <p id="ct-p"></p>
              </div>

              <div class="bar">
                <button id="ct-prev">◀ Prev</button>
                <button id="ct-play" class="main">▶ Play</button>
                <button id="ct-next">Next ▶</button>
                <button id="ct-reset">↺ Reset</button>
              </div>

              <div class="prog">
                <span id="ct-n">Step 1 of 4</span>
                <span class="dots" id="ct-d"></span>
              </div>
            </div>

            <script>
            (function(){
            const root=document.getElementById('ct'),row=document.getElementById('ct-row');
            if(!root || !row) return;
            const A=s=>'<i>a</i><sub>'+s+'</sub>', P='+\u2009';
            const defs={L1:'(',R1:')',L2:'(',R2:')',L3:'(',R3:')',Ln:'(',Rn:')',pl1:'+',pl2:'+',pl3:'+',pl4:'+',dots:'⋯',
              p1:s=>s<2?A(1):P+A(1),p2:s=>s<2?A(2):P+A(2),p3:()=>A(3),pn:s=>(s==1||s==4)?A('n'):P+A('n'),pn1:()=>P+A('n−1'),
              m0:()=>'−\u2009'+A(0),m1:()=>'−\u2009'+A(1),m2:()=>'−\u2009'+A(2),mn:()=>'−\u2009'+A('n−1')};
            const S1=['L1','p1','m0','R1','pl1','L2','p2','m1','R2','pl2','L3','p3','m2','R3','pl3','dots','pl4','Ln','pn','mn','Rn'];
            const S2=['m0','p1','m1','p2','m2','dots','pn1','mn','pn'];
            const ORDER=[S1,S2,S2,['pn','m0']];
            const CANCEL=['p1','m1','p2','m2','pn1','mn','dots'],CHK=['m1','m2','mn','dots'],KEEP=['m0','pn'];
            const AP='<i>a</i><span>′</span><sub>k</sub>';
            const CAP=[
             ['Step 1 · The expanded sum','Write out every discrete difference '+AP+' = <i>a</i><sub>k+1</sub> − <i>a</i><sub>k</sub> for <i>k</i> = 0, …, <i>n</i>−1 explicitly. Each bracket is one tube of the telescope, fully extended.'],
             ['Step 2 · Rearrange &amp; regroup','Remove the parentheses (addition is associative and commutative) and reorder so each +<i>a</i><sub>j</sub> sits right beside the −<i>a</i><sub>j</sub> that follows it. The ⋯ hides the middle pairs, which line up in exactly the same way.'],
             ['Step 3 · The intermediate collapse','Each adjacent pair +<i>a</i><sub>j</sub> − <i>a</i><sub>j</sub> equals 0, so every intermediate value cancels, like inner tubes sliding into one another. Only −<i>a</i><sub>0</sub> and +<i>a</i><sub>n</sub> have no partner.'],
             ['Step 4 · The final identity','Only the front boundary term (−<i>a</i><sub>0</sub>) and the back boundary term (+<i>a</i><sub>n</sub>) survive. The whole sum collapses to the last value minus the first: <b style="display:inline;color:#15803d;">∑ '+AP+' = <i>a</i><sub>n</sub> − <i>a</i><sub>0</sub></b>.']
            ];
            // build DOM
            const lhs=document.createElement('span');lhs.className='lhs';
            lhs.innerHTML='<span class="sum"><span>n−1</span><span class="sig">∑</span><span>k=0</span></span><span>'+AP+'</span><span>=</span>';
            row.append(lhs);
            const els={},vis={};
            Object.keys(defs).forEach(id=>{const e=document.createElement('span');
              e.className='tok gone '+(/^p[0-9n]/.test(id)?'p':/^m/.test(id)?'m':'op');e.dataset.id=id;row.append(e);els[id]=e;vis[id]=false;});
            const dots=document.getElementById('ct-d');
            for(let i=0;i<4;i++){const b=document.createElement('button');b.setAttribute('aria-label','Go to step '+(i+1));b.onclick=()=>{stop();go(i)};dots.append(b);}
            let step=0,timer=null,first=true;
            function go(n){
              step=Math.max(0,Math.min(3,n));const s=step+1,order=ORDER[step];
              const rc=row.getBoundingClientRect(),before={};
              Object.keys(els).forEach(id=>{if(vis[id])before[id]=els[id].getBoundingClientRect()});
              // ghosts for terms that disappear
              if(!first)Object.keys(els).forEach(id=>{if(vis[id]&&!order.includes(id)){
                const g=els[id].cloneNode(true),r=before[id];g.className=els[id].className+' ghost';
                g.style.left=(r.left-rc.left)+'px';g.style.top=(r.top-rc.top)+'px';row.append(g);setTimeout(()=>g.remove(),480);}});
              const wasVis=Object.assign({},vis);
              Object.keys(els).forEach(id=>{const e=els[id],on=order.includes(id);vis[id]=on;
                e.classList.toggle('gone',!on);e.classList.remove('enter','cx','chk','keep');
                if(on){e.innerHTML=h(id,s);
                  if(s==3&&CANCEL.includes(id))e.classList.add('cx');
                  if(s==3&&CHK.includes(id))e.classList.add('chk');
                  if(s>=3&&KEEP.includes(id))e.classList.add('keep');
                  if(!wasVis[id]&&!first)e.classList.add('enter');}});
              row.append(...order.map(id=>els[id]));
              if(!first)order.forEach(id=>{const b=before[id];if(!b)return;const a=els[id].getBoundingClientRect(),dx=b.left-a.left,dy=b.top-a.top;
                if(dx||dy){const e=els[id];e.style.transition='none';e.style.transform='translate('+dx+'px,'+dy+'px)';e.getBoundingClientRect();
                  e.style.transition='transform .75s cubic-bezier(.4,0,.2,1),opacity .5s,color .5s';e.style.transform='';}});
              first=false;
              row.classList.toggle('final',s==4);
              root.querySelector('.tele').dataset.s=s;
              document.getElementById('ct-t').innerHTML=CAP[step][0];
              document.getElementById('ct-p').innerHTML=CAP[step][1];
              document.getElementById('ct-n').textContent='Step '+s+' of 4';
              [...dots.children].forEach((b,i)=>b.classList.toggle('on',i==step));
              document.getElementById('ct-prev').disabled=step==0;
              document.getElementById('ct-next').disabled=step==3;
              if(step==3&&timer)stop();
            }
            function h(id,s){const d=defs[id];return typeof d==='function'?d(s):d}
            function play(){if(step==3)go(0);const b=document.getElementById('ct-play');b.textContent='❚❚ Pause';
              timer=setInterval(()=>go(step+1),3400);}
            function stop(){clearInterval(timer);timer=null;document.getElementById('ct-play').textContent='▶ Play';}
            document.getElementById('ct-play').onclick=()=>timer?stop():play();
            document.getElementById('ct-next').onclick=()=>{stop();go(step+1)};
            document.getElementById('ct-prev').onclick=()=>{stop();go(step-1)};
            document.getElementById('ct-reset').onclick=()=>{stop();go(0)};
            go(0);
            })();
            </script>
"""

    new_content = content[:start_idx] + WIDGET_HTML + "\n            " + content[end_idx:]
    target.write_text(new_content, encoding="utf-8")
    print(f"Successfully integrated telescoping widget into {target.name}")

    py_files = [str(p) for p in Path(".").glob("*.py")]
    stage_targets = list(set([str(target)] + py_files))

    execute_git(["git", "add"] + stage_targets)
    diff_status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if diff_status.returncode != 0:
        commit_subject = "Integrate interactive telescoping sum widget directly into HTML"
        commit_body = (
            "Replace the static SVG visual cancellation diagram in week1-lecture3.html\n"
            "with a fully interactive HTML/CSS/JS widget. The widget dynamically\n"
            "animates the expansion, rearrangement, and collapse of telescoping\n"
            "differences with synchronized narrative explanations."
        )
        execute_git(["git", "commit", "-m", f"{commit_subject}\n\n{commit_body}"])
        execute_git(["git", "push"])
        print("Successfully committed and pushed the widget integration.")
    else:
        print("No staged changes detected to commit.")

if __name__ == "__main__":
    main()
