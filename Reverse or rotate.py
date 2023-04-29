def rev_rot(strng, sz):
    if not strng or sz <= 0 or sz > len(strng):
        return ''

    chunks = [strng[i:i+sz] for i in range(0, len(strng), sz)]
    new_strng = ''

    for chunk in chunks:
        if len(chunk) != sz:
            continue

        sum_of_cubes = sum(int(d)**3 for d in chunk)

        if sum_of_cubes % 2 == 0:
            new_strng += chunk[::-1]
        else:
            new_strng += chunk[1:] + chunk[0]

    return new_strng
