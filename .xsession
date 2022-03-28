# Env vars
export PATH=$HOME/.local/bin:$PATH
export _JAVA_AWT_WM_NONREPARENTING=1
export QT_STYLE_OVERRIDE=kvantum 

# Screens
hdmi=`xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'`

if [ "$hdmi" = "HDMI-0" ]; then
  xrandr --output HDMI-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output eDP-1-1 --mode 1920x1080 --pos 0x1080 --rotate normal
else
  xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-0 --mode 1920x1080 --pos 0x0 --rotate normal
fi

# Composer
picom &
# Network
nm-applet &
# Keyboard Layout
setxkbmap en &
# Automount Devices
udiskie -t &
# bluetooth
blueman-applet &
# Java Fonts
#xsettingsd &
# Wallpaper
feh --bg-fill -z Image/negro.jpg
# Overlay Bar
xob-pulse-py | xob -s pulse &
xob-brightness-js | xob -s brightness &
