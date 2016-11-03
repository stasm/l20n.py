# coding=utf8
import textwrap

from l20n.format.parser import FTLParser
from l20n.format.serializer import FTLSerializer


ftl_parser = FTLParser()
ftl_serializer = FTLSerializer()


def parse(Parser, string):
    if Parser is FTLParser:
        ast, errors = ftl_parser.parse(string, with_source=False)
        return ast

    # Parsing a legacy resource.

    # Parse the string into the internal Context.
    parser = Parser()
    parser.readContents(string)
    # Transform the parsed result which is an iterator into a dict.
    return {ent.get_key(): ent for ent in parser}


def ftl(code):
    """Nicer indentation for FTL code.

    The code returned by this function is meant to be compared against the
    output of the FTL Serializer.  The input code will be UTF8-decoded and will
    end with a newline to match the output of the serializer.
    """

    # The FTL Serializer returns Unicode data so we use it as the baseline.
    code = code.decode('utf8')

    # The code might be triple-quoted.
    code = code.lstrip('\n')

    return textwrap.dedent(code)


def ftl_resource_to_json(code):
    ast, errors = ftl_parser.parseResource(ftl(code), with_source=False)
    return ast


def ftl_message_to_json(code):
    ast, errors = ftl_parser.parse(ftl(code), with_source=False)
    return ast.body[0].toJSON()


def to_json(merged_iter):
    return {
        path: resource.toJSON()
        for path, resource in merged_iter
    }