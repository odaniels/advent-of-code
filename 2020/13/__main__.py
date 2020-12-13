from pathlib import Path
import numpy as np

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    arrival, bus_string = input.read().split("\n")
    bus_ids = [int(bus_id) for bus_id in bus_string.split(",") if bus_id != "x"]
    bus_with_waiting_times = {bus_id: bus_id - (int(arrival) % bus_id) for bus_id in bus_ids}
    bus_id, waiting_time = min(bus_with_waiting_times.items(), key=lambda x: x[1])
    print("PART 1: ", bus_id * waiting_time)

    bus_ids_with_index = {int(bus_id): i for i, bus_id in enumerate(bus_string.split(",")) if bus_id != "x"}
    sorted_buses = sorted(bus_ids_with_index.items(), key=lambda item: item[0])
    print(sorted_buses)
    timestamp = 0
    iteration = 0
    next_step = 1
    for bus_id, index in sorted_buses:
        while True:
            iteration += 1
            timestamp += next_step
            time_to_next = (bus_id - (timestamp % bus_id))
            diff = (time_to_next - index) % bus_id
            if not diff:
                next_step *= bus_id
                break
    print(timestamp, iteration)