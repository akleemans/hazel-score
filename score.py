def get_borders(img):
    """Recognize borders of the area to check"""
    w, h = img.size
    threshold = 90
    margin = 12
    a, b, c, d = 0, 0, 0, 0

    for i in range(int(w / 3), w):
        p = img.getpixel((i, h / 2))[0]
        if p < threshold:
            a = i + margin
            break

    for i in range(5, h):
        p = img.getpixel((w / 2, i))[0]
        if p < threshold:
            b = i + margin
            break

    for i in range(int(2 * w / 3), 0, -1):
        p = img.getpixel((i, h / 2))[0]
        if p < threshold:
            c = i - margin
            break

    for i in range(h - 5, 0, -1):
        p = img.getpixel((w / 2, i))[0]
        if p < threshold:
            d = i - margin
            break
    return a, b, c, d


def score(img):
    """Score an image of a hazelnut using thresholds"""
    # Convert to greyscale
    img = img.convert('LA')
    w, h = img.size
    print('Read image, w/h:', w, h)

    print('Recognizing borders...')
    a, b, c, d = get_borders(img)
    print('Found rectangle:', a, b, c, d)

    img = img.crop((a + 1, b + 1, c - 1, d - 1))
    w_new, h_new = img.size
    print('Cropped image, new size:', w_new, h_new)

    print('Checking thresholds...')
    count120 = 0
    count80 = 0
    count70 = 0
    count60 = 0

    mi = 255
    ma = 0
    for i in range(w_new - 1):
        for j in range(h_new - 1):
            p = img.getpixel((i, j))[0]
            if p < mi: mi = p
            if p > ma: ma = p
            # add to counters
            if p < 120: count120 += 1
            if p < 80: count80 += 1
            if p < 70: count70 += 1
            if p < 60: count60 += 1

    print('Report. Range:', mi, ma, ', counters: 120:', count120, '80:',
          count80, '70:', count70, '60:', count60)

    if count120 < 300:
        return None, 'No hazelnut\nrecognized.'
    elif count70 > 500:
        return False, 'Class B :(\nIDX: ' + str(count60) + '/' + str(
            count70) + '/' + str(count80)
    else:
        return True, '==> Class A!\nIDX: ' + str(count60) + '/' + str(
            count70) + '/' + str(count80)
