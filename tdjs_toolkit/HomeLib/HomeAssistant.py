import requests
import json





class LightEntityObject:
    def __init__(self,
                 AUTHORITY: HomeAssistant,
                 entity_id: str):
        self.AUTHORITY = AUTHORITY
        self.entity_id = entity_id
        self.entity_request_data = requests.get(
            f"{AUTHORITY.HA_URL}/api/states/{entity_id}",
            headers=AUTHORITY.HEADERS,
        )
        self.entity_data = json.loads(self.entity_request_data.text,)
        self.area = self.entity_data

    def toggle(self):
        return requests.post(
            f"{self.AUTHORITY.HA_URL}/api/services/light/toggle",
            headers=self.AUTHORITY.HEADERS,
            json={
                "entity_id": self.entity_id
            }
        )

    def turn_off(self):
        return requests.post(
            f"{self.AUTHORITY.HA_URL}/api/services/light/turn_off",
            headers=self.AUTHORITY.HEADERS,
            json={
                "entity_id": self.entity_id
            }
        )

    def turn_on(self,
                transition: int =2,
                brightness: int | None = None,
                color: list | None = None):
        data: dict[str, object] = {
                "entity_id": self.entity_id,
                "transition": transition
            }
        if isinstance(brightness, int):
            data["brightness_pct"] = brightness
        if isinstance(color, list):
            data["rgb_color"] = color
        return requests.post(
            f"{self.AUTHORITY.HA_URL}/api/services/light/turn_on",
            headers=self.AUTHORITY.HEADERS,
            json=data,
            timeout=5
        )

class FanEntityObject:
    def __init__(self, AUTHORITY: HomeAssistant, entity_id: str):
        self.AUTHORITY = AUTHORITY
        self.entity_id = entity_id
        self.entity_request_data = requests.get(
            f"{AUTHORITY.HA_URL}/api/states/{entity_id}",
            headers=AUTHORITY.HEADERS,
        )
        self.entity_data = json.loads(self.entity_request_data.text, )

    def toggle(self,):
        return requests.post(
            f"{self.AUTHORITY.HA_URL}/api/services/fan/toggle",
            headers=self.AUTHORITY.HEADERS,
            json={
                "entity_id": self.entity_id
            },
            timeout=5
        )

    def turn_off(self,):
        return requests.post(
            f"{self.AUTHORITY.HA_URL}/api/services/fan/turn_off",
            headers=self.AUTHORITY.HEADERS,
            json={
                "entity_id": self.entity_id
            },
            timeout=5
        )

    def turn_on(self,):
        return requests.post(
            f"{self.AUTHORITY.HA_URL}/api/services/fan/turn_on",
            headers=self.AUTHORITY.HEADERS,
            json={
                "entity_id": self.entity_id
            },
            timeout=5
        )

    def set_settings(self, oscillate: bool | None = None,
                     direction: str | None = None,
                     speed: int | None = None,
                     preset: str | None = None
                     ):
        def request(data, ep, value):
            requests.post(
                f"{self.AUTHORITY.HA_URL}/api/services/fan/{ep}",
                headers=self.AUTHORITY.HEADERS,
                json={
                    "entity_id": self.entity_id,
                    data: value
                },
                timeout=5
            )

        if oscillate is not None:
            request("oscillate", "oscillate", oscillate)
        if speed is not None:
            request("percentage", "set_percentage", speed)
        if preset is not None:
            request("preset_mode", "set_preset_mode", preset)
        if direction is not None:
            request("direction", "set_direction", direction)



class HomeAssistant:
    def __init__(self, url: str, token: str):
        if url is None or token is None:
            raise NameError("Missing a parameter of tdjs.homeassistant.HomeAssistant")
        self.HA_URL = url.rstrip("/")
        self.HA_TOKEN = token
        self.HEADERS = {
            "Authorization": f"Bearer {self.HA_TOKEN}",
            "content-type": "application/json",
        }


        requests.get(
            f"{self.HA_URL}/api",
            headers=self.HEADERS
        )


        print("TDJS.HomeAssistantLib Initialized")

    def ping_api(self):
        return requests.get(
            f"{self.HA_URL}/api/",
            headers=self.HEADERS
        )
    def get_state(self, entity):
        return requests.get(
            f"{self.HA_URL}/api/states/{entity}",
            headers=self.HEADERS,
        )
    def get_entities(self):
        return requests.get(
            f"{self.HA_URL}/api/states",
            headers=self.HEADERS
        )