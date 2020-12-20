import json
import pogreshnosti


class Const:
    K = 100
    d = 0.5 * 10 ** -6
    sigma = 0.34
    B = 1.25 * 10 ** -4
    a = 5.3 * 10 ** -4


def print_json(j: dict):
    print(json.dumps(j, indent=2, skipkeys=True))


def load_config():
    with open("config.json", "r") as f:
        cfg = json.load(f)
    new_cfg = {}
    for k0, v0 in cfg.items():
        new_cfg[k0] = {}
        for k1, v1 in cfg[k0].items():
            nk1 = float(k1)
            new_cfg[k0][nk1] = {}
            for k2, v2 in cfg[k0][k1].items():
                new_cfg[k0][nk1][k2] = {}
                for k3, v3 in cfg[k0][k1][k2].items():
                    new_cfg[k0][nk1][k2][float(k3)] = v3

    return new_cfg


def R(U1, I1, I2):
    R = (U1 * Const.d) / (Const.K * I2 * (Const.B + Const.a * I1))
    return R


def mu(RR):
    mu_ = round(abs(RR * Const.sigma), 3)
    return mu_


def calc1(cfg: dict):
    l = []
    core = ""
    for k0, v0 in cfg.items():  # I1 : dict
        for k1, v1 in cfg[k0].items():  # I val : dict
            line = f"\\multirow{{7}}{{*}}{{{k1}}}\n "
            core += line
            for k2, v2 in cfg[k0][k1].items():  # U2 : dict
                i = 1
                for k3, v3 in cfg[k0][k1][k2].items():  # U2 val : U1 val
                    U1 = v3
                    I1 = k1 * 10 ** -3
                    I2 = k3 * 10 ** -3
                    RR = round(R(U1, I1, I2), 5)
                    l.append(RR)
                    line = f"& {k3} & {v3} & {RR}\\\\\n"
                    if i == 7:
                        line += "\\hline"
                    else:
                        line += "\\cline{2-4}"
                    line += '\n'
                    i += 1
                    core += line

    calc1 = f"""
    \\begin{{table}}[htp!]
        \\centering
        \\label{{table}}
        \\scalebox{{1}}{{
            \\begin{{tabular}}{{|c|c|c|c|}}
                \\hline
                $ I_1 $, мА & $ I_2 = U_2 $, мА & $ U_1 $, В & $ R = \\dfrac{{U_x * d}}{{BI_{{xi}}}} $\\\\
                \\hline
                {core}
            \\end{{tabular}}
        }}  % scalebox
    \\end{{table}}
        """
    return calc1, l


def calc2(Rl):
    l = []
    core = ""
    for r in Rl:
        l.append(mu(r))
        line = f"{r} & {mu(r)}\\\\\n"
        core += line
    calc2 = f"""
    \\begin{{table}}[htp!]
        \\centering
        \\label{{table}}
        \\scalebox{{1}}{{
            \\begin{{tabular}}{{|c|c|}}
                \\hline
                $ R $ & $ \\mu = \\sigma R $\\\\
                \\hline
                {core}
            \\end{{tabular}}
        }}  % scalebox
    \\end{{table}}
        """
    return calc2, l


def make_protocol(cfg: dict):
    protocol_core = ""
    for k0, v0 in cfg.items():  # I1 : dict
        for k1, v1 in cfg[k0].items():  # I val : dict
            line = f"\\multirow{{7}}{{*}}{{{k1}}}\n "
            protocol_core += line
            for k2, v2 in cfg[k0][k1].items():  # U2 : dict
                i = 1
                for k3, v3 in cfg[k0][k1][k2].items():  # U2 val : U1 val
                    line = f"& {k3} & {v3}\\\\\n"
                    if i == 7:
                        line += "\\hline"
                    else:
                        line += "\\cline{2-3}"
                    line += '\n'
                    i += 1
                    protocol_core += line

    constants = r"""
\quad
\begin{tabular}{|l|c|r|}
    \hline
    \multicolumn{3}{|c|}{Константы эксперимента}\\
    \hline
    $ K $ & Коэффициент усиления ОУ & 100\\
    \hline
    $ d $ & Толщина полупроводника & 0.5 мкм\\
    \hline
    $ \sigma $ & Удельная эл-сть полу-ка & $ 3.4 * 10^{-1} $ Ом$^{-1} \times$м$^{-1}$\\
    \hline
    $ B_0 $ & Коэффициент & $ 1.25 \times 10^{-4} $ Тл\\
    \hline
    $ a $ & Коэффициент & $ 5.3 \times 10^{-4} $ Тл/А\\
    \hline
\end{tabular}
    """
    protocol = f"""
\\begin{{table}}[htp!]
    \\centering
    \\label{{table}}
    \\scalebox{{1}}{{
        \\begin{{tabular}}{{|c|c|c|}}
            \\hline
            $ I_1 $, мА & $ I_2 = U_2 $, мА & $ U_1 $, В\\\\
            \\hline
            {protocol_core}
        \\end{{tabular}}
    {constants}
    }}  % scalebox
\\end{{table}}
    """
    return protocol


if __name__ == '__main__':
    config = load_config()
    # print_json(config)
    with open("protocol.tex", "w", encoding='utf-8') as f:
        f.write("\\section*{Протокол}\n\n")
        f.write(make_protocol(config))

    with open("I.tex", "w", encoding='utf-8') as f:
        f.write("\\section*{I}\n\n")
        content, Rl = calc1(config)
        f.write(content)

    with open("II.tex", "w", encoding='utf-8') as f:
        f.write("\\section*{II}\n\n")
        content, mul = calc2(Rl)
        f.write(content)

    Rc = pogreshnosti.PreInfo()
    Rc.lst = Rl
    Rc.N = len(Rl)
    Rc.theta = 0.00
    Rc.tpn = 2.021075383
    Rc.name = "R_{x}"
    Rc.i_name = "R_{xi}"
    Rc = pogreshnosti.Calc(Rc)
    # Rc.print()

    mup = pogreshnosti.PreInfo()
    mup.lst = mul
    mup.N = len(mul)
    mup.theta = 0.00
    mup.tpn = 2.021075383
    mup.name = "\\mu"
    mup.i_name = "\\mu_{i}"
    mup = pogreshnosti.Calc(mup)
    # mup.print()

    ooo = [3.33,
           1.78,
           2.68,
           1.80,
           1.49,
           2.68,
           3.33,
           1.90,
           2.36,
           1.49,
           2.36,
           2.36]

    print(sum(ooo))
