import itertools

class Building:

    def __init__(self, no_of_floors, elevators) -> None:
        print(f"Building created")
        self.no_of_floors = no_of_floors
        self.floors = [Floor(i) for i in range(0, no_of_floors+1)]
        self.elevators = elevators

class Floor:
    def __init__(self, floor_no, ext_button):
        self.floor_no = floor_no
        self.ext_button = ext_button
        print(f"Floor created {self.floor_no}")
        

class Elevator:

    id_iter = itertools.count(1)

    def __init__(self, name, capacity_weight, current_floor, direction, status, internal_panel, internal_screen):
        self.id = next(Elevator.id_iter)
        self.name = name
        self.capacity = capacity_weight
        self.current_floor = current_floor
        self.direction = direction
        self.status = status
        self.internal_panel = internal_panel
        self.internal_screen = internal_screen

    def move(self, dest_floor, direction):
        print(f"Moving on floor {dest_floor} in {direction} direction")


class ExternalButton:

    def __init__(self, ext_dispatcher):
        self.ext_dispatcher = ext_dispatcher

    def press_button(self, floor, direction):
        self.floor = floor
        self.direction = direction


class ExternalDispatcher:

    # list of elevator controllers
    def __init__(self, ele_controllers) -> None:
        self.ele_controllers = ele_controllers

        


class InternalPanel:

    def __init__(self) -> None:
        # Internal Dispatcher object
        pass

    def press_button(self, dest_floor):
        print(f"You have pressed the button for {dest_floor} floor.")


class InternalScreen:
    
    def __init__(self, curr_floor, direction) -> None:
        self.curr_floor = curr_floor
        self.direction = direction


class ElevatorController:

    def __init__(self) -> None:
        # Elevator object
        pass

    def accept_new_request(self, dets_floor, direction):
        print(f"Acceptig new request")

    def control_elevator(self):
        # instruct elevator to move
        pass



if __name__ == "__main__":
    ext_dispatcher = ExternalDispatcher()
    building = Building(20, 3)

# internal_panel = "internal panel object"
# internal_screen = "internal screen object"

# ele1 = Elevator("Elevator-1", 600, 0, "Upwards", "Idle", internal_panel, internal_screen)
# ele2 = Elevator("Elevator-2", 600, 0, "Upwards", "Idle", internal_panel, internal_screen)
# ele3 = Elevator("Elevator-3", 800, 0, "Upwards", "Idle", internal_panel, internal_screen)

# print(ele1.id, ele2.id, ele3.id)

