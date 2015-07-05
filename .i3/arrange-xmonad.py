import i3
import time

def xmonify():
    # get currently focused windows
    current = i3.filter(nodes=[], focused=True)
    # get unfocused windows
    other = i3.filter(nodes=[], focused=False)
    # focus each previously unfocused window for 0.5 seconds

    # The following is done in a hackish way as there is no way to wait for a
    # successfull ending of previous command

    for window in other:
        status = i3.focus(con_id=window['id'])
        status = i3.move('workspace temp')

    for window in current:
        status = i3.focus(con_id=window['id'])
        status = i3.move('workspace 1')

    counter = 0
    for window in other:
        status = i3.focus(con_id=window['id'])
        status = i3.move('workspace 1')

        if counter==0:
            status = i3.command("split", "v")

        counter += 1

    for window in current:
        i3.focus(con_id=window['id'])


if __name__ == '__main__':
    xmonify()
