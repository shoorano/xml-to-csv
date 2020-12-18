import pandas as pd
import xml.etree.ElementTree as ET
import xmltodict

def xml_to_csv(xml_path, csv_path):
    """
    Reads in xml doc from xml_path
    Parses for item tags
    Parses column names and outputs as csv to csv_path.
    """
    with open(xml_path) as fd:
        doc = xmltodict.parse(fd.read())
    item_dict = doc["rss"]["channel"]["item"]
    df = pd.DataFrame(item_dict)
    df.columns = df.columns.str.replace("g:", "")
    df.to_csv(path_or_buf=csv_path)

xml_to_csv('test.xml', 'test.csv')
