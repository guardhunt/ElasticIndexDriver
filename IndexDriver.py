import requests
from Config import Config

class IndexDriver:

  def __init__(self):
    self.cf = Config()		#configuration
    self.prtcl = self.cf.protocol #protocol identifier
    self.method = ""		#call method
    self.ip = self.cf.ip	#elasticsearch ip
    self.port = self.cf.port	#elasticsearch port
    self.extra = ""		#specified api call or storage location
    self.header = self.cf.header#header for call
    self.query  = ""		#path to search/put query file


  def _search(self):
    """build and run requests query"""
    query_payload = getattr(requests, self.method)(self.prtcl + self.ip + self.port + self.extra, headers=self.header, data=self.query)
    query_feed = query_payload.text

    return query_feed


  def _store(self, data):
    """store any json object for testing output by passing on a call"""
    storage = open("storage/test_storage.json", "a")
    storage.write(data)
    storage.close()    
    return data

  def _build(self, indexingData):
    """configure get statistics and put statistics searches"""
    self.method = self.cf.getMethod
    self.query = open(self.query)	#set self.query to json search
    self.extra = self.cf.extraSearch	#set extra to search from config module		
    stats  = self._search()		#get stats retured from search query
    
    self.query.close()			#close json search file
    
    self.method = self.cf.putMethod
    self.query = stats			#set query to stats
    self.extra = indexingData		#change extra to driver specific informaiton
    feedback = self._search()		#run put query to add stats data to index
    
    return(self._store(stats), feedback)


  def _delete(self):
    pass


  def weekly_driver(self):
    """execute weekly search, store and delete"""
    indexingData = (self.cf.monthlyIndex +  self.cf.weekType + self.cf.weekDoc)
    self.query = self.cf.weeklySearch	
    (stats, feedback) = self._build(indexingData)

    return (stats,feedback)


  def monthly_driver(self):
    """execute monthyl search, store, and delete"""
    indexingData = (self.cf.yearlyIndex + self.cf.monthType + self.cf.monthDoc)
    self.query = self.cf.monthlySearch
    (stats, feedback) = self._build(indexingData)

    return (stats, feedback)


  def yearly_driver(self):
    """execute yearly search, store, and delete"""
    indexingData = (self.cf.yearIndex + self.cf.yearType + self.cf.yearDoc)
    self.query = self.cf.yearlySearch
    (stats, feedback) = self._build(indexingData)

    return (stats, feedback)

   
