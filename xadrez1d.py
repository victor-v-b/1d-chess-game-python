class Cavalo:
    def __init__(self, michael):
        self.michael = michael
        if michael==1:
            self.posAtual = 1
            board[1] = self
        else:
            self.posAtual = 10
            board[10] = self

    def __repr__(self):
        return f"C({self.michael})"
    
    def move(self, pos):
        global debug
        if(abs(self.posAtual - pos)!=2):
            debug = "nao se move"
            return
        self.posAnterior = self.posAtual     
        self.posAtual = pos
        ocupa(self, self.posAtual, self.posAnterior)   
class Peao:
    def __init__(self, michael):
        self.michael = michael
        if michael==1:
            self.posAtual = 3
            board[self.posAtual] = self
        else:
            self.posAtual = 8
            board[8] = self

    def __repr__(self):
        return f"P({self.michael})"

    def move(self, pos):
        self.posAnterior = self.posAtual
        if self.michael:
            self.posAtual+=1
        else:
            self.posAtual-=1
        ocupa(self, self.posAtual, self.posAnterior)
class Torre:
    def __init__(self, michael):
        self.michael = michael
        if michael==1:
            self.posAtual = 2
            board[2] = self
        else:
            self.posAtual = 9
            board[9] = self

    def __repr__(self):
        return f"T({self.michael})"

    def move(self, pos):
        global debug
        self.posAnterior = self.posAtual     
        #sub-lista de valores entre a posiçao atual e a posiçao movida  
        betweenPieces = board[min(pos, self.posAtual) + 1 : max(pos, self.posAtual)+1]   
        count = 0
        for y in betweenPieces:  
            count+=1
            if(y!=0 and count != len(betweenPieces)):
                debug = "alguém bloqueia o caminho"
                return       
        self.posAtual = pos
        ocupa(self, self.posAtual, self.posAnterior)       
class Rei:
    def __init__(self, michael):
        self.michael = michael
        if michael==1:
            self.posAtual = 0
            board[0] = self
        else:
            self.posAtual = 11
            board[11] = self

    def __repr__(self):
        return f"R({self.michael})"
    
    def move(self, pos):
        global debug
        if(abs(self.posAtual - pos)!=1):
            debug ="nao se move"
            return
        self.posAnterior = self.posAtual     
        self.posAtual = pos
        ocupa(self, self.posAtual, self.posAnterior)  

board = [0 for x in range(12)]
P1,P2,C1,C2,T1,T2,R1,R2 = None,None,None,None,None,None,None,None
debug = ""

selectedPiece = 0

def ocupa(piece, pos, posAnterior):
    global debug
    global selectedPiece
    if  board[pos] == 0:
        board[pos] = piece
        board[posAnterior] = 0       
    elif board[pos].michael == piece.michael:
         debug = "nao pode matar aliado"
         piece.posAtual = posAnterior
         selectedPiece = 0
    elif board[pos] !=0 and board[pos].michael != piece.michael:
         debug = f"{board[piece.posAtual]} matou {board[pos]}"
         board[pos] = piece
         board[posAnterior] = 0
         

def initBoard():
    global board
    board = [0 for x in range(12)] 
    global R1
    global R2
    global C1
    global C2
    global T1
    global T2
    global P1
    global P2
    C1 = Cavalo(1)
    C2 = Cavalo(0)
    R1 = Rei(1)
    R2 = Rei(0)
    T1 = Torre(1)
    T2 = Torre(0)       
    P1 = Peao(1)
    P2 = Peao(0)
initBoard() 


