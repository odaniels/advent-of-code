from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    memory = {}
    input_data = input.read().split("\n")

    for line in input_data:
        if "mask" in line:   
            raw_mask = line.split(" ")[-1]
            bit_mult = int(raw_mask.replace("X","1"), 2)
            bit_add = int(raw_mask.replace("X","0"), 2)
        else:
            command_parts = line.split(" ")
            adress, command = (int(command_parts[0][4:-1]), int(command_parts[-1]))
            memory[adress] = (command & bit_mult) | bit_add
    print("PART 1:", sum(adress for adress in memory.values()))

    memory = {}
    for line in input_data:
        if "mask" in line:  
            raw_mask = line.split(" ")[-1]
            bit_add = int(raw_mask.replace("X","0"), 2)
            bit_not_x = int(raw_mask.replace("0","1").replace("X","0"), 2)
            num_x = sum(c == "X" for c in line)
            raw_mask_parts = raw_mask.split("X")
            masks = []
            for comb in range(pow(2, num_x)):
                swaps = format(comb, f"0{num_x}b")
                mask = raw_mask_parts[0] + "".join(swaps[i] + part for i, part in enumerate(raw_mask_parts[1:]))
                masks.append(int(mask, 2))
        else:
            command_parts = line.split(" ")
            adress, command = (int(command_parts[0][4:-1]), int(command_parts[-1]))
            before_floats =  (adress | bit_add ) & bit_not_x
            for mask in masks:
                new_adress = before_floats | mask
                memory[new_adress] = command
    print("PART 2:", sum(adress for adress in memory.values()))