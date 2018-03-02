"""
file: quickSort.py
version: python3
author: Arthur Nunes-Harwitt, Ivona Bezakova
purpose: Implementation of the quick-sort algorithm ( not in-place )
"""

def quickSortGrowth( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0].value2 - L[0].value1
        ( less, same, more ) = partition( pivot, L )
        return quickSortGrowth( less ) + same + quickSortGrowth( more )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if (e.value2 - e.value1) < pivot:
            less.append( e )
        elif (e.value2 - e.value1) > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

if __name__ == "__main__":
    print( quickSortGrowth( [1, 5, 3, 4, 2, 2, 7, 5, 3, 4, 9, 0, 1, 2, 5, 4, 76, 6] ) )

