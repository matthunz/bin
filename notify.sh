font='xft:tangerine'
glyphs='-wuncon-siji-medium-*-*-*-24-*-*-*-*-*-*-*'

for i in {1..50}; do
  echo '   ' $1
  sleep .1
done | lemonbar -g "800x50x0x0" -o 0 -f $font -o -3 -f $glyphs
