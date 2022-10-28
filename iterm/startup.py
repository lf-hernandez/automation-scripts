#!/usr/bin/env python3

import iterm2


async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    if window is not None:
        tab = window.current_tab
        pane_1a = tab.current_session
        pane_2 = await pane_1a.async_split_pane(vertical=False)
        pane_1b = await pane_1a.async_split_pane(vertical=True)
        pane_3 = await pane_2.async_split_pane(vertical=False)
        pane_4 = await pane_3.async_split_pane(vertical=False)
        pane_5 = await pane_4.async_split_pane(vertical=False)

        await pane_5.async_send_text("docker\n")
        await pane_4.async_send_text("db\n")
        await pane_3.async_send_text("task-queue\n")
        await pane_2.async_send_text("backend\n")
        await pane_1a.async_send_text("web\n")
        await pane_1b.async_send_text("proxy\n")

    else:
        print("No current window")


iterm2.run_until_complete(main)
