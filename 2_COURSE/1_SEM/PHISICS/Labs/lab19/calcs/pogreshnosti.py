from math import sqrt


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

    def long_x_(self):
        sko = ""
        for i in self.pre.lst:
            sko += f"\\dfrac{{{i}}}{{{self.x.N}}} + \n"
        return sko

    def get_latex_string(self):
        res_str = f"""
% выборочное среднее
$ 
\\overline{{{self.x.name}}}= 
\\sum_{{i=1}}^{{{self.x.N}}} {self.x.i_name} = 
{self.long_x_()}
= {self.x.mid_x}
$
\\\\

% выборочное СКО
$
S_{{{self.x.name}}} = 
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
        {sum(list(map(lambda x: float(x), self.post.Sx_numerator)))}
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