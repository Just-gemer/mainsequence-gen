import random
print("MAINSEQUENCE GENERATOR BY Just gemer")
mapname = str(input("MapName:"))
clip = str(input("Hide UI clip or Amb clip? (hideui or amb or both):"))
time = int(input("Start time (in milliseconds):"))
duration = int(input("Duration (in milliseconds):"))
out = open(mapname.lower()+"_mainsequence.tape.ckd","w")
if clip == "hideui":
    out.write('''{
    "__class": "Tape",
    "Clips": [
        {
            "__class": "HideUserInterfaceClip",
            "Id": '''+str(random.randint(100000000, 400000000))+''',
            "TrackId": '''+str(random.randint(100000000, 400000000))+''',
            "IsActive": 1,
            "StartTime": '''+str(time//48)+''',
            "Duration": '''+str(duration//48)+''',
            "EventType": 18,
            "CustomParam": ""
        }
    ],
    "TapeClock": 0,
    "TapeBarCount": 1,
    "FreeResourcesAfterPlay": 0,
    "MapName": "'''+mapname+'''"
}''')
elif clip == "both":
    fx = str(input("amb fx name:"))
    timeui = str(input("Start time of hide ui clip (in milliseconds):"))
    durationui = str(input("Duration of hide ui clip (in milliseconds):"))
    timeamb = str(input("Start time of amb clip (in milliseconds):"))
    durationamb = str(input("Duration of amb clip (in milliseconds):"))
    out.write('''{
    "__class": "Tape",
    "Clips": [
        {
            "__class": "HideUserInterfaceClip",
            "Id": '''+str(random.randint(100000000, 400000000))+''',
            "TrackId": '''+str(random.randint(100000000, 400000000))+''',
            "IsActive": 1,
            "StartTime": '''+str(timeui//48)+''',
            "Duration": '''+str(durationui//48)+''',
            "EventType": 18,
            "CustomParam": ""
        },
 		{
			"__class": "SoundSetClip",
			"Id": '''+str(random.randint(100000000, 400000000))+''',
			"TrackId": '''+str(random.randint(100000000, 400000000))+''',
			"IsActive": 1,
			"StartTime": '''+str(timeamb//48)+''',
			"Duration": '''+str(durationamb//48)+''',
			"SoundSetPath": "world/maps/'''+mapname.lower()+'''/audio/amb/amb_'''+mapname.lower()+'''_'''+fx.lower()+'''.tpl",
			"SoundChannel": 0,
			"StartOffset": 0,
			"StopsOnEnd": 0,
			"AccountedForDuration": 0
		}
    ],
    "TapeClock": 0,
    "TapeBarCount": 1,
    "FreeResourcesAfterPlay": 0,
    "MapName": "'''+mapname+'''"
}''')
else:
    fx = str(input("amb fx name:"))
    out.write('''{
    "__class": "Tape",
    "Clips": [
 		{
			"__class": "SoundSetClip",
			"Id": '''+str(random.randint(100000000, 400000000))+''',
			"TrackId": '''+str(random.randint(100000000, 400000000))+''',
			"IsActive": 1,
			"StartTime": '''+str(time//48)+''',
			"Duration": '''+str(duration//48)+''',
			"SoundSetPath": "world/maps/'''+mapname.lower()+'''/audio/amb/amb_'''+mapname.lower()+'''_'''+fx.lower()+'''.tpl",
			"SoundChannel": 0,
			"StartOffset": 0,
			"StopsOnEnd": 0,
			"AccountedForDuration": 0
		}
    ],
    "TapeClock": 0,
    "TapeBarCount": 1,
    "FreeResourcesAfterPlay": 0,
    "MapName": "'''+mapname+'''"
}''')
out.close()