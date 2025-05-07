import time
import curses
import xadrez1d as x

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Make getch() non-blocking
    stdscr.timeout(100)  # Set the delay for getch() to 100 milliseconds

    # Array positions
    selected_index = 0
    
    MSG = ""
    height, width = (stdscr.getmaxyx())

    while True:
        stdscr.clear()

        ###### Display array  
        array = x.board
        for i, item in enumerate(array):
            if i == selected_index:
                stdscr.addstr(0, i * 6, f"> {item}")  # Add '>' to the selected position
            else:
                stdscr.addstr(0, i * 6, f"  {item}")

        ###### Display mensagens
        stdscr.addstr(f"\n\n {MSG}")

        hovered = x.board[selected_index]
        if hovered:
            stdscr.addstr(8, 1, f"{x.board[selected_index].michael}")

        # se houver algo selecionado:
        if x.selectedPiece != 0:
            MSG = f"selecionado:{x.selectedPiece}"
        
        # debug
        drow = height-1
        dcolumn = 1
        if len(x.debug) > 3*28:
            stdscr.addstr(drow, dcolumn, f"{x.debug}", curses.A_BLINK)
        else:
            stdscr.addstr(drow, dcolumn, f"{x.debug}", curses.A_REVERSE)
        
        # regras
        rrow = height -4
        rcolumn = 1
        stdscr.addstr(rrow, rcolumn, "Q para iniciar, setas para selecionar")

        ##### Get user input
        key = stdscr.getch()

        if key == curses.KEY_LEFT and selected_index > 0:
            selected_index -= 1
        elif key == curses.KEY_RIGHT and selected_index < len(array) - 1:
            selected_index += 1

        elif key == curses.KEY_DOWN:
            #se estiver selecionado
            if  x.selectedPiece !=0:
                x.selectedPiece.move(selected_index)
                x.selectedPiece = 0 
                MSG = ""
            else:
                x.selectedPiece = array[selected_index]

        elif key == curses.KEY_UP:
            if x.selectedPiece != 0:
                x.selectedPiece = 0
                x.debug == ""
            if x.selectedPiece == 0:
                if x.debug[:3] == "..." or x.debug == "": x.debug += "..."
                else: x.debug = ""    

            MSG = ""
            
        elif key == ord("q") or key == ord("Q"):
            for i in range(10):
                stdscr.addstr(10,10,"aaaa") 
                time.sleep(0.3)
                x.debug = ""
            x.initBoard()

        #elif key == ord("z") or key == ord("Z"):
            #redo last play       

        stdscr.refresh()

# Run the game
try:
    curses.wrapper(main)
except Exception as e:
    error_message = f"An unhandled exception occurred: {str(e)}"
    for x in range(10):
        time.sleep(0.5)
        print(error_message)
    time.sleep(30)