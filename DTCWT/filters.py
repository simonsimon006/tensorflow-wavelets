
def FSfarras():

    a_lo_hi_rows_cols = list()
    s_lo_hi_rows_cols = list()

    a_lo_hi_rows_cols.append([
        [0,
         -0.0883883476483200,
         0.0883883476483200,
         0.695879989034000,
         0.695879989034000,
         0.0883883476483200,
         -0.0883883476483200,
         0.0112267921525400,
         0.0112267921525400,
         0],
        [0,
         -0.0112267921525400,
         0.0112267921525400,
         0.0883883476483200,
         0.0883883476483200,
         -0.695879989034000,
         0.695879989034000,
         -0.0883883476483200,
         -0.0883883476483200,
         0]
    ])

    a_lo_hi_rows_cols.append([
        [0.0112267921525400,
         0.0112267921525400,
         -0.0883883476483200,
         0.0883883476483200,
         0.695879989034000,
         0.695879989034000,
         0.0883883476483200,
         -0.0883883476483200,
         0,
         0],
        [0,
         0,
         -0.0883883476483200,
         -0.0883883476483200,
         0.695879989034000,
         -0.695879989034000,
         0.0883883476483200,
         0.0883883476483200,
         0.0112267921525400,
         -0.0112267921525400]

    ])
    s_lo_hi_rows_cols.append(list())
    s_lo_hi_rows_cols.append(list())

    s_lo_hi_rows_cols[0].append(a_lo_hi_rows_cols[0][0][::-1])
    s_lo_hi_rows_cols[0].append(a_lo_hi_rows_cols[0][1][::-1])
    s_lo_hi_rows_cols[1].append(a_lo_hi_rows_cols[1][0][::-1])
    s_lo_hi_rows_cols[1].append(a_lo_hi_rows_cols[1][1][::-1])

    return a_lo_hi_rows_cols, s_lo_hi_rows_cols


def duelfilt():
    a_lo_hi_rows_cols = list()
    s_lo_hi_rows_cols = list()
    a_lo_hi_rows_cols.append([
        [0,
         0.0112267921525400,
         0.0112267921525400,
         -0.0883883476483200,
         0.0883883476483200,
         0.695879989034000,
         0.695879989034000,
         0.0883883476483200,
         -0.0883883476483200,
         0],
        [0,
         -0.0883883476483200,
         -0.0883883476483200,
         0.695879989034000,
         -0.695879989034000,
         0.0883883476483200,
         0.0883883476483200,
         0.0112267921525400,
         -0.0112267921525400,
         0]
    ])
    a_lo_hi_rows_cols.append([
        [0,
         0,
         -0.0883883476483200,
         0.0883883476483200,
         0.695879989034000,
         0.695879989034000,
         0.0883883476483200,
         -0.0883883476483200,
         0.0112267921525400,
         0.0112267921525400
         ],
        [-0.0112267921525400,
         0.0112267921525400,
         0.0883883476483200,
         0.0883883476483200,
         -0.695879989034000,
         0.695879989034000,
         -0.0883883476483200,
         -0.0883883476483200,
         0,
         0]
    ])

    s_lo_hi_rows_cols.append(list())
    s_lo_hi_rows_cols.append(list())

    s_lo_hi_rows_cols[0].append(a_lo_hi_rows_cols[0][0][::-1])
    s_lo_hi_rows_cols[0].append(a_lo_hi_rows_cols[0][1][::-1])
    s_lo_hi_rows_cols[1].append(a_lo_hi_rows_cols[1][0][::-1])
    s_lo_hi_rows_cols[1].append(a_lo_hi_rows_cols[1][1][::-1])

    return a_lo_hi_rows_cols, s_lo_hi_rows_cols