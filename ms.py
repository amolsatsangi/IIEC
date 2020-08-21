#########simple text based assitent

print("Hey chat with me!")
while(1):
 print("Give me instructions to open any application.")
 p=input()
 if((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("VLC" in p)or("vlc" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("VLC")
 elif((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("chrome" in p)or("CHROME" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("chrome")
 elif((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("slack" in p)or("SLACK" in p)or("slack.exe" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("slack.exe")
 elif((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("notepad" in p)or("NOTEPAD" in p)or("WRITING PAD" in p)or("writing pad" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("notepad")
 elif((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("notepad" in p)or("NOTEPAD" in p)or("WRITING PAD" in p)or("writing pad" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("notepad")
 elif((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("control panel" in p)or("CONTROL PANEL" in p)or("panel" in p)or("PANEL" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("control panel")
 elif((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("zoom" in p)or("ZOOM" in p)or("ZOOM MEETING" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("zoom.exe")
 elif((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("SUBLIME" in p)or("sublime" in p)or("SUBLIME TEXT" in p)or("sublime text" in p)or("SUBLIME TEXT3" in p)or("sublime text3" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("sublime_text.exe")
 elif((("RUN" in p)or("OPEN" in p)or("run" in p)or("open" in p)or("start" in p)or("START" in p))and(("wmplayer" in p)or("WMPLAYER" in p)or("WINDOW MEDIA PLAYER" in p)or("window media player" in p)or("media player" in p)or("MEDIA PLAYER" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	import os
 	os.system("wmplayer")
 elif((("exit" in p)or("close" in p)or("end" in p)or("break" in p)or("terminate" in p)or("stop" in p))and(("not" not in p)and("NOT" not in p)and("don't" not in p)and("DON'T" not in p ))):
 	break
