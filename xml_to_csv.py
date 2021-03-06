import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path, ipath):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (os.path.join(ipath, root.find('filename').text),
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['Path', 'Width', 'Height', 'ClassId', 'Roi.X1', 'Roi.Y1', 'Roi.X2', 'Roi.Y2']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    annotation_path = os.path.join(os.getcwd(), 'MyAnno')
    image_path = 'MyTest'
    xml_df = xml_to_csv(annotation_path, image_path)
    xml_df.to_csv('MyTest.csv', index=None)
    print('Successfully converted xml to csv.')


main()
