from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    input_data = input.read().split("\n\n")
    valid_ranges = {row.split(':')[0] : row.split(':')[1] for row in input_data[0].split("\n")}
    valid_ranges = {field: range_string.split(" or ") for field, range_string in valid_ranges.items()}
    valid_ranges = {field: [[int(limit) for limit in range_string.split('-')]
                            for range_string in range_strings] 
                    for field, range_strings in valid_ranges.items()}
    other_tickets = [{idx: int(value) for idx, value in enumerate(row.split(','))} 
                     for row in input_data[2].split("\n")[1:]]
    invalid_entries = []
    valid_tickets = []
    
    for ticket in other_tickets:
        for value in ticket.values():
            for ranges in valid_ranges.values():
                for limits in ranges:
                    if limits[0] <= value <= limits[1]:
                        break
                else:
                    continue
                break
            else:
                invalid_entries.append(value)
                break
        else:
            valid_tickets.append(ticket)

    valid_fields = {idx: list(valid_ranges.keys()) for idx in range(20)}

    for ticket in valid_tickets:
        for idx, value in ticket.items():
            for field, ranges in valid_ranges.items():
                for limits in ranges:
                    if limits[0] <= value <= limits[1]:
                        break
                else:
                    try:
                        valid_fields[idx].remove(field)
                    except:
                        pass
        
    final_fields = {idx: None for idx in range(20)}
    while not all(final_fields.values()):
        for idx, fields in valid_fields.items():
            if final_fields[idx]:
                continue
            if len(fields) == 1:
                final_fields.update({idx: fields[0]})
                for idx2 in valid_fields.keys():
                    if idx2 != idx and not final_fields[idx2]:
                        try:
                            valid_fields[idx2].remove(fields[0])
                        except:
                            pass

    my_ticket = {idx: int(value) for idx, value in enumerate(input_data[1].split("\n")[1].split(','))} 
    product = 1
    for index, field in final_fields.items():
        if "departure" in field:
            print(field, my_ticket[index])
            product *= my_ticket[index]
    print(product)
    