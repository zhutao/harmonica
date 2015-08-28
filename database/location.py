#-*- coding: utf-8 -*-

import sys

import geoip2.database

GEOIPCITYDB = './GeoLite2-City.mmdb'

class Location:
    '''
    This class for Geoip2 API
    IP -> Country and City
    '''
    def __init__(self, IP):
        self.reader = geoip2.database.Reader(GEOIPCITYDB)

        self.response = None
    
        self.country = None
        self.country_iso_code = None
        self.country_name = None
        
        self.subdivisions = None
        self.subdivisions_most_specific = None
        self.subdivisions_most_specific_name = None
        self.subdivisions_most_specific_iso_code = None
        
        self.city = None
        self.city_name = None

        try:
            self.response = self.reader.city(IP)

            self.country = self.response.country
            self.country_iso_code = self.country.iso_code
            self.country_name = self.country.name

            self.subdivisions = self.response.subdivisions
            self.subdivisions_most_specific = self.subdivisions.most_specific
            self.subdivisions_most_specific_name = self.subdivisions.most_specific.name
            self.subdivisions_most_specific_iso_code = self.subdivisions.most_specific.iso_code
            
            self.city = self.response.city
            self.city_name = self.city.name
            
        except Exception, e:
            print e
                        

    def getLocation(self):
        return self.response
            
            
    def getCountry(self):
        return self.country


    def getCountryISOCode(self):
        return self.country_iso_code


    def getCountryName(self):
        return self.country_name


    def getSubdivisions(self):
        return self.subdivisions


    def getSubdivisionsMostSpecific(self):
        return self.subdivisions_most_specific


    def getSubdivisionsMostSpecificName(self):
        return self.subdivisions_most_specific_name


    def getSubdivisionsMostSpecificISOCode(self):
        return self.subdivisions_most_specific_iso_code
        

    def getCity(self):
        return self.city


    def getCityName(self):
        return self.city_name

        


#########################################################################3
def test():
    location = Location(sys.argv[2])
    print location.getLocation()

    #print location.getCountry()
    #print location.getCountryISOCode()
    #print location.getCountryName()

    #print location.getSubdivisions()
    #print location.getSubdivisionsMostSpecific()
    #print location.getSubdivisionsMostSpecificName()
    #print location.getSubdivisionsMostSpecificISOCode()
    
    #print location.getCity()
    #print location.getCityName()

    
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        exit()

    if sys.argv[1] == 'test':
        test()


    exit()