#!/usr/bin/env python

# A simple program for creating new interpolated xml settings files
# from example start and end files.

# Mike McCabe

import sys
from lxml import etree
import re
import os

def main(argv):
    import optparse

    parser = optparse.OptionParser(usage='usage: %prog start.xml end.xml top_step current_step',
                 version='%prog 0.1',
                 description="Compute step [current_step] of 0 to [top_step] steps between a given start and end xml file, replacing any numeric values with interpolated values.  Outputs a new xml file on standard out.",
                 epilog="If current_step is 0, the values from start.xml are used; if current_step is top_step, the values from end.xml are used.  Thus there are top_step + 1 total steps (including step 0.)  If integer values occur in start.xml (they don't have a decimal point) then the interpolated value will be rounded to the nearest integer.")
    opts, args = parser.parse_args(argv)

    if len(args) != 4:
        parser.error("4 arguments required")

    start_xml = args[0];
    end_xml = args[1];

    if not os.path.exists(start_xml):
        parser.error("Couldn't find start.xml file " + start_xml)
    if not os.path.exists(end_xml):
        parser.error("Couldn't find end.xml file " + end_xml)
    
    try:
        top_step = int(args[2]);
    except ValueError:
        parser.error("Couldn't convert top_step to int");

    try:
        current_step = int(args[3]);
    except ValueError:
        parser.error("Couldn't convert current_step to int");

    if top_step < 0 or current_step < 0 or current_step > top_step:
        parser.error("current_step should be less than or equal to top_step, "
                     "and both should be positive")

    parser.destroy()

    tree = interpolate_xml(start_xml, end_xml, top_step, current_step)

    sys.stdout.write(etree.tostring(tree) + "\n")

                          # pretty_print=True,
                          # xml_declaration=False,
                          # encoding='utf-8'


int_pattern = re.compile(r'^-?\d+$')
float_pattern = re.compile(r'^-?\d*\.\d+$');

# find all numeric texts in an xml stream, and return them in an array
def find_data(xml_stream):
    result = []
    tree = etree.parse(xml_stream)
    root = tree.getroot()
    for el in root.iterfind('.//*'):
        if int_pattern.match(el.text):
            result.append(int(el.text))
        elif float_pattern.match(el.text):
            result.append(float(el.text))
    return result

def interpolate_xml(start_xml, end_xml, top_step, current_step):
    # get numbers from end_xml
    end_data = find_data(open(end_xml));
    tree = etree.parse(open(start_xml))
    root = tree.getroot();

    # for each element, if it's a number, assume it matches with
    # a number from end_xml, and replace it with an interpolated value
    for el in root.iterfind('.//*'):
        if int_pattern.match(el.text) or float_pattern.match(el.text):
            try:
                end = end_data.pop(0);
            except IndexError:
                sys.stderr.write("error! more numbers detected in start_xml "
                                 "than in end_xml - files not matched up\n")
                break
            isint = int_pattern.match(el.text) is not None
            if isint and not isinstance(end, int):
                sys.stderr.write("error! found an int in start_xml and "
                                 "a float in end_xml.\n"
                                 "tag: " + el.tag + " text: " + el.text + "\n")
            elif not isint and not isinstance(end, float):
                sys.stderr.write("error! found a float in start_xml and "
                                 "an int in end_xml.\n"
                                 "tag: " + el.tag + " text: " + el.text + "\n")
            end = float(end)
            start = float(el.text)
            interpolated = start + ((end - start) / top_step) * current_step
            if isint:
                interpolated = int(round(interpolated))
            el.text = str(interpolated)
    if len(end_data) is not 0:
        sys.stderr.write("error! more numbers detected in end_xml than "
                         "start_xml - things probably didn't match up.\n")
    return tree
            
if __name__ == '__main__':
    main(sys.argv[1:])
