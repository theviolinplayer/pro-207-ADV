import random
import time
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
world = client.get_world()

blueprint_library = world.get_blueprint_library()
vehicle_blueprints = blueprint_library.filter('vehicle.*')

random_vehicle_bp = random.choice(vehicle_blueprints)

spawn_point = carla.Transform(carla.Location(x=230, y=195, z=40), carla.Rotation(yaw=180))
dropped_vehicle = world.spawn_actor(random_vehicle_bp, spawn_point)

dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.4))
time.sleep(0.006)

dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.4, steer=-0.6))
time.sleep(0.004)

dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.4))
time.sleep(0.01)

location = dropped_vehicle.get_location()
print(f"Car location: x={location.x}, y={location.y}, z={location.z}")

target_location = carla.Location(x=66.648193, y=0.766224, z=0.162060)

if location != target_location:
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.4, reverse=True))
    time.sleep(5)
else:
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.5))
    time.sleep(5)
