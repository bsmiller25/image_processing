import os
import time

nframe   = 100
cmd_wget = "wget http://207.251.86.238/cctv391.jpg"
cmd_mv   = "mv cctv391.jpg images/dot/cctv391_{0:03}.jpg"

for i in range(nframe):
    os.system(cmd_wget)
    os.system(cmd_mv.format(i))
    time.sleep(1)
