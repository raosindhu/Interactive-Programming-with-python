# template for "Stopwatch: The Game"

# define global variables
import simplegui
interval = 100
t = 0
millisec = 0
counter = 0
netcount = 0
stopped = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t): 
    global millisec
    millisec = (t%1000)/100
    secs = t/1000
    if (secs >= 60):
        mins = secs/60
        secs -= (mins*60)
    else:
         mins = 0
    strSecs = str(secs)
    if (secs < 10):
        strSecs = "0" + strSecs
    t = str(mins) + ":" + strSecs + '.' + str(millisec)
    return t

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global t
    timer.start()
    
def stop():
    global t, millisec, counter, netcount
    timer.stop()
    counter += 1
    if (millisec == 0):
        netcount += 1
    
def reset():
    global t, netcount, counter
    t = 0
    netcount = 0
    counter = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += interval

# define draw handler
def draw(canvas):
    global t
    canvas.draw_text(format(t), [70,100], 36, "white"),
    canvas.draw_text((str(netcount)+"/"+str(counter)), [160,20], 20, "white")
    
# create frame
frame = simplegui.create_frame("Home", 200, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
