import csv
import json
from wake import get_wikidata_entities
from language_codes import language_codes


def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
        except:
            print(str(key) + " not in " + str(dct))
    return dct

fieldnames=['entity_id'] + language_codes
with open('./wiki_names.csv', 'w') as f:
    csv.DictWriter(f, fieldnames=fieldnames).writeheader()

for entity in get_wikidata_entities(sleep_time=0):
    #print(json.dumps(entity, indent=4))

    entity_id = entity['id']
    #print("entity_id:", entity_id)

    if 'claims' in entity:
        claims = entity['claims']
        if 'P31' in claims:
            instances = claims['P31']
            qids = ["Q" + str(safeget(i, "mainsnak", "datavalue", "value", "numeric-id")) for i in instances]
            #print("qids:", qids)
            if 'Q101352' in qids:
                print("instance of surname")
                if 'labels' in entity:
                    row = {}
                    row['entity_id'] = entity['id']
                    labels = entity['labels']
                    for language in language_codes:
                        if language in labels:
                            spellings = labels[language]
                            if isinstance(spellings, list):
                                row[language] = ";".join([spelling['value'] for spelling in spellings])
                            elif isinstance(spellings, dict):
                                row[language] = spellings['value']
                    print("row:", row)
                    with open('./wiki_names.csv', 'a') as f:
                        csv.DictWriter(f, fieldnames=fieldnames).writerow(row)

