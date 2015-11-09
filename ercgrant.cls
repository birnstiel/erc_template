\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{my_cv}[2011/03/26 My custom CV class]

\let\@firstchapter\@empty

\newif\ifisBtwo

\DeclareOption{B2}{%
\isBtwotrue
\def\@firstchapter{1}%
}

\ProcessOptions

\LoadClass{scrreprt}

%\ifx\@firstchapter\@empty \addtocounter{chapter}{1}\else\addtocounter{chapter}{\@firstchapter}\fi

\addtocounter{chapter}{1}

%%% PACKAGES %%%
\RequirePackage[english]{babel}
\RequirePackage[right]{eurosym}
\setlength{\footskip}{1.45\baselineskip}
\RequirePackage[left=2cm,top=1.5cm,bottom=1.5cm,right=2cm,includefoot,includehead]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage{graphicx} 		% Add graphics capabilities
\RequirePackage{xspace}
\RequirePackage{blindtext}
\RequirePackage{amsmath}  		% Better maths support
\RequirePackage{pslatex} %Times font
\RequirePackage{todonotes}
\RequirePackage{mdframed}

% for the open and filled star symbols
\RequirePackage{bbding}
\newcommand{\fstar}{\raisebox{-0.12em}{\begin{scriptsize}\FiveStar\end{scriptsize}}}
\newcommand{\ostar}{\raisebox{-0.12em}{\begin{scriptsize}\FiveStarOpen\end{scriptsize}}}

% ========= HYPERREF & Colors ===========
\RequirePackage{xcolor}
\definecolor{lightgray} {gray}{0.7}
\definecolor{darkgray}  {gray}{0.43}
\definecolor{darkblue}  {rgb} {0,0,.65}
\definecolor{citegreen} {rgb} {0.28,0.41,0.19}
\definecolor{darkgreen} {rgb} {0.37,0.72,0.17}
\definecolor{lightgreen}{rgb} {0.56,0.88,0.28}
\RequirePackage[%
  pdfstartview=FitH,%
  breaklinks=true,%
  bookmarks=true,%
  colorlinks=true,%
  linkcolor= darkblue,
  anchorcolor=black,%
  citecolor=citegreen,
  filecolor=black,%
  menucolor=black,%
  urlcolor=darkblue%
  ]{hyperref}

\AtBeginDocument{%
  \hypersetup{%
    pdfauthor={\@author},%
    pdftitle={ERC proposal - \@title}%
  }
}


% ========== BIBLIOGRAPHY STUFF ============

\RequirePackage{natbib}
\bibpunct{(}{)}{;}{a}{,}{,}
\input{abbrev.tex}
\setlength{\bibsep}{0.0cm}

% ========== SECTION FORMATTING ============
\RequirePackage{titlesec}
\renewcommand\thesection{\alph{section}}
%###
\titleformat{\section}{\Large\bfseries}{Section \thesection: }{0em}{}
%###

%###
% have the chapter on the same page
\titleclass{\chapter}{straight}
% calling the chapters B1, B2, \ldots
\renewcommand{\thechapter}{B\arabic{chapter}}
\titleformat{\chapter}{\Large\bfseries}{Part \thechapter: }{0em}{}
%###
% 
% save space between section headings, and after figures
% 
%###
\titlespacing*{\chapter}      {0pt}{1.5ex}{1ex}
\titlespacing*{\section}      {0pt}{1.5ex}{1ex}
\titlespacing*{\subsection}   {0pt}{1.5ex}{0.8ex}
\titlespacing*{\subsubsection}{0pt}{1.5ex}{0.8ex}
\titlespacing*{\paragraph}    {0pt}{1.0ex}{0.8ex}
\setlength{\belowcaptionskip}{-0.5cm}
%###


% === FIGURE AND CAPTION STUFF ====
\RequirePackage[font=small]{caption}
\RequirePackage{chngcntr}
% don't show the chapter part in the caption
%\counterwithout{figure}{chapter}
%\counterwithout{table}{chapter}

% for ``side-figures''
\RequirePackage{wrapfig}



% ==== TABLE STUFF ===========
\RequirePackage{makecell}
\RequirePackage{longtable}
\RequirePackage{multirow}
\RequirePackage{colortbl}
\definecolor{kugray5}{RGB}{224,224,224}
\newcommand{\specialcell}[2][c]{%
  \begin{tabular}[#1]{@{}c@{}}#2\end{tabular}}

% to hide a table column
\RequirePackage{array}
\newcolumntype{H}{>{\setbox0=\hbox\bgroup}c<{\egroup}@{}}
\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{B}[1]{>{\columncolor{lightgreen}\bf\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}

% align digits in tables
\RequirePackage{dcolumn}
\newcolumntype{d}[1]{D{.}{.}{#1}}

% change font size of captions
\RequirePackage[font=small]{caption}

% ======== To fix list things ============ 
\RequirePackage{enumitem}
\setitemize{noitemsep,topsep=0ex,parsep=0.25ex,partopsep=0pt,leftmargin=*}
\setenumerate{topsep=0pt,parsep=0pt,partopsep=0pt,leftmargin=*}
\RequirePackage{amssymb}
\renewcommand{\labelitemi}{\tiny$\blacksquare$}
\RequirePackage{nopageno}
\RequirePackage{enumitem}

\RequirePackage{fancyhdr}
\pagestyle{fancy}
\renewcommand{\headrulewidth}{0pt} % Remove line at top
 
\lhead{\emph{\@author}}
\chead{Part \thechapter}
\rhead{\@acro}
\cfoot{\thepage}

\newenvironment{itemize*}%
  {\begin{itemize}%
    \setlength{\itemsep}{0pt}%
    \setlength{\parskip}{0pt}}%
  {\end{itemize}}

% ============== SOME MACROS ===============

\newcommand{\cont}{\textcolor{red}{\textbf{continue}}\xspace}
\newcommand{\comment}[1]{\textcolor{red}{\textbf{#1}}\xspace}
\newcommand{\x}{\textcolor{red}{XXX}\xspace}
\let\@acro\empty
\newcommand{\acro}[1]{\def\@acro{#1}}
\newcommand{\theacro}{\textsc{\@acro}\xspace}
\newcommand{\proposal@duration}{60 Months}
\let\@institution\empty
\newcommand{\institution}[1]{\def\@institution{#1}}

% ========= DEFINE TITLE, AUTHOR, DATE =========
\title{\@acro}

% ========= Format title page =========


\ifisBtwo
\renewcommand{\maketitle}{%
\begin{center}
\LARGE{\textbf{ERC Starting Grant 2016\\
Research proposal [Part B2] }
}
\end{center}
\vspace{1cm}
}
\else
\renewcommand{\maketitle}{%
\begin{center}
\makeatletter
\LARGE{\textbf{ERC Starting Grant 2016\\
Research proposal [Part B1] }
}
\vfill
%
\LARGE{\textsc{\@title}}
%
\vfill
%
\LARGE{\textsc{---~\@acro~---}}
%
\vfill
\makeatother
\end{center}
%
\vfill
%
\begin{itemize}
\makeatletter
\item Principal investigator (PI): \@author
\item Host institution: \@institution
\item Proposal full title: \@title
\item Proposal short name: \@acro
\item Proposal duration: \proposal@duration
\makeatother
\end{itemize}
\vfill
}
\fi

\renewenvironment{abstract}{%
\begin{mdframed}
}{%
\end{mdframed}
\vfill
\newpage
}
