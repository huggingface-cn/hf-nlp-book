from panflute import *

def action( elem, doc ):
    if isinstance( elem, Div ) and 'Tip-green' in elem.classes:
        return Div( Para(*elem.content), attributes={'custom-style': 'Tip-green'} )
    if isinstance( elem, Div ) and 'Tip-yellow' in elem.classes:
        return Div( Para(*elem.content), attributes={'custom-style': 'Tip-yellow'} )
    if isinstance( elem, Div ) and 'Tip-red' in elem.classes:
        return Div( Para(*elem.content), attributes={'custom-style': 'Tip-red'} )

def main(doc=None):
    return run_filter( action, doc=doc )

if __name__ == "__main__":
    main()
