import time
class Config:

  def __init__(self):

    #---------------------GENERAL CONFIG-------------------------#
    #The default protocol identifier
    self.protocol = "http://"
    
    #The default call ip location for the elastic stack
    self.ip = "127.0.0.1"

    #the default port to use where elasticsearch is listening
    self.port = ":9200"


    #---------------------SEARCH CONFIG--------------------------#
    #the default extra information for simple search
    self.extraSearch = "/_search"

    #the default methods for search
    self.getMethod = "get"
    self.putMethod = "put"
    self.deleteMethod = "delete"

    #the default header information
    self.header = {'Content-Type':'application/json'}

    #the defualt path to WEEKLY search json
    self.weeklySearch = "search_scripts/search_weekly/searchWeekly.json"

    #the default path to MONTHLY search json
    self.monthlySearch = "search_scripts/search_monthly/searchMonthly.json"

    #the default path to YEARLY search json
    self.yearlySearch = "search_scripts/search_yearly/searchYearly.json"


    #--------------------INDEXING CONFIG----------------------#
    #week docs go into monthly indexes using week type
    self.weekDoc = "/week_stats"+ str(time.strftime("%d-%m-%y"))
    self.weekType ="/week_stats"
    self.monthlyIndex = "/stats_month_"+ str(time.strftime("%m-%y"))

    #month docs go into yearly indexes using month type
    self.monthDoc = "/month_stats"+ str(time.strftime("%m-%y"))
    self.monthType = "/month_stats"
    self.yearlyIndex = "/stats_year_"+ str(time.strftime("%y"))

    #year docs go into year index using year type
    self.yearDoc = "/year_stats"+ str(time.strftime("%y"))
    self.yearType = "/year_stats"
    self.yearIndex ="/stats_years"


    #--------------------STORAGE CONFIG------------------------#
    #the default path for monthly reports
    self.monthyReport = "storage/reports/monthly/"

    #the default path for yearly reports
    self.yearlyReport = "storage/reports/yearly/"
