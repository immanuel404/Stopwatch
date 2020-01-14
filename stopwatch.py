# Sourcecode for "Stopwatch"
# By Emmanuel.O

# CodeSkulptor GUI module
import simplegui

second = 0
minute = 0
hour = 0

# Event handler
def start():
    global second, minute, hour
    second += 1
    if second == 60:
        second = 0
        minute += 1
    else:
        minute = minute
    if minute == 60:
        minute = 0
        hour += 1
    else:
        hour = hour
    print "Hour:", hour, " Min:", minute, " Sec:", second

def stop():
    timer.stop()
    
def reset():
    global second, minute, hour
    second = 0
    minute = 0
    hour = 0
        
def draw(canvas):
    canvas.draw_text("STOPWATCH", [100,170], 30, "Green")
    canvas.draw_text("hour:" + str(hour) + " minute:" + str(minute) + " seconds" + str(second), [50,220], 30, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 400,400)

# register event handlers
timer = simplegui.create_timer(1000, start)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()
timer.start()
