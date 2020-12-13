from pathlib import Path

curr_dir = Path(__file__).parent
with (curr_dir / "input.txt").open() as input:
    input_list = [in_line.split("\n")[0] for in_line in input]
    passport = {}
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    for line in input_list:
        if line:
            entries = { pair.split(":")[0] : pair.split(":")[1] for pair in line.split(" ")}
            passport.update(entries)
        else:
            try:
                if not (1920 <= int(passport["byr"]) <= 2002):
                    print(passport, "invalid byr")
                elif not (2010 <= int(passport["iyr"]) <= 2020):
                    print(passport, "invalid iyr")
                elif not (2020 <= int(passport["eyr"]) <= 2030):
                    print(passport, "invalid eyr")
                elif not (passport["ecl"] in ["amb" ,"blu" ,"brn" ,"gry" ,"grn" ,"hzl" ,"oth"]):
                    print(passport, "invalid ecl")
                elif not (len(passport["pid"]) == 9 and int(passport["pid"])):
                    print(passport, "invalid pid")
                elif not (passport["hcl"][0] == "#" and len(passport["hcl"]) == 7 and int(passport["hcl"][1:7], 16)):
                    print(passport, "invalid hcl")
                elif passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193:
                    valid_passports += 1
                elif passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76:
                    valid_passports += 1
                else:
                    print(passport, "invalid hgt", passport["hgt"][:-2])
            except Exception as e:
                print(passport, "invalid", e)
            finally:
                passport = {}
    print(valid_passports)