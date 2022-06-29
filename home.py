import requests

gover_encode = r'h3%2FCptW8MZ4KfUVyw0ghR2KGSmCYLHVAP2rMLPX93EO0rJ%2Bq3wlZeLK4pubReLPflFv8uB9R5EUQ4rqmpZI6SA%3D%3D'
gover_decode = r'h3/CptW8MZ4KfUVyw0ghR2KGSmCYLHVAP2rMLPX93EO0rJ+q3wlZeLK4pubReLPflFv8uB9R5EUQ4rqmpZI6SA=='
url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'

params ={'serviceKey' : gover_decode, 'pageNo' : '1', 'numOfRows' : '10', 'LAWD_CD' : '11110', 'DEAL_YMD' : '202112' }


response = requests.get(url, params=params)
print(response.text)