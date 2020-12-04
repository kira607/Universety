from math import sin, cos, radians, sqrt

PI = 3.14159265359


class PreInfo:
    """needed"""

    def __init__(self):
        self.lst = []  # выборка
        self.N = 0  # (+N)
        self.theta = 0  # тета
        self.tpn = 0  # tpn
        self.name = ""  # имя-переменной
        self.i_name = ""  # имя переменной с i


class PostInfo:
    """calculated"""

    def __init__(self):
        self.mid_x = 0  # среднее-квадратичное
        self.Sx_numerator = []  # числитель СКО
        self.Sx_denominator = 0  # знаминатель СКО
        self.Sx = 0  # СКО
        self.dx = 0  # дельта
        self.dx_ = 0  # дельта-среднее


class Info:
    def __init__(self, pre: PreInfo, post: PostInfo):
        pre.lst = list(map(lambda x: str(x), pre.lst))
        self.lst = ' + '.join(pre.lst)  # выборка
        self.N = pre.N  # (+N)
        self.theta = pre.theta  # тета
        self.tpn = pre.tpn  # tpn
        self.name = pre.name  # имя-переменной
        self.i_name = pre.i_name  # имя переменной с i

        self.mid_x = post.mid_x  # среднее-квадратичное
        post.Sx_numerator = list(map(lambda x: str(x), post.Sx_numerator))
        self.Sx_numerator = ' + '.join(post.Sx_numerator)  # числитель СКО
        self.Sx_denominator = post.Sx_denominator  # знаминатель СКО
        self.Sx = post.Sx  # СКО
        self.dx = post.dx  # дельта
        self.dx_ = post.dx_  # дельта-среднее


class Calc:
    def __init__(self, pre: PreInfo):
        self.pre = pre
        self.post = PostInfo()
        self.x = None
        self.calc()

    def calc(self):
        self.post = PostInfo()
        self.post.mid_x = sum(self.pre.lst) / self.pre.N
        self.post.Sx_denominator = self.pre.N * (self.pre.N - 1)
        self.post.Sx_numerator = []
        for x_ in self.pre.lst:
            el = round((x_ - self.post.mid_x) ** 2, 5)
            self.post.Sx_numerator.append(el)
        self.post.Sx = sqrt(sum(self.post.Sx_numerator) / self.post.Sx_denominator)
        self.post.dx = self.pre.tpn * self.post.Sx
        self.post.dx_ = sqrt(self.post.dx ** 2 + self.pre.theta ** 2)
        self.x = Info(self.pre, self.post)

    def get_latex_string(self):
        res_str = f"""
% выборочное среднее
$ 
\\overline{{{self.x.name}}}= 
\\sum_{{i=1}}^{{{self.x.N}}} {self.x.i_name} = 
\\dfrac{{{self.x.lst}}}{{{self.x.N}}} 
= {self.x.mid_x}
$
\\\\

% выборочное СКО
$
S_{{\\overline U_B}} = 
\\sqrt{{
    \\dfrac
    {{
        \\sum_{{i=1}}^{{{self.x.N}}}({self.x.i_name} - \\overline{{{self.x.name}}})
    }}
    {{
        N(N-1)
    }}
}}
=\\\\
\\sqrt{{
    \\dfrac
    {{
        {self.x.Sx_numerator}
    }}
    {{
        {self.x.Sx_denominator}
    }}
}}
=\\\\
{self.x.Sx}
$
\\\\

% случайная погрешность
$ 
\\varDelta {self.x.name} = 
t_{{P,N}}S_{{\\overline{{{self.x.name}}}}} = 
{self.x.tpn} * {self.x.Sx} = 
{self.x.dx}
$
\\\\

% полная погрешность
$ 
\\varDelta \\overline{{{self.x.name}}} = 
\\sqrt{{\\varDelta {self.x.name}^2 + \\theta_{{{self.x.name}}}^2}} =
\\sqrt{{{self.x.dx}^2 + {self.x.theta}^2}} = 
{self.x.dx_} \\approx 
% подставить округление
$
\\\\

% результат
$ {self.x.name} = 
\\overline{{{self.x.name}}} \\pm \\varDelta \\overline{{{self.x.name}}} = 
{self.x.mid_x} \\pm {round(self.x.dx_, 5)}, P = 95\\%
$
\\\\
        """
        return res_str

    def print(self):
        print(self.get_latex_string())


if __name__ == '__main__':
    ug = PreInfo()
    ug.lst = [2.3, 2.3, 2.3, 2.5, 2.5, 2.5, 2.6, 2.6, 2.6, 2.7]
    ug.N = len(ug.lst)
    ug.theta = 0.01
    ug.tpn = 2.2622
    ug.name = "U_{\\Gamma}"
    ug.i_name = "U_{\\Gamma i}"
    ug = Calc(ug)
    # ug.print()

    r = 0.1
    N = 2000
    C = 0.000002
    R = 470
    U = 1
    k = (R * C) / (2 * N * PI * r ** 2)
    B_gamma = []
    for u in ug.pre.lst:
        bg = float(u) * k
        B_gamma.append(round(bg * 10 ** 5, 2))
    B_gamma = list(map(lambda x: round(x * 10 ** -5, 10), B_gamma))

    bg = PreInfo()
    bg.lst = B_gamma
    bg.N = len(bg.lst)
    bg.theta = 0.01
    bg.tpn = 2.2622
    bg.name = "B_{\\Gamma}"
    bg.i_name = "B_{\\Gamma i}"
    bg = Calc(bg)
    # bg.print()

    uw = PreInfo()
    uw.lst = [7.5, 7.2, 7.5, 7.4, 6.9, 7.2, 7.1, 7.2, 7.0, 7.4]
    uw.N = len(uw.lst)
    uw.theta = 0.01
    uw.tpn = 2.2622
    uw.name = "U_B"
    uw.i_name = "U_{Bi}"
    uw = Calc(uw)
    # uw.print()

    B_B = []
    for u in uw.pre.lst:
        bb = float(u) * k
        B_B.append(round(bb * 10 ** 5, 2))
    B_B = list(map(lambda x: round(x * 10 ** -5, 10), B_B))

    li = str(B_B).replace("e-05", "").replace("[", "").replace("]", "").split(",")
    print(li)
    i = 0
    for le in li:
        li[i] = float(le)
        i += 1
    print(li)
    print(sum(li))

    bb = PreInfo()
    bb.lst = B_B
    bb.N = len(bb.lst)
    bb.theta = 0.01
    bb.tpn = 2.2622
    bb.name = "B_{B}"
    bb.i_name = "B_{Bi}"
    bb = Calc(bb)
    # bb.print()

    for i in range(10):
        print(i+1, " & ", ug.pre.lst[i], " \\\\", sep="")
        print("\\hline")

    for i in range(10):
        print(i+1, " & ", uw.pre.lst[i], " \\\\", sep="")
        print("\\hline")
