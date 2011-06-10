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

    print 'TIME FOR ', h, m, t  

    print RED + 'Z W O D ' + GREEN + 'I T ' + RED + 'L ' + GREEN + 'I S ' + RED +'A S'

    line = ""
    line += bold_if(t == 3 or t == 9, 'A ')   
    line +=  'C '
    line += bold_if(t == 3 or t == 9, 'Q U A R T E R ')
    line += 'D C'
    print line 

    line = bold_if(4 <= t <= 5 or 7 <= t <= 8, 'T W E N T Y ')
    line += bold_if(t == 5 or t == 7 or t == 1 or t == 11, 'F I V E ')
    line += 'X'
    print line 

    line = bold_if(t == 6, 'H A L F ')
    line += 'B '
    line += bold_if(t == 2 or t == 10, 'T E N ')
    line += 'F '
    line += bold_if(t > 6, 'T O ')
    print line 

    line = bold_if(1 <= t <= 6, 'P A S T ')
    line += 'E R U '

    if t >= 7:
        h += 1

    line += bold_if(h == 9, 'N I N E ');
    print line 

    line = bold_if(h == 1, 'O N E ');
    line += bold_if(h == 6, 'S I X ');
    line += bold_if(h == 3, 'T H R E E ');
    print line

    line = bold_if(h == 4, 'F O U R ');
    line += bold_if(h == 5, 'F I V E ');
    line += bold_if(h == 2, 'T W O ');
    print line 

    line = bold_if(h == 8, 'E I G H T ');
    line += bold_if(h == 11, 'E L E V E N ');
    print line 

    line = bold_if(h == 7, 'S E V E N ');
    line += bold_if(h == 0 or h == 12, 'T W E L V E');
    print line 

    line = bold_if(h == 10, 'T E N ');
    line += 'S E '
    line += bold_if(am, 'A M ')
    line += 'G '
    line += bold_if(not am, 'P M ')
    line += 'P '
    line += RESET
    print line

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
