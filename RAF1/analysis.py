def histogram_keyspace():
    counts = {
        '00': '',
        '01': '',
        '10': '',
        '11': '',
    }
    sub_index = {}
    for i in range(64):
        sub_index[i] = ''

    # Keyspace of a-zA-Z0-9~`!@#$%^&*()_+-={} |[]\:";'<>?,./
    for byte in range(32, 127):
        sBoxIndex = '{}{}'.format(
            str(((byte >> 1) & 1)),
            str(((byte >> 0) & 1))
        )
        counts[sBoxIndex] += '#'
        index = ''
        for bit_pos in range(2,8):
            index += str(((byte >> bit_pos) & 1))
        index = '{}{}{}{}{}{}'.format(
            str(((byte >> 2) & 1)),
            str(((byte >> 3) & 1)),
            str(((byte >> 7) & 1)),
            str(((byte >> 6) & 1)),
            str(((byte >> 4) & 1)),
            str(((byte >> 5) & 1))
        )
        sub_index[int(index, 2)] += '#'

    for k, v in counts.iteritems():
        print("S-Box {}: {} - {}".format(k, v, len(v)))

    for k, v in sub_index.iteritems():
        print("S-Boxes_Index {}: {} - {}".format(k, v, len(v)))
