# coding=utf8
import textwrap

from l20n.format.parser import FTLParser
from l20n.format.serializer import FTLSerializer


ftl_parser = FTLParser()
ftl_serializer = FTLSerializer()


def parse(Parser, string):
    if Parser is FTLParser:
        ast, errors = ftl_parser.parse(string)
        return ast

    # Parsing a legacy resource.

    # Parse the string into the internal Context.
    parser = Parser()
    parser.readContents(string)
    # Transform the parsed result which is an iterator into a dict.
    return {ent.get_key(): ent for ent in parser}


def dumpEntry(node):
    return ftl_serializer.dumpEntry(node.toJSON())


def serialize(resource):
    return ftl_serializer.serialize(resource.toJSON())


def ftl(code):
    """Nicer indentation for FTL code.

    The code returned by this function is meant to be compared against the
    output of the FTL Serializer.  The input code will be UTF8-decoded and will
    end with a newline to match the output of the serializer.
    """

    # The FTL Serializer returns Unicode data.
    code = code.decode('utf8')

    # The code might be triple-quoted.
    code = textwrap.dedent(code.lstrip('\n'))

    # The FTL Serializer always appends EOL to serialized entries. The FTL code
    # that we want to compare against the serializer's output should too.
    if not code.endswith('\n'):
        code += '\n'

    return code
