def manual():
    return {
        'A' : {
            '0' : {
                "value" : 1,
                "move"  : 1,
                "state" : 'B'
            },
            '1' : {
                "value" : 0,
                "move"  : -1,
                "state" : 'C'
            }
        },
        'B' : {
            '0' : {
                "value" : 1,
                "move"  : -1,
                "state" : 'A'
            },
            '1' : {
                "value" : 1,
                "move"  : -1,
                "state" : 'D'
            }
        },
        'C' : {
            '0' : {
                "value" : 1,
                "move"  : 1,
                "state" : 'D'
            },
            '1' : {
                "value" : 0,
                "move"  : 1,
                "state" : 'C'
            }
        },
        'D' : {
            '0' : {
                "value" : 0,
                "move"  : -1,
                "state" : 'B'
            },
            '1' : {
                "value" : 0,
                "move"  : 1,
                "state" : 'E'
            }
        }
        'E' : {
            '0' : {
                "value" : 1,
                "move"  : 1,
                "state" : 'C'
            },
            '1' : {
                "value" : 1,
                "move"  : -1,
                "state" : 'F'
            }
        }
        'F' : {
            '0' : {
                "value" : 1,
                "move"  : -1,
                "state" : 'E'
            },
            '1' : {
                "value" : 1,
                "move"  : 1,
                "state" : 'A'
            }
        }
}
