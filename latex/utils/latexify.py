#
# convert .md file for latex
#

import sys

def process_latex(finname):
    inheader = False
    notpdf = False
    with open(finname, 'r') as file:
        for line in file:
            if inheader:
                if line.startswith('---') or line.startswith('+++'):
                    inheader = False
                else:
                    if line.startswith('title'):
                        startquote = line.find('"')
                        endquote = line.find('"', startquote + 1)
                        assert startquote != -1
                        assert endquote != -1
                        assert endquote > startquote
                        title = line[startquote + 1:endquote]
                        print("% " + title)
                    elif line.startswith('date:'):
                        print("% " + line[6:], end="")
                    else:
                        pass # ingore rest of header
            else:
                line = line.replace('&rarr;', '$\\rightarrow$')
                line = line.replace('&Sigma;', '$\\Sigma$')
                line = line.replace('&isin;', '$\\in$')
                line = line.replace('&delta;', '$\\delta$')
                line = line.replace('KU<sub>X</sub>', '$KU_{X}$')
                line = line.replace('KR<sub>X</sub>', '$KR_{X}$')
                line = line.replace('_k_<sub>i</sub>', '$k_i$')
                line = line.replace('_n_<sub>0</sub>', '$n_0$')
                line = line.replace('_q_<sub>0</sub>', '$q_0$')
                line = line.replace('_n_<sup>2</sup>', '$n^2$')
                line = line.replace('_N_<sup>2</sup>', '$N^2$')
                line = line.replace('_N_<sup>7</sup>', '$N^7$')
                line = line.replace('_N_<sup>29</sup>', '$N^{29}$')
                line = line.replace('2<sup>_N_</sup>', '$2^N$')
                line = line.replace('_n_<sup>3</sup>', '$n^3$')
                line = line.replace('&Theta;(log _N_)', '$\Theta(log N)$')
                line = line.replace('log<sup>_b_</sup> _n_ = _x_', '$log_{b} n = x$')
                line = line.replace('_b_<sup>_x_</sup> = _n_', '$b^x = n$')
                line = line.replace('log<sup>2</sup> 1,000,000,000', '$log_2 1000000000$')
                line = line.replace('&le;', '$<=$')
                line = line.replace('&ge;', '$>=$')
                line = line.replace('&Omega;', '$\Omega$')
                line = line.replace('&Theta;', '$\Theta$')
                line = line.replace('&epsilon;', '$\epsilon$')
                line = line.replace('<!--indent-->', '\\begin{quote}')
                line = line.replace('<!--endindent-->', '\\end{quote}')
                line = line.replace('<!--page-->', '\clearpage')
                line = line.replace('<pre class="brush: python;">', '```Python')
                line = line.replace('</pre><!--python-->', '```')
                if line.startswith('<!--end-->'): 
                    break

                if line.startswith('---') or line.startswith('+++'):
                    inheader = True
                elif line.startswith('<div class="printing">'):
                    pass
                elif line.startswith('<div class="notpdf">') or line.startswith('   <div class="notpdf">'):
                    notpdf = True
                elif notpdf:
                    if line.startswith('</div><!--endpdf-->') or line.startswith('   </div><!--endpdf-->'):
                        notpdf = False
                elif line.startswith('<div class="spacer"></div>'):
                    print("\n###\n")
                elif line.startswith('<div class="gap"></div>'):
                    print("\n#\n")
                elif line.startswith('<div class="biggap"></div>'):
                    print("\n#\n#\n")
                elif line.startswith('<div class="biggergap"></div>'):
                    print("\n#\n#\n#\n#\n")
                else:
                    print(line, end="")


if __name__ == "__main__":
    fin = sys.argv[1]
    process_latex(fin)
