#!/usr/bin/env python
""" Simple HTML page generation """

import argparse
import os


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--columnA", required=True, nargs="+",
                        help="First column of images")
    parser.add_argument("--columnB", nargs="+", default=None,
                        help="Second column of images")
    parser.add_argument("--image-size", type=int, default=500,
                        help="Individual image size")
    parser.add_argument("--page-name", type=str, default="index.html",
                        help="Output name")
    args = parser.parse_args()
    return args


def write_to_file(args, body):
    text = ["<!DOCTYPE html>", "<html>", "<body>"]
    text += body
    text += ["</body>", "</html>"]
    index_file = f"{args.page_name}"
    with open(index_file, "w+") as f:
        print("\n".join(text), file=f)


def get_table_list(args):
    """ Generates the ncols x nrows list of files to show in the table """
    ncols = 1
    nrows = len(args.columnA)
    table_list = [args.columnA]

    if args.columnB is not None:
        ncols += 1
        nrowsB = len(args.columnB)
        if nrowsB > nrows:
            print("Column B has more rows than Column A, truncating")
            args.columnB = args.columnB[:nrows]
        elif nrowsB < nrows:
            print("Column B has fewer rows than Column A, fill with None")
            args.columnB += [None] * (nrows - len(args.columnB))
        table_list.append(args.columnB)

    return table_list


def convert_element_to_HTML(args, element):
    if os.path.isfile(element):
        return f'<img src="{element}"  width="{args.image_size}">'
    else:
        return f'<b> {element} </b>'


def convert_table_list_to_body(args, table_list):
    """ Generates the body (a list of HTML strings) """
    body = ['<table style="width:80%">']
    ncols = len(table_list)
    nrows = len(table_list[0])
    for i in range(nrows):
        body += ["<tr>"]
        for j in range(ncols):
            html = convert_element_to_HTML(args, table_list[j][i])
            body += [f"<td> {html} <td>"]
        body += ["</tr>"]
    return body


def main():
    args = get_args()
    table_list = get_table_list(args)
    body = convert_table_list_to_body(args, table_list)
    write_to_file(args, body)