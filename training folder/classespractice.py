class SmartHomeSystem:
    def __init__(self, owner_name: str):
        self.owner = owner_name
        self.security_armed = False
        self.devices = {
            "living_room_light": {"status": "off", "brightness": 100},
            "air_conditioner": {"status": "off", "temperature": 22},
            "front_door_lock": {"status": "locked"}
        }

    def toggle_security(self, password: str) -> str:
        if password != "safe123":
            return "Access Denied: Incorrect password!"
        
        self.security_armed = not self.security_armed
        
        if self.security_armed:
            self.devices["front_door_lock"]["status"] = "locked"
            return "Security system is ARMED. Front door is locked."
        else:
            return "Security system is DISARMED."

    def adjust_light(self, room_light: str, status: str, brightness: int = 100) -> str:
        if room_light not in self.devices:
            return f"Error: Device '{room_light}' not found!"
        
        if status not in ["on", "off"]:
            return "Error: Status must be 'on' or 'off'!"
            
        if not (0 <= brightness <= 100):
            return "Error: Brightness must be between 0 and 100!"

        self.devices[room_light]["status"] = status
        self.devices[room_light]["brightness"] = brightness if status == "on" else 0
        
        return f"{room_light} is now {status} (Brightness: {self.devices[room_light]['brightness']}%)."

    def set_temperature(self, temp: int) -> str:
        if self.devices["air_conditioner"]["status"] == "off":
            return "Error: Air conditioner is turned off. Turn it on first!"
            
        if not (16 <= temp <= 30):
            return "Error: Temperature must be between 16 and 30 degrees Celsius!"
            
        self.devices["air_conditioner"]["temperature"] = temp
        return f"Air conditioner temperature set to {temp}°C."

    def get_system_status(self) -> dict:
        return {
            "owner": self.owner,
            "security_active": self.security_armed,
            "devices_state": self.devices
        }