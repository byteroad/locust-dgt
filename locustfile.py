from locust import HttpUser, task

#wfs = 'https://www.mapsforeurope.org/maps/wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&typename=ome:egm_wfs_coastl&token=$OEMAPS'

crus_col = 'https://ogcapi.dgterritorio.gov.pt/collections/crus'
crus_items = 'https://ogcapi.dgterritorio.gov.pt/collections/crus/items'
crus_nl = 'https://ogcapi.dgterritorio.gov.pt/collections/crus/items?limit=10000'
crus_tiles = 'https://ogcapi.dgterritorio.gov.pt/collections/crus/tiles'

class TestEndpoint(HttpUser):
    @task
    def test(self):
        #self.client.get(wfs)
        self.client.get(crus_col)