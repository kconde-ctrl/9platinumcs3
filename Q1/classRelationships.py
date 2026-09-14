class ComputerDevice:
  def __init__(self, device_id: str, is_functional: bool, ram_GB: int, assigned_user: str):
    self.device_id = device_id
    self.is_functional = is_functional
    self.ram_GB = ram_GB
    self.__assigned_user = assigned_user

def get_assigned_user(self) -> str:
  return self.__assigned_user

def assign_user(self, new_user: str) -> None:
  if self.is_functional:
    self.__assigned_user = new_user
    print(f"Device {self.device_id} seccessfully assigned to {self. __assigned_user}")
  else:
    print(f"Cannot assign user: Device {self.device_id} is not functional")

def report_issue(self) -> None:
  self.is_functional = False
  print(f"Issue reported: Device {self.device_id} status set to non-functional")

def power_on(self) -> None:
  if self.is_functional:
    print(f"Device {self.device_id} is powering on. . . ")
  else:
    print(f"Device {self.device_id} failed to power on")

class ITDepartment:
  def __init__(self, dept_name: str, location: str):
    self.dept_name = dept_name
    self.location = location
    self.managed_devices = []

def add_devices(self, device: ComputerDevice) -> None:
  """Stores the actual object reference inside the list."""
        self.managed_devices.append(device)
        print(f"Added device {device.device_id} to {self.dept_name} inventory.")

    def display_inventory(self) -> None:
        print(f"\n--- Inventory for {self.dept_name} ({self.location}) ---")
        if not self.managed_devices:
            print("No devices assigned to this department.")
            return 
          
      for dev in self.managed_devices:
            status = "Functional" if dev.is_functional else "Non-Functional"
            print(f"- Device ID: {dev.device_id} | User: {dev.get_assigned_user()} | RAM: {dev.ram_gb}GB | Status: {status}")

if __name__ == "__main__":
    print("=== BEFORE RELATIONSHIP ===")
    
    it_dept = ITDepartment("Main Tech Support", "Building A Room 101")
    
    dev1 = ComputerDevice("DEV-101", True, 16, "Frexus")
    dev2 = ComputerDevice("DEV-102", True, 8, "Armel")
    dev3 = ComputerDevice("DEV-103", False, 32, "Charlie")

    print(f"Department created: {it_dept.dept_name}")
    print(f"Created standalone devices: {dev1.device_id}, {dev2.device_id}, {dev3.device_id}")
    it_dept.display_inventory()

    print("\n=== BUILDING RELATIONSHIP ===")
    it_dept.add_device(dev1)
    it_dept.add_device(dev2)
    it_dept.add_device(dev3)

    print("\n=== AFTER RELATIONSHIP ===")
    
    it_dept.display_inventory()

    print("\n=== DEMONSTRATING SHARED OBJECT DATA & MUTABILITY ===")
    
    dev1.report_issue()
    print("\nUpdated Inventory Status (reflects real-time object changes):")
    it_dept.display_inventory()
