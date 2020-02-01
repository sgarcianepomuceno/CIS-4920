'''This program will display Eastern Standard Time'''

import time

# GMT seconds.
GMTSeconds = int(time.time())
remainingSeconds = GMTSeconds % 60

# GMT minutes.
GMTMinutes = GMTSeconds // 60
remainingMinutes = GMTMinutes % 60

# GMT hours.
GMTHours = GMTMinutes // 60
remainingHours = GMTHours % 24

# Eastern hour.
if remainingHours <= 5:
    EasternHour = remainingHours - 5 + 24 
elif remainingHours > 5:
    EasternHour = remainingHours - 5
    
print("It is", EasternHour, ":", remainingMinutes,
      ":", remainingSeconds, "EST")