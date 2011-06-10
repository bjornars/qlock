GREEN = BOLD = '\033[01;32m'
RED = NORMAL = '\033[01;31m'
RESET = '\033[00m'

def bold_if(cond, text):
    s = ""
    if cond:
        s = BOLD
    s += text
    if cond:
        s += NORMAL
    return s

def print_time(hour, minute):
    h = hour
    am = h < 12
    h = h % 12
    m = minute
    t = m / 5

    quarter = t == 3 or t == 9
    twenty = 4 <= t <= 5 or 7 <= t <= 8
    five = t == 5 or t == 7 or t == 1 or t == 11
    half = t == 6
    ten = t == 2 or t == 10
    to = t > 6
    past = 1 <=t <= 6

    print GREEN + 'I T ' + RED + 'L ' + GREEN + 'I S ' + RED + 'A S T I M E '
    print bold_if(quarter, 'A ') + 'C ' + bold_if(quarter, 'Q U A R T E R ') + 'D C'
    print bold_if(twenty, 'T W E N T Y ') + bold_if(five, 'F I V E ') + 'X'
    print bold_if(half, 'H A L F ') + 'B ' + bold_if(ten, 'T E N ') + 'F ' + bold_if(to, 'T O ')

    if t >= 7: h += 1
    print bold_if(past, 'P A S T ') + 'E R U ' + bold_if(h == 9, 'N I N E ')
    print bold_if(h == 1, 'O N E ') + bold_if(h == 6, 'S I X ') + bold_if(h == 3, 'T H R E E ')
    print bold_if(h == 4, 'F O U R ') + bold_if(h == 5, 'F I V E ') + bold_if(h == 2, 'T W O ') 
    print bold_if(h == 8, 'E I G H T ') + bold_if(h == 11, 'E L E V E N ')
    print bold_if(h == 7, 'S E V E N ') + bold_if(h == 0 or h == 12, 'T W E L V E')
    print bold_if(h == 10, 'T E N ') + 'S E ' + bold_if(am, 'A M ') + 'G ' + bold_if(not am, 'P M ') + 'P ' + RESET

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        h = int(sys.argv[1])
        m = int(sys.argv[2])
    else:
        import datetime
        h = datetime.datetime.now().hour
        m = datetime.datetime.now().minute

    print_time(h, m)
