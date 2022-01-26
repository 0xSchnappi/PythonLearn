#! python3
# quickWeather.py - 取得当前的天气预报
import requests, json

cityName = 'chengdu'
APIkey = 'OpenWeatherMap Token'
lang = 'zh_cn'
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&appid=' + APIkey + '&lang=' + lang
print(url)
jsonRes = requests.get(url)
weatherData = json.loads(jsonRes.text)
print(weatherData)

print('Current weather in %s:' % cityName)
print(weatherData['weather'][0]['main'], '-' , weatherData['weather'][0]['description'])
'''
# json数据包各个字段的含义
coord
    coord.lon城市地理位置，经度
    coord.lat城市地理位置、纬度
weather（更多信息天气条件代码）
    weather.id天气状况 ID
    weather.main 一组天气参数（雨、雪、极端等）
    weather.description组内天气状况。您可以使用您的语言获得输出。学到更多
    weather.icon天气图标 ID
base 内部参数
main
    main.temp温度。单位默认值：开尔文，公制：摄氏，英制：华氏。
    main.feels_like温度。这个温度参数解释了人类对天气的感知。单位默认值：开尔文，公制：摄氏，英制：华氏。
    main.pressure 大气压力（在海平面上，如果没有 sea_level 或 grnd_level 数据），hPa
    main.humidity 湿度， ％
    main.temp_min目前最低温度。这是目前观察到的最低温度（在大都市和城市地区）。单位默认值：开尔文，公制：摄氏，英制：华氏。
    main.temp_max目前最高温度。这是目前观察到的最高温度（在大都市和城市地区）。单位默认值：开尔文，公制：摄氏，英制：华氏。
    main.sea_level 海平面上的大气压，hPa
    main.grnd_level 地面大气压，hPa
wind
    wind.speed风速。单位默认值：米/秒，公制：米/秒，英制：英里/小时。
    wind.deg风向，度数（气象）
    wind.gust阵风。单位默认值：米/秒，公制：米/秒，英制：英里/小时
clouds
    clouds.all 云量，%
rain
    rain.1h 近1小时雨量，mm
    rain.3h 近 3 小时雨量，mm
snow
    snow.1h 过去1小时积雪量，mm
    snow.3h 最近 3 小时的降雪量，mm
dt 数据计算时间，unix，UTC
sys
    sys.type 内部参数
    sys.id 内部参数
    sys.message 内部参数
    sys.country 国家代码（GB、JP 等）
    sys.sunrise 日出时间，unix，UTC
    sys.sunset 日落时间，unix，UTC
timezone 以秒为单位从 UTC 偏移
id 城市编号
name城市名
cod 内部参数
XML
'''