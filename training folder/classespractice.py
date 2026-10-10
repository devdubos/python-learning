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


class CoffeeMachinePro:
    def __init__(self, location_name: str):
        self.location = location_name
        self.maintenance_mode = False
        self.resources = {
            "water_ml": 2000,
            "coffee_beans_g": 500,
            "milk_ml": 1000
        }

    def toggle_maintenance(self, pin_code: str) -> str:
        if pin_code != "0000":
            return "Access Denied: Invalid PIN code!"
        
        self.maintenance_mode = not self.maintenance_mode
        
        if self.maintenance_mode:
            return "Machine is now in MAINTENANCE mode. Service required."
        else:
            return "Machine is now READY for customer orders."

    def refill_resource(self, resource_name: str, amount: int) -> str:
        if resource_name not in self.resources:
            return f"Error: Resource '{resource_name}' does not exist!"
        
        if amount <= 0:
            return "Error: Amount must be a positive number!"

        self.resources[resource_name] += amount
        return f"Successfully added {amount} to {resource_name}. Current total: {self.resources[resource_name]}."

    def brew_coffee(self, coffee_type: str, sugar_cubes: int = 0) -> str:
        if self.maintenance_mode:
            return "Error: Cannot brew coffee. Machine is in maintenance mode!"
            
        if not (0 <= sugar_cubes <= 5):
            return "Error: Sugar cubes must be between 0 and 5!"

        if coffee_type == "espresso":
            water_needed = 50
            beans_needed = 15
            milk_needed = 0
        elif coffee_type == "cappuccino":
            water_needed = 100
            beans_needed = 15
            milk_needed = 150
        else:
            return f"Error: Drink '{coffee_type}' is not on the menu!"