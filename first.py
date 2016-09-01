from urllib import request

google_url ='http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=0&e=16&f=2016&g=d&a=2&b=27&c=2014&ignore=.csv'

def download(csv_url):
    responce = request.urlopen(google_url)
    csv = responce.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'Goog.csv'
    fx = open('Goog.csv','w')
    for line in lines:
        fx.write(line +'\n')
    fx.close()

download(google_url)
