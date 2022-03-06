import time
def main():
    M = 4
    N = 60
    subconnectors = ["A", "B", "C", "D"]

    dx_outline = -3.175
    dy_outline = 3.175

    w_outline = 77
    h_outline = 60

    dx_conn = (3.77, 70.65)
    dy_conn = -8.09
    dx_standoff = 70.38
    dy_standoff = -53.65

    dia_standoff = 4.45

    dy_pad = -0.635
    dx_pad = (0, -0.96, -2.54, -3.50) # note col 'A' is outermost
    dia_pad = 0.46 # TODO

    # Relative to pad A1
    dx_calign = (-1.75, -0.48)
    dy_calign = (1.4, -38.87)
    dia_calign = 0.9
    dx_conn_outline = -4.25
    dy_conn_outline = 2.675
    w_conn = 5
    h_conn = 42.82
    cr_conn = 1.33

    mod_name = "KRIA_K26"
    with open(f"../meowality.pretty/{mod_name}.kicad_mod", "w") as f:
        print(f'(footprint "{mod_name}" (version 20210126) (generator pcbnew) (layer "F.Cu")', file=f)
        print(f'  (fp_text reference "REF**" (at 0 0 unlocked) (layer "F.SilkS")', file=f)
        print(f'    (effects (font (size 1 1) (thickness 0.15)))', file=f)
        print(f'  )', file=f)
        print(f'  (fp_text value "{mod_name}" (at 0 2 unlocked) (layer "F.Fab")', file=f)
        print(f'    (effects (font (size 1 1) (thickness 0.15)))', file=f)
        print(f'  )', file=f)
        # SoM outline
        print(f'  (fp_line (start {dx_outline} {dy_outline}) (end {dx_outline+w_outline} {dy_outline}) (layer "F.SilkS") (width 0.15))', file=f)
        print(f'  (fp_line (start {dx_outline+w_outline} {dy_outline}) (end {dx_outline+w_outline} {dy_outline-h_outline}) (layer "F.SilkS") (width 0.15))', file=f)
        print(f'  (fp_line (start {dx_outline+w_outline} {dy_outline-h_outline}) (end {dx_outline} {dy_outline-h_outline}) (layer "F.SilkS") (width 0.15))', file=f)
        print(f'  (fp_line (start {dx_outline} {dy_outline-h_outline}) (end {dx_outline} {dy_outline}) (layer "F.SilkS") (width 0.15))', file=f)
        # Standoff holes
        print(f'  (pad "" np_thru_hole circle (at 0 0) (size {dia_standoff} {dia_standoff}) (drill {dia_standoff}) (layers *.Cu *.Mask))', file=f)
        print(f'  (pad "" np_thru_hole circle (at {dx_standoff} 0) (size {dia_standoff} {dia_standoff}) (drill {dia_standoff}) (layers *.Cu *.Mask))', file=f)
        print(f'  (pad "" np_thru_hole circle (at 0 {dy_standoff}) (size {dia_standoff} {dia_standoff}) (drill {dia_standoff}) (layers *.Cu *.Mask))', file=f)
        print(f'  (pad "" np_thru_hole circle (at {dx_standoff} {dy_standoff}) (size {dia_standoff} {dia_standoff}) (drill {dia_standoff}) (layers *.Cu *.Mask))', file=f)
        for conn in range(2):
            # Connector balls
            for col in range(M):
                sc = subconnectors[col]
                for row in range(N):
                    x = dx_conn[conn] + dx_pad[col]
                    y = dy_conn + dy_pad * row
                    print(f'  (pad {conn+1}{sc}{row+1} smd circle (at {x} {y}) (size {dia_pad} {dia_pad}) (layers F.Cu F.Paste F.Mask))', file=f)
            # Alignment holes
            x0 = dx_conn[conn] + dx_pad[0]
            y0 = dy_conn
            for (dx, dy) in zip(dx_calign, dy_calign):
                print(f'  (pad "" np_thru_hole circle (at {x0+dx} {y0+dy}) (size {dia_calign} {dia_calign}) (drill {dia_calign}) (layers *.Cu *.Mask))', file=f)
            # Connector outline
            xc = x0 + dx_conn_outline
            yc = y0 + dy_conn_outline
            print(f'  (fp_line (start {xc} {yc}) (end {xc+w_conn-cr_conn} {yc}) (layer "F.SilkS") (width 0.15))', file=f) # ---
            print(f'  (fp_line (start {xc+w_conn-cr_conn} {yc}) (end {xc+w_conn} {yc-cr_conn}) (layer "F.SilkS") (width 0.15))', file=f) 
            print(f'  (fp_line (start {xc+w_conn} {yc-cr_conn}) (end {xc+w_conn} {yc-h_conn+cr_conn}) (layer "F.SilkS") (width 0.15))', file=f) 
            print(f'  (fp_line (start {xc+w_conn} {yc-h_conn+cr_conn}) (end {xc+w_conn-cr_conn} {yc-h_conn}) (layer "F.SilkS") (width 0.15))', file=f)
            print(f'  (fp_line (start {xc+w_conn-cr_conn} {yc-h_conn}) (end {xc} {yc-h_conn}) (layer "F.SilkS") (width 0.15))', file=f)
            print(f'  (fp_line (start {xc} {yc-h_conn}) (end {xc} {yc}) (layer "F.SilkS") (width 0.15))', file=f)
            print(f'  (fp_text user ".{conn+1}" (at {xc+w_conn/2} {yc+1.5} unlocked) (layer "F.SilkS")', file=f)
            print(f'    (effects (font (size 1 1) (thickness 0.15)))', file=f)
            print(f'  )', file=f)
        print(f')', file=f)

if __name__ == '__main__':
    main()
