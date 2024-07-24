


#        Write a script to make an HTTP request against the below provided API by setting New Zealand & Canada - country names as a query parameter and print first 5 colleges/universities info for each response.


# Method	: 	GET
# Path		: 	/search
# Host		: 	http://universities.hipolabs.com
# Query Param: 	country={country_name}

# *Bonus points if you can assert the responses.
import requests
import pytest

class TestReq:


    @pytest.mark.parametrize("country", [("Canada"),("New Zealand")])
    def test_met(self,country):
        self.url = "http://universities.hipolabs.com/search?country="+country
        resposne = requests.get(self.url)
        for data in resposne.json():
            assert data["country"] == country, str(data["name"]) + " does not have the expected country"
        
