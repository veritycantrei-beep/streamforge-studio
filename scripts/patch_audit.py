from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')

audit='https://tally.so/r/Pd72Bb?utm_source=website&utm_campaign=free-audit'
paid='https://tally.so/r/kd2Rxo?utm_source=website&utm_campaign=thumbnail-trial'

repls={
'<a class="btn primary" href="https://tally.so/r/kd2Rxo?utm_source=website&utm_campaign=thumbnail-trial&utm_content=nav" target="_blank" rel="noopener">Try one for $19</a>':f'<a class="btn primary" href="{audit}&utm_content=nav" target="_blank" rel="noopener">Free thumbnail audit</a>',
'<div class="cta"><a class="btn primary" href="https://tally.so/r/kd2Rxo?utm_source=website&utm_campaign=thumbnail-trial&utm_content=hero" target="_blank" rel="noopener">Start the paid trial →</a><a class="btn" href="#work">See concept work</a></div>':f'<div class="cta"><a class="btn primary" href="{audit}&utm_content=hero" target="_blank" rel="noopener">Get a free thumbnail audit →</a><a class="btn" href="{paid}&utm_content=hero-secondary" target="_blank" rel="noopener">Try a design for $19</a></div>',
'<div class="mobileCta"><a class="btn primary" href="https://tally.so/r/kd2Rxo?utm_source=website&utm_campaign=thumbnail-trial&utm_content=mobile" target="_blank" rel="noopener">Try 1 thumbnail for $19 →</a></div>':f'<div class="mobileCta"><a class="btn primary" href="{audit}&utm_content=mobile" target="_blank" rel="noopener">Get a free thumbnail audit →</a></div>'
}
for old,new in repls.items():
    if old in s:
        s=s.replace(old,new,1)

marker='<section class="section"><div class="wrap strip">'
if 'id="free-audit"' not in s and marker in s:
    block=f'''<section class="section" id="free-audit"><div class="wrap"><div class="upsellCard"><div class="kicker">Free thumbnail audit</div><h3>Not ready to pay yet? Send one video.</h3><p>We’ll review the thumbnail hook, hierarchy, readability and visual angle, then send a short audit with concrete changes you can test. No payment required. If you want us to build the redesign after that, the paid trial is $19.</p><div class="cta"><a class="btn primary" href="{audit}&utm_content=section" target="_blank" rel="noopener">Get my free audit →</a><a class="btn" href="{paid}&utm_content=audit-section-paid" target="_blank" rel="noopener">Skip to paid trial</a></div></div></div></section>'''
    s=s.replace(marker,block+marker,1)

p.write_text(s,encoding='utf-8')
