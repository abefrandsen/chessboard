from flask import Flask, request, render_template, escape
import chess

# set up board
board = chess.Board()
board.reset()
turn_map = {
    chess.WHITE : 'white',
    chess.BLACK : 'black'
}
player = turn_map[board.turn]
board_string = str(board)
msg = 'good luck!'

# set op flask app
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('main_page_template.html', player=player, board=board_string, message=msg)

@app.route('/', methods=['POST'])
def my_form_post():
    move = request.form['text']
    try: 
        board.push_san(move)
        msg = 'interesting choice...'
    except ValueError:
        msg = '{0} is an invalid move!'.format(escape(move))
    player = turn_map[board.turn]
    board_string = str(board)
    return render_template('main_page_template.html', player=player, board=board_string, message=msg)
