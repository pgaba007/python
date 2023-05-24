#Formula 1 coding question:
#For a formula one race starting. 
#The initial lap time of wet tyre is 90 seconds for every lap after first lap, the wet tyre will lap 0.055 seconds slowe every lap. 
#The initial lap time of medium tyre is 95 seconds for every lap after first lap, the medium tyre will lap 0.085 seconds faster every lap. 
#For a 58 lap race find and print lap number at which medium tyre is faster than wet tyre. 

#Python 3

wet_tyre_lap_time = 90
medium_tyre_lap_time = 95

for lap in range(2, 59):
    wet_tyre_lap_time += 0.055  # Wet tire gets 0.055 seconds slower each lap
    medium_tyre_lap_time -= 0.085  # Medium tire gets 0.085 seconds faster each lap
    
    if medium_tyre_lap_time < wet_tyre_lap_time:
        print("Medium tire is faster than wet tire at lap", lap)
        break
