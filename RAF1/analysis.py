def histogram_keyspace():
    counts = {
        '00': '',
        '01': '',
        '10': '',
        '11': '',
    }

    # Keyspace of a-zA-Z0-9~`!@#$%^&*()_+-={} |[]\:";'<>?,./
    for byte in range(32, 127):
        sBoxIndex = '{}{}'.format(
            str(((byte >> 7) & 1)),
            str(((byte >> 0) & 1))
        )
        counts[sBoxIndex] += '#'

    for k, v in counts.iteritems():
        print("S-Box {}: {} - {}".format(k, v, len(v)))
