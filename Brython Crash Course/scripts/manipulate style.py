from browser import document, html

box = document["rotate-box"]
angle = 10


def change(event):
    global angle
    box.style.transform = f"rotate({angle}deg)"
    angle += 10


document["rotate-button"].bind("click", change)