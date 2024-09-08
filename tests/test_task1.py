import pytest  # noqa: F401
from project.task1 import graph_data_by_name, save_two_cycles_graph


def test_graph_data_by_name():
    assert graph_data_by_name("skos") == (
        144,
        252,
        {
            "creator",
            "scopeNote",
            "type",
            "range",
            "rest",
            "definition",
            "subClassOf",
            "example",
            "domain",
            "subPropertyOf",
            "description",
            "contributor",
            "label",
            "title",
            "unionOf",
            "seeAlso",
            "comment",
            "isDefinedBy",
            "disjointWith",
            "inverseOf",
            "first",
        },
    )
    assert graph_data_by_name("wc") == (332, 269, {"d", "a"})
    assert graph_data_by_name("generations") == (
        129,
        273,
        {
            "hasSex",
            "first",
            "someValuesFrom",
            "hasSibling",
            "rest",
            "hasParent",
            "oneOf",
            "onProperty",
            "inverseOf",
            "intersectionOf",
            "equivalentClass",
            "range",
            "hasChild",
            "type",
            "hasValue",
            "versionInfo",
            "sameAs",
        },
    )


EXPECTED_DOT_FILE_1_4_TEXT = """digraph  {
1;
0;
2;
3;
4;
5;
1 -> 0 [key=0, label=hello];
0 -> 1 [key=0, label=hello];
0 -> 2 [key=0, label=world];
2 -> 3 [key=0, label=world];
3 -> 4 [key=0, label=world];
4 -> 5 [key=0, label=world];
5 -> 0 [key=0, label=world];
}
"""

EXPECTED_DOT_FILE_5_3_TEXT = """digraph  {
1;
2;
3;
4;
5;
0;
6;
7;
8;
1 -> 2 [key=0, label=a];
2 -> 3 [key=0, label=a];
3 -> 4 [key=0, label=a];
4 -> 5 [key=0, label=a];
5 -> 0 [key=0, label=a];
0 -> 1 [key=0, label=a];
0 -> 6 [key=0, label=b];
6 -> 7 [key=0, label=b];
7 -> 8 [key=0, label=b];
8 -> 0 [key=0, label=b];
}
"""


def test_save_two_cycles_graph(tmpdir):
    path = tmpdir / "tcg.dot"
    save_two_cycles_graph(5, 3, "a", "b", path)
    assert open(path, "r").read() == EXPECTED_DOT_FILE_5_3_TEXT

    path = tmpdir / "tcg.dot"
    save_two_cycles_graph(1, 4, "hello", "world", path)
    assert open(path, "r").read() == EXPECTED_DOT_FILE_1_4_TEXT
