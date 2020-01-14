import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--value', required=True)
args = parser.parse_args()

def text2float(textamount, numwords={}):
    """Converts a NL text sting of numbers into a float value
    https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
    """

    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    scales = ["hundred", "thousand", "million", "billion", "trillion"]

    numwords["and"] = (1, 0)
    numwords["dollars"] = (1, 0)
    numwords["dollar"] = (1,0)
    numwords["cents"] = (1, 0)
    numwords["a"] = (1, 0)

    for idx, word in enumerate(units):
        numwords[word] = (1, idx)
    for idx, word in enumerate(tens):
        numwords[word] = (1, idx*10)
    for idx, word in enumerate(scales):
        numwords[word] = (10**(idx * 3 or 2), 0)

    current = result = 0
    for word in textamount.split():
        if word not in numwords:
            continue

        scale, increment = numwords[word]
        current = current * scale + increment

        if scale > 100:
            result += current
            current = 0

    return result + current


def split_dollars_cents(text):

    dollars = []
    cents = []
    flag = False
    for j in text.split():
        if j == 'dollars' or j == 'dollar':
            flag = True
            continue
        if flag == False:
            dollars.append(j)
        if flag == True:
            cents.append(j)

    dollars = " ".join(dollars)
    cents = " ".join(cents)

    return dollars, cents


def text2value(textamount):

    dollars, cents = split_dollars_cents(textamount)
    dollars = text2float(dollars)
    cents = round(text2float(cents) / 100, 2)
    return dollars+cents


if __name__ == "__main__":

    print(text2value(args.value))