class ComputerDevice:
    def __init__(self, device_id: str, is_functional: bool, ram_gb: int, assigned_user: str):
        # Public attributes
        self.device_id = device_id
        self.is_functional = is_functional
        self.ram_gb = ram_gb
        
        # Private attribute 
        self.__assigned_user = assigned_user
      
    # Method 1: Reads/returns information about the private attribute
    def get_assigned_user(self) -> str:
        return self.__assigned_user

    # Method 2: Takes a parameter and modifies state
    def assign_user(self, new_user: str) -> None:
        if self.is_functional:
            self.__assigned_user = new_user
            print(f"Device {self.device_id} successfully assigned to {self.__assigned_user}.")
        else:
            print(f"Cannot assign user: Device {self.device_id} is not functional.")

    # Method 3: Modifies state safely
    def report_issue(self) -> None:
        self.is_functional = False
        print(f"Issue reported: Device {self.device_id} status set to non-functional.")

    # Method 4: General status action
    def power_on(self) -> None:
        if self.is_functional:
            print(f"Device {self.device_id} is powering on...")
        else:
            print(f"Device {self.device_id} failed to power on (Maintenance required).")


# Step 6 & 7: Test Script (Instantiate 2 Objects & Modify Only Object 1)
if __name__ == "__main__":
    # Instantiate two independent objects
    dev1 = ComputerDevice("DEV-101", True, 16, "Frexus")
    dev2 = ComputerDevice("DEV-102", True, 8, "Armel")

    print("--- BEFORE ---")
    print(f"Device 1 ({dev1.device_id}): User = {dev1.get_assigned_user()}, Functional = {dev1.is_functional}")
    print(f"Device 2 ({dev2.device_id}): User = {dev2.get_assigned_user()}, Functional = {dev2.is_functional}\n")

    print("--- Performing action on Object 1 ---")
    dev1.assign_user("Charlie")
    dev1.report_issue()
    print()

    print("--- AFTER ---")
    print(f"Device 1 ({dev1.device_id}): User = {dev1.get_assigned_user()}, Functional = {dev1.is_functional}")
    print(f"Device 2 ({dev2.device_id}): User = {dev2.get_assigned_user()}, Functional = {dev2.is_functional}")
