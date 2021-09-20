import pandas as pd, csv
# Table: bicraszzgit
# linenumber [0], path [1], content [2], project [3] , szz_date [4], copypath [5] , copyrevision [6],
# mergerev [7], branchrev [8], changeproperty [9], missed [10],  furtherback [11] , contentdiff [12] ,
# issample [13] , diffjmessage [14]  , diffjlocation [15] , refdiffindex [16] , adjustmentindex [17] ,
# indexposrefac [18] ,  indexfurtherback [19] , indexchangepath [20], isrefac [21] , revision [22] ,
# fixrevision  [23], islargest [24] , islatest [25] ,  startrevision [26], startpath [27],
# startlinenumber [28], startcontent [29] ,  isvalidfix [30], hasmatchmaszz [31],  isvalidresult [32]
mycsvfile = "/home/hareem/raszzprime/result.csv"

# linenumber, path, content, szz_date, isrefac,  revision, fixrevision, startrevision ,
# startpath,  startlinenumber , startcontent  isvalidfix, isvalidresult

with open(mycsvfile) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter="|")
    line_count = 0
    for row in csv_reader:
        line_count+=1
        print((line_count),len(row))
        if(len(row)==33):
            print(row[0], row[1], row[2], row[4], row[21], row[22], row[23], row[26], row[27], row[28], row[29], row[30], row[32])
