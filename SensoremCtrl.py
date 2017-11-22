######## Imports ########
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
import csv



######## Directory Settings ##########
FILENAME = "/home/pi/Documents/Python Projects/CSV-files/sensor_data.csv"
WRITE_FREQUENCY = 1


######## Instanciate variables ########
sense = SenseHat()
sensorData = []
######## LED Notification ########
OnlineMessage = sense.show_message("Online")


######## Functions ########
def fileSetup():
    dataHeader = ['Temperature','Humidity','Timestamp']

    with open(sensor_data.csv, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for row in rows:
            writer.writerows(dataHeader)
            writer.close()

def appendFileHeaders():
    header = ['Temperature', 'Humidity', 'Timestamp']
    with open("/home/pi/Documents/Python Projects/CSV-files/sensor_data.csv", newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open("/home/pi/Documents/Python Projects/CSV-files/sensor_data.csv", 'a', newline='')  as f:
        write = csv.writer(f, delimiter=',')
        write.writerow(['Temperature', 'Humidity', 'Timestamp'])
        
        
def getSensorData():
    sensorData = []
    
    temperature = getTemperatureFromSensor()
    humidity = getHumidityFromSensor()
    time = getCurrentFormatedTimestamp()
    
    sensorData.append(round(temperature))
    sensorData.append(round(humidity))
    sensorData.append(time)

    return sensorData


def writeDataToFile():
    sensorData = []
    sensorData = getSensorData()
    
    with open("/home/pi/Documents/Python Projects/CSV-files/sensor_data.csv", 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(sensorData)


def getTemperatureFromSensor():
    temperature = sense.get_temperature()
    return temperature


def getHumidityFromSensor():
    humidity = sense.get_humidity()
    return humidity


def getCurrentFormatedTimestamp():
    localTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return localTime
    


######## Main Application ########
#fileSetup()
appendFileHeaders()
while True:
    OnlineMessage
    writeDataToFile()
    sense.clear()
    sleep(5)
