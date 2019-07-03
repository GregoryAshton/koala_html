#!/usr/bin/env python
""" Simple HTML page generation """

import argparse
import os


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-1", "--column1", required=True, nargs="+",
                        help="First column of images")
    parser.add_argument("-2", "--column2", nargs="+", default=None,
                        help="Second column of images")
    parser.add_argument("-3", "--columns3", nargs="+", default=None,
                        help="Third column of images")
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
    nrows = len(args.column1)
    table_list = [args.column1]

    col_idx = 2
    while True:
        column_name = f"column{col_idx}"
        if getattr(args, column_name, None) is not None:
            column = getattr(args, column_name)
            ncols += 1
            if len(column) > nrows:
                print(f"Column {col_idx} has more rows than Column 1, truncating")
                column = column[:nrows]
            elif len(column) < nrows:
                print(f"Column {col_idx} has fewer rows than Column 1, fill with None")
                column += [None] * (nrows - len(column))
            table_list.append(column)
            col_idx += 1
        else:
            break

    return table_list


def convert_element_to_HTML(args, element):
    if element is None:
        return "N/A"
    elif os.path.isfile(element):
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
