# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import cpu,BatteryIcon, battery, khal_calendar
import psutil
import dateutil
#import iwlib


from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])

mod = "mod4"
#terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "Return", lazy.spawn("tilix"), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("tilix -t Ranger -e ranger"), desc="Launch terminal"),
    Key([mod], "g", lazy.spawn("tilix -t Htop -e htop"), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("vivaldi-stable"), desc="Launch browser"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch text editor"),
    Key([mod], "a", lazy.spawn("scrot"), desc="Launch screenshot"),
    Key([mod], "s", lazy.spawn("snap run spotify"), desc="Launch spotify"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "m", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
     # Menu
    Key([mod], "v", lazy.spawn("snap run discord")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),
        # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
        # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

groups = [Group(i) for i in [
    "  爵  ", "    ", "    ", "    ", "    ", "    ", "    ", "  戮  "
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2d2a2e", "#2d2a2e"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#ffffff", "#ffffff"],
                    inactive=["#ffffff", "#ffffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#ff6188", "#ff6188"],
                    this_current_screen_border=["#ab9df2","#ab9df2"],
                    this_screen_border=["#5a565b", "#5a565b"],
                    other_current_screen_border=["#2d2a2e", "#2d2a2e"],
                    other_screen_border=["#2d2a2e", "#2d2a2e"],
                    disable_drag=True,
                ),
                widget.WindowName(
                    foreground=[ "#a9dc76", "#a9dc76"],
                    background=["#2d2a2e", "#2d2a2e"],
                    fontsize=16,
                ),

                widget.Systray(
                    background=[ "#2d2a2e", "#2d2a2e"],
                ),

                
                widget.PulseVolume(
                    foreground=["#ab9df2","#ab9df2"],
                    background=["#2d2a2e", "#2d2a2e"],
                    emoji=True,
                    volume_app="pavucontrol",

                ),
                widget.Wttr(
                    background=["#5a565b", "#5a565b" ],
                    foreground=[ "#ff6188","#ff6188"],
                    font='UbuntuMono Nerd Font Bold',
                    location={
                        'Cali':'Cali'
                    },
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=[ "#5a565b", "#5a565b"]
                ),
                 widget.BatteryIcon(
                     update_interval=1,
                     background=["#ab9df2","#ab9df2"],
                     #theme_path='/home/docs/checkouts/readthedocs.org/user_builds/qtile/checkouts/latest/libqtile/resources/battery-icons',

                 ),
                widget.Battery(
                     background=["#ab9df2","#ab9df2"],
                     full_char='=',
                     markup=False,
                     show_short_text=False
                 ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=[ "#ab9df2","#ab9df2"]
                ),
                widget.CurrentLayoutIcon(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ffd866","#ffd866" ],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ffd866","#ffd866" ],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#ffd866","#ffd866"]
                ),
                widget.TextBox(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#a9dc76","#a9dc76"],
                    text=' ',
                ),
                widget.Clock(
                    timezone="America/Bogota",
                    format='%Y-%m-%d %a - %H:%M ',
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#a9dc76","#a9dc76"],
                    padding=5,
                ),
                
            ],
            24,
            opacity=0.95,
        ),
        bottom=bar.Bar(
            [
                
                widget.Sep(
                    background=[ "#2d2a2e", "#2d2a2e"],
                    foreground=["#ab9df2","#ab9df2"],
                    linewidth=0,
                    padding=5,
                ),
                widget.TextBox(
                    text='ZERO',
                    background=[ "#2d2a2e", "#2d2a2e"],
                    foreground=["#ab9df2","#ab9df2"],
                ),
                widget.Sep(
                    background=[ "#2d2a2e", "#2d2a2e"],
                    foreground=["#ab9df2","#ab9df2"],
                    linewidth=0,
                    padding=5,
                ),
                widget.Sep(
                    background=["#ffd866","#ffd866" ],
                    linewidth=0,
                    padding=5,
                ),
                widget.TextBox(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ffd866","#ffd866"],
                    text="Window(s):"
                ),
                widget.WindowCount(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ffd866","#ffd866" ],
                ),
                widget.CPU(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ff6188","#ff6188"], 
                ),
                widget.Sep(
                    background=["#ff6188","#ff6188"],
                    linewidth=0,
                    padding=5,
                ),
                widget.TextBox(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#a9dc76","#a9dc76"],
                    text="NET:"
                ),
                widget.NetGraph(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#a9dc76","#a9dc76"],
                ),
                widget.Net(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#a9dc76","#a9dc76"],
                ),
                widget.Sep(
                    background=["#a9dc76","#a9dc76"],
                    linewidth=0,
                    padding=5,
                ),
                widget.Sep(
                    background=["#ab9df2","#ab9df2"], 
                    linewidth=0,
                    padding=5,
                ),
                widget.TextBox(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ab9df2","#ab9df2"],
                    text="Storage:"
                ),
                widget.MemoryGraph(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ab9df2","#ab9df2"],
                ),
                widget.Memory(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ab9df2","#ab9df2"],
                ),
                widget.Sep(
                    background=["#5a565b", "#5a565b" ],
                    foreground=[ "#ff6188","#ff6188"],
                    linewidth=0,
                    padding=5,
                ),
                widget.TextBox(
                    background=["#5a565b", "#5a565b" ],
                    foreground=[ "#ff6188","#ff6188"],
                    text="Keyboard:"
                ),
                widget.KeyboardLayout(
                    background=["#5a565b", "#5a565b" ],
                    foreground=[ "#ff6188","#ff6188"],
                ),
            ], 
            24,  
            opacity=0.95,  
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2d2a2e", "#2d2a2e"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#ffffff", "#ffffff"],
                    inactive=["#ffffff", "#ffffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#ff6188", "#ff6188"],
                    this_current_screen_border=["#ab9df2","#ab9df2"],
                    this_screen_border=["#5a565b", "#5a565b"],
                    other_current_screen_border=["#2d2a2e", "#2d2a2e"],
                    other_screen_border=["#2d2a2e", "#2d2a2e"],
                    disable_drag=True,
                ),
                widget.WindowName(
                    foreground=[ "#a9dc76", "#a9dc76"],
                    background=["#2d2a2e", "#2d2a2e"],
                    fontsize=16,
                ),

                widget.CurrentLayoutIcon(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ab9df2","#ab9df2"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#ab9df2","#ab9df2"],
                ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#ab9df2","#ab9df2"]
                ),
                widget.TextBox(
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#a9dc76","#a9dc76"],
                    text=' ',
                ),
                widget.Clock(
                    timezone="America/Bogota",
                    format='%Y-%m-%d %a - %H:%M ',
                    foreground=[ "#2d2a2e", "#2d2a2e"],
                    background=["#a9dc76","#a9dc76"],
                    padding=5,
                ),
                
            ],
            24,
            opacity=0.95,
        ),
    )
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
   # Match(wm_class='confirmreset'),  # gitk
    #Match(wm_class='makebranch'),  # gitk
    #Match(wm_class='maketag'),  # gitk
    #Match(wm_class='ssh-askpass'),  # ssh-askpass
    #Match(title='branchdialog'),  # gitk
    #Match(title='pinentry'),  # GPG key password entry
],
border_focus='#ab9df2')
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
