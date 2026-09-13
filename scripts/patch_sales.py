from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

replacements = {
    'Premium visuals for streamers, YouTubers and gaming creators. Avatars, banners, thumbnails and stream screens built around your identity. Fast delivery, clear packages and no subscription nonsense.':
    'Premium visuals for YouTubers, streamers, podcasts and creator brands. Thumbnails, avatars, banners and stream assets built around the audience, hook and identity. Fast delivery, clear packages and no subscription nonsense.',

    '<div class="feature"><div class="icon">🎯</div><b>Gaming-first</b><p>Designed for Twitch, YouTube, Kick and creator socials.</p></div>':
    '<div class="feature"><div class="icon">🎯</div><b>Creator-first</b><p>Built for YouTube, Twitch, Kick, podcasts and creator brands across multiple niches.</p></div>',

    'One-off pricing for creators who want a serious look without hiring a full agency.':
    'One-off pricing for creators who want a serious look without hiring a full agency. For recurring thumbnail work or agency volume, start with a paid trial and we’ll quote ongoing rates separately.',

    '<article class="priceCard"><h3>Starter</h3><div class="amount">$19 <span>one-off</span></div><ul class="list"><li>Custom avatar</li><li>Channel banner</li><li>1 visual direction</li><li>1 revision round</li><li>Target: 24–48h delivery</li></ul><a class="btn ghost tracked" data-cta="starter" href="https://tally.so/r/kd2Rxo?utm_source=website&amp;utm_campaign=launch&amp;utm_content=starter" target="_blank" rel="noopener">Choose Starter</a></article>':
    '<article class="priceCard"><h3>Starter / Paid Trial</h3><div class="amount">$19 <span>one-off</span></div><ul class="list"><li>1 custom thumbnail OR avatar + banner</li><li>1 visual direction</li><li>1 revision round</li><li>Target: 24–48h delivery</li><li>Good entry point for ongoing work</li></ul><a class="btn ghost tracked" data-cta="starter" href="https://tally.so/r/kd2Rxo?utm_source=website&amp;utm_campaign=launch&amp;utm_content=starter-trial" target="_blank" rel="noopener">Start with $19</a></article>',

    '<span>Branding for streamers, YouTubers &amp; gaming creators.</span>':
    '<span>Branding and thumbnail design for YouTubers, streamers &amp; creator brands.</span>',

    'Custom streamer branding packs for Twitch, YouTube, Kick and gaming creators. Avatars, banners, thumbnails and stream screens. Fast turnaround. No subscription.':
    'Custom creator branding and high-CTR thumbnail design for YouTube, Twitch, Kick, podcasts and creator brands. Fast turnaround. No subscription.'
}

changed = 0
for old, new in replacements.items():
    if old in s:
        s = s.replace(old, new, 1)
        changed += 1
    else:
        print('Pattern not found:', old[:90])

if changed:
    p.write_text(s, encoding='utf-8')
print(f'Applied {changed} sales copy updates')
