from collections import deque


def product(values):
    result = values[0]
    for value in values[1:]:
        result *= value
    return result


def calculate_value(operator, packet_values):
    if operator == 0: return sum(packet_values)
    elif operator == 1: return product(packet_values)
    elif operator == 2: return min(packet_values)
    elif operator == 3: return max(packet_values)
    elif operator == 5: return int(packet_values[0] > packet_values[1])
    elif operator == 6: return int(packet_values[0] < packet_values[1])
    elif operator == 7: return int(packet_values[0] == packet_values[1])


def parse_packet(packet, p, version_sum):
    while True:
        version_sum += int(packet[p:p+3], 2)
        operator = int(packet[p+3:p+6], 2)
        p += 6

        if operator == 4:
            value = ""
            while True:
                start = packet[p]
                value += packet[p+1:p+5]
                p += 5
                if start == "0":
                    return int(value, 2), version_sum, p
        else:
            lt = packet[p]
            p += 1
            values = []
            if lt == "0":
                length = int(packet[p:p+15], 2)
                p += 15
                end = p + length
                while p < end:
                    value, version_sum, p = parse_packet(packet, p, version_sum)
                    values.append(value)
            if lt == "1":
                length = int(packet[p:p+11], 2)
                p += 11
                for _ in range(length):
                    value, version_sum, p = parse_packet(packet, p, version_sum)
                    values.append(value)

            return calculate_value(operator, values), version_sum, p


def main(input):
    bits = "".join([format(int(a, 16), "04b") for a in input.read().strip()])
    result, v_sum, _ = parse_packet(bits, 0, 0)
    return v_sum, result


TEST_EXPECTED = 20, 1
PUZZLE_EXPECTED = 821, 2056021084691