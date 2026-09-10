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
