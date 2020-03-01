#!/usr/bin/env python3
import libtmux
import time
tmuxServer = libtmux.Server()
session = tmuxServer.new_session("contrSSH")
window = session.attached_window
window.split_window(vertical=True)
window.panes[0].split_window(vertical=False)
window.panes[2].split_window(vertical=False)
time.sleep(1)

window.panes[0].send_keys("tail -f " +)
window.panes[0].send_keys("tail -f " +)
window.panes[0].send_keys("tail -f " +)
window.panes[0].send_keys("tail -f " +)
