def main():
    pins = {}
    subconnectors = ["A", "B", "C", "D"]
    curr_connector = None
    with open("pins.txt", "r") as f:
        for line in f:
            l = line.split("#")[0].strip()
            if len(l) == 0:
                continue
            if l[0] == '.':
                curr_connector = l[1:]
                for sc in subconnectors:
                    pins[f"{curr_connector[-1]}{sc}"] = []
                continue
            l = l.split(" ")
            assert len(l) == (len(subconnectors) + 1)
            for (sc, pin_name) in zip(subconnectors, l[1:]):
                pins[f"{curr_connector[-1]}{sc}"].append((l[0], pin_name))
    lib_name = "kria_k26"
    comp_name = "KRIA_K26"
    with open(f"../{lib_name}.kicad_sym", "w") as f:
        print(f'(kicad_symbol_lib (version 20201005) (generator kria_k26_import)', file=f)
        print(f'  (symbol "{lib_name}:{comp_name}" (in_bom yes) (on_board yes)', file=f)
        print(f'    (property "Reference" "SOM" (id 0) (at 0 1.27 0)', file=f)
        print(f'      (effects (font (size 1.27 1.27)))', file=f)
        print(f'    )', file=f)
        print(f'    (property "Value" "{lib_name}" (id 1) (at 0 3.81 0)', file=f)
        print(f'      (effects (font (size 1.27 1.27)))', file=f)
        print(f'    )', file=f)
        print(f'    (property "Footprint" "" (id 2) (at 0 0 0)', file=f)
        print(f'      (effects (font (size 1.27 1.27)) hide)', file=f)
        print(f'    )', file=f)
        print(f'    (property "Datasheet" "" (id 3) (at 0 0 0)', file=f)
        print(f'      (effects (font (size 1.27 1.27)) hide)', file=f)
        print(f'    )', file=f)
        for (i, (unit, pins)) in enumerate(sorted(pins.items(), key=lambda x: x[0])):
            pin_x = -20.32
            pin_y = -2.54
            pin_dy = -2.54
            pin_len = 5.08
            print(f'    (symbol "{comp_name}_{i+1}_1"', file=f)
            for pin_num, pin_name in pins:
                print(f'      (pin passive line (at {pin_x:.2f} {pin_y:.2f} 0) (length {pin_len})', file=f)
                print(f'        (name "{pin_name}" (effects (font (size 1.27 1.27))))', file=f)
                print(f'        (number "{unit}{pin_num}" (effects (font (size 1.27 1.27))))', file=f)
                print(f'      )', file=f)
                pin_y += pin_dy
            print(f'       (rectangle (start {pin_x + pin_len:.2f} 0) (end {-(pin_x + pin_len):.2f} {pin_y:.2f})', file=f)
            print(f'         (stroke (width 0.1524)) (fill (type background))', file=f)
            print(f'       )', file=f)
            print(f'    )', file=f)
        print(f'  )', file=f)
        print(f')', file=f)

if __name__ == '__main__':
    main()
