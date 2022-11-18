from beewi_smartclim import BeewiSmartClimPoller

b = BeewiSmartClimPoller("78:A5:04:5A:9E:1D")
b.update_sensor()

temperature = b.get_temperature()
humidity = b.get_humidity()
battery = b.get_battery()

print(temperature, humidity, battery)
