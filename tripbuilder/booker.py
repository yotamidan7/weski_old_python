#!/usr/bin/env python
import os
import sys

import unirest

def searchHotels(location):
   
    parameters = {}
    parameters["apiKey"] = "bd5n2kvxfvcezq7tfa2u6wkc"
    parameters["cid"] = "55505"
    parameters["apiExperience"] = "PARTNER_WEBSITE"
    parameters["numberOfResults"] = "2"
    parameters["city"] = location
    response = unirest.post("http://api.ean.com/ean-services/rs/hotel/v3/list?", headers={ "Accept": "application/json" }, params=parameters)

    names = []
    for hotel in response.body["HotelListResponse"]["HotelList"]["HotelSummary"]:
        names.append(hotel["name"])
    return names
