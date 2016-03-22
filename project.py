import re
import requests
from lxml import etree
# http://pdslab.biochem.iisc.ernet.in/hspir/stattb1.php?ST1=HSP60&ST2=bacteria
# http://pdslab.biochem.iisc.ernet.in/hspir/stattb1.php?ST1=HSP60&ST2=archaea
# http://pdslab.biochem.iisc.ernet.in/hspir/stattb1.php?ST1=HSP60&ST2=protist
# http://pdslab.biochem.iisc.ernet.in/hspir/stattb1.php?ST1=HSP60&ST2=fungi
# http://pdslab.biochem.iisc.ernet.in/hspir/stattb1.php?ST1=HSP60&ST2=algae
# http://pdslab.biochem.iisc.ernet.in/hspir/stattb1.php?ST1=HSP60&ST2=plant
# http://pdslab.biochem.iisc.ernet.in/hspir/stattb1.php?ST1=HSP60&ST2=animal
for i in range(1,13):
    link_page = "http://pdslab.biochem.iisc.ernet.in/hspir/stattb1.php?pagenum=" + str(i) + "&ST1=HSP60&ST2=plant"
    # print(link_page)

    url1 = link_page
    for_new_link = "http://pdslab.biochem.iisc.ernet.in/hspir/"

    data = requests.get(url1).text
    parser = etree.HTMLParser()
    tree = etree.fromstring(data, parser)

    for i in tree.iter("a"):
        b = str(i.get('href'))
        f = re.findall("action.php\?accession_number=HSP60_(.+)", b)
        if f != []:
            new_link = for_new_link + "action.php?accession_number=HSP60_" + f[0]
            # print(new_link)

            data = requests.get(new_link).text
            parser = etree.HTMLParser()
            tree = etree.fromstring(data, parser)
            for i in tree.iter("a"):
                b = str(i.get('href'))
                f = re.findall("fasta.php\?Acno=HSP60_(.+)", b)
                # print(f)
                if f != []:
                    finish_link = for_new_link + "fastadownload.php?Acno=HSP60_" + f[0]
                    # print(finish_link)
                    response = requests.get(finish_link)
                    html_code = response.text

                    if re.findall(".+FAB.+", html_code):
                        print(html_code)


