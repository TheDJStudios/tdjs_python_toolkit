import requests

class LightEntity:
    def __init__(self,url,token,headers):
        self.haurl = url
        self.hatoken = token
        self.headers = headers
        pass
    def toggle(self, entity):
        return requests.post(
            f"{self.haurl}/api/services/light/toggle",
            headers=self.headers,
            json={
                "entity_id": entity
            },
            timeout=5
        )
    def turn_on(self,
                entity,
                transition=2,
                brightness: int | None = None,
                rgb_color: list | None = None):
        data = {
                "entity_id": entity,
            }
        if brightness is not None:
            data["brightness_pct"] = brightness
        if rgb_color is not None:
            data["rgb_color"] = rgb_color
        return requests.post(
            f"{self.haurl}/api/services/light/turn_on",
            headers=self.headers,
            json=data,
            timeout=5
        )
    def turn_off(self, entity):
        return requests.post(
            f"{self.haurl}/api/services/light/turn_off",
            headers=self.headers,
            json={
                "entity_id": entity
            },
            timeout=5
        )



class FanEntity:
    def __init__(self,url,token,headers):
        self.haurl = url
        self.hatoken = token
        self.headers = headers
        pass
    def toggle(self, entity):
        return requests.post(
            f"{self.haurl}/api/services/fan/toggle",
            headers=self.headers,
            json={
                "entity_id": entity
            },
            timeout=5
        )
    def turn_off(self, entity):
        return requests.post(
            f"{self.haurl}/api/services/fan/turn_off",
            headers=self.headers,
            json={
                "entity_id": entity
            },
            timeout=5
        )
    def turn_on(self, entity):
        return requests.post(
            f"{self.haurl}/api/services/fan/turn_on",
            headers=self.headers,
            json={
                "entity_id": entity
            },
            timeout=5
        )
    def set_settings(self,entity, oscillate: bool | None = None,
                     direction: str | None = None,
                     speed: int | None = None,
                     preset: str | None = None
                     ):
        def request(data, ep, value):
            requests.post(
                f"{self.haurl}/api/services/fan/{ep}",
                headers=self.headers,
                json={
                    "entity_id": entity,
                    data: value
                },
                timeout=5
            )
        if oscillate is not None:
            request("oscillate", "oscillate", oscillate)
        if speed is not None:
            request("percentage","set_percentage", speed)
        if preset is not None:
            request("preset_mode", "set_preset_mode", preset)
        if direction is not None:
            request("direction","set_direction", direction)




class HomeAssistant:
    def __init__(self, url, token):
        if url is None or token is None:
            raise NameError("Missing a parameter of tdjs.homeassistant.HomeAssistant")
        self.ha_url = url
        self.ha_token = token
        self.request_headers = {
            "Authorization": f"Bearer {self.ha_token}",
            "content-type": "application/json",
        }

        self.LightEntity = LightEntity(self.ha_url, self.ha_token, self.request_headers)
        self.FanEntity = FanEntity(self.ha_url, self.ha_token, self.request_headers)


        requests.get(
            f"{self.ha_url}/api",
            headers=self.request_headers
        )


        print("TDJS.HomeAssistantLib Initialized")
    def get_state(self, entity):
        return requests.get(
            f"{self.ha_url}/api/states/{entity}",
            headers=self.request_headers,
        )
    def get_entities(self):
        return requests.get(
            f"{self.ha_url}/api/states",
            headers=self.request_headers
        )