font="xft:tangerine"
glyphs="-wuncon-siji-medium-*-*-*-24-*-*-*-*-*-*-*"

getTime(){
  echo "%{F"#586ca7"} %{F"#aaaaaa"}$(date +"%I:%M")"
}
getDesktop(){
  for i in $(bspc query -D); do
    if [ $i = $(bspc query -D -d) ]; then
      echo %{F"#586ca7"}
    else
      echo %{F"#aaaaaa"}
    fi
  done
}
while true; do
  echo %{c}$(getDesktop)%{r}$(getTime)"   "   
  sleep .1
done | lemonbar -g "3840x50x0x0" -B "#222222" -F "#aaaaaa" -o 0 -f $font -o -3 -f $glyphs | sh &
