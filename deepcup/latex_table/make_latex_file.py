"""
@author: daviddeepwell
"""

def make_latex_file(year, rnd):
    # create and run the latex file from the csv data file
    
    import pandas as pd
    import os
    import deepcup.latex_table.read_round as read_round
    import deepcup.latex_table.helpers as helpers
    
    ltn = helpers.lengthen_team_name_acronym 
    stn = helpers.shorten_team_name_acronym 
    
    # read the csv file with the data for the round
    df = read_round(year, rnd)
    
    # drop the results row and sort by name (index)
    df.drop(index='Results', inplace=True)
    df.sort_index(inplace=True)
    
    # team names and number of series
    teams_west, teams_east = helpers.team_list(year, rnd)
    N_series = 2**(4-rnd)

    ###### Latex file code #####

    # head matter
    
    headmatter = ["%----------------------------------------------------------------------------------------\n",
            "%	Settings and packages\n",
            "%----------------------------------------------------------------------------------------",
            "\n",
            "\\documentclass[10pt]{article}\n",
            "\n",
            "\\usepackage{colortbl}\n",
            "\\usepackage{multirow}\n",
            "\\usepackage[table]{xcolor}\n",
            "\\usepackage{ctable}\n",
            "\\usepackage[landscape,margin=0.25in,legalpaper]{geometry}\n",
            "\n",
            "\\newcommand{\\mcn}[2]{\\multicolumn{#1}{l}{#2}}	\n",
            "\\newcommand{\mccn}[2]{\multicolumn{#1}{c}{#2}}\n",
            "\\newcommand{\\mcl}[1]{\\multicolumn{2}{l}{#1}}\n",
            "\\newcommand{\\mclg}[1]{\\multicolumn{2}{l}{\\gr #1}}\n",
            "\\newcommand{\\mcc}[1]{\\multicolumn{2}{c}{#1}}\n",
            "\\newcommand{\\mccg}[1]{\\multicolumn{2}{c}{\\gr #1}}\n",
            "\\newcommand{\\mr}[1]{\\multirow{-2}{*}{#1}}\n",
            "\\definecolor{Gray}{gray}{0.90}\n",
            "\\newcommand{\\gr}{\\cellcolor{Gray}}\n",
            "\n",
            "\\newcommand{\\thickline}{\specialrule{.1em}{.05em}{.05em} }\n",
            "% column colours\n",
            "\n",
            "\\newcolumntype{g}{>{\columncolor{Gray}}l}\n",
            "\\newcolumntype{w}{>{\columncolor{white}}l}\n",
            "\n",
            "\n",
            "%\\usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.\n",
            "%\\geometry{letterpaper}                   		% ... or a4paper or a5paper or ... \n",
            "%\\geometry{landscape}                		% Activate for for rotated page geometry\n",
            "\n",
            "%----------------------------------------------------------------------------------------\n",
            "%	Create new commands\n",
            "%----------------------------------------------------------------------------------------\n",
            "\n",
            "% Commands are in LatexCommands.tex. New commands for this file only can be written here.\n",
            "%\\input{/Applications/TeX/Latex_ancillary/LatexCommands.tex}\n",
            "\n",
            "\n",
            "%----------------------------------------------------------------------------------------\n",
            "%	Table\n",
            "%----------------------------------------------------------------------------------------\n",
            "\n",
            "\\begin{document}\n",
            "\n",
            "\\thispagestyle{empty}\n",
            "\n",
            "{\\bf ", str(year), " Friendly Playoff Hockey Pool}\n",
            "\n",
            ]
    
    ## main table
    
    N_people = len(df.index)
    N_cols = 2*N_people + 1
    
    # initialize table
    table_start = ("\\begin{table}[h!]\n"
                    "\\centering\n"
                    "\\begin{tabular}{l")
    table_start += " g g w w"*(N_people//2)
    if N_people%2:
        table_start += " g g"
    table_start += "}\n"
    
    # table header
    if rnd == 1:
        table_title = "Round 1: Division Semi-Finals"
    elif rnd == 2:
        table_title = "Round 2: Division Finals"
    elif rnd == 3:
        table_title = "Round 3: Conference Finals"
    elif rnd == 4:
        table_title = "Round 4: Stanley Cup Finals"
    table_start += "\\rowcolor{black} \\mcn{"+str(N_cols)+"}{\\color{white}\\bf "\
        +table_title+"} \\\\\n"\
        "\\rowcolor{white}\\\\\n"
    
    # table column titles (Player names)
    for ii in range(N_people):
        print(df.index[ii])
        if ii%2 == 0:
            table_start += "&  \\mccg{"+df.index[ii]+"}"
        else:
            table_start += "&  \\mcc{"+df.index[ii]+"}"
    table_start += " \\\\\\thickline\n"
    
    # subtitles
    table_west = "{\\bf West} "+(N_cols-1)*"&"+"\\\\\\hline\n"
    table_east = "{\\bf East} "+(N_cols-1)*"&"+"\\\\\\hline\n"
    
    # define white space
    blank = (N_cols-1)*"&"+" \\\\\\hline\n"
    blanker = (N_cols-1)*"&"+" \\\\\n"
    white = "\\rowcolor{white}\\\\\n"
    
    # rows of picks for each series
    for nn in range(N_series):
        if nn % 2:
            table_west += teams_west[nn]
            table_east += teams_east[nn]
            for ii in range(N_people):
                table_west += " & \\mr{"+stn(df.iloc[ii]["T"+str(nn//2+1)])+"} & \\mr{"+str(df.iloc[ii]["G"+str(nn//2+1)])+"}"
                table_east += " & \\mr{"+stn(df.iloc[ii]["T"+str(nn//2+5)])+"} & \\mr{"+str(df.iloc[ii]["G"+str(nn//2+5)])+"}"
                if ii == N_people - 1:
                    table_west += "\\\\\\hline\n"
                    table_east += "\\\\\\hline\n"
                    if nn == N_series-1:
                        table_west += blanker
                        table_east += white
                    else:
                        table_west += blank
                        table_east += blank
        else:
            table_west += teams_west[nn]+(N_cols-1)*"&"+"\\\\\n"
            table_east += teams_east[nn]+(N_cols-1)*"&"+"\\\\\n"
            
    # Conference Champion setup
    champtitle = "\\rowcolor{black} \\mcn{"+str(N_cols)+"}{\\color{white}\\bf Conference Champions} \\\\\n"
    wchamp = "Western"
    echamp = "Eastern"
    schamp = "Stanley Cup"

    # individual picks for the conference champions
    for ii in range(N_people):
        if ii%2 == 0:
            wchamp += " & \\mclg{"+stn(df.iloc[ii]["WCC"])+"}"
            echamp += " & \\mclg{"+stn(df.iloc[ii]["ECC"])+"}"
            schamp += " & \\mclg{"+stn(df.iloc[ii]["SCC"])+"}"
        else:
            wchamp += " & \\mcl{"+stn(df.iloc[ii]["WCC"])+"}"
            echamp += " & \\mcl{"+stn(df.iloc[ii]["ECC"])+"}"
            schamp += " & \\mcl{"+stn(df.iloc[ii]["SCC"])+"}"
    wchamp += "\\\\\n"
    echamp += "\\\\\n"
    schamp += "\n"

    conf_champ = champtitle + wchamp + echamp + schamp
    table_end = "\\end{tabular}\n"+"\\end{table}\n"+"\n"
    
    maintable = table_start + table_west + table_east + conf_champ + table_end
    
    
    # bottom tables/info
    
    table_start = [
        "\\begin{table}[!htb]\n",
        "    \\begin{minipage}[t]{.27\linewidth}\n",
        "    	{\\bf Points}\\\\\n",
        "		\\begin{tabular}{l l}\n",
        "			If correct team chosen:	& $15 - 2|P-A|$\\\\\n",
        "			If incorrect team chosen:	& $P+A-8$\\\\\n",
        "			Western/Eastern Conference champion:	& 20\\\\\n",
        "			Stanley Cup champion:		& 20\\\\\n",
        "			Where $P$ is the predicted number of games&\\\\\n",
        "			Where $A$ is the actual number of games&\n",
        "		\\end{tabular}\n",
        "	\\end{minipage}\n",
        "	\\begin{minipage}[t]{0.12\linewidth}\n",
        "	\\qquad Correct team\\\\\n",
        "	\\begin{tabular}{c l | c c c c }\n",
        "		\\mccn{2}{} & \\mccn{4}{Predicted}\\\\\n",
        "		& & 4 & 5 & 6 & 7\\\\\\cline{2-6}\n",
        "		\\parbox[t]{2mm}{\\multirow{4}{*}{\\rotatebox[origin=c]{90}{Actual}}}&4 & 15 & 13 & 11 & 9\\\\\n",
        "		&5 & 13 & 15 & 13 & 11\\\\\n",
        "		&6 & 11 & 13 & 15 & 13\\\\\n",
        "		&7 &  9 & 11 & 13 & 15\n",
        "	\\end{tabular}\n",
        "	\\end{minipage}\n",
        "	\\begin{minipage}[t]{0.12\\linewidth}\n",
        "	\\quad Incorrect team\\\\\n",
        "	\\begin{tabular}{c l | c c c c }\n",
        "		\\mccn{2}{} & \\mccn{4}{Predicted}\\\\\n",
        "		& & 4 & 5 & 6 & 7\\\\\\cline{2-6}\n",
        "		\\parbox[t]{2mm}{\\multirow{4}{*}{\\rotatebox[origin=c]{90}{Actual}}}&4 & 0 & 1 & 2 & 3\\\\\n",
        "		&5 & 1 & 2 & 3 & 4\\\\\n",
        "		&6 & 2 & 3 & 4 & 5\\\\\n",
        "		&7 & 3 & 4 & 5 & 6\n",
        "	\\end{tabular}\n",
        "	\\end{minipage}\n",
        "    \\begin{minipage}[t]{.45\linewidth}\n",
        "    	{\\bf Number of picks per team:}\\\\\n"
    ]

    begintabular = "\\begin{tabular}{lc "+(N_series-1)*"| lc "+"}\n"

    s1_num = ""
    s2_num = ""
    for ii in range(0, N_series, 2):
        ts = df['T'+str(ii//2+1)].value_counts()
        if len(ts) == 1:
            # If everyone picked a single team,
            # manually add the zero value for the other team
            ts2 = pd.Series(0, index=[ltn(teams_west[ii+1])])
            ts = ts.append(ts2)
        s1_num += teams_west[ii] + "&"+str(ts[ltn(teams_west[ii])]) + "&"
        s2_num += teams_west[ii+1]+"&"+str(ts[ltn(teams_west[ii+1])])+"&"
    for ii in range(0, N_series, 2):
        ts = df['T'+str(ii//2+N_series//2+1)].value_counts()
        if len(ts) == 1:
            # If everyone picked a single team,
            # manually add the zero value for the other team
            ts2 = pd.Series(0, index=[ltn(teams_east[ii+1])])
            ts = ts.append(ts2)
        s1_num += teams_east[ii] + "&"+str(ts[ltn(teams_east[ii])]) + "&"
        s2_num += teams_east[ii+1]+"&"+str(ts[ltn(teams_east[ii+1])])+"&"

    s1_num = s1_num[:-1]+"\\\\\n"
    s2_num = s2_num[:-1]+"\\\\\n"

    table_end = ["        \\end{tabular}\n",
                 "    \\end{minipage}\n",
                 "\\end{table}\n",
                 "\n",
                 "\\end{document}\n"
                 ]

    endlines = table_start + [begintabular + s1_num + s2_num] + table_end
    
    
    # put it all together
    
    f = open("round"+str(rnd)+".tex","w+")
    f.writelines(headmatter)
    f.writelines(maintable)
    f.writelines(endlines)
    f.close()
    
    # run tex
    latex_pdf_command = "/Library/TeX/texbin/pdflatex round"+str(rnd)+".tex"
    os.system(latex_pdf_command)
    
