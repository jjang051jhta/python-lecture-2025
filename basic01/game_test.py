import game.sound.echo

# python2버전에서는 필수 __init__.py가 필수 3에서도 관례적으로 쓰는게 좋다
game.sound.echo.echo_test()

from game.sound.echo import echo_test

echo_test()


import game.graphic.render

game.graphic.render.render_test()
from game.graphic.render import render_test

render_test()
