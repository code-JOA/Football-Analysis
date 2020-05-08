class WeatherGetter(object):
    """First initialised using Lat, Long data. By default latitude
    and long is of Berlin. Note there has been some changes in the
    API . Read Detrous/darksky on github. He fixed the summary issue
    a few days ago. Return to his github whenever you have any issues
    """
    
    def __init__(self, loc =["52.5200", "13.4050"]):
        self.lat = loc[0]
        self.long = loc[1]
        self.url = "https://api.darksky.net/forecast/{}/{},{},{}T12:00:00?exclude=currently,flag"
        
    def keys(self, path='/Users/flatironschool/.secret/darksky.json'):
        with open(path) as f:
            keys = json.load(f)
        return keys['api_key']
    
    def onDay(self, date):
        api_key = self.keys()
        resp = requests.get(self.url.format(api_key,self.lat,self.long, date))
        result = resp.json()
        try:
            weather = result['daily']['data'][0]['icon']
        except:
            try:
                weather = result['daily']['data'][0]['summary']
            except: 
                weather = 'no data'
            
            
        return weather
    
    def for_days(self, datelist):
        weather = []
        for date in datelist:
            weather.append(self.onDay(date))
        return weather
    
    def test_one(self, date, cond='rain'):
        self.cond = cond
        weather_report = self.onDay(date)
        try:
            if cond in weather_report:
                return True
            else:
                return False
        except:
            return '?'
    
    def test_many(self, datelist, cond='rain'):
        weather_reports = {}
        for date in datelist:
            weather_reports[date] = self.test_one(date, cond)
        return weather_reports
                
