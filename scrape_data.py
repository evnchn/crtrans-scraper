import requests
import bs4 as bs

seq = 1
master_dict = {}

while True:
    print(seq)

    params = {
        'page': seq,
        'admission_term': 'Any',
        'institution': 'Any',
        'hkustsubject': 'Any',
        'hkust_course_code': 'Any',
        'country_institution': 'Any',
    }

    response = requests.get('https://registry.hkust.edu.hk/ajax/results-institution', params=params)
    print(response.text[0:100])

    soup = bs.BeautifulSoup(response.text, "lxml")

    
    all_items = soup.select(".result-items")
    if not all_items:
        break
    for each_result_item in all_items:
        country = each_result_item.select(".country")[0].get_text().strip()
        other_school = each_result_item.select(".result-item__qualification__non-ust")[0].get_text().strip()
        for each_result_subitem in soup.select(".result-items__item"):
            other_school_subject = each_result_subitem.select(".tile-transfer__subject")[0].get_text().replace("+","", 1).strip()
            other_school_ccode = each_result_subitem.select(".tile-transfer__ust-course-code")[0].get_text().strip()
            refno = each_result_subitem.select(".tile__ref__number")[0].get_text().strip()
            hkust_subject = each_result_subitem.select(".tile-transfer__course-title")[0].get_text().replace("+","", 1).strip()
            hkust_ccode = each_result_subitem.select(".tile-transfer__course-code")[0].get_text().strip()
            creds = each_result_subitem.select(".tile-transfer__credit")[0].get_text().strip()
            if each_result_subitem.select(".tile-transfer__ribbon-text__restrictions"):
                restriction_elem = each_result_subitem.select(".tile-transfer__ribbon-text__restrictions")[0]
                restriction_text = soup.select(f'#{restriction_elem["data-id"]}')[0].select(".restrictions__content")[0].get_text().strip()
            else:
                restriction_text = ""
            # print(other_school_subject, other_school_ccode, refno, hkust_subject, hkust_ccode, creds, sep="\n")
            master_dict[refno] = {"SCHOOL_NAME": other_school, "COUNTRY":country, "FROM_SCHOOL":{"SUBJECT":other_school_subject, "CODE":other_school_ccode}, "HKUST":{"SUBJECT":hkust_subject, "CODE":hkust_ccode}, "CREDS": creds, "RESTRICTIONS": restriction_text}
    seq += 1
import json

with open("all_crtrans.json","w") as json_file:
    json.dump(master_dict, json_file)


import pprint

pprint.pprint(master_dict)

