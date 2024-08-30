from locust import HttpUser, task

wfs = 'https://www.mapsforeurope.org/maps/wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&typename=ome:egm_wfs_coastl&token=$OEMAPS'

oaf = 'https://emotional.byteroad.net/collections/hex350_grid_cardio_1920/items?limit=10000'


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        #self.client.get(wfs)
        self.client.get(oaf)