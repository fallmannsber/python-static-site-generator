import typer
from ssg.site import Site

def __main__(source="content", dest="dist"):
    config = {"source":source, "dest":dest}
    s = Site(**config)
    s.build()

typer.run(__main__)
